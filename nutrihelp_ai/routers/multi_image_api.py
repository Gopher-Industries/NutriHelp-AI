# nutrihelp_ai/routers/multi_image_api.py
from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from typing import List
from nutrihelp_ai.services.multi_image_pipeline import MultiImagePipelineService
from nutrihelp_ai.schemas import MultiImageAnalysisResponse
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

pipeline = MultiImagePipelineService()

@router.post(
    "/multi-image-analysis",
    response_model=MultiImageAnalysisResponse,
    summary="Multi Image Classification",
    description=(
        "Analyze multiple images and return standardized predictions with quality flags, "
        "top-k alternatives, and an 'unclear image' signal."
    ),
)
async def multi_image_analysis(
    files: List[UploadFile] = File(...),
    topk: int = Query(5, ge=1, le=50, description="How many top classes to return per image"),
):
    try:
        results = await pipeline.process_images(files, topk=topk)
        return {"predictions": results}
    except RuntimeError as e:
        logger.error("Multi-image predictor unavailable: %s", str(e), exc_info=True)
        raise HTTPException(
            status_code=503,
            detail="Multi-image model is unavailable. Check multi_image_classifier.pt and model compatibility.",
        )
    except Exception as e:
        logger.error(f"Multi-image analysis endpoint failed: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
