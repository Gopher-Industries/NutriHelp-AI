import joblib
import tensorflow as tf
import pandas as pd
import numpy as np


try:
    model = tf.keras.models.load_model("nutrihelp_ai/models/obesity_model.keras")
    preprocessor = joblib.load("nutrihelp_ai/models/preprocessor.joblib")
    label_encoder = joblib.load("nutrihelp_ai/models/label_encoder.joblib")
except Exception as e:
    print("⚠️ Models not loaded yet. Using mock prediction.")
    model = preprocessor = label_encoder = None

categorical_columns = ['Gender', 'family_history_with_overweight', 'FAVC', 'CAEC',
                       'SMOKE', 'SCC', 'CALC', 'MTRANS']
numerical_columns = ['Age', 'Height', 'Weight', 'NCP', 'CH2O', 'FAF', 'TUE']

def predict_obesity_class(input_data):
    # from nutrihelp_ai.routers.obesity_api import ObesityInput
    # df = pd.DataFrame([input_data.dict()])
    # X = preprocessor.transform(df)
    # probs = model.predict(X)
    # pred_class = np.argmax(probs, axis=1)[0]
    # label = label_encoder.inverse_transform([pred_class])[0]
    # return {"prediction": label}
    return {
        "prediction": "Mock_Label"
    }