import numpy as np
import joblib
import tensorflow as tf
import pandas as pd
from nutrihelp_ai.utils.exceptions import InvalidInputException, ModelNotLoadedException
from nutrihelp_ai.services.predict_obesity import predict_obesity_service
from nutrihelp_ai.services.predict_diabetes import predict_diabetes_service
<<<<<<< HEAD
from nutrihelp_ai.services.nutribot.Agents import AgentClass  # <-- NutriBot agent
=======
from nutrihelp_ai.utils.model_loader import load_keras_model, load_joblib_file, MODEL_PATHS

>>>>>>> f52e7122478d8cf656be02d9464e313ee486eefa

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

def _build_nutribot_prompt(obesity_label: str, obesity_conf: float, diabetes_pos: bool, diabetes_conf: float) -> str:
    """
    Create a short, structured summary for NutriBot to turn into user-friendly advice.
    """
    diab_str = "Positive (higher risk)" if diabetes_pos else "Negative (lower risk)"
    return (
        "Please generate a short, supportive, and actionable health recommendation (2–3 sentences) "
        "based on the following risk summary. Avoid medical diagnoses; focus on daily lifestyle tips.\n\n"
        f"- Obesity status: {obesity_label} (confidence {obesity_conf}%).\n"
        f"- Diabetes risk: {diab_str} (confidence {diabetes_conf}%).\n\n"
        "Keep it clear and encouraging, with simple steps the user can try this week."
    )


def _get_nutribot_recommendation(obesity_label: str, obesity_conf: float, diabetes_pos: bool, diabetes_conf: float) -> str:
    """
    Call the NutriBot Agent to convert model outputs into a human-friendly message.
    Gracefully degrade if NutriBot fails.
    """
    try:
        prompt = _build_nutribot_prompt(obesity_label, obesity_conf, diabetes_pos, diabetes_conf)
        agent = AgentClass()
        msg = agent.run_agent(prompt)
        # Agent returns plain text in res["output"] -> run_agent already extracts it.
        return msg.strip() if isinstance(msg, str) and msg.strip() else "Recommendation currently unavailable."
    except Exception:
        # Do not break the endpoint if NutriBot is unavailable
        return "Recommendation currently unavailable."

def generate_medical_report_service(input_data):
    if not all([diabetes_model, diabetes_scaler]):
        raise ModelNotLoadedException()

    input_dict = input_data.dict()

    # ===== OBESITY PREDICTION =====
    obesity_label, obesity_confidence = predict_obesity_service(input_dict)

    # ===== DIABETES PREDICTION =====
    diabetes_prediction, diabetes_confidence = predict_diabetes_service(input_dict)

    # ===== NUTRIBOT RECOMMENDATION (NEW) =====
    nutribot_msg = _get_nutribot_recommendation(
        obesity_label=obesity_label,
        obesity_conf=obesity_confidence,
        diabetes_pos=bool(diabetes_prediction),
        diabetes_conf=diabetes_confidence,
    )

    return {
        "medical_report": {
            "obesity_prediction": {
                "obesity_level": obesity_label,
                "confidence": obesity_confidence
            },
            "diabetes_prediction": {
                "diabetes": diabetes_prediction,
                "confidence": diabetes_confidence
            },
            "nutribot_recommendation": nutribot_msg
        }
    }
