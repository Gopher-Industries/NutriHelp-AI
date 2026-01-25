from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from ultralytics import YOLO
import io
from PIL import Image

# Load YOLO model
model = YOLO(r"C:\Users\Naman Shah\OneDrive\Documents\Assignement_Deakin\T3\SIT764\Project\NutriHelp-AI\nutrihelp_ai\model\image_class.pt")

router = APIRouter(
    prefix="/ai-model/classifier",
    tags=["Classifier v2"],
)

# ============================
# Response Models (NA-112)
# ============================


class PredictionItem(BaseModel):
    class_name: str
    confidence: float


class ClassifierV2Response(BaseModel):
    top_prediction: PredictionItem
    top_3_predictions: List[PredictionItem]
    allergy_warning: Optional[str] = None
    message: str = "Classification successful"

# ============================
# POST /ai-model/classifier/v2
# YOLO Food Image Classifier with Allergy Check
# ============================


@router.post(
    "/v2",
    response_model=ClassifierV2Response,
    summary="Classifier v2 – Food Image Predictor with YOLO",
    description="Classifies food images using YOLO model and checks for allergen warnings."
)
async def classifier_v2_predict(
    image: UploadFile = File(..., description="Food image to analyze"),
    allergies: Optional[str] = Form(
        None,
        description="Comma-separated allergies (e.g. 'nuts,dairy,gluten,shellfish')"
    )
):
    try:
        image_bytes = await image.read()
        img = Image.open(io.BytesIO(image_bytes))
        print(image)
        results = model(img, max_det=3, save=True, verbose=False)
        print(results, "<<<<<<<<<<<")
        predictions = []

        # Check if results exist
        if results and len(results) > 0:
            result = results[0]

            # Check if it's a classification model (has probs attribute)
            if hasattr(result, 'probs') and result.probs is not None:
                # Classification model
                probs = result.probs

                # Get top 5 predictions
                if hasattr(probs, 'top5'):
                    top_indices = probs.top5
                    top_confidences = probs.top5conf.tolist()
                else:
                    # Alternative method for getting top predictions
                    all_probs = probs.data.cpu().numpy()
                    top_indices = all_probs.argsort()[-5:][::-1]
                    top_confidences = [float(all_probs[i])
                                       for i in top_indices]

                # Get class names
                class_names = result.names

                # Create predictions list (limit to top 3)
                for idx, conf in zip(top_indices[:3], top_confidences[:3]):
                    predictions.append({
                        "class_name": class_names[int(idx)],
                        "confidence": float(conf)
                    })

            # Check if it's a detection model (has boxes attribute)
            elif hasattr(result, 'boxes') and result.boxes is not None and len(result.boxes) > 0:
                # Detection model
                boxes = result.boxes

                # Extract data
                confidences = boxes.conf.cpu().tolist()
                classes = boxes.cls.cpu().tolist()
                class_names = result.names

                # Combine and sort by confidence
                detections = [(class_names[int(cls)], float(conf))
                              for cls, conf in zip(classes, confidences)]
                detections.sort(key=lambda x: x[1], reverse=True)

                # Take top 3
                for class_name, conf in detections[:3]:
                    predictions.append({
                        "class_name": class_name,
                        "confidence": conf
                    })

            else:
                # Try to extract any available predictions
                if hasattr(result, 'names') and hasattr(result, 'probs'):
                    print(f"Result type: {type(result)}")
                    print(f"Result attributes: {dir(result)}")
                    print(f"Probs: {result.probs}")

        # Fallback if no predictions
        if not predictions:
            raise HTTPException(
                status_code=400,
                detail="No food items detected in the image. Please upload a clearer image or check model format."
            )

        # Ensure we have at least top prediction
        top_pred = predictions[0]

        # Pad predictions to 3 if needed
        while len(predictions) < 3:
            predictions.append({
                "class_name": "unknown",
                "confidence": 0.0
            })

        # NA-113: Allergy restriction logic
        warning = None
        if allergies and allergies.strip():
            allergy_list = [a.strip().lower()
                            for a in allergies.split(",") if a.strip()]
            food_lower = top_pred["class_name"].lower()

            for allergy in allergy_list:
                if allergy in food_lower:
                    warning = f"⚠️ ALLERGY ALERT: '{top_pred['class_name']}' may contain '{allergy}'"
                    break

        return ClassifierV2Response(
            top_prediction=PredictionItem(**top_pred),
            top_3_predictions=[PredictionItem(**p) for p in predictions[:3]],
            allergy_warning=warning,
            message="Classification successful"
        )

    except HTTPException:
        raise
    except Exception as e:
        import traceback
        print(f"Error during prediction: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(
            status_code=500,
            detail=f"Error processing image: {str(e)}"
        )
