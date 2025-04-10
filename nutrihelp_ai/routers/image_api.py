from fastapi import APIRouter, File, UploadFile
from PIL import Image
import io
from nutrihelp_ai.services.predict_image import predict_image_service

router = APIRouter()

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    result = predict_image_service(image)
    return result
