import pandas as pd
import joblib
import tensorflow as tf
import numpy as np
from nutrihelp_ai.utils.exceptions import InvalidInputException, ModelNotLoadedException
from nutrihelp_ai.utils.model_loader import load_keras_model, load_joblib_file, MODEL_PATHS



# Expected input fields
REQUIRED_FEATURES = [
    "Gender", "Age", "Height", "Weight", "FAVC", "FCVC",
    "NCP", "CAEC", "SMOKE", "CH2O", "FAF", "CALC"
]

def predict_diabetes_service(input_dict: dict):
    try:
        # Load model + scaler
        model = load_keras_model("diabetes_model")
        scaler = load_joblib_file("diabetes_scaler")

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
