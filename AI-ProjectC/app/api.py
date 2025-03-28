from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io

from .inference import predict_image  # relative import from inference.py

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Model API!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    result = predict_image(image)
    return result
