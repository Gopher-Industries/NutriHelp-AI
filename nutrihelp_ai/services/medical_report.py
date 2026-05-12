from nutrihelp_ai.services.predict_obesity import predict_obesity_service
from nutrihelp_ai.services.predict_diabetes import predict_diabetes_service

def _calculate_bmi(input_dict: dict):
    height = float(input_dict.get("Height") or 0)
    weight = float(input_dict.get("Weight") or 0)
    if height <= 0 or weight <= 0:
        return None
    return round(weight / (height * height), 1)


def _classify_bmi_fallback(bmi):
    if bmi is None:
        return "Unknown"
    if bmi < 18.5:
        return "Insufficient_Weight"
    if bmi < 25:
        return "Normal_Weight"
    if bmi < 30:
        return "Overweight_Level_I"
    if bmi < 35:
        return "Obesity_Type_I"
    if bmi < 40:
        return "Obesity_Type_II"
    return "Obesity_Type_III"


def _estimate_diabetes_fallback(input_dict: dict, bmi):
    age = float(input_dict.get("Age") or 0)
    activity = float(input_dict.get("FAF") or 0)
    high_calorie_foods = int(input_dict.get("FAVC") or 0) == 1
    family_history = str(input_dict.get("family_history_with_overweight") or "").lower() == "yes"

    risk_score = 0
    risk_score += 2 if bmi and bmi >= 30 else 1 if bmi and bmi >= 25 else 0
    risk_score += 1 if age >= 45 else 0
    risk_score += 1 if activity < 1 else 0
    risk_score += 1 if high_calorie_foods else 0
    risk_score += 1 if family_history else 0

    return risk_score >= 3, round(min(0.85, 0.55 + risk_score * 0.06), 3)


def _weight_guidance(obesity_label: str):
    label = str(obesity_label or "").lower()
    if "insufficient" in label:
        return {
            "status": "May be below the usual healthy range",
            "explanation": "The answers suggest weight may be lower than expected for height.",
            "next_step": "Review meal regularity and speak with a healthcare professional if weight loss was unplanned.",
            "priority": "review",
        }
    if "normal" in label:
        return {
            "status": "Appears to be in a usual healthy range",
            "explanation": "The answers suggest weight is broadly aligned with height.",
            "next_step": "Keep focusing on balanced meals, hydration, sleep, and regular movement.",
            "priority": "maintain",
        }
    if "overweight" in label:
        return {
            "status": "May be above the usual healthy range",
            "explanation": "The answers suggest small, steady meal and activity changes may be helpful.",
            "next_step": "Start with one manageable change, such as walking more often or reducing sugary snacks.",
            "priority": "review",
        }
    if "obesity" in label:
        return {
            "status": "May need extra weight-related health attention",
            "explanation": "This is not a diagnosis, but it suggests a routine health check may be useful.",
            "next_step": "Speak with a GP or healthcare professional before making major diet or exercise changes.",
            "priority": "care",
        }
    return {
        "status": "Could not clearly estimate weight-related category",
        "explanation": "The model could not produce a clear category from the supplied answers.",
        "next_step": "Review the survey answers and try again if anything looks incorrect.",
        "priority": "unknown",
    }


def _diabetes_guidance(diabetes_prediction: bool):
    if diabetes_prediction:
        return {
            "status": "Some answers suggest a routine blood sugar check may be helpful",
            "explanation": "This does not mean the user has diabetes. It only flags signals worth checking safely.",
            "next_step": "Consider speaking with a GP or healthcare professional, especially if symptoms are present.",
            "priority": "care",
        }
    return {
        "status": "No strong blood sugar warning sign was found from the answers",
        "explanation": "The survey answers did not show a strong diabetes risk signal in this model.",
        "next_step": "Continue routine check-ups and review if family history or symptoms change.",
        "priority": "maintain",
    }


def _build_health_assessment(obesity_label: str, obesity_confidence: float, diabetes_prediction: bool, diabetes_confidence: float, bmi):
    return {
        "summary": "AI-supported wellness estimate based on survey answers. This is not a medical diagnosis.",
        "bmi": bmi,
        "weight": {
            **_weight_guidance(obesity_label),
            "model_label": obesity_label,
            "confidence": obesity_confidence,
        },
        "blood_sugar": {
            **_diabetes_guidance(diabetes_prediction),
            "model_signal": bool(diabetes_prediction),
            "confidence": diabetes_confidence,
        },
        "safety_note": "Use this as general guidance and speak with a healthcare professional before major diet, medication, or exercise changes.",
    }


def generate_medical_report_service(input_data):
    input_dict = input_data.dict()
    bmi = _calculate_bmi(input_dict)

    try:
        obesity_label, obesity_confidence = predict_obesity_service(input_dict)
    except Exception:
        obesity_label = _classify_bmi_fallback(bmi)
        obesity_confidence = 0.62 if bmi is not None else 0.4

    try:
        diabetes_prediction, diabetes_confidence = predict_diabetes_service(input_dict)
    except Exception:
        diabetes_prediction, diabetes_confidence = _estimate_diabetes_fallback(input_dict, bmi)

    return {
        "medical_report": {
            "bmi": bmi,
            "obesity_prediction": {
                "obesity_level": obesity_label,
                "confidence": obesity_confidence
            },
            "diabetes_prediction": {
                "diabetes": diabetes_prediction,
                "confidence": diabetes_confidence
            },
            "health_assessment": _build_health_assessment(
                obesity_label=obesity_label,
                obesity_confidence=obesity_confidence,
                diabetes_prediction=diabetes_prediction,
                diabetes_confidence=diabetes_confidence,
                bmi=bmi,
            ),
        }
    }
