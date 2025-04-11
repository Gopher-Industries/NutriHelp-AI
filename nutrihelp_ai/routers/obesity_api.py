from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from nutrihelp_ai.services.predict_obesity import predict_obesity_service

router = APIRouter()

from pydantic import BaseModel, Field

class ObesityInput(BaseModel):
    Gender: str = Field(..., example="Male")
    Age: float = Field(..., example=25)
    Height: float = Field(..., example=1.75)
    Weight: float = Field(..., example=85)
    family_history_with_overweight: str = Field(..., example="yes")
    FAVC: str = Field(..., example="yes")
    FCVC: float = Field(..., example=2.5)
    NCP: float = Field(..., example=3)
    CAEC: str = Field(..., example="Sometimes")
    SMOKE: str = Field(..., example="no")
    CH2O: float = Field(..., example=2.5)
    SCC: str = Field(..., example="no")
    FAF: float = Field(..., example=0.5)
    TUE: float = Field(..., example=1)
    CALC: str = Field(..., example="Sometimes")
    MTRANS: str = Field(..., example="Public_Transportation")


@router.post("/predict")
def predict_obesity(input_data: ObesityInput):
    try:
        return predict_obesity_service(input_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
