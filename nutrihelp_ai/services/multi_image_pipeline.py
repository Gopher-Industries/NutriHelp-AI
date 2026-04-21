from typing import Any, Dict, List, Optional

from fastapi import UploadFile

from nutrihelp_ai.services.image_quality import ImageQualityService, InvalidImageError
from nutrihelp_ai.services.multi_image_classifier.scripts.training.predict import Predictor
import logging

logger = logging.getLogger(__name__)

DEFAULT_TOPK = 5
UNCLEAR_THRESHOLD = 0.25
UNCLEAR_SUGGESTION = "Please upload a clearer image."


class MultiImagePipelineService:
    def __init__(self):
        self.predictor = None
        self._predictor_error: Optional[str] = None
        self.quality_service = ImageQualityService()

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
            logger.error("Failed to initialize multi-image predictor: %s", exc, exc_info=True)
            raise RuntimeError(self._predictor_error) from exc

    async def process_images(
        self,
        files: List[UploadFile],
        topk: int = DEFAULT_TOPK,
    ) -> List[Dict[str, Any]]:
        results: List[Dict[str, Any]] = []
        predictor = self._get_predictor()
        safe_topk = max(1, int(topk)) if topk is not None else DEFAULT_TOPK

        for file in files:
            try:
                if file.content_type and not file.content_type.startswith("image/"):
                    raise InvalidImageError("Uploaded file must use an image content type.")

                image_bytes = await file.read()
                quality = self.quality_service.analyze(image_bytes)
                pred = predictor.predict_from_bytes(image_bytes, safe_topk)

                topk_items = [
                    {"label": label, "score": round(float(score), 4)}
                    for label, score in zip(
                        pred.get("topk_labels", []) or [],
                        pred.get("topk_scores", []) or [],
                    )
                ]
                matches = [
                    {"label": label, "score": round(float(score), 4)}
                    for label, score in zip(
                        pred.get("labels", []) or [],
                        pred.get("confidences", []) or [],
                    )
                ]

                label = topk_items[0]["label"] if topk_items else None
                confidence = float(topk_items[0]["score"]) if topk_items else 0.0
                quality_unclear = bool(quality.get("should_mark_unclear", False))
                low_confidence = confidence < UNCLEAR_THRESHOLD
                is_unclear = quality_unclear or low_confidence

                reasons: List[str] = []
                if low_confidence:
                    reasons.append(
                        f"Top-1 confidence {confidence:.2f} below threshold {UNCLEAR_THRESHOLD:.2f}."
                    )
                reasons.extend(quality.get("issues", []))

                results.append(
                    {
                        "label": label,
                        "confidence": confidence,
                        "matches": matches,
                        "topk": topk_items,
                        "is_unclear": is_unclear,
                        "unclear_reason": " ".join(reasons).strip(),
                        "suggestion": UNCLEAR_SUGGESTION if is_unclear else "",
                        "quality": self.quality_service.response_payload(quality),
                        "error": None,
                    }
                )

            except Exception as e:
                logger.error(
                    "Failed to process image %s: %s",
                    getattr(file, "filename", ""),
                    e,
                    exc_info=True,
                )
                results.append(
                    {
                        "label": None,
                        "confidence": 0.0,
                        "matches": [],
                        "topk": [],
                        "is_unclear": True,
                        "unclear_reason": str(e) if isinstance(e, InvalidImageError) else "Processing error occurred.",
                        "suggestion": UNCLEAR_SUGGESTION,
                        "quality": self.quality_service.fallback_payload([str(e)]),
                        "error": "Failed to process this image",
                    }
                )

        return results
