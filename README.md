# 🧠 NutriHelp-AI

This repository contains the AI service for the NutriHelp project. It exposes machine learning model predictions through a FastAPI server, allowing other services (e.g., Backend) to send data and receive results.

---

## 🚀 Getting Started

Follow the steps below to clone and run the AI model server locally.

### 1. 📥 Clone the Repository

```bash
git clone https://github.com/Gopher-Industries/NutriHelp-AI.git
cd NutriHelp-AI
```

---

### 2. 🐍 (Optional) Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

If you see a PowerShell error, try this instead:

```bash
venv\Scripts\activate.bat
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. 🧪 Run the AI Server

```bash
python run.py
```

By default, the FastAPI server will run at:

```
http://127.0.0.1:8000
```

You can access the Swagger UI documentation at:

```
http://127.0.0.1:8000/docs
```

If you want to run on different port, go to run.py file and change the port to different one.

---

## 📬 API Endpoint Example

### `POST /ai-model/obesity/predict`

Accepts JSON-formatted input and returns a prediction result.

#### 🔄 Example Request Payload:

```json
{
  "Gender": "Male",
  "family_history_with_overweight": "yes",
  "Age": 25,
  "Height": 1.75,
  "Weight": 85,
}
```

---

# 📡 How the Backend Team Can Use the NutriHelp AI API

Once the AI server is running (locally or on a deployed environment), the Backend team can send requests to it over HTTP.

---

## 🔗 Endpoint Information

| Method | Endpoint                            | Description                  |
|--------|-------------------------------------|------------------------------|
| POST   | `/ai-model/obesity/predict`         | Get obesity prediction       |
| POST   | `/ai-model/chatbot/query`           | Get response from AI         |
---

## 📤 Example Request

### 🔧 URL (Local Testing)
```
http://localhost:8000/ai-model/obesity/predict
```

### 🧾 Headers
```http
Content-Type: application/json
```

### 📦 JSON Body
```json
{
  "Gender": "Male",
  "Age": 25,
  "Height": 1.75,
  "Weight": 85,
}
```

### ✅ Example Successful Response
```json
{
  "obesity_level": "Overweight"
}
```

---

## 🧪 How to Test 

### ✅ Example: Send Obesity Prediction Request

```js
const data = {
  "Gender": "Male",
  "Age": 25,
  "Height": 1.75,
  "Weight": 65,
  "family_history_with_overweight": "yes",
  "FAVC": "yes",
  "FCVC": 2.5,
  "NCP": 3,
  "CAEC": "Sometimes",
  "SMOKE": "no",
  "CH2O": 2.5,
  "SCC": "no",
  "FAF": 0.5,
  "TUE": 1,
  "CALC": "Sometimes",
  "MTRANS": "Public_Transportation"
};

fetch("http://localhost:8000/predict", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify(data)
})
.then(response => response.json())
.then(result => console.log("Prediction:", result))
.catch(error => console.error("Error:", error));

```

---
