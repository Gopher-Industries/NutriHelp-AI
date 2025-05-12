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
        raise Exception("Scaler not found.")

    input = pd.DataFrame([input])
    input = scaler.transform(input)
    y_pred_prob = model.predict(input)
    
    y_pred_class = np.round(y_pred_prob)
    if y_pred_class == 1:
        confidence = round(y_pred_prob[0][0] * 100, 2)
    else:
        confidence = round((1 - y_pred_prob[0][0]) * 100, 2)

    has_diabetes = True if y_pred_class == 1 else False
    return has_diabetes, confidence

#---------------------- Example Usage ----------------------#
input_data_high_risk = {
    'Gender': 1,            # Gender (1:Male, 2:Female)
    'Age': 65,              # Age (year)
    'Height': 1.70,         # Height (metre)
    'Weight': 100,          # Weight (kg)
    'FAVC': 3000,           # Calories intake (cal)
    'FCVC': 0,              # Vegetables consumption (number of meals contain vege)
    'NCP': 5,               # Number of meals per day e.g. Dinner
    'CAEC': 3,              # Frequent eat between main meals e.g. Brunch
    'SMOKE': 1,             # Smoker (1:Yes, 0, No)
    'CH2O': 1,              # Water intake (litre)
    'FAF': 0,               # Physical activity (hours)
    'CALC': 2               # Alcohol consumption frequency (0:Never, 1:Sometimes, 2:Frequent)
}

has_diabetes, confidence = predict(input_data_high_risk, 
                                   model_path='models/diabetes_model.keras',
                                   scaler_path='AI-ProjectD/Diabetes-Prediction/scaler.pkl')
print(f"Diabetes: {has_diabetes}, Confidence: {confidence}%")