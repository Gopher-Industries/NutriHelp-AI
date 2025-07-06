## How to Use

To use the predict function, you’ll need to provide an input in the form of a dictionary representing the personal health data. Here is an example of how you can call the predict function:

## Example Usage
```python
import obesity_prediction

# Example input data
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

>>> Prediction: Overweight_Level_II, Confidence: 78.76%
```

## Important Note ❗️

Please adjust the file paths (model_path, encoder_path, label_encoder_path) according to your local environment where the files are stored. Incorrect paths will lead to errors in loading the model and the preprocessors.

```python
import os
print("Current working directory:", os.getcwd())
print("Files in expected directory:", os.listdir('/models'))
```

## Categorical Feature Encoding ❗️

The model strictly expects categorical features to match the following categories:
- **Gender**: ['Female', 'Male']
- **family_history_with_overweight**: ['no', 'yes']
- **FAVC**: ['no', 'yes']
- **CAEC**: ['Always', 'Frequently', 'Sometimes', 'no']
- **SMOKE**: ['no', 'yes']
- **SCC**: ['no', 'yes']
- **CALC**: ['Frequently', 'Sometimes', 'no']
- **MTRANS**: ['Automobile', 'Bike', 'Motorbike', 'Public_Transportation', 'Walking']

Ensure input data uses these exact string values (case-sensitive) for proper one-hot encoding. Any unknown categories will be ignored during inference.