# nutrihelp_ai/routers/multi_image_api.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from nutrihelp_ai.services.multi_image_pipeline import MultiImagePipelineService
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


pipeline = MultiImagePipelineService()

@router.post(
    "/multi-image-analysis",
    summary="Multi Image Classification",
    description="Analyze multiple images and return predicted labels and confidences"
)
async def multi_image_analysis(files: List[UploadFile] = File(...)):
    """
    Endpoint to analyze multiple images.
    Returns:
    - labels
    - confidences
    """
    try:
        results = await pipeline.process_images(files)
        return {"predictions": results}

    except Exception as e:
        logger.error(f"Multi-image analysis endpoint failed: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
