import numpy as np
import joblib
import tensorflow as tf
import pandas as pd
from nutrihelp_ai.utils.exceptions import InvalidInputException, ModelNotLoadedException
from nutrihelp_ai.services.predict_obesity import predict_obesity_service
from nutrihelp_ai.services.predict_diabetes import predict_diabetes_service
from nutrihelp_ai.utils.model_loader import load_keras_model, load_joblib_file, MODEL_PATHS


# Load obesity model components
try:
    preprocessor = load_joblib_file("obesity_preprocessor")
    label_encoder = load_joblib_file("obesity_label_encoder")
    obesity_model = load_keras_model("obesity_model")
except Exception:
    preprocessor = None
    label_encoder = None
    obesity_model = None

# Load diabetes model components
try:
    diabetes_model = load_keras_model("diabetes_model")
    diabetes_scaler = load_joblib_file("diabetes_scaler")
except Exception:
    diabetes_model = None
    diabetes_scaler = None

# Features used by each model
required_diabetes_features = [
    "Gender", "Age", "Height", "Weight", "FAVC", "FCVC",
    "NCP", "CAEC", "SMOKE", "CH2O", "FAF", "CALC"
]

required_obesity_features = None  # Will use all for now

def generate_medical_report_service(input_data):
    if not all([diabetes_model, diabetes_scaler]):
        raise ModelNotLoadedException()

    input_dict = input_data.dict()

    # ===== OBESITY PREDICTION =====
    obesity_label, obesity_confidence = predict_obesity_service(input_dict)

    # ===== DIABETES PREDICTION =====
    diabetes_prediction, diabetes_confidence = predict_diabetes_service(input_dict)

    return {
        "medical_report": {
            "obesity_prediction": {
                "obesity_level": obesity_label,
                "confidence": obesity_confidence
            },
            "diabetes_prediction": {
                "diabetes": diabetes_prediction,
                "confidence": diabetes_confidence
            }
        }
    }
