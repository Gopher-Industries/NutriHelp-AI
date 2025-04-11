import numpy as np
import joblib
import tensorflow as tf
import pandas as pd

# Load preprocessor, label encoder, and model
preprocessor = joblib.load("nutrihelp_ai/model/obesity_preprocessor.pkl")
label_encoder = joblib.load("nutrihelp_ai/model/obesity_label_encoder.pkl")
model = tf.keras.models.load_model("nutrihelp_ai/model/obesity_model.keras")


def predict_obesity_service(input_data):
    try:
        # Convert input to dictionary and wrap in list (1 sample)
        input_df = pd.DataFrame([input_data.dict()])  # ✅ DataFrame with named columns

        # Transform with preprocessor (expects DataFrame with column names)
        processed_input = preprocessor.transform(input_df)

        # Predict
        prediction = model.predict(processed_input)
        predicted_index = np.argmax(prediction)
        predicted_label = label_encoder.inverse_transform([predicted_index])[0]

        return {
            "status": "success",
            "prediction": predicted_label
        }

    except Exception as e:
        raise RuntimeError(f"Prediction failed: {e}")
