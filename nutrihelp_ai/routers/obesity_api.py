from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from nutrihelp_ai.services.predict_obesity import predict_obesity_service

router = APIRouter()

class ObesityInput(BaseModel):
    gender: str = Field(..., example="Male")
    age: float = Field(..., example=24.443011)
    height: float = Field(..., example=1.699998)
    weight: float = Field(..., example=81.66995)
    family_history_with_overweight: str = Field(..., example="yes")
    frequent_consumption_of_high_caloric_food: str = Field(..., example="yes")
    frequency_of_consumption_of_vegetables: float = Field(..., example=2)
    number_of_main_meals: float = Field(..., example=2.983297)
    consumption_of_food_between_meals: str = Field(..., example="Sometimes")
    smoker: str = Field(..., example="no")
    consumption_of_water_daily: float = Field(..., example=2.763573)
    calories_consumption_monitoring: str = Field(..., example="no")
    physical_activity_frequency: float = Field(..., example=0)
    time_using_technology_devices: float = Field(..., example=0.976473)
    consumption_of_alcohol: str = Field(..., example="Sometimes")
    transportation_used: str = Field(..., example="Public_Transportation")

@router.post("/predict")
def predict_obesity(input_data: ObesityInput):
    try:
        return predict_obesity_service(input_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
