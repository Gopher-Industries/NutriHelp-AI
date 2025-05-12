from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field, confloat
from typing import Literal
from nutrihelp_ai.services.medical_report import generate_medical_report_service
from nutrihelp_ai.extensions import limiter

router = APIRouter()

# ---- Input Model ----
class MedicalReportInput(BaseModel):
    Gender: int  # 1: Male, 2: Female
    Age: confloat(gt=0, lt=120)
    Height: confloat(gt=0.5, lt=2.5)
    Weight: confloat(gt=10, lt=300)
    family_history_with_overweight: Literal["yes", "no"]
    FAVC: int
    FCVC: confloat(ge=0, le=5)
    NCP: confloat(ge=0, le=10)
    CAEC: int  # 0 = Never, 1 = Sometimes, etc.
    SMOKE: int  # 0 = No, 1 = Yes
    CH2O: confloat(ge=0, le=10)
    SCC: Literal["yes", "no"]
    FAF: confloat(ge=0, le=10)
    TUE: confloat(ge=0, le=24)
    CALC: int  # 0 = Never, 1 = Sometimes, 2 = Frequently
    MTRANS: Literal["Walking", "Bike", "Public_Transportation", "Automobile", "Motorbike"]


# ---- No response model defined for now because it returns a nested JSON ----

@router.post("/retrieve")
@limiter.limit("15/minute")
async def generate_medical_report(request: Request, input_data: MedicalReportInput):
    try:
        return generate_medical_report_service(input_data)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception:
        raise HTTPException(status_code=500, detail="Prediction failed due to server error.")
