from fastapi import FastAPI
from nutrihelp_ai.routers import image_api, obesity_api

app = FastAPI(
    title="NutriHelp AI API",
    description="API for Image & Obesity Prediction",
    version="1.0"
)

app.include_router(image_api, prefix="/image", tags=["Image Classification"])
app.include_router(obesity_api, prefix="/obesity", tags=["Obesity Prediction"])
