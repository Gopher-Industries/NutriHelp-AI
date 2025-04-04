from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np
from nutrihelp_ai.services.predict_obesity import predict_obesity_class

router = APIRouter()

class ObesityInput(BaseModel):
    Gender: str
    family_history_with_overweight: str
    FAVC: str
    CAEC: str
    SMOKE: str
    SCC: str
    CALC: str
    MTRANS: str
    Age: float
    Height: float
    Weight: float
    NCP: float
    CH2O: float
    FAF: float
    TUE: float

@router.post("/predict")
def predict_obesity(input_data: ObesityInput):
    try:
        return predict_obesity_class(input_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
