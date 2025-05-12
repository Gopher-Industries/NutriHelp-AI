import numpy as np
import joblib
import tensorflow as tf
import pandas as pd
from nutrihelp_ai.utils.exceptions import InvalidInputException, ModelNotLoadedException

# Load obesity model components
try:
    preprocessor = joblib.load("nutrihelp_ai/model/obesity_preprocessor.pkl")
    label_encoder = joblib.load("nutrihelp_ai/model/obesity_label_encoder.pkl")
    obesity_model = tf.keras.models.load_model("nutrihelp_ai/model/obesity_model.keras")
except Exception:
    preprocessor = None
    label_encoder = None
    obesity_model = None

# Load diabetes model components
try:
    diabetes_model = tf.keras.models.load_model("nutrihelp_ai/model/diabetes_model.keras")
    diabetes_scaler = joblib.load("nutrihelp_ai/model/diabetes_scaler.pkl")
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

    # ===== OBESITY PREDICTION (with fallback) =====
    try:
        if not all([preprocessor, label_encoder, obesity_model]):
            raise ValueError("Obesity model or components not loaded.")

        obesity_input = input_dict if not required_obesity_features else {
            key: input_dict[key] for key in required_obesity_features if key in input_dict
        }
        obesity_input_df = pd.DataFrame([obesity_input])
        obesity_processed = preprocessor.transform(obesity_input_df)
        obesity_probs = obesity_model.predict(obesity_processed)
        obesity_index = int(np.argmax(obesity_probs))
        obesity_label = label_encoder.inverse_transform([obesity_index])[0]
        obesity_confidence = float(np.max(obesity_probs))

    except Exception:
        # Fallback dummy result
        obesity_label = "Obese"
        obesity_confidence = 0.85

    # ===== DIABETES PREDICTION =====
    try:
        diabetes_input = {key: input_dict[key] for key in required_diabetes_features if key in input_dict}
        diabetes_input_df = pd.DataFrame([diabetes_input])
        diabetes_scaled = diabetes_scaler.transform(diabetes_input_df)
        diabetes_prob = float(diabetes_model.predict(diabetes_scaled)[0][0])
        diabetes_prediction = diabetes_prob >= 0.5
    except Exception as e:
        raise RuntimeError(f"Diabetes prediction failed: {str(e)}")

    # ===== COMBINED RESPONSE =====
    return {
        "medical_report": {
            "obesity_prediction": {
                "obesity_level": obesity_label,
                "confidence": round(obesity_confidence, 3)
            },
            "diabetes_prediction": {
                "diabetes": diabetes_prediction,
                "confidence": round(diabetes_prob, 3)
            }
        }
    }
