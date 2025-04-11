# Data Analysis and Wrangling
import pandas as pd
import numpy as np

# Data Preprocessing
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


# Visualization
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


# Deep Learning Libraries
from tensorflow.keras.models import Sequential, load_model, Model
from tensorflow.keras.layers import Dense, BatchNormalization, Dropout, Input, Add, Concatenate, LeakyReLU
from tensorflow.keras.optimizers import Adam, RMSprop
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.initializers import HeUniform
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers.schedules import ExponentialDecay
from tensorflow.keras.metrics import F1Score

# File Handling
import joblib

#---------------------- Methods Start Here ----------------------#
def preprocess_data(df, target_column='NObeyesdad', mode='train', encoder_path=None, label_encoder_path=None):
    categorical_columns = ['Gender', 'family_history_with_overweight', 'FAVC', 'CAEC', 'SMOKE', 'SCC', 'CALC', 'MTRANS']
    numerical_columns = ['Age', 'Height', 'Weight', 'NCP', 'CH2O', 'FAF', 'TUE']
    
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
    
    input = pd.DataFrame([input])
    input_transformed = preprocess_data(input, target_column=None, mode='test', encoder_path=encoder_path, label_encoder_path=label_encoder_path)
    y_pred_temp = model.predict(input_transformed)
    y_pred_temp = np.argmax(y_pred_temp, axis=1)
    y_pred_temp = label_encoder.inverse_transform(y_pred_temp)
    return y_pred_temp[0]