# nutrihelp_ai/services/predict_diabetes.py

from nutrihelp_ai.utils.exceptions import InvalidInputException

def predict_diabetes_service(data: dict):
    try:
        glucose = float(data.get("glucose", 0))
        bmi = float(data.get("bmi", 0))
        age = int(data.get("age", 0))
    except (ValueError, TypeError):
        raise InvalidInputException("Input values must be numeric")

    # --- Dummy logic: Replace with real ML model in production ---
    if glucose > 125 or bmi > 30 or age > 50:
        prediction = "diabetes"
        probability = 0.85
    else:
        prediction = "no_diabetes"
        probability = 0.75

    return {
        "prediction": prediction,
        "probability": probability
    }
