import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import joblib

#---------------------- Methods Start Here ----------------------#
def predict(input, model_path='diabetes_model.keras', scaler_path='scaler.pkl'):
    model = load_model(model_path)

    scaler = joblib.load(scaler_path)

    if not model:
        raise Exception("Model not found.")
    if not scaler:
        raise Exception("Encoder not found.")

    input = pd.DataFrame([input])
    input = scaler.transform(input)
    y_pred_prob = model.predict(input)
    
    y_pred_class = np.round(y_pred_prob)
    if y_pred_class == 1:
        confidence = y_pred_prob[0][0] * 100
    else:
        confidence = (1 - y_pred_prob[0][0]) * 100

    has_diabetes = True if y_pred_class == 1 else False
    return has_diabetes, confidence

#---------------------- Example Usage ----------------------#
input_data_high_risk = {
    'Gender': 1,            # Male (slightly higher risk in some populations)
    'Age': 65,              # Older age (risk increases with age)
    'Height': 1.70,         # Average height
    'Weight': 100,          # High BMI (~34.6 – Obese)
    'FAVC': 3000,           # High caloric intake
    'FCVC': 0,              # No vegetables consumed
    'NCP': 5,               # High number of meals per day
    'CAEC': 3,              # Frequent use of car (sedentary behavior)
    'SMOKE': 1,             # Smoker (linked to insulin resistance)
    'CH2O': 1,              # Low water intake
    'FAF': 0,               # No physical activity
    'CALC': 2               # Frequent alcohol consumption
}

has_diabetes, confidence = predict(input_data_high_risk, 
                                   model_path='models/diabetes_model.keras',
                                   scaler_path='AI-ProjectD/Diabetes-Prediction/scaler.pkl')
print(f"Diabetes: {has_diabetes}, Confidence: {confidence}%")