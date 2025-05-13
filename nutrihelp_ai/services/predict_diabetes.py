import pandas as pd
import joblib
import tensorflow as tf
import numpy as np
from nutrihelp_ai.utils.exceptions import InvalidInputException, ModelNotLoadedException

# Model files
MODEL_PATH = "nutrihelp_ai/model/diabetes_model.keras"
SCALER_PATH = "nutrihelp_ai/model/diabetes_scaler.pkl"

# Expected input fields
REQUIRED_FEATURES = [
    "Gender", "Age", "Height", "Weight", "FAVC", "FCVC",
    "NCP", "CAEC", "SMOKE", "CH2O", "FAF", "CALC"
]

def predict_diabetes_service(input_dict: dict):
    try:
        # Load model + scaler
        model = tf.keras.models.load_model(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)

        # Extract and prepare input
        filtered = {key: input_dict[key] for key in REQUIRED_FEATURES if key in input_dict}
        input_df = pd.DataFrame([filtered])
        scaled_input = scaler.transform(input_df)

        # Predict
        probability = float(model.predict(scaled_input)[0][0])
        prediction = probability >= 0.5

        return prediction, round(probability, 3)

    except FileNotFoundError as fnf:
        raise ModelNotLoadedException(f"Model file not found: {fnf}")
    except Exception as e:
        raise InvalidInputException(f"Diabetes prediction failed: {e}")
