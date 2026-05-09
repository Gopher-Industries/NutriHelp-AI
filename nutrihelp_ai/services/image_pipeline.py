import logging
from typing import Any, Dict, List, Optional

from fastapi import UploadFile

from nutrihelp_ai.services.Food_Image_Classifier.scripts.predict import Predictor
from nutrihelp_ai.services.image_quality import ImageQualityService, InvalidImageError
from nutrihelp_ai.services.nutrition_lookup import NutritionLookupService


logger = logging.getLogger(__name__)

DEFAULT_TOPK = 5
# The classifier is closed-set: every image is forced into one of the known food
# classes. Keep nutrition enrichment conservative so non-food or ambiguous images
# do not look like confirmed meals.
CONFIRMATION_THRESHOLD = 0.90
AMBIGUITY_MARGIN = 0.15
UNCLEAR_SUGGESTION = "Please upload a clearer food image or confirm the dish manually."
UNCLEAR_NUTRITION_SOURCE = "withheld_unclear_prediction"
REJECTED_SUGGESTION = (
    "Please upload a clear food photo. The current image could not be validated as a food item."
)
REJECTED_NUTRITION_SOURCE = "withheld_rejected_image"

def get_confidence_tier(confidence: float) -> str:
    if confidence >= CONFIRMATION_THRESHOLD:
        return "high"
    elif confidence >= 0.50:
        return "medium"
    else:
        return "low"


def get_second_score(topk_items: List[Dict[str, Any]]) -> float:
    if len(topk_items) < 2:
        return 0.0
    return float(topk_items[1].get("score", 0.0))

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

        top3_predictions = [
            {"class": item["label"], "confidence": item["score"]}
            for item in topk_items[:3]
        ]

        prediction_rejected = bool(quality.get("should_reject_prediction", False))
        public_label = None if prediction_rejected else label
        public_confidence = 0.0 if prediction_rejected else confidence
        public_topk = [] if prediction_rejected else topk_items
        matches: List[Dict[str, Any]] = public_topk[:1] if public_label else []

        quality_unclear = bool(quality.get("should_mark_unclear", False))
        low_confidence = False if prediction_rejected else confidence < CONFIRMATION_THRESHOLD
        second_score = get_second_score(topk_items)
        ambiguous_prediction = (
            False
            if prediction_rejected
            else second_score > 0 and (confidence - second_score) < AMBIGUITY_MARGIN
        )
        is_unclear = prediction_rejected or quality_unclear or low_confidence or ambiguous_prediction

        reasons: List[str] = []
        if prediction_rejected:
            reasons.append("Image could not be validated as a clear food photo.")
        if low_confidence:
            reasons.append(
                f"Top-1 confidence {confidence:.2f} below confirmation threshold {CONFIRMATION_THRESHOLD:.2f}."
            )
        if ambiguous_prediction:
            reasons.append(
                f"Top predictions are close together; margin {confidence - second_score:.2f} below {AMBIGUITY_MARGIN:.2f}."
            )
        reasons.extend(quality.get("issues", []))
        unclear_reason = " ".join(reasons).strip()

        nutrition = (
            self.nutrition_lookup.unavailable(
                public_label,
                source=REJECTED_NUTRITION_SOURCE
                if prediction_rejected
                else UNCLEAR_NUTRITION_SOURCE,
            )
            if is_unclear
            else self.nutrition_lookup.lookup(public_label)
        )
        recommendation = self.nutrition_lookup.build_recommendation(
            nutrition,
            is_unclear=is_unclear,
        )

        return {
            "label": public_label,
            "confidence": public_confidence,
            "matches": matches,
            "topk": public_topk,
            "is_unclear": is_unclear,
            "unclear_reason": unclear_reason,
            "suggestion": REJECTED_SUGGESTION
            if prediction_rejected
            else UNCLEAR_SUGGESTION
            if is_unclear
            else "",
            "quality": self.quality_service.response_payload(quality),
            "error": None,
            "nutrition": nutrition,
            "recommendation": recommendation,
            "confidence_tier": get_confidence_tier(public_confidence),
            "retake_needed": is_unclear,
            "retake_reason": unclear_reason if is_unclear else None,
            "top3_predictions": top3_predictions if not prediction_rejected else [],
        }
