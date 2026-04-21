import logging
from typing import Any, Dict, List, Optional

from fastapi import UploadFile

from nutrihelp_ai.services.Food_Image_Classifier.scripts.predict import Predictor
from nutrihelp_ai.services.image_quality import ImageQualityService, InvalidImageError
from nutrihelp_ai.services.nutrition_lookup import NutritionLookupService


logger = logging.getLogger(__name__)

DEFAULT_TOPK = 5
UNCLEAR_THRESHOLD = 0.60
UNCLEAR_SUGGESTION = "Please upload a clearer, closer food image."


class ImagePipelineService:
    def __init__(self):
        self.predictor = None
        self._predictor_error: Optional[str] = None
        self.quality_service = ImageQualityService()
        self.nutrition_lookup = NutritionLookupService()

    def _get_predictor(self) -> Predictor:
        if self.predictor is not None:
            return self.predictor
        if self._predictor_error is not None:
            raise RuntimeError(self._predictor_error)

        try:
            self.predictor = Predictor()
            return self.predictor
        except Exception as exc:
            self._predictor_error = str(exc)
            logger.error("Failed to initialize single-image predictor: %s", exc, exc_info=True)
            raise RuntimeError(self._predictor_error) from exc

    async def process_image(
        self,
        file: UploadFile,
        topk: int = DEFAULT_TOPK,
    ) -> Dict[str, Any]:
        if file.content_type and not file.content_type.startswith("image/"):
            raise InvalidImageError("Uploaded file must use an image content type.")

        image_bytes = await file.read()
        quality = self.quality_service.analyze(image_bytes)
        predictor = self._get_predictor()
        prediction = predictor.predict_from_bytes(image_bytes, topk=topk)

        topk_items = list(prediction.get("topk", []))
        label = prediction.get("label")
        confidence = float(prediction.get("confidence", 0.0))
        matches: List[Dict[str, Any]] = topk_items[:1] if label else []

        quality_unclear = bool(quality.get("should_mark_unclear", False))
        low_confidence = confidence < UNCLEAR_THRESHOLD
        is_unclear = quality_unclear or low_confidence

        reasons: List[str] = []
        if low_confidence:
            reasons.append(
                f"Top-1 confidence {confidence:.2f} below threshold {UNCLEAR_THRESHOLD:.2f}."
            )
        reasons.extend(quality.get("issues", []))
        unclear_reason = " ".join(reasons).strip()

        nutrition = self.nutrition_lookup.lookup(label)
        recommendation = self.nutrition_lookup.build_recommendation(
            nutrition,
            is_unclear=is_unclear,
        )

        return {
            "label": label,
            "confidence": confidence,
            "matches": matches,
            "topk": topk_items,
            "is_unclear": is_unclear,
            "unclear_reason": unclear_reason,
            "suggestion": UNCLEAR_SUGGESTION if is_unclear else "",
            "quality": self.quality_service.response_payload(quality),
            "error": None,
            "nutrition": nutrition,
            "recommendation": recommendation,
        }
