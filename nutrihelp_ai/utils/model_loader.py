# nutrihelp_ai/utils/model_loader.py
import joblib
import tensorflow as tf
from nutrihelp_ai.utils.exceptions import ModelNotLoadedException

# Centralized model path registry
MODEL_PATHS = {
    "obesity_model": "nutrihelp_ai/model/obesity_model.keras",
    "obesity_preprocessor": "nutrihelp_ai/model/obesity_preprocessor.pkl",
    "obesity_label_encoder": "nutrihelp_ai/model/obesity_label_encoder.pkl",
    "diabetes_model": "nutrihelp_ai/model/diabetes_model.keras",
    "diabetes_scaler": "nutrihelp_ai/model/diabetes_scaler.pkl",

}

def load_keras_model(name: str):
    try:
        path = MODEL_PATHS[name]
        return tf.keras.models.load_model(path)
    except Exception as e:
        raise ModelNotLoadedException(f"Failed to load Keras model '{name}': {e}")

def load_joblib_file(name: str):
    try:
        path = MODEL_PATHS[name]
        return joblib.load(path)
    except Exception as e:
        raise ModelNotLoadedException(f"Failed to load joblib file '{name}': {e}")
