from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from nutrihelp_ai.services.image_pipeline import ImagePipelineService
from nutrihelp_ai.services.image_quality import InvalidImageError
from nutrihelp_ai.schemas import SingleImageAnalysisResponse
import logging

router = APIRouter()
logger = logging.getLogger(__name__)
pipeline = ImagePipelineService()

@router.post(
    "/image-analysis",
    response_model=SingleImageAnalysisResponse,
    summary="Full Image Analysis",
    description=(
        "Analyze a single food image and return classification, quality flags, top-k alternatives, "
        "and a local nutrition lookup."
    ),
)
async def full_image_analysis(
    file: UploadFile = File(...),
    topk: int = Query(5, ge=1, le=10, description="How many top classes to return"),
):
    """
    Endpoint to analyze a food image and return estimated nutrition info.
    """
    try:
        return await pipeline.process_image(file, topk=topk)
    except InvalidImageError as e:
        logger.warning("Image validation failed: %s", str(e))
        raise HTTPException(status_code=422, detail=str(e))
    except RuntimeError as e:
        logger.error("Single-image predictor unavailable: %s", str(e), exc_info=True)
        raise HTTPException(
            status_code=503,
            detail="Single-image model is unavailable. Check food_classifier.pth and model compatibility.",
        )
    except Exception as e:
        logger.error(f"Image analysis endpoint failed: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
