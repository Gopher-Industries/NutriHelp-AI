import numpy as np
import joblib
import tensorflow as tf
import pandas as pd
from nutrihelp_ai.utils.exceptions import InvalidInputException, ModelNotLoadedException

# Load model components at module-level to avoid reloading each request
try:
    preprocessor = joblib.load("nutrihelp_ai/model/obesity_preprocessor.pkl")
    label_encoder = joblib.load("nutrihelp_ai/model/obesity_label_encoder.pkl")
    model = tf.keras.models.load_model("nutrihelp_ai/model/obesity_model.keras")
except Exception:
    preprocessor = None
    label_encoder = None
    model = None

def predict_obesity_service(input_data):
    if preprocessor is None or label_encoder is None or model is None:
        raise ModelNotLoadedException()

    try:
        # Convert Pydantic input to a one-row DataFrame
        input_df = pd.DataFrame([input_data.dict()])

        # Preprocess the input (will raise if input columns mismatch)
        processed_input = preprocessor.transform(input_df)

        # Predict using the trained model
        prediction_probs = model.predict(processed_input)

        # Get class with highest probability
        predicted_index = int(np.argmax(prediction_probs))
        predicted_label = label_encoder.inverse_transform([predicted_index])[0]
        probability = float(np.max(prediction_probs))

        return {
            "status": "success",
            "prediction": predicted_label,
            "probability": round(probability, 4)
        }

    except ValueError as ve:
        raise InvalidInputException(f"Input preprocessing failed: {ve}")
    except Exception as e:
        raise RuntimeError(f"Prediction failed: {str(e)}")
