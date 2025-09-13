from fastapi import UploadFile
from PIL import Image
from nutrihelp_ai.services.Food_Image_Classifier.scripts.predict import predict_image
import os
import tempfile

class ImagePipelineService:
    async def process_image(self, file: UploadFile):
        # Step 1: Save uploaded file temporarily
        suffix = os.path.splitext(file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(await file.read())
            temp_path = tmp.name

        print("[Stage 1] Image received and loaded.")

        # Step 2: Run prediction using your trained model
        result = predict_image(temp_path)
        food_type = result["predicted_class"]
        confidence = result["confidence"]  # get confidence from predict_image
        print(f"[Stage 2] Food classification complete: {food_type} ({confidence:.2f})")

        # Step 3: Estimate calories (dummy logic for now)
        estimated_calories = 200  # placeholder
        print(f"[Stage 3] Calorie estimation complete: {estimated_calories} kcal")

        # Return confidence as well
        return food_type, estimated_calories, confidence