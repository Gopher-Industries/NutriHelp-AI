import logging
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field, confloat
from typing import List, Literal, Optional, Any, Dict

from nutrihelp_ai.extensions import limiter
from nutrihelp_ai.services.nutribot_rag import NutriBotRAGService

# ---------- Setup logger ----------
logger = logging.getLogger(__name__)

router = APIRouter()
_service = NutriBotRAGService()

# ---------- Input Models ----------
ObesityLevel = Literal[
    "Insufficient_Weight",
    "Normal_Weight",
    "Overweight_Level_I",
    "Overweight_Level_II",
    "Obesity_Type_I",
    "Obesity_Type_II",
    "Obesity_Type_III"
]

class ObesityPrediction(BaseModel):
    obesity_level: ObesityLevel
    confidence: confloat(ge=0, le=100)

class DiabetesPrediction(BaseModel):
    diabetes: bool
    confidence: confloat(ge=0, le=100)

class MedicalReport(BaseModel):
    obesity_prediction: ObesityPrediction
    diabetes_prediction: DiabetesPrediction

class HealthPlanInput(BaseModel):
    medical_report: MedicalReport
    # Optional controls to mirror notebook cells when you tweak runs
    n_results: int = Field(4, ge=1, le=10)
    max_tokens: int = Field(1200, ge=256, le=4096)
    temperature: float = Field(0.2, ge=0.0, le=1.0)

# ---------- Response Models (strict JSON as per notebook) ----------
class WeekPlan(BaseModel):
    week: int = Field(..., ge=1)
    target_calories_per_day: int = Field(..., ge=800, le=5000)
    focus: str
    workouts: List[str]
    meal_notes: str
    reminders: List[str]

class HealthPlanResponse(BaseModel):
    suggestion: str
    weekly_plan: List[WeekPlan]

# ---------- Route ----------
@router.post("/generate", response_model=Optional[HealthPlanResponse])
@limiter.limit("15/minute")
async def generate_health_plan(request: Request, input_data: HealthPlanInput):
    try:
        logger.info("Received request for health plan")

        analyzed: Dict[str, Any] = {
            "medical_report": {
                "obesity_prediction": {
                    "obesity_level": input_data.medical_report.obesity_prediction.obesity_level,
                    "confidence": float(input_data.medical_report.obesity_prediction.confidence),
                },
                "diabetes_prediction": {
                    "diabetes": bool(input_data.medical_report.diabetes_prediction.diabetes),
                    "confidence": float(input_data.medical_report.diabetes_prediction.confidence),
                },
            },
            "health_survey": None,
            "followup_qa": None,
        }

        logger.debug("Analyzed input: %s", analyzed)

        raw = _service.generate_plan(
            analyzed_health_condition=analyzed,
            n_results=input_data.n_results,
            max_tokens=input_data.max_tokens,
            temperature=input_data.temperature,
        )

        logger.debug("Raw service output: %s", raw)

        response = HealthPlanResponse(**raw)
        logger.info("Generated health plan successfully")
        return response

    except ValueError as ve:
        logger.warning("Validation/Value error: %s", ve, exc_info=True)
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logger.error("Unexpected error in /plan/generate: %s", e, exc_info=True)
        raise HTTPException(status_code=500, detail="Plan generation failed due to server error.")
