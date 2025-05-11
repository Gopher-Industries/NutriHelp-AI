from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field, confloat
from typing import Literal
from nutrihelp_ai.services.predict_obesity import predict_obesity_service
from nutrihelp_ai.extensions import limiter

router = APIRouter()

# ---- Input Model ----
class ObesityInput(BaseModel):
    Gender: Literal["Male", "Female"]
    Age: confloat(gt=0, lt=120) = Field(..., example=25)
    Height: confloat(gt=0.5, lt=2.5) = Field(..., example=1.75)
    Weight: confloat(gt=10, lt=300) = Field(..., example=85)
    family_history_with_overweight: Literal["yes", "no"]
    FAVC: Literal["yes", "no"]
    FCVC: confloat(ge=0, le=3) = Field(..., example=2.7)
    NCP: confloat(ge=1, le=5) = Field(..., example=3)
    CAEC: Literal["Always", "Frequently", "Sometimes", "no"]
    SMOKE: Literal["yes", "no"]
    CH2O: confloat(ge=0, le=5) = Field(..., example=2.5)
    SCC: Literal["yes", "no"]
    FAF: confloat(ge=0, le=5) = Field(..., example=0.5)
    TUE: confloat(ge=0, le=5) = Field(..., example=1)
    CALC: Literal["no", "Sometimes", "Frequently", "Always"]
    MTRANS: Literal["Walking", "Bike", "Public_Transportation", "Automobile", "Motorbike"]

# ---- Response Model ----
class ObesityPrediction(BaseModel):
    prediction: str
    probability: float

# ---- Endpoint with Rate Limiting and Exception Handling ----
@router.post("/predict", response_model=ObesityPrediction)
@limiter.limit("5/minute")  # ⏱️ Rate limit
async def predict_obesity(request: Request, input_data: ObesityInput):
    try:
        result = predict_obesity_service(input_data)
        return ObesityPrediction(**result)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception:
        raise HTTPException(status_code=500, detail="Prediction failed due to server error.")
