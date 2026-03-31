import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Any, Dict

from nutrihelp_ai.services.meal_generator import plan as generate_plan_logic, meal_library

logger = logging.getLogger(__name__)
router = APIRouter()

# Load meals once
MEALS = meal_library()

class MealPlanInput(BaseModel):
    name: Optional[str] = None
    label_text: Optional[str] = ""
    allergies: List[str] = Field(default_factory=list)
    conditions: List[str] = Field(default_factory=list)
    texture: Optional[str] = "normal"
    budget: Optional[str] = "medium"
    calories_target: Optional[int] = 2000

@router.post("/generate")
async def generate_meal_plan(input_data: MealPlanInput) -> Dict[str, Any]:
    try:
        logger.info("Received request for meal plan")

        user_profile = input_data.model_dump()
        result = generate_plan_logic(user_profile, MEALS)

        # If nothing is available after filtering
        if not result.get("breakfast") and not result.get("lunch") and not result.get("dinner"):
            raise HTTPException(
                status_code=400,
                detail="No meals available after filtering. Try relaxing allergies/conditions/texture/budget."
            )

        logger.info("Generated meal plan successfully")
        return result

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Unexpected error in /meal-plan/generate: %s", e, exc_info=True)
        raise HTTPException(status_code=500, detail="Meal plan generation failed due to server error.")