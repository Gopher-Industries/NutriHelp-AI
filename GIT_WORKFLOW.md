# NutriHelp AI Team – Git Version Control Guide

This guide outlines the Git workflow and rules for the NutriHelp AI Team. It covers best practices for managing changes to AI models and the API endpoint server, ensuring consistency, reproducibility, and clean collaboration.

---

## 📁 Repository Structure (AI-related)
nutrihelp/ ├── ai_model/ # AI model training, evaluation scripts ├── ai_api/ # FastAPI or Flask API code ├── data/ # (Optional) Reference to processed datasets (avoid raw/large files) ├── notebooks/ # Exploratory or model training notebooks ├── README.md └── requirements.txt

markdown
Copy
Edit

---

## 🌱 Branching Strategy

- `main`: Production-ready model + API.
- `dev`: AI team’s integration branch (do NOT push to `main` directly).
- `model/[model-name-version]`: For changes related to training/evaluating a new model.
- `api/[feature-name]`: For AI API development (e.g., new endpoints).
- `refactor/[scope]`: For code clean-up or architecture improvements.
- `docs/[purpose]`: For document management.

### Example:
```bash
git checkout -b model/obesity-prediction-v2

```
---

## 🧾 Commit Message Format
Use conventional commits to maintain clarity.

Examples:
feat(model): add CNN obesity classifier

fix(api): handle missing input data error

refactor(api): restructure prediction pipeline

docs(model): update README with training steps

---
## 🔁 Pull Request Workflow
Push changes to a feature branch.

Create PR to dev-ai.

Include:

Description of what changed

Input/output format (for model or API)

Sample cURL or Postman request (if endpoint changed)

Any breaking changes or model version updates

Tag at least one team member for review.

---
## ✅ Model Versioning
Always save trained models with version identifiers:

Copy
Edit
obesity_model_v1.keras
scaler_v1.pkl


---
## 🚫 Do NOT
Push directly to main or dev.
Hardcode paths, credentials, or secrets in scripts or API code.

---
## 🔒 Environment & Secrets
Store .env locally (include .env.example in repo).

Keep model registry or cloud API keys out of version control.

