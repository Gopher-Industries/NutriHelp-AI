# # nutrihelp_ai/services/multi_image_pipeline.py
# import asyncio
# import tempfile
# import os
# from typing import List, Dict, Any
# from fastapi import UploadFile
# from PIL import Image
# from nutrihelp_ai.services.multi_image_classifier.scripts.training.predict import Predictor
# import logging

# logger = logging.getLogger(__name__)

# class MultiImagePipelineService:
#     def __init__(self):
#         self.predictor = Predictor()

#     async def process_images(self, files: List[UploadFile]) -> List[Dict[str, Any]]:
#         """
#         Process multiple UploadFile images and return predictions.
#         Only labels and confidences are returned.
#         """
#         results = []
#         loop = asyncio.get_running_loop()

#         for file in files:
#             try:
#                 suffix = os.path.splitext(file.filename)[1]
#                 with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
#                     tmp.write(await file.read())
#                     temp_path = tmp.name

#                 print(f"[Stage 1] Image saved temporarily: {temp_path}")

#                 prediction = await loop.run_in_executor(
#                     None, self.predictor.predict_paths, [temp_path]
#                 )
#                 result = {
#                     "labels": prediction[0].get("labels", []),
#                     "confidences": prediction[0].get("confidences", [])
#                 }

#                 print(f"[Stage 2] Prediction complete: {result['labels']}")

#                 os.remove(temp_path)
#                 print(f"[Stage 3] Temporary file deleted: {temp_path}")

#                 results.append(result)

#             except Exception as e:
#                 logger.error(f"Failed to process image {file.filename}: {e}", exc_info=True)
#                 results.append({
#                     "error": "Failed to process this image"
#                 })

#         return results


# nutrihelp_ai/services/multi_image_pipeline.py
import asyncio
import tempfile
import os
from typing import List, Dict, Any, Optional
from fastapi import UploadFile
from nutrihelp_ai.services.multi_image_classifier.scripts.training.predict import Predictor
import logging

logger = logging.getLogger(__name__)

DEFAULT_TOPK = 5

# Internal threshold (not exposed to Swagger)
UNCLEAR_THRESHOLD = 0.25

# User-facing suggestion
UNCLEAR_SUGGESTION = "Please upload a clearer image."


class MultiImagePipelineService:
    def __init__(self):
        self.predictor = Predictor()

    async def process_images(
        self,
        files: List[UploadFile],
        topk: int = DEFAULT_TOPK,
    ) -> List[Dict[str, Any]]:
        results: List[Dict[str, Any]] = []
        loop = asyncio.get_running_loop()

        safe_topk = max(1, int(topk)) if topk is not None else DEFAULT_TOPK

        for file in files:
            temp_path: Optional[str] = None
            try:
                suffix = os.path.splitext(file.filename or "")[1]
                if not suffix:
                    suffix = ".jpg"

                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                    tmp.write(await file.read())
                    temp_path = tmp.name

                prediction_list = await loop.run_in_executor(
                    None, self.predictor.predict_paths, [temp_path], safe_topk
                )

                if not prediction_list:
                    results.append(
                        {
                            "labels": [],
                            "confidences": [],
                            "max_label": None,
                            "max_conf": 0.0,
                            "topk_labels": [],
                            "topk_scores": [],
                            "is_unclear": True,
                            "unclear_reason": "No prediction returned by model.",
                            "suggestion": UNCLEAR_SUGGESTION,
                        }
                    )
                    continue

                pred = prediction_list[0]

                topk_labels = pred.get("topk_labels", []) or []
                topk_scores = pred.get("topk_scores", []) or []

                if topk_labels and topk_scores:
                    max_label = topk_labels[0]
                    max_conf = float(topk_scores[0])
                else:
                    scores = pred.get("scores", []) or []
                    max_label = None
                    max_conf = float(max(scores)) if scores else 0.0

                is_unclear = max_conf < UNCLEAR_THRESHOLD
                unclear_reason = (
                    f"Top-1 confidence {max_conf:.2f} below threshold {UNCLEAR_THRESHOLD:.2f}."
                    if is_unclear
                    else ""
                )

                result = {
                    "labels": pred.get("labels", []) or [],
                    "confidences": pred.get("confidences", []) or [],
                    "max_label": max_label,
                    "max_conf": max_conf,
                    "topk_labels": topk_labels,
                    "topk_scores": topk_scores,
                    "is_unclear": is_unclear,
                    "unclear_reason": unclear_reason,
                }

                if is_unclear:
                    result["suggestion"] = UNCLEAR_SUGGESTION

                results.append(result)

            except Exception as e:
                logger.error(
                    f"Failed to process image {getattr(file, 'filename', '')}: {e}",
                    exc_info=True,
                )
                results.append(
                    {
                        "error": "Failed to process this image",
                        "is_unclear": True,
                        "unclear_reason": "Processing error occurred.",
                        "suggestion": UNCLEAR_SUGGESTION,
                    }
                )
            finally:
                if temp_path and os.path.exists(temp_path):
                    try:
                        os.remove(temp_path)
                    except Exception:
                        pass

        return results
