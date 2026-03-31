# NutriHelp-AI Backend – Complete Project Documentation

**Version:** 1.0  
**Date:** December 25, 2025  
**Author:** [Your Name/Team]  
**Tech Stack:** FastAPI • Supabase • Python • Pydantic

## Project Overview

NutriHelp-AI is a personalized nutrition backend that:

- Generates 3-day meal plans based on user health data
- Supports dietary preferences (vegan, keto, etc.)
- Avoids user allergies automatically
- Considers health conditions (diabetes, hypertension, celiac, etc.)
- Classifies food images with allergy warnings
- Handles incomplete profiles intelligently

**Status:** Feature complete – Ready for production

## Features

- Calorie calculation using Harris-Benedict formula
- Dietary templates with macro adjustments
- Allergy keyword avoidance + safe meal fallbacks
- Health condition-aware recommendations
- Data quality feedback (completeness %, warnings)
- Swagger UI documentation
- Full Supabase integration

## Base URLs

- **Local Development:** `http://localhost:8000`
- **Production:** `[Update after deployment]`

**API Docs:**

- Swagger UI: `/docs`
- ReDoc: `/redoc`

## Key Endpoints

### 1. Generate Meal Plan from Profile (PRIMARY & RECOMMENDED)

GET /ai/mealplan/from-profile/{user_id}

**Path Parameter:**  
`user_id` – User's Supabase auth ID (string)

**Example:**

GET /ai/mealplan/from-profile/user123abc

**Success Response Includes:**

- `success`: true
- `message`: Personalized message
- `meal_plan`: Array of 3 `DailyMealPlan` objects (breakfast, lunch, dinner, snacks)
- `data_quality`: Profile completeness % + warnings + fallbacks
- `recommendations`: List of tips (allergies avoided, health conditions considered)

**Error Handling:**

- 404 → User not found → Prompt login
- Incomplete data → Use `recommendations` to guide user

**Backend Flow:**

1. Fetch from Supabase:
   - `users` → age, gender, weight (kg), height (cm)
   - `user_preferences` → activity_level, dietary_preference, etc.
   - `user_allergies` → allergy names
   - `user_health_conditions` → with joined `health_conditions` details
2. Validate required fields
3. Calculate BMR × activity multiplier
4. Select meals from dietary templates
5. **Skip unsafe meals** (nuts, dairy, gluten, shellfish keywords)
6. Add health-specific recommendations

### 2. Food Image Classifier v2 using YOLO model

**Success Response Includes:**

- `success`: true
- `message`: Personalized message
- `meal_plan`: Array of 3 `DailyMealPlan` objects (breakfast, lunch, dinner, snacks)
- `data_quality`: Profile completeness % + warnings + fallbacks
- `recommendations`: List of tips (allergies avoided, health conditions considered)

**Error Handling:**

- 404 → User not found → Prompt login
- Incomplete data → Use `recommendations` to guide user

**Backend Flow:**

1. Fetch from Supabase:
   - `users` → age, gender, weight (kg), height (cm)
   - `user_preferences` → activity_level, dietary_preference, etc.
   - `user_allergies` → allergy names
   - `user_health_conditions` → with joined `health_conditions` details
2. Validate required fields
3. Calculate BMR × activity multiplier
4. Select meals from dietary templates
5. **Skip unsafe meals** (nuts, dairy, gluten, shellfish keywords)
6. Add health-specific recommendations

### 2. Food Image Classifier v2 (Dummy)

POST /ai-model/classifier/v2

**Form Data:**

- `image`: Food photo (JPG/PNG file)
- `allergies`: Optional comma-separated string (e.g., "nuts,dairy")

**Response:**

- Top prediction + top-3
- Allergy warning if predicted food contains user's allergen

## Data Flow Diagram

Frontend
↓
GET /ai/mealplan/from-profile/{user_id}
↓
Backend fetches Supabase tables:
├─ users
├─ user_preferences
├─ user_allergies
└─ user_health_conditions → health_conditions (join)
↓
Validate + enrich missing data
↓
Calculate calories + select safe meals
↓
Generate recommendations
↓
Return full JSON response

## Frontend Integration Tips

- Show `recommendations` as banners/tips
- Use `data_quality.data_completeness` for profile progress bar
- Display allergy/health messages prominently
- Cache meal plan for 24 hours (optional)
- Handle errors gracefully with user-friendly messages

## Local Development Setup

1. Clone repository
2. Create `dbconnection.py` file:

SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-anon-key

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run server:

```bash
Run server:Bashuvicorn main:app --reload
Open API docs: http://localhost:8000/docs
```

Database Schema (Supabase Tables)

users: id (PK), age, gender, weight, height, ...
user_preferences: user_id (FK), activity_level, dietary_preference, health_goals, meals_per_day
user_allergies: user_id (FK), allergy_name
user_health_conditions: user_id (FK), condition_id (FK), severity, diagnosed_date
health_conditions: id (PK), name, description

Testing Guidelines
Test with users who have:

Allergies → Verify no unsafe ingredients appear
Health conditions → Check correct recommendations
Incomplete profile → Verify helpful feedback and defaults
Extreme values (age 18–80, weight 40–150kg) → Proper handling

Deployment Notes
Recommended Platforms:

Render.com
Railway.app
Fly.io

Production Command:
Bashuvicorn main:app --host 0.0.0.0 --port $PORT
Environment Variables Required:

SUPABASE_URL
SUPABASE_ANON_KEY

Health Check: Visit /docs or add simple /health endpoint if needed
Project Structure
textnutrihelp_ai/
├── main.py # FastAPI app + routers
├── routers/
│ ├── classifier_v2.py # Food classifier
│ └── mealplan_api.py # Meal plan endpoints
├── model/
│ ├── dbConnection.py # Supabase client
│ ├── fetchUserProfile.py
│ ├── fetchUserPreferences.py
│ ├── fetchUserAllergies.py
│ ├── fetchAllHealthConditions.py
│ └── fetchUserHealthConditions.py
├── docs/
│ └── AI_INTEGRATION_RUNBOOK.md
├── requirements.txt
├── .env.example
└── PROJECT_DOCUMENTATION.md # ← This file
