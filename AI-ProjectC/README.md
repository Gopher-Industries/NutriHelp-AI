
# AI Project Setup Guide

This comprehensive README provides **all** instructions in **Markdown** format, covering **cloning** the repository, **setting up the environment**, **running the API**, **training the model**, and **troubleshooting issues**.


## 1. Obtain the Project Code

You have **two** primary ways to get the code: **cloning** the repository using Git or **downloading** the ZIP.

### **Option A: Clone the Repository**
1. **Open** a terminal (macOS/Linux) or Command Prompt/PowerShell (Windows).
2. **Navigate** to the folder where you want the project to live.
3. **Run**:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   ```
4. **Enter** the new folder:
   ```bash
   cd yourproject
   ```

### **Option B: Download ZIP**
1. **Visit** the GitHub repository in your web browser.
2. **Click** the green **Code** button and select **Download ZIP**.
3. **Unzip** the downloaded file into a folder of your choice.
4. **Open** a terminal/command prompt in that folder:
   ```bash
   cd path/to/yourproject
   ```

Either approach will give you the **same** files locally.


## 2. Create and Activate a Virtual Environment

A **virtual environment** keeps project dependencies isolated from your system. Follow the steps for **your** OS:

### **Windows (Command Prompt/PowerShell)**
```bash
cd path/to/yourproject
python -m venv venv
```
- **Activate** the environment:
  - **Command Prompt**:
    ```bash
    venv\Scripts\activate.bat
    ```
  - **PowerShell**:
    ```powershell
    .\venv\Scripts\Activate.ps1
    ```
    *(If you get an execution policy error, see [Troubleshooting](#10-troubleshooting))*

### **macOS/Linux (Terminal)**
```bash
cd path/to/yourproject
python3 -m venv venv
source venv/bin/activate
```
Your prompt should now show `(venv)`.

---

## 3. Install Dependencies

1. **(Optional)** Upgrade pip:
   ```bash
   pip install --upgrade pip
   ```
2. **Install** requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. **Check** installed packages:
   ```bash
   pip list
   ```
   Ensure all expected packages (e.g., FastAPI, PyTorch, etc.) are listed.

---

## 4. Project Structure (Example)

```
yourproject/
│── app/
│   ├── __init__.py       # Marks app/ as a package
│   ├── api.py            # FastAPI application
│   ├── inference.py      # Model loading & prediction logic
│   └── models/
│       └── model.pth     # Trained model weights (if available)
│
├── scripts/              # Data scripts & training utilities
│   ├── data_get.py
│   ├── data_clean.py
│   ├── data_split.py
│   ├── train.py
│   ├── test.py
│   └── torchutils.py
│
├── requirements.txt      # Python dependencies
├── .gitignore            # Files/folders to exclude from version control
└── README.md             # Documentation (this file)
```

---

## 5. Running the API Locally

Assuming your **FastAPI app** is defined in `app/api.py`:

```bash
uvicorn app.api:app --host 0.0.0.0 --port 8000 --reload
```

- **Open** `http://localhost:8000/docs` in your browser to see Swagger UI.
- Or `http://localhost:8000/redoc` for ReDoc documentation.

---

## 6. Testing Your API

### **Using cURL**
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "accept: application/json" \
  -F "file=@test.jpg"
```
Replace `test.jpg` with your actual image path.

### **Using Python (requests library)**
```python
import requests

url = "http://localhost:8000/predict"
files = {"file": open("test.jpg", "rb")}
response = requests.post(url, files=files)
print(response.json())
```
Again, `test.jpg` should be replaced by your real image.

---

## 7. Training & Other Scripts

If your project includes scripts for data collection/cleaning/training:

```bash
python scripts/data_get.py
python scripts/data_clean.py
python scripts/data_split.py
python scripts/train.py
python scripts/test.py
```

Adjust paths in these scripts to match your dataset structure.

---

## 8. Deactivating the Virtual Environment

When you’re done working in this project:

```bash
deactivate
```

Your prompt no longer shows `(venv)`.

---



