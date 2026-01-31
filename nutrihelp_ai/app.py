import json

import os
import uuid
import numpy as np
# from imutils import face_utils
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
    goal: str = Form(...),
    sport: str = Form(...),
    level: str = Form(...),
    diet: str = Form(...),
    condition: str = Form("None"),
    allergies: str = Form("None")
):
    from ai_reasoning import generate_meal_plan

    # Clean and parse allergies properly
    allergy_list = []
    if allergies and allergies.strip() and allergies.lower() not in ['none', 'no', 'nothing']:
        # Split by comma and clean each item
        allergy_list = [a.strip() for a in allergies.split(",")
                        if a.strip() and len(a.strip()) > 1]

    # If no valid allergies, set to None
    if not allergy_list:
        allergy_list = ["None"]

    # Clean condition
    clean_condition = condition.strip() if condition and condition.strip() else "None"

    user_profile = {
        "goal": goal,
        "sport": sport,
        "level": level,
        "diet": diet,
        "condition": clean_condition,
        "allergies": allergy_list
    }

    # Generate meal plan
    meal_plan_text = generate_meal_plan(
        user_profile, data_loader=None, start_day=1)

    # Save to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"meal_plan_{timestamp}_{uuid.uuid4().hex[:8]}.txt"

    # Ensure directory exists
    os.makedirs("meal_plans", exist_ok=True)
    filepath = os.path.join("meal_plans", filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("=== YOUR PERSONALIZED MEAL PLAN ===\n\n")
        f.write(f"Goal: {goal}\n")
        f.write(f"Activity: {sport}\n")
        f.write(f"Level: {level}\n")
        f.write(f"Diet: {diet}\n")
        f.write(f"Condition: {clean_condition}\n")
        f.write(f"Allergies: {', '.join(allergy_list)}\n")
        f.write("\n" + "="*50 + "\n\n")
        f.write(meal_plan_text)

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

if __name__ == "__main__":
    import uvicorn
    print("🥗 NutriHelp Starting... Open http://127.0.0.1:8000")
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
