from fastapi import APIRouter, UploadFile, File, HTTPException
from nutrihelp_ai.services.image_pipeline import ImagePipelineService
from nutrihelp_ai.services.active_ai_backend import GroqChromaBackend
import logging

router = APIRouter()
logger = logging.getLogger(__name__)
agent = GroqChromaBackend()

@router.post("/image-analysis")
async def full_image_analysis(file: UploadFile = File(...)):
    """
    Endpoint to analyze a food image and return estimated nutrition info.
    """
    try:
        # Step 1: Run image through the AI pipeline
        pipeline = ImagePipelineService()
        food_type, _, confidence = await pipeline.process_image(file)

        # Step 2: Get nutrition data from the active AI backend
        nutrition_data = agent.run_agent_dynamic(food_type)

        # Step 4: Ensure keys exist to avoid KeyError
        calories = nutrition_data.get("calories")
        recommendation = nutrition_data.get("recommendation", "")

        # Step 5: Return structured response
        return {
            "food": food_type,
            "estimated_calories": calories,
            "confidence": confidence,
            "recommendation": recommendation
        }

    except Exception as e:
        logger.error(f"Image analysis endpoint failed: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
