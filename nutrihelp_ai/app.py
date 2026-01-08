import json
import cv2
import dlib
import os
import uuid
import numpy as np
from imutils import face_utils
from scipy.spatial import distance as dist
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
from datetime import datetime
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse
from fastapi.templating import Jinja2Templates


# PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
USERS_FILE = "users.json"
EYE_AR_THRESH = 0.25
EYE_AR_CONSEC_FRAMES = 3
REQUIRED_BLINKS = 2

app = FastAPI(title="NutriHelp - Jenny AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

os.makedirs("uploads", exist_ok=True)
os.makedirs("meal_plans", exist_ok=True)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


MODEL_PATH = r"C:\Users\Naman Shah\OneDrive\Documents\Assignement_Deakin\T3\SIT764\Project\NutriHelp-AI\nutrihelp_ai\model\image_class.pt"
model = YOLO(MODEL_PATH)

CALORIE_DICT = {
    "apple": 52, "banana": 89, "orange": 47, "pizza": 285, "burger": 295,
    "sandwich": 300, "salad": 150, "rice": 200, "chicken": 165, "egg": 78,
    "bread": 80, "pasta": 200, "cake": 350, "ice cream": 207, "hot dog": 150,

}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload-image")
async def upload_image(images: list[UploadFile] = File(...)):
    file_paths = []
    for file in images:
        if file.content_type.startswith("image/"):
            ext = file.filename.split(".")[-1]
            filename = f"{uuid.uuid4().hex}.{ext}"
            filepath = os.path.join("uploads", filename)
            with open(filepath, "wb") as f:
                content = await file.read()
                f.write(content)
            file_paths.append(f"/uploads/{filename}")
    return JSONResponse({"filePaths": file_paths})


@app.post("/analyze-images")
async def analyze_images(request: Request):
    data = await request.json()
    image_paths = data.get("image_paths", [])
    response_lines = [
        "🥗 I analyzed your food photo(s)! Here's what I found:\n"]
    total_calories = 0

    for i, rel_path in enumerate(image_paths, 1):
        full_path = "." + rel_path
        try:
            results = model(full_path, conf=0.5, iou=0.5)
            classes = results[0].boxes.cls.tolist()
            class_names = [model.names[int(c)].lower() for c in classes]
            unique_names = list(set(class_names))

            response_lines.append(f"Photo {i}:")
            if not unique_names:
                response_lines.append("- No food detected.\n")
                continue

            photo_cal = 0
            for name in unique_names:
                cal = CALORIE_DICT.get(name, 145)
                response_lines.append(f"- {name.title()} (~{cal} calories)")
                photo_cal += cal
            response_lines.append(
                f"Estimated for this photo: {photo_cal} calories\n")
            total_calories += photo_cal
        except Exception as e:
            response_lines.append(f"- Error analyzing photo {i}.\n")

    response_lines.append(
        f"Total estimated calories: {total_calories} calories")
    response_lines.append(
        "\nNote: Estimates are approximate per typical serving. Portion size affects actual calories!")

    return JSONResponse({"answer": "\n".join(response_lines)})


@app.post("/ask")
async def ask_nutrition_question(request: Request):
    try:
        data = await request.json()
        print(data)
        question = data.get("question", "").strip()
        print(f"Question received: {question}")
        if not question:
            return JSONResponse({"answer": "Please ask something! 😊"})
        try:
            from ai_reasoning import get_quick_nutrition_advice
            answer = get_quick_nutrition_advice(question)
        except Exception as e:
            print(f"Error in getting advice: {e}")
            answer = "Service unavailable."
        print(f"[AI] Question: {question}\n[AI] Answer: {answer}")
        return JSONResponse({"answer": answer})
    except Exception as e:
        return JSONResponse({"answer": "Trouble connecting. Try again! 😊"})


@app.post("/generate-plan")
async def generate_plan(
    goal: str = Form(...), sport: str = Form(...), level: str = Form(...),
    diet: str = Form(...), condition: str = Form(""), allergies: str = Form("")
):

    meal_plan_text = "Day 1:\nBreakfast: Oatmeal with fruits\nLunch: Grilled chicken salad\nDinner: Baked salmon with veggies\n..."
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"meal_plan_{timestamp}_{uuid.uuid4().hex[:8]}.txt"
    filepath = os.path.join("meal_plans", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("Sample Meal Plan\n" + meal_plan_text)
    return JSONResponse({
        "meal_plan": meal_plan_text,
        "filename": filename
    })


@app.get("/download/{filename}")
async def download(filename: str):
    filepath = os.path.join("meal_plans", filename)
    if not os.path.exists(filepath):
        return JSONResponse({"error": "File not found"}, status_code=404)
    return FileResponse(filepath, filename=f"NutriHelp_MealPlan_{datetime.now().strftime('%Y%m%d')}.txt")


# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor(PREDICTOR_PATH)
# if os.path.exists(USERS_FILE):
#     with open(USERS_FILE, "r") as f:
#         users_db = json.load(f)
# else:
#     users_db = {}

camera = None
camera_active = False
current_mode = None
current_user = None
blink_counter = 0
total_blinks = 0
auth_result = None


def calculate_ear(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)


# def generate_frames():
#     global camera, camera_active, blink_counter, total_blinks, auth_result
#     camera = cv2.VideoCapture(0)
#     camera_active = True

#     while camera_active:
#         success, frame = camera.read()
#         if not success:
#             break

#         frame = cv2.resize(frame, None, fx=0.75, fy=0.75)
#         rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         rects = detector(gray, 0)

#         for rect in rects:
#             shape = predictor(gray, rect)
#             shape = face_utils.shape_to_np(shape)

#             left_eye = shape[36:42]
#             right_eye = shape[42:48]

#             ear = (calculate_ear(left_eye) + calculate_ear(right_eye)) / 2.0

#             if ear < EYE_AR_THRESH:
#                 blink_counter += 1
#             else:
#                 if blink_counter >= EYE_AR_CONSEC_FRAMES:
#                     total_blinks += 1
#                 blink_counter = 0

#             cv2.putText(frame, f"Blinks: {total_blinks}/{REQUIRED_BLINKS}",
#                         (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

#             if total_blinks >= REQUIRED_BLINKS and auth_result is None:
#                 face_locations = [
#                     (rect.top(), rect.right(), rect.bottom(), rect.left())]
#                 encodings = face_recognition.face_encodings(
#                     rgb, face_locations)

#                 if encodings:
#                     encoding = encodings[0]

#                     if current_mode == "register":
#                         users_db[current_user] = {
#                             "encoding": encoding.tolist()}
#                         with open(USERS_FILE, "w") as f:
#                             json.dump(users_db, f, indent=2)
#                         auth_result = {
#                             "status": "success",
#                             "message": f"Registered as {current_user}",
#                             "redirect": True
#                         }

#                     elif current_mode == "login":

#                         if users_db:
#                             known_encodings = [
#                                 np.array(user["encoding"]) for user in users_db.values()]
#                             known_names = list(users_db.keys())

#                             distances = face_recognition.face_distance(
#                                 known_encodings, encoding)
#                             best_match_idx = np.argmin(distances)

#                             if distances[best_match_idx] < 0.6:
#                                 matched_name = known_names[best_match_idx]
#                                 auth_result = {
#                                     "status": "success",
#                                     "message": f"Welcome back {matched_name}!",
#                                     "redirect": True
#                                 }
#                             else:
#                                 auth_result = {
#                                     "status": "failed",
#                                     "message": "Face not recognized"
#                                 }
#                         else:
#                             auth_result = {
#                                 "status": "failed",
#                                 "message": "No registered users found"
#                             }

#                     camera_active = False

#             cv2.putText(frame, "Blink Twice to Authenticate",
#                         (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

#         ret, buffer = cv2.imencode(".jpg", frame)
#         frame_bytes = buffer.tobytes()

#         yield (b"--frame\r\n"
#                b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n")

#     if camera is not None:
#         camera.release()
#         camera = None


# @app.get("/", response_class=HTMLResponse)
# def index(request: Request):
#     return templates.TemplateResponse("login.html", {"request": request})


# @app.get("/video")
# def video():
#     if not camera_active:
#         return JSONResponse({"error": "Camera not active"}, status_code=400)

#     return StreamingResponse(
#         generate_frames(),
#         media_type="multipart/x-mixed-replace; boundary=frame"
#     )


# @app.post("/register")
# def register(username: str):
#     global current_mode, current_user, total_blinks, auth_result, camera_active
#     if username in users_db:
#         return JSONResponse({"error": "User already exists"}, status_code=400)

#     current_mode = "register"
#     current_user = username
#     total_blinks = 0
#     auth_result = None
#     camera_active = True
#     return {"status": "Camera started for registration"}


# @app.post("/login")
# def login():
#     global current_mode, total_blinks, auth_result, camera_active
#     current_mode = "login"
#     total_blinks = 0
#     auth_result = None
#     camera_active = True
#     return {"status": "Camera started for login"}


# @app.get("/result")
# def result():
#     global auth_result
#     if auth_result:
#         print(auth_result, "<<<<<<<<<<<<")
#         return JSONResponse({"result": auth_result})
#     return JSONResponse({"result": None})


if __name__ == "__main__":
    import uvicorn
    print("🥗 NutriHelp Starting... Open http://127.0.0.1:8000")
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
