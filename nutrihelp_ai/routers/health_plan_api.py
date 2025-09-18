import logging
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field, confloat, conint, field_validator
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

class HealthInfo(BaseModel):
    gender: Optional[str] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    age: Optional[int] = None 
    activity_level: Optional[str] = Field(
        None, description="sedentary, moderate, active"
    )
    recorded_at: Optional[str] = Field(
        None, description="ISO timestamp (e.g. 2025-09-15T08:00:00Z)"
    )

class MedicalReport(BaseModel):
    health_info: Optional[HealthInfo] = None
    obesity_prediction: ObesityPrediction
    diabetes_prediction: DiabetesPrediction

#New: strict validation for the extra fields
class HealthGoal(BaseModel):
    target_weight: float | None = Field(None, gt=0)
    days_per_week: conint(ge=0, le=7) = Field(..., description="Workout days per week (0–7)")
    workout_place: str | None = Field(None, description="'home' or 'gym'")

    @field_validator("workout_place", mode="before")
    def normalize_workout_place(cls, v):
        if v is None:
            return v
        v = str(v).lower().strip()
        if v not in {"home", "gym"}:
            raise ValueError("workout_place must be 'home' or 'gym'")
        return v


class HealthPlanInput(BaseModel):
    medical_report: List[MedicalReport]
    health_goal: HealthGoal

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
    progress_analysis: Optional[str] = None      #New: trend analysis

# ---------- Route ----------
@router.post("/generate", response_model=Optional[HealthPlanResponse])
@limiter.limit("15/minute")
async def generate_health_plan(request: Request, input_data: HealthPlanInput):
    try:
        logger.info("Received request for health plan")

        analyzed: Dict[str, Any] = {
            "medical_report": [r.dict() for r in input_data.medical_report],  # support array
            "health_goal": input_data.health_goal.dict(),
            "health_survey": None,
            "followup_qa": None,
        }

        logger.debug("Analyzed input: %s", analyzed)

        raw = _service.generate_plan(
            analyzed_health_condition=analyzed,
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
