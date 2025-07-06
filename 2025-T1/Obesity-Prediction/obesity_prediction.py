# Data Analysis and Wrangling
import pandas as pd
import numpy as np

# Data Preprocessing
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder

# Deep Learning Libraries
from tensorflow.keras.models import load_model

# File Handling
import joblib

#---------------------- Methods Start Here ----------------------#
def preprocess_to_categorical(input):
    # Gender (1:Male, 2:Female)
    # FAVC (male>=3000cal:yes, female>=2400:yes)
    # CAEC (>=3:Always, 2:Frequently, 1:Sometimes, 0:no)
    # SMOKE (0=no, 1=yes)
    # CALC (2=Frequently, 1=Sometimes, 0=no)

    # Mapping definitions
    gender_map = {1: "Male", 2: "Female"}
    caec_map = {3: "Always", 2: "Frequently", 1: "Sometimes", 0: "no"}
    smoke_map = {0: "no", 1: "yes"}
    calc_map = {2: "Frequently", 1: "Sometimes", 0: "no"}

    # Create a copy to avoid mutating the original input
    output = input.copy()

    # Gender conversion
    gender = input.get("Gender")
    output["Gender"] = gender_map.get(gender, "Unknown")

    # FAVC conversion based on gender and calorie intake
    calorie_intake = input.get("FAVC")
    if calorie_intake is not None and gender in [1, 2]:
        favc_threshold = 3000 if gender == 1 else 2400
        favc_value = "yes" if calorie_intake >= favc_threshold else "no"
        output["FAVC"] = favc_value
    else:
        output["FAVC"] = "Unknown"

    # Other categorical mappings
    output["CAEC"] = caec_map.get(input.get("CAEC"), "Unknown")
    output["SMOKE"] = smoke_map.get(input.get("SMOKE"), "Unknown")
    output["CALC"] = calc_map.get(input.get("CALC"), "Unknown")

    return output
    
    

def preprocess_to_numerical(df, target_column='NObeyesdad', mode='train', encoder_path=None, label_encoder_path=None):
    categorical_columns = ['Gender', 'family_history_with_overweight', 'FAVC', 'CAEC', 'SMOKE', 'SCC', 'CALC', 'MTRANS']
    numerical_columns = ['Age', 'Height', 'Weight', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE']
    
    numerical_pipeline = Pipeline([('scaler', StandardScaler())])
    categorical_pipeline = Pipeline([('onehot', OneHotEncoder(sparse_output=False, handle_unknown='ignore'))])
    
    preprocessor = ColumnTransformer(transformers=[
        ('num', numerical_pipeline, numerical_columns),
        ('cat', categorical_pipeline, categorical_columns)
    ])

    if mode == 'train':
        if target_column in df.columns:
            le = LabelEncoder()
            y = le.fit_transform(df[target_column])
            y = to_categorical(y, num_classes=len(le.classes_))
            X = df.drop(target_column, axis=1)
            print(f'Label Encoded target classes: {le.classes_}')
            # Fit and transform
            X_transformed = preprocessor.fit_transform(X)
            # Save the preprocessor and label encoder
            joblib.dump(preprocessor, encoder_path)
            joblib.dump(le, label_encoder_path)
        else:
            y = None
            X = df
            X_transformed = preprocessor.fit_transform(X)
            joblib.dump(preprocessor, encoder_path)
    else:
        # Load the saved preprocessor and label encoder
        preprocessor = joblib.load(encoder_path)
        le = joblib.load(label_encoder_path)
        y = None if target_column not in df.columns else to_categorical(le.transform(df[target_column]), num_classes=len(le.classes_))
        X = df.drop(target_column, axis=1) if target_column in df.columns else df
        X_transformed = preprocessor.transform(X)

    return (X_transformed, y, le) if target_column in df.columns else (X_transformed)

def predict(input, model_path='obesity_model.keras', encoder_path='obesity_preprocessor.pkl', label_encoder_path='obesity_label_encoder.pkl'):
    model = load_model(model_path)
    label_encoder = joblib.load(label_encoder_path)

    # Check model, encoder, and label encoder existence
    if not model:
        raise Exception("Model not found.")
    if not label_encoder:
        raise Exception("Encoder not found.")
    if not joblib.load(label_encoder_path):
        raise Exception("Label encoder not found.")
    
    df_input = pd.DataFrame([preprocess_to_categorical(input)])
    input_transformed = preprocess_to_numerical(df_input, target_column=None, mode='test', encoder_path=encoder_path, label_encoder_path=label_encoder_path)
    
    # Predict probabilities
    y_probs = model.predict(input_transformed)  # shape (1, num_classes)

    # Get predicted index and corresponding label
    pred_index = np.argmax(y_probs, axis=1)[0]
    pred_label = label_encoder.inverse_transform([pred_index])[0]
    confidence = round(y_probs[0][pred_index] * 100, 2)

    return pred_label, confidence

#---------------------- Example Usage ----------------------#
input = {
    "Gender": 1,
    "Age": 24.443011,
    "Height": 1.699998,
    "Weight": 81.66995,
    "family_history_with_overweight": "yes",
    "FAVC": 2500,
    "FCVC": 2,
    "NCP": 3,
    "CAEC": 1,
    "SMOKE": 0,
    "CH2O": 2.763573,
    "SCC": "no",
    "FAF": 0,
    "TUE": 0.976473,
    "CALC": 1,
    "MTRANS": "Public_Transportation"
}

# Path to the model and encoder files
model_path = 'models/obesity_model.keras'
encoder_path = 'AI-ProjectD/Obesity-Prediction/obesity_preprocessor.pkl'
label_encoder_path = 'AI-ProjectD/Obesity-Prediction/obesity_label_encoder.pkl'

# Make a prediction
result, confidence = predict(input, model_path, encoder_path, label_encoder_path)
print(f"Prediction: {result}, Confidence: {confidence}%")