from fastapi import FastAPI
from nutrihelp_ai.routers import image_api, obesity_api, chatbot_api

app = FastAPI(
    title="NutriHelp AI API",
    description="API for AI models",
    version="1.0"
)

app.include_router(image_api, prefix="/ai-model/image", tags=["Image Classification"])
app.include_router(obesity_api, prefix="/ai-model/obesity", tags=["Obesity Prediction"])
app.include_router(chatbot_api, prefix="/ai-model/chatbot", tags=["AI assistant"])
