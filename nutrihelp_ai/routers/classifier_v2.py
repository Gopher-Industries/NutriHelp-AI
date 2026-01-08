from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(
    prefix="/ai-model/classifier",
    tags=["Classifier v2"],
)

# ============================
# Response Models (NA-112)
# ============================


class PredictionItem(BaseModel):
    class_name: str
    confidence: float


class ClassifierV2Response(BaseModel):
    top_prediction: PredictionItem
    top_3_predictions: List[PredictionItem]
    allergy_warning: Optional[str] = None
    message: str = "Classification successful"


# ============================
# POST /ai-model/classifier/v2
# Dummy predictor + allergy check (NA-112 + NA-113)
# ============================
@router.post(
    "/v2",
    response_model=ClassifierV2Response,
    # requeired model image classifier ai ml team
    summary="Classifier v2 – Food Image Predictor (Dummy)",
    description="Dummy version for Week 6. Returns top prediction + top-3 + allergy warning based on user allergies."
)
async def classifier_v2_predict(
    image: UploadFile = File(..., description="Food image to analyze"),
    allergies: Optional[str] = Form(
        None,
        description="Comma-separated allergies from user profile (e.g. 'nuts,dairy,gluten,shellfish')"
    )
):
    # DUMMY predictions — replace with real model in Sprint 3
    dummy_predictions = [
        {"class_name": "peanut_butter_cookie", "confidence": 0.94},
        {"class_name": "chocolate_cake",       "confidence": 0.04},
        {"class_name": "bread_pudding",        "confidence": 0.02},
    ]

    top_pred = dummy_predictions[0]

    # NA-113: Allergy restriction logic
    warning = None
    if allergies and allergies.strip():  # Check if allergies is not empty
        allergy_list = [a.strip().lower()
                        for a in allergies.split(",") if a.strip()]
        food_lower = top_pred["class_name"].lower()

        for allergy in allergy_list:
            if allergy in food_lower:
                warning = f"ALLERGY ALERT: '{top_pred['class_name']}' may contain '{allergy}'"
                break

    return ClassifierV2Response(
        top_prediction=PredictionItem(**top_pred),
        top_3_predictions=[PredictionItem(**p) for p in dummy_predictions],
        allergy_warning=warning
    )
