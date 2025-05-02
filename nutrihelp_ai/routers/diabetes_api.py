# nutrihelp_ai/routers/diabetes_api.py
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field, confloat, conint
from typing import Optional
from nutrihelp_ai.services.predict_diabetes import predict_diabetes_service
from nutrihelp_ai.extensions import limiter

router = APIRouter()

# ---- Input Model with Validation ----
class DiabetesInput(BaseModel):
    glucose: confloat(gt=0, lt=300) = Field(..., example=120)
    bmi: confloat(gt=0, lt=100) = Field(..., example=28.5)
    age: conint(gt=0, lt=120) = Field(..., example=45)

# ---- Response Model ----
class DiabetesPrediction(BaseModel):
    prediction: str
    probability: Optional[float] = None

# ---- Endpoint with Rate Limiting and Error Handling ----
@router.post("/predict-diabetes", response_model=DiabetesPrediction)
@limiter.limit("5/minute")  # ⏱️ 5 requests/minute per IP
async def predict_diabetes(request: Request, input_data: DiabetesInput):
    try:
        result = predict_diabetes_service(input_data.dict())
        return DiabetesPrediction(**result)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception:
        raise HTTPException(status_code=500, detail="Prediction failed due to server error.")
