# nutrihelp_ai/services/multi_image_pipeline.py
import asyncio
import tempfile
import os
from typing import List, Dict, Any
from fastapi import UploadFile
from PIL import Image
from nutrihelp_ai.services.multi_image_classifier.scripts.training.predict import Predictor
import logging

logger = logging.getLogger(__name__)

class MultiImagePipelineService:
    def __init__(self):
        self.predictor = Predictor()

    async def process_images(self, files: List[UploadFile]) -> List[Dict[str, Any]]:
        """
        Process multiple UploadFile images and return predictions.
        Only labels and confidences are returned.
        """
        results = []
        loop = asyncio.get_running_loop()

        for file in files:
            try:
                suffix = os.path.splitext(file.filename)[1]
                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                    tmp.write(await file.read())
                    temp_path = tmp.name

                print(f"[Stage 1] Image saved temporarily: {temp_path}")

                prediction = await loop.run_in_executor(
                    None, self.predictor.predict_paths, [temp_path]
                )
                result = {
                    "labels": prediction[0].get("labels", []),
                    "confidences": prediction[0].get("confidences", [])
                }

                print(f"[Stage 2] Prediction complete: {result['labels']}")

                os.remove(temp_path)
                print(f"[Stage 3] Temporary file deleted: {temp_path}")

                results.append(result)

            except Exception as e:
                logger.error(f"Failed to process image {file.filename}: {e}", exc_info=True)
                results.append({
                    "error": "Failed to process this image"
                })

        return results
