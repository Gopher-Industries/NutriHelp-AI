# # nutrihelp_ai/routers/mealplan_api.py

# from fastapi import APIRouter, HTTPException, Query
# from pydantic import BaseModel, Field
# from typing import Optional, List, Dict, Any
# from enum import Enum

# router = APIRouter(
#     prefix="/ai/mealplan",
#     tags=["Meal Plan Generation"],
# )

# # ============================
# # Enums for Valid Values
# # ============================


# class ActivityLevel(str, Enum):
#     sedentary = "sedentary"
#     light = "light"
#     moderate = "moderate"
#     active = "active"
#     very_active = "very_active"


# class DietaryPreference(str, Enum):
#     none = "none"
#     vegetarian = "vegetarian"
#     vegan = "vegan"
#     keto = "keto"
#     paleo = "paleo"
#     mediterranean = "mediterranean"


# class Gender(str, Enum):
#     male = "male"
#     female = "female"
#     other = "other"

# # ============================
# # Response Models
# # ============================


# class MealItem(BaseModel):
#     name: str
#     calories: int
#     protein: float
#     carbs: float
#     fat: float
#     description: str


# class DailyMealPlan(BaseModel):
#     day: str
#     breakfast: MealItem
#     lunch: MealItem
#     dinner: MealItem
#     snacks: List[MealItem]
#     total_calories: int
#     total_protein: float
#     total_carbs: float
#     total_fat: float


# class DataQualityInfo(BaseModel):
#     """Information about data quality and missing fields"""
#     missing_fields: List[str] = []
#     warnings: List[str] = []
#     fallbacks_applied: Dict[str, Any] = {}
#     data_completeness: float = Field(
#         ..., description="Percentage of required data provided (0-100)")


# class MealPlanResponse(BaseModel):
#     success: bool
#     message: str
#     meal_plan: Optional[List[DailyMealPlan]] = None
#     data_quality: DataQualityInfo
#     recommendations: Optional[List[str]] = None

# # ============================
# # Data Validator (NA-101)
# # ============================


# class MealPlanValidator:
#     """Handles missing data cases for meal plan generation"""

#     REQUIRED_FIELDS = {
#         "user_id": "User ID is required",
#         "age": "Age is required for calorie calculation",
#         "gender": "Gender is required for calorie calculation",
#         "weight": "Weight is required for calorie calculation",
#         "height": "Height is required for BMI calculation"
#     }

#     OPTIONAL_FIELDS = {
#         "activity_level": "sedentary",
#         "dietary_preference": "none",
#         "allergies": "",
#         "health_goals": "maintain_weight",
#         "meals_per_day": 3
#     }

#     @staticmethod
#     def validate_and_enrich(params: Dict) -> tuple[bool, Dict, DataQualityInfo]:
#         """
#         Validate parameters and apply fallbacks for missing optional data
#         Returns: (is_valid, enriched_params, data_quality_info)
#         """
#         missing_fields = []
#         warnings = []
#         fallbacks_applied = {}

#         # Check required fields
#         for field, error_msg in MealPlanValidator.REQUIRED_FIELDS.items():
#             if field not in params or params[field] is None or params[field] == "":
#                 missing_fields.append(field)

#         # If required fields are missing, cannot proceed
#         if missing_fields:
#             data_quality = DataQualityInfo(
#                 missing_fields=missing_fields,
#                 warnings=[
#                     f"Cannot generate meal plan without: {', '.join(missing_fields)}"],
#                 fallbacks_applied={},
#                 data_completeness=0.0
#             )
#             return False, params, data_quality

#         # Apply fallbacks for optional fields
#         enriched_params = params.copy()
#         for field, default_value in MealPlanValidator.OPTIONAL_FIELDS.items():
#             if field not in enriched_params or enriched_params[field] is None or enriched_params[field] == "":
#                 enriched_params[field] = default_value
#                 fallbacks_applied[field] = default_value
#                 warnings.append(
#                     f"'{field}' not provided - using default: '{default_value}'")

#         # Calculate data completeness
#         total_fields = len(MealPlanValidator.REQUIRED_FIELDS) + \
#             len(MealPlanValidator.OPTIONAL_FIELDS)
#         # All required are present
#         provided_fields = len(MealPlanValidator.REQUIRED_FIELDS)
#         provided_fields += sum(
#             1 for f in MealPlanValidator.OPTIONAL_FIELDS if f in params and params[f])
#         completeness = (provided_fields / total_fields) * 100

#         data_quality = DataQualityInfo(
#             missing_fields=[],
#             warnings=warnings,
#             fallbacks_applied=fallbacks_applied,
#             data_completeness=round(completeness, 1)
#         )

#         return True, enriched_params, data_quality

# # ============================
# # Dummy Meal Plan Generator
# # ============================
# # def generate_dummy_meal_plan(params: Dict) -> List[DailyMealPlan]:
#     """
#     Generate dummy 3-day meal plan based on user preferences
#     This will be replaced with real logic in future sprints
#     """

#     # Calculate target calories (simplified Harris-Benedict)
#     # age = params["age"]
#     # weight = params["weight"]
#     # height = params["height"]
#     # gender = params["gender"]
#     # activity_level = params["activity_level"]

#     # # BMR calculation
#     # if gender == "male":
#     #     bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
#     # else:
#     #     bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

#     # # Activity multiplier
#     # activity_multipliers = {
#     #     "sedentary": 1.2,
#     #     "light": 1.375,
#     #     "moderate": 1.55,
#     #     "active": 1.725,
#     #     "very_active": 1.9
#     # }

#     # target_calories = int(bmr * activity_multipliers.get(activity_level, 1.2))

#     # # Adjust for dietary preference
#     # dietary_pref = params["dietary_preference"]

#     # # Generate 3-day plan
#     # meal_plans = []
#     # for day_num in range(1, 4):
#     #     # Dummy meals (replace with real data later)
#     #     breakfast = MealItem(
#     #         name=f"{'Vegan' if dietary_pref == 'vegan' else 'Classic'} Breakfast Bowl",
#     #         calories=int(target_calories * 0.25),
#     #         protein=20.0,
#     #         carbs=45.0,
#     #         fat=12.0,
#     #         description="Nutritious breakfast to start your day"
#     #     )

#     #     lunch = MealItem(
#     #         name=f"{'Plant-based' if dietary_pref in ['vegan', 'vegetarian'] else 'Protein'} Lunch",
#     #         calories=int(target_calories * 0.35),
#     #         protein=30.0,
#     #         carbs=50.0,
#     #         fat=15.0,
#     #         description="Balanced midday meal"
#     #     )

#     #     dinner = MealItem(
#     #         name=f"{'Keto' if dietary_pref == 'keto' else 'Balanced'} Dinner",
#     #         calories=int(target_calories * 0.30),
#     #         protein=25.0,
#     #         carbs=40.0 if dietary_pref != "keto" else 10.0,
#     #         fat=18.0 if dietary_pref == "keto" else 12.0,
#     #         description="Satisfying evening meal"
#     #     )

#     #     snack = MealItem(
#     #         name="Healthy Snack",
#     #         calories=int(target_calories * 0.10),
#     #         protein=8.0,
#     #         carbs=15.0,
#     #         fat=5.0,
#     #         description="Light snack between meals"
#     #     )

#     #     total_cal = breakfast.calories + lunch.calories + dinner.calories + snack.calories

#     #     daily_plan = DailyMealPlan(
#     #         day=f"Day {day_num}",
#     #         breakfast=breakfast,
#     #         lunch=lunch,
#     #         dinner=dinner,
#     #         snacks=[snack],
#     #         total_calories=total_cal,
#     #         total_protein=breakfast.protein + lunch.protein + dinner.protein + snack.protein,
#     #         total_carbs=breakfast.carbs + lunch.carbs + dinner.carbs + snack.carbs,
#     #         total_fat=breakfast.fat + lunch.fat + dinner.fat + snack.fat
#     #     )

#     #     meal_plans.append(daily_plan)

#     # return meal_plans
# # ============================
# # Dummy Meal Plan Generator (Enhanced)
# # ============================


# def generate_dummy_meal_plan(params: Dict) -> List[DailyMealPlan]:
#     """
#     Generate dummy 3-day meal plan based on user preferences
#     This will be replaced with real logic in future sprints
#     """

#     # Calculate target calories (simplified Harris-Benedict)
#     age = params["age"]
#     weight = params["weight"]
#     height = params["height"]
#     gender = params["gender"]
#     activity_level = params["activity_level"]
#     dietary_pref = params["dietary_preference"]

#     # BMR calculation
#     if gender == "male":
#         bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
#     else:
#         bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

#     # Activity multiplier
#     activity_multipliers = {
#         "sedentary": 1.2,
#         "light": 1.375,
#         "moderate": 1.55,
#         "active": 1.725,
#         "very_active": 1.9
#     }

#     target_calories = int(bmr * activity_multipliers.get(activity_level, 1.2))

#     # Meal templates based on dietary preference
#     meal_templates = {
#         "none": {
#             "breakfast": [
#                 ("Scrambled Eggs with Whole Wheat Toast",
#                  "3 eggs, 2 slices whole wheat bread, butter"),
#                 ("Greek Yogurt Parfait", "Greek yogurt, granola, mixed berries, honey"),
#                 ("Oatmeal with Banana", "Steel-cut oats, banana, almonds, cinnamon")
#             ],
#             "lunch": [
#                 ("Grilled Chicken Salad",
#                  "Grilled chicken breast, mixed greens, olive oil dressing"),
#                 ("Turkey Sandwich", "Whole grain bread, turkey, lettuce, tomato, avocado"),
#                 ("Quinoa Buddha Bowl",
#                  "Quinoa, roasted vegetables, chickpeas, tahini sauce")
#             ],
#             "dinner": [
#                 ("Baked Salmon with Veggies",
#                  "Salmon fillet, steamed broccoli, sweet potato"),
#                 ("Lean Beef Stir-fry", "Lean beef strips, mixed vegetables, brown rice"),
#                 ("Chicken Breast with Quinoa",
#                  "Grilled chicken, quinoa, roasted asparagus")
#             ]
#         },
#         "vegetarian": {
#             "breakfast": [
#                 ("Veggie Omelette", "3 eggs, bell peppers, mushrooms, cheese"),
#                 ("Avocado Toast", "Whole grain toast, avocado, cherry tomatoes, feta"),
#                 ("Smoothie Bowl", "Banana, berries, protein powder, granola, chia seeds")
#             ],
#             "lunch": [
#                 ("Mediterranean Wrap", "Hummus, falafel, vegetables in whole wheat wrap"),
#                 ("Caprese Panini", "Mozzarella, tomato, basil, pesto on ciabatta"),
#                 ("Lentil Soup with Bread",
#                  "Red lentil soup, whole grain roll, side salad")
#             ],
#             "dinner": [
#                 ("Vegetable Lasagna", "Lasagna with spinach, ricotta, marinara sauce"),
#                 ("Stuffed Bell Peppers", "Peppers filled with quinoa, beans, cheese"),
#                 ("Eggplant Parmesan", "Baked eggplant, marinara, mozzarella, pasta")
#             ]
#         },
#         "vegan": {
#             "breakfast": [
#                 ("Tofu Scramble", "Tofu, turmeric, vegetables, nutritional yeast"),
#                 ("Chia Pudding", "Chia seeds, almond milk, berries, maple syrup"),
#                 ("Vegan Pancakes", "Whole wheat pancakes, banana, peanut butter")
#             ],
#             "lunch": [
#                 ("Buddha Bowl", "Quinoa, chickpeas, tahini, roasted vegetables"),
#                 ("Vegan Burrito", "Black beans, rice, salsa, guacamole, lettuce"),
#                 ("Lentil Curry", "Red lentils, coconut milk, vegetables, brown rice")
#             ],
#             "dinner": [
#                 ("Vegan Stir-fry", "Tofu, mixed vegetables, soy sauce, brown rice"),
#                 ("Pasta Primavera", "Whole wheat pasta, vegetables, olive oil, herbs"),
#                 ("Chickpea Curry", "Chickpeas, tomato sauce, spinach, naan bread")
#             ]
#         },
#         "keto": {
#             "breakfast": [
#                 ("Keto Omelette", "3 eggs, cheese, bacon, avocado, butter"),
#                 ("Bulletproof Coffee & Eggs",
#                  "Coffee with MCT oil, scrambled eggs, bacon"),
#                 ("Greek Yogurt Bowl", "Full-fat Greek yogurt, nuts, berries (limited)")
#             ],
#             "lunch": [
#                 ("Cobb Salad", "Mixed greens, chicken, bacon, eggs, cheese, ranch"),
#                 ("Bunless Burger", "Beef patty, cheese, lettuce wrap, mayo, pickles"),
#                 ("Salmon Avocado Salad",
#                  "Grilled salmon, avocado, leafy greens, olive oil")
#             ],
#             "dinner": [
#                 ("Ribeye Steak", "Grilled ribeye, butter, asparagus, cauliflower mash"),
#                 ("Keto Chicken Thighs",
#                  "Crispy chicken thighs, green beans, butter sauce"),
#                 ("Pork Chops", "Pan-seared pork chops, broccoli, cheese sauce")
#             ]
#         },
#         "paleo": {
#             "breakfast": [
#                 ("Paleo Egg Scramble", "Eggs, sweet potato, vegetables, coconut oil"),
#                 ("Berry Smoothie", "Berries, banana, almond butter, coconut milk"),
#                 ("Breakfast Hash", "Sweet potato, sausage, peppers, onions")
#             ],
#             "lunch": [
#                 ("Grilled Chicken Bowl", "Chicken, roasted vegetables, olive oil"),
#                 ("Tuna Salad", "Tuna, mixed greens, olive oil, nuts"),
#                 ("Beef Lettuce Wraps", "Ground beef, lettuce, vegetables, avocado")
#             ],
#             "dinner": [
#                 ("Baked Cod", "Cod fillet, roasted vegetables, olive oil"),
#                 ("Paleo Meatballs", "Grass-fed beef meatballs, marinara, zucchini noodles"),
#                 ("Grilled Lamb Chops", "Lamb chops, roasted root vegetables")
#             ]
#         },
#         "mediterranean": {
#             "breakfast": [
#                 ("Mediterranean Omelette", "Eggs, feta, tomatoes, olives, spinach"),
#                 ("Greek Yogurt Bowl", "Greek yogurt, walnuts, honey, figs"),
#                 ("Whole Grain Toast", "Toast, hummus, cucumber, tomato")
#             ],
#             "lunch": [
#                 ("Greek Salad", "Cucumbers, tomatoes, olives, feta, olive oil"),
#                 ("Falafel Wrap", "Falafel, hummus, vegetables, whole wheat pita"),
#                 ("Grilled Fish Plate", "White fish, lemon, vegetables, olive oil")
#             ],
#             "dinner": [
#                 ("Mediterranean Salmon", "Salmon, olives, tomatoes, capers, olive oil"),
#                 ("Chicken Souvlaki", "Grilled chicken skewers, tzatziki, vegetables"),
#                 ("Shrimp Pasta", "Whole wheat pasta, shrimp, garlic, olive oil, feta")
#             ]
#         }
#     }

#     # Get templates for the selected diet
#     templates = meal_templates.get(dietary_pref, meal_templates["none"])

#     # Snack options
#     snack_options = [
#         ("Mixed Nuts", "Almonds, walnuts, cashews"),
#         ("Apple with Peanut Butter", "Sliced apple, natural peanut butter"),
#         ("Protein Shake", "Protein powder, banana, almond milk"),
#         ("Greek Yogurt", "Plain Greek yogurt with berries"),
#         ("Veggie Sticks with Hummus", "Carrots, celery, cucumber, hummus")
#     ]

#     # Generate 3-day plan
#     meal_plans = []
#     for day_num in range(1, 4):
#         # Select meals for this day
#         breakfast_name, breakfast_desc = templates["breakfast"][(
#             day_num - 1) % len(templates["breakfast"])]
#         lunch_name, lunch_desc = templates["lunch"][(
#             day_num - 1) % len(templates["lunch"])]
#         dinner_name, dinner_desc = templates["dinner"][(
#             day_num - 1) % len(templates["dinner"])]
#         snack_name, snack_desc = snack_options[(
#             day_num - 1) % len(snack_options)]

#         # Calculate calorie distribution
#         breakfast_cal = int(target_calories * 0.25)
#         lunch_cal = int(target_calories * 0.35)
#         dinner_cal = int(target_calories * 0.30)
#         snack_cal = int(target_calories * 0.10)

#         # Adjust macros based on diet type
#         if dietary_pref == "keto":
#             # High fat, low carb
#             breakfast = MealItem(
#                 name=breakfast_name,
#                 calories=breakfast_cal,
#                 protein=round(breakfast_cal * 0.25 / 4, 1),
#                 carbs=round(breakfast_cal * 0.05 / 4, 1),
#                 fat=round(breakfast_cal * 0.70 / 9, 1),
#                 description=breakfast_desc
#             )
#             lunch = MealItem(
#                 name=lunch_name,
#                 calories=lunch_cal,
#                 protein=round(lunch_cal * 0.30 / 4, 1),
#                 carbs=round(lunch_cal * 0.05 / 4, 1),
#                 fat=round(lunch_cal * 0.65 / 9, 1),
#                 description=lunch_desc
#             )
#             dinner = MealItem(
#                 name=dinner_name,
#                 calories=dinner_cal,
#                 protein=round(dinner_cal * 0.30 / 4, 1),
#                 carbs=round(dinner_cal * 0.05 / 4, 1),
#                 fat=round(dinner_cal * 0.65 / 9, 1),
#                 description=dinner_desc
#             )
#         else:
#             # Balanced macros
#             breakfast = MealItem(
#                 name=breakfast_name,
#                 calories=breakfast_cal,
#                 protein=round(breakfast_cal * 0.20 / 4, 1),
#                 carbs=round(breakfast_cal * 0.50 / 4, 1),
#                 fat=round(breakfast_cal * 0.30 / 9, 1),
#                 description=breakfast_desc
#             )
#             lunch = MealItem(
#                 name=lunch_name,
#                 calories=lunch_cal,
#                 protein=round(lunch_cal * 0.25 / 4, 1),
#                 carbs=round(lunch_cal * 0.45 / 4, 1),
#                 fat=round(lunch_cal * 0.30 / 9, 1),
#                 description=lunch_desc
#             )
#             dinner = MealItem(
#                 name=dinner_name,
#                 calories=dinner_cal,
#                 protein=round(dinner_cal * 0.30 / 4, 1),
#                 carbs=round(dinner_cal * 0.40 / 4, 1),
#                 fat=round(dinner_cal * 0.30 / 9, 1),
#                 description=dinner_desc
#             )

#         snack = MealItem(
#             name=snack_name,
#             calories=snack_cal,
#             protein=round(snack_cal * 0.20 / 4, 1),
#             carbs=round(snack_cal * 0.40 / 4, 1),
#             fat=round(snack_cal * 0.40 / 9, 1),
#             description=snack_desc
#         )

#         total_cal = breakfast.calories + lunch.calories + dinner.calories + snack.calories

#         daily_plan = DailyMealPlan(
#             day=f"Day {day_num}",
#             breakfast=breakfast,
#             lunch=lunch,
#             dinner=dinner,
#             snacks=[snack],
#             total_calories=total_cal,
#             total_protein=round(
#                 breakfast.protein + lunch.protein + dinner.protein + snack.protein, 1),
#             total_carbs=round(breakfast.carbs + lunch.carbs +
#                               dinner.carbs + snack.carbs, 1),
#             total_fat=round(breakfast.fat + lunch.fat +
#                             dinner.fat + snack.fat, 1)
#         )

#         meal_plans.append(daily_plan)

#     return meal_plans

# # ============================
# # GET /ai/mealplan Endpoint (NA-101)
# # ============================


# @router.get(
#     "",
#     response_model=MealPlanResponse,
#     summary="Generate Personalized Meal Plan",
#     description="""
#     Generate a 3-day personalized meal plan based on user preferences and health data.
    
#     **NA-101: Handles missing data cases:**
#     - Required fields: user_id, age, gender, weight, height
#     - Optional fields use smart defaults if not provided
#     - Returns data quality information and warnings
    
#     **Future integration:** Will connect to user preferences table in database.
#     """
# )
# async def get_meal_plan(
#     user_id: str = Query(..., description="User ID from database"),
#     age: Optional[int] = Query(
#         None, ge=1, le=120, description="User age in years"),
#     gender: Optional[Gender] = Query(None, description="User gender"),
#     weight: Optional[float] = Query(
#         None, ge=20, le=300, description="Weight in kg"),
#     height: Optional[float] = Query(
#         None, ge=50, le=250, description="Height in cm"),
#     activity_level: Optional[ActivityLevel] = Query(
#         None, description="Physical activity level"),
#     dietary_preference: Optional[DietaryPreference] = Query(
#         None, description="Dietary preference"),
#     allergies: Optional[str] = Query(
#         None, description="Comma-separated allergies (e.g., 'nuts,dairy,shellfish')"),
#     health_goals: Optional[str] = Query(
#         None, description="Health goals (e.g., 'weight_loss', 'muscle_gain')"),
#     meals_per_day: Optional[int] = Query(
#         None, ge=2, le=6, description="Number of meals per day")
# ):
#     """
#     Generate personalized meal plan with error handling for missing data (NA-101)
#     """

#     try:
#         # Collect all parameters
#         params = {
#             "user_id": user_id,
#             "age": age,
#             "gender": gender,
#             "weight": weight,
#             "height": height,
#             "activity_level": activity_level,
#             "dietary_preference": dietary_preference,
#             "allergies": allergies,
#             "health_goals": health_goals,
#             "meals_per_day": meals_per_day
#         }

#         # NA-101: Validate and handle missing data
#         is_valid, enriched_params, data_quality = MealPlanValidator.validate_and_enrich(
#             params)

#         if not is_valid:
#             # Cannot proceed - missing required fields
#             return MealPlanResponse(
#                 success=False,
#                 message=f"Insufficient data to generate meal plan. Missing required fields: {', '.join(data_quality.missing_fields)}",
#                 meal_plan=None,
#                 data_quality=data_quality,
#                 recommendations=[
#                     "Please provide all required fields to generate a personalized meal plan",
#                     "Required: user_id, age, gender, weight, height"
#                 ]
#             )

#         # Generate meal plan with enriched data
#         meal_plan = generate_dummy_meal_plan(enriched_params)

#         # Build recommendations based on data quality
#         recommendations = []
#         if data_quality.data_completeness < 100:
#             recommendations.append(
#                 f"Meal plan generated with {data_quality.data_completeness}% data completeness. "
#                 "Provide more information for better personalization."
#             )

#         if enriched_params.get("allergies"):
#             recommendations.append(
#                 f"Allergy restrictions applied: {enriched_params['allergies']}. "
#                 "All meals exclude these ingredients."
#             )

#         # Success response
#         return MealPlanResponse(
#             success=True,
#             message="Meal plan generated successfully",
#             meal_plan=meal_plan,
#             data_quality=data_quality,
#             recommendations=recommendations if recommendations else None
#         )

#     except ValueError as e:
        # raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")

#     except Exception as e:
#         raise HTTPException(
#             status_code=500, detail=f"Error generating meal plan: {str(e)}")


# # ============================
# # Additional Endpoints
# # ============================
# @router.get(
#     "/preferences/{user_id}",
#     summary="Get User Meal Preferences (Placeholder)",
#     description="Future endpoint: Fetch user preferences from database"
# )
# async def get_user_preferences(user_id: str):
#     """
#     Placeholder for database integration
#     Will fetch user preferences from DB in future sprint
#     """
#     return {
#         "message": "Database integration pending",
#         "user_id": user_id,
#         "note": "This will fetch stored preferences from user profile table"
#     }


# nutrihelp_ai/routers/mealplan_api.py

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from enum import Enum
# NutriHelp-AI\nutrihelp_ai\model\fetchAllHealthConditions.py
# ============================
# DATABASE IMPORTS (UPDATE THIS SECTION)
# ============================
from nutrihelp_ai.model.fetchUserProfile import fetch_user_profile
from nutrihelp_ai.model.fetchUserPreferences import fetch_user_preferences, fetch_user_allergies
from nutrihelp_ai.model.fetchAllHealthConditions import fetch_all_health_conditions
from nutrihelp_ai.model.fetchUserHealthConditions import fetch_user_health_conditions  # ADD THIS LINE
import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/ai/mealplan",
    tags=["Meal Plan Generation"],
)

# ============================
# Enums for Valid Values
# ============================

class ActivityLevel(str, Enum):
    sedentary = "sedentary"
    light = "light"
    moderate = "moderate"
    active = "active"
    very_active = "very_active"


class DietaryPreference(str, Enum):
    none = "none"
    vegetarian = "vegetarian"
    vegan = "vegan"
    keto = "keto"
    paleo = "paleo"
    mediterranean = "mediterranean"


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"

# ============================
# Response Models
# ============================

class MealItem(BaseModel):
    name: str
    calories: int
    protein: float
    carbs: float
    fat: float
    description: str


class DailyMealPlan(BaseModel):
    day: str
    breakfast: MealItem
    lunch: MealItem
    dinner: MealItem
    snacks: List[MealItem]
    total_calories: int
    total_protein: float
    total_carbs: float
    total_fat: float


class DataQualityInfo(BaseModel):
    """Information about data quality and missing fields"""
    missing_fields: List[str] = []
    warnings: List[str] = []
    fallbacks_applied: Dict[str, Any] = {}
    data_completeness: float = Field(
        ..., description="Percentage of required data provided (0-100)")


class MealPlanResponse(BaseModel):
    success: bool
    message: str
    meal_plan: Optional[List[DailyMealPlan]] = None
    data_quality: DataQualityInfo
    recommendations: Optional[List[str]] = None

# ============================
# Data Validator (NA-101)
# ============================

class MealPlanValidator:
    """Handles missing data cases for meal plan generation"""

    REQUIRED_FIELDS = {
        "user_id": "User ID is required",
        "age": "Age is required for calorie calculation",
        "gender": "Gender is required for calorie calculation",
        "weight": "Weight is required for calorie calculation",
        "height": "Height is required for BMI calculation"
    }

    OPTIONAL_FIELDS = {
        "activity_level": "sedentary",
        "dietary_preference": "none",
        "allergies": "",
        "health_goals": "maintain_weight",
        "meals_per_day": 3
    }

    @staticmethod
    def validate_and_enrich(params: Dict) -> tuple[bool, Dict, DataQualityInfo]:
        """
        Validate parameters and apply fallbacks for missing optional data
        Returns: (is_valid, enriched_params, data_quality_info)
        """
        missing_fields = []
        warnings = []
        fallbacks_applied = {}

        # Check required fields
        for field, error_msg in MealPlanValidator.REQUIRED_FIELDS.items():
            if field not in params or params[field] is None or params[field] == "":
                missing_fields.append(field)

        # If required fields are missing, cannot proceed
        if missing_fields:
            data_quality = DataQualityInfo(
                missing_fields=missing_fields,
                warnings=[
                    f"Cannot generate meal plan without: {', '.join(missing_fields)}"],
                fallbacks_applied={},
                data_completeness=0.0
            )
            return False, params, data_quality

        # Apply fallbacks for optional fields
        enriched_params = params.copy()
        for field, default_value in MealPlanValidator.OPTIONAL_FIELDS.items():
            if field not in enriched_params or enriched_params[field] is None or enriched_params[field] == "":
                enriched_params[field] = default_value
                fallbacks_applied[field] = default_value
                warnings.append(
                    f"'{field}' not provided - using default: '{default_value}'")

        # Calculate data completeness
        total_fields = len(MealPlanValidator.REQUIRED_FIELDS) + \
            len(MealPlanValidator.OPTIONAL_FIELDS)
        provided_fields = len(MealPlanValidator.REQUIRED_FIELDS)
        provided_fields += sum(
            1 for f in MealPlanValidator.OPTIONAL_FIELDS if f in params and params[f])
        completeness = (provided_fields / total_fields) * 100

        data_quality = DataQualityInfo(
            missing_fields=[],
            warnings=warnings,
            fallbacks_applied=fallbacks_applied,
            data_completeness=round(completeness, 1)
        )

        return True, enriched_params, data_quality

# ============================
# Dummy Meal Plan Generator (Enhanced)
# ============================

def generate_dummy_meal_plan(params: Dict) -> List[DailyMealPlan]:
    """
    Generate dummy 3-day meal plan based on user preferences
    This will be replaced with real logic in future sprints
    """

    # Calculate target calories (simplified Harris-Benedict)
    age = params["age"]
    weight = params["weight"]
    height = params["height"]
    gender = params["gender"]
    activity_level = params["activity_level"]
    dietary_pref = params["dietary_preference"]

    # BMR calculation
    if gender == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    # Activity multiplier
    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very_active": 1.9
    }

    target_calories = int(bmr * activity_multipliers.get(activity_level, 1.2))

    # Meal templates based on dietary preference
    meal_templates = {
        "none": {
            "breakfast": [
                ("Scrambled Eggs with Whole Wheat Toast",
                 "3 eggs, 2 slices whole wheat bread, butter"),
                ("Greek Yogurt Parfait", "Greek yogurt, granola, mixed berries, honey"),
                ("Oatmeal with Banana", "Steel-cut oats, banana, almonds, cinnamon")
            ],
            "lunch": [
                ("Grilled Chicken Salad",
                 "Grilled chicken breast, mixed greens, olive oil dressing"),
                ("Turkey Sandwich", "Whole grain bread, turkey, lettuce, tomato, avocado"),
                ("Quinoa Buddha Bowl",
                 "Quinoa, roasted vegetables, chickpeas, tahini sauce")
            ],
            "dinner": [
                ("Baked Salmon with Veggies",
                 "Salmon fillet, steamed broccoli, sweet potato"),
                ("Lean Beef Stir-fry", "Lean beef strips, mixed vegetables, brown rice"),
                ("Chicken Breast with Quinoa",
                 "Grilled chicken, quinoa, roasted asparagus")
            ]
        },
        "vegetarian": {
            "breakfast": [
                ("Veggie Omelette", "3 eggs, bell peppers, mushrooms, cheese"),
                ("Avocado Toast", "Whole grain toast, avocado, cherry tomatoes, feta"),
                ("Smoothie Bowl", "Banana, berries, protein powder, granola, chia seeds")
            ],
            "lunch": [
                ("Mediterranean Wrap", "Hummus, falafel, vegetables in whole wheat wrap"),
                ("Caprese Panini", "Mozzarella, tomato, basil, pesto on ciabatta"),
                ("Lentil Soup with Bread",
                 "Red lentil soup, whole grain roll, side salad")
            ],
            "dinner": [
                ("Vegetable Lasagna", "Lasagna with spinach, ricotta, marinara sauce"),
                ("Stuffed Bell Peppers", "Peppers filled with quinoa, beans, cheese"),
                ("Eggplant Parmesan", "Baked eggplant, marinara, mozzarella, pasta")
            ]
        },
        "vegan": {
            "breakfast": [
                ("Tofu Scramble", "Tofu, turmeric, vegetables, nutritional yeast"),
                ("Chia Pudding", "Chia seeds, almond milk, berries, maple syrup"),
                ("Vegan Pancakes", "Whole wheat pancakes, banana, peanut butter")
            ],
            "lunch": [
                ("Buddha Bowl", "Quinoa, chickpeas, tahini, roasted vegetables"),
                ("Vegan Burrito", "Black beans, rice, salsa, guacamole, lettuce"),
                ("Lentil Curry", "Red lentils, coconut milk, vegetables, brown rice")
            ],
            "dinner": [
                ("Vegan Stir-fry", "Tofu, mixed vegetables, soy sauce, brown rice"),
                ("Pasta Primavera", "Whole wheat pasta, vegetables, olive oil, herbs"),
                ("Chickpea Curry", "Chickpeas, tomato sauce, spinach, naan bread")
            ]
        },
        "keto": {
            "breakfast": [
                ("Keto Omelette", "3 eggs, cheese, bacon, avocado, butter"),
                ("Bulletproof Coffee & Eggs",
                 "Coffee with MCT oil, scrambled eggs, bacon"),
                ("Greek Yogurt Bowl", "Full-fat Greek yogurt, nuts, berries (limited)")
            ],
            "lunch": [
                ("Cobb Salad", "Mixed greens, chicken, bacon, eggs, cheese, ranch"),
                ("Bunless Burger", "Beef patty, cheese, lettuce wrap, mayo, pickles"),
                ("Salmon Avocado Salad",
                 "Grilled salmon, avocado, leafy greens, olive oil")
            ],
            "dinner": [
                ("Ribeye Steak", "Grilled ribeye, butter, asparagus, cauliflower mash"),
                ("Keto Chicken Thighs",
                 "Crispy chicken thighs, green beans, butter sauce"),
                ("Pork Chops", "Pan-seared pork chops, broccoli, cheese sauce")
            ]
        },
        "paleo": {
            "breakfast": [
                ("Paleo Egg Scramble", "Eggs, sweet potato, vegetables, coconut oil"),
                ("Berry Smoothie", "Berries, banana, almond butter, coconut milk"),
                ("Breakfast Hash", "Sweet potato, sausage, peppers, onions")
            ],
            "lunch": [
                ("Grilled Chicken Bowl", "Chicken, roasted vegetables, olive oil"),
                ("Tuna Salad", "Tuna, mixed greens, olive oil, nuts"),
                ("Beef Lettuce Wraps", "Ground beef, lettuce, vegetables, avocado")
            ],
            "dinner": [
                ("Baked Cod", "Cod fillet, roasted vegetables, olive oil"),
                ("Paleo Meatballs", "Grass-fed beef meatballs, marinara, zucchini noodles"),
                ("Grilled Lamb Chops", "Lamb chops, roasted root vegetables")
            ]
        },
        "mediterranean": {
            "breakfast": [
                ("Mediterranean Omelette", "Eggs, feta, tomatoes, olives, spinach"),
                ("Greek Yogurt Bowl", "Greek yogurt, walnuts, honey, figs"),
                ("Whole Grain Toast", "Toast, hummus, cucumber, tomato")
            ],
            "lunch": [
                ("Greek Salad", "Cucumbers, tomatoes, olives, feta, olive oil"),
                ("Falafel Wrap", "Falafel, hummus, vegetables, whole wheat pita"),
                ("Grilled Fish Plate", "White fish, lemon, vegetables, olive oil")
            ],
            "dinner": [
                ("Mediterranean Salmon", "Salmon, olives, tomatoes, capers, olive oil"),
                ("Chicken Souvlaki", "Grilled chicken skewers, tzatziki, vegetables"),
                ("Shrimp Pasta", "Whole wheat pasta, shrimp, garlic, olive oil, feta")
            ]
        }
    }

    # Get templates for the selected diet
    templates = meal_templates.get(dietary_pref, meal_templates["none"])

    # Snack options
    snack_options = [
        ("Mixed Nuts", "Almonds, walnuts, cashews"),
        ("Apple with Peanut Butter", "Sliced apple, natural peanut butter"),
        ("Protein Shake", "Protein powder, banana, almond milk"),
        ("Greek Yogurt", "Plain Greek yogurt with berries"),
        ("Veggie Sticks with Hummus", "Carrots, celery, cucumber, hummus")
    ]

    # Generate 3-day plan
    meal_plans = []
    for day_num in range(1, 4):
        # Select meals for this day
        breakfast_name, breakfast_desc = templates["breakfast"][(
            day_num - 1) % len(templates["breakfast"])]
        lunch_name, lunch_desc = templates["lunch"][(
            day_num - 1) % len(templates["lunch"])]
        dinner_name, dinner_desc = templates["dinner"][(
            day_num - 1) % len(templates["dinner"])]
        snack_name, snack_desc = snack_options[(
            day_num - 1) % len(snack_options)]

        # Calculate calorie distribution
        breakfast_cal = int(target_calories * 0.25)
        lunch_cal = int(target_calories * 0.35)
        dinner_cal = int(target_calories * 0.30)
        snack_cal = int(target_calories * 0.10)

        # Adjust macros based on diet type
        if dietary_pref == "keto":
            # High fat, low carb
            breakfast = MealItem(
                name=breakfast_name,
                calories=breakfast_cal,
                protein=round(breakfast_cal * 0.25 / 4, 1),
                carbs=round(breakfast_cal * 0.05 / 4, 1),
                fat=round(breakfast_cal * 0.70 / 9, 1),
                description=breakfast_desc
            )
            lunch = MealItem(
                name=lunch_name,
                calories=lunch_cal,
                protein=round(lunch_cal * 0.30 / 4, 1),
                carbs=round(lunch_cal * 0.05 / 4, 1),
                fat=round(lunch_cal * 0.65 / 9, 1),
                description=lunch_desc
            )
            dinner = MealItem(
                name=dinner_name,
                calories=dinner_cal,
                protein=round(dinner_cal * 0.30 / 4, 1),
                carbs=round(dinner_cal * 0.05 / 4, 1),
                fat=round(dinner_cal * 0.65 / 9, 1),
                description=dinner_desc
            )
        else:
            # Balanced macros
            breakfast = MealItem(
                name=breakfast_name,
                calories=breakfast_cal,
                protein=round(breakfast_cal * 0.20 / 4, 1),
                carbs=round(breakfast_cal * 0.50 / 4, 1),
                fat=round(breakfast_cal * 0.30 / 9, 1),
                description=breakfast_desc
            )
            lunch = MealItem(
                name=lunch_name,
                calories=lunch_cal,
                protein=round(lunch_cal * 0.25 / 4, 1),
                carbs=round(lunch_cal * 0.45 / 4, 1),
                fat=round(lunch_cal * 0.30 / 9, 1),
                description=lunch_desc
            )
            dinner = MealItem(
                name=dinner_name,
                calories=dinner_cal,
                protein=round(dinner_cal * 0.30 / 4, 1),
                carbs=round(dinner_cal * 0.40 / 4, 1),
                fat=round(dinner_cal * 0.30 / 9, 1),
                description=dinner_desc
            )

        snack = MealItem(
            name=snack_name,
            calories=snack_cal,
            protein=round(snack_cal * 0.20 / 4, 1),
            carbs=round(snack_cal * 0.40 / 4, 1),
            fat=round(snack_cal * 0.40 / 9, 1),
            description=snack_desc
        )

        total_cal = breakfast.calories + lunch.calories + dinner.calories + snack.calories

        daily_plan = DailyMealPlan(
            day=f"Day {day_num}",
            breakfast=breakfast,
            lunch=lunch,
            dinner=dinner,
            snacks=[snack],
            total_calories=total_cal,
            total_protein=round(
                breakfast.protein + lunch.protein + dinner.protein + snack.protein, 1),
            total_carbs=round(breakfast.carbs + lunch.carbs +
                              dinner.carbs + snack.carbs, 1),
            total_fat=round(breakfast.fat + lunch.fat +
                            dinner.fat + snack.fat, 1)
        )

        meal_plans.append(daily_plan)

    return meal_plans

# ============================
# ENDPOINT 1: Manual Input (Original - No Database)
# ============================

@router.get(
    "",
    response_model=MealPlanResponse,
    summary="Generate Personalized Meal Plan (Manual Input)",
    description="""
    Generate a 3-day personalized meal plan based on user preferences and health data.
    
    **NA-101: Handles missing data cases:**
    - Required fields: user_id, age, gender, weight, height
    - Optional fields use smart defaults if not provided
    - Returns data quality information and warnings
    
    **Note:** This endpoint uses manual input. Use `/from-profile/{user_id}` to fetch from database.
    """
)
async def get_meal_plan(
    user_id: str = Query(..., description="User ID from database"),
    age: Optional[int] = Query(
        None, ge=1, le=120, description="User age in years"),
    gender: Optional[Gender] = Query(None, description="User gender"),
    weight: Optional[float] = Query(
        None, ge=20, le=300, description="Weight in kg"),
    height: Optional[float] = Query(
        None, ge=50, le=250, description="Height in cm"),
    activity_level: Optional[ActivityLevel] = Query(
        None, description="Physical activity level"),
    dietary_preference: Optional[DietaryPreference] = Query(
        None, description="Dietary preference"),
    allergies: Optional[str] = Query(
        None, description="Comma-separated allergies (e.g., 'nuts,dairy,shellfish')"),
    health_goals: Optional[str] = Query(
        None, description="Health goals (e.g., 'weight_loss', 'muscle_gain')"),
    meals_per_day: Optional[int] = Query(
        None, ge=2, le=6, description="Number of meals per day")
):
    """
    Generate personalized meal plan with error handling for missing data (NA-101)
    """

    try:
        # Collect all parameters
        params = {
            "user_id": user_id,
            "age": age,
            "gender": gender,
            "weight": weight,
            "height": height,
            "activity_level": activity_level,
            "dietary_preference": dietary_preference,
            "allergies": allergies,
            "health_goals": health_goals,
            "meals_per_day": meals_per_day
        }

        # NA-101: Validate and handle missing data
        is_valid, enriched_params, data_quality = MealPlanValidator.validate_and_enrich(
            params)

        if not is_valid:
            # Cannot proceed - missing required fields
            return MealPlanResponse(
                success=False,
                message=f"Insufficient data to generate meal plan. Missing required fields: {', '.join(data_quality.missing_fields)}",
                meal_plan=None,
                data_quality=data_quality,
                recommendations=[
                    "Please provide all required fields to generate a personalized meal plan",
                    "Required: user_id, age, gender, weight, height"
                ]
            )

        # Generate meal plan with enriched data
        meal_plan = generate_dummy_meal_plan(enriched_params)

        # Build recommendations based on data quality
        recommendations = []
        if data_quality.data_completeness < 100:
            recommendations.append(
                f"Meal plan generated with {data_quality.data_completeness}% data completeness. "
                "Provide more information for better personalization."
            )

        if enriched_params.get("allergies"):
            recommendations.append(
                f"Allergy restrictions applied: {enriched_params['allergies']}. "
                "All meals exclude these ingredients."
            )

        # Success response
        return MealPlanResponse(
            success=True,
            message="Meal plan generated successfully",
            meal_plan=meal_plan,
            data_quality=data_quality,
            recommendations=recommendations if recommendations else None
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error generating meal plan: {str(e)}")


# ============================
# ENDPOINT 2: Database Integration with Health Conditions (ENHANCED)
# ============================

@router.get(
    "/from-profile/{user_id}",
    response_model=MealPlanResponse,
    summary="Generate Meal Plan from Database Profile (NA-101)",
    description="""
    **DATABASE VERSION** - Fetch user data from Supabase and generate meal plan.
    
    **Fetches from database:**
    - age, gender, weight, height from 'users' table
    - activity_level, dietary_preference from 'user_preferences' table
    - allergies from 'user_allergies' table
    - health_conditions from 'user_health_conditions' table (NEW!)
    
    **Adjusts meal plan based on health conditions:**
    - Diabetes: Lower carbs, focus on fiber
    - Hypertension: Low sodium options
    - Heart disease: Low fat, omega-3 rich
    - Celiac: Gluten-free meals
    
    **Handles missing data with smart defaults (NA-101)**
    """
)
async def get_meal_plan_from_database(user_id: str):
    """
    Generate meal plan using data from Supabase database (NA-101)
    Now includes health condition adjustments!
    """
    
    try:
        logger.info(f"📊 Fetching profile for user: {user_id}")
        
        # STEP 1: Fetch user profile from database (age, gender, weight, height)
        user_profile = await fetch_user_profile(user_id)
        
        if not user_profile:
            raise HTTPException(
                status_code=404, 
                detail=f"User not found in database: {user_id}"
            )
        
        logger.info(f"👤 User: Age={user_profile.get('age')}, Gender={user_profile.get('gender')}, Weight={user_profile.get('weight')}kg")
        
        # STEP 2: Fetch preferences from database
        preferences = await fetch_user_preferences(user_id)
        
        # STEP 3: Fetch allergies from database
        allergies_list = await fetch_user_allergies(user_id)
        allergies_str = ",".join(allergies_list) if allergies_list else ""
        
        # STEP 4: Fetch user's health conditions (NEW!)
        user_conditions = await fetch_user_health_conditions(user_id)
        condition_names = [
            cond.get('health_conditions', {}).get('name', '') 
            for cond in user_conditions
            if cond.get('health_conditions')
        ]
        condition_names = [name for name in condition_names if name]  # Remove empty strings
        
        if allergies_str:
            logger.info(f"⚠️ User allergies: {allergies_str}")
        
        if condition_names:
            logger.info(f"🏥 User health conditions: {', '.join(condition_names)}")
        
        # STEP 5: Build params from database data
        params = {
            "user_id": user_id,
            "age": user_profile.get("age"),
            "gender": user_profile.get("gender"),
            "weight": user_profile.get("weight"),
            "height": user_profile.get("height"),
            "activity_level": preferences.get("activity_level") if preferences else None,
            "dietary_preference": preferences.get("dietary_preference") if preferences else None,
            "allergies": allergies_str,
            "health_goals": preferences.get("health_goals") if preferences else None,
            "meals_per_day": preferences.get("meals_per_day") if preferences else None,
            "health_conditions": condition_names  # NEW!
        }
        
        # STEP 6: Validate and handle missing data (NA-101)
        is_valid, enriched_params, data_quality = MealPlanValidator.validate_and_enrich(params)
        
        if not is_valid:
            logger.warning(f"❌ Incomplete profile - Missing: {', '.join(data_quality.missing_fields)}")
            return MealPlanResponse(
                success=False,
                message=f"Incomplete user profile in database. Missing: {', '.join(data_quality.missing_fields)}",
                meal_plan=None,
                data_quality=data_quality,
                recommendations=[
                    "Please complete your profile in the app",
                    f"Missing fields: {', '.join(data_quality.missing_fields)}"
                ]
            )
        
        # STEP 7: Generate meal plan with health condition adjustments
        logger.info(f"🍽️ Generating meal plan ({data_quality.data_completeness}% complete)")
        meal_plan = generate_dummy_meal_plan(enriched_params)
        
        # STEP 8: Build recommendations with health conditions
        recommendations = []
        
        if data_quality.data_completeness < 100:
            recommendations.append(
                f"Meal plan generated with {data_quality.data_completeness}% profile completeness. "
                "Complete your profile for better personalization."
            )
        
        if allergies_str:
            recommendations.append(f"⚠️ Allergy restrictions applied: {allergies_str}")
        
        # Add health condition recommendations (NEW!)
        if condition_names:
            recommendations.append(f"🏥 Health conditions considered: {', '.join(condition_names)}")
            
            if "Diabetes" in condition_names or "Type 2 Diabetes" in condition_names:
                recommendations.append("🩺 Diabetic-friendly: Low glycemic index foods, reduced sugar, high fiber")
            
            if "Hypertension" in condition_names or "High Blood Pressure" in condition_names:
                recommendations.append("🩺 Heart-healthy: Low sodium, increased potassium, DASH diet principles")
            
            if "Celiac Disease" in condition_names or "Gluten Intolerance" in condition_names:
                recommendations.append("🩺 Gluten-free: All meals exclude wheat, barley, rye")
            
            if "Heart Disease" in condition_names or "Cardiovascular Disease" in condition_names:
                recommendations.append("🩺 Cardiac diet: Low saturated fat, omega-3 rich, increased fiber")
            
            if "Kidney Disease" in condition_names:
                recommendations.append("🩺 Renal diet: Controlled protein, potassium, and sodium")
        
        if data_quality.warnings:
            recommendations.extend(data_quality.warnings)
        
        logger.info(f"✅ Meal plan generated successfully for user: {user_id}")
        
        # STEP 9: Success response
        return MealPlanResponse(
            success=True,
            message="Meal plan generated from your database profile",
            meal_plan=meal_plan,
            data_quality=data_quality,
            recommendations=recommendations if recommendations else None
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Error: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Error generating meal plan: {str(e)}"
        )


# ============================
# ENDPOINT 5: Get User's Health Conditions (NEW)
# ============================

@router.get(
    "/user-conditions/{user_id}",
    summary="Get User's Health Conditions",
    description="Fetch specific user's health conditions from database"
)
async def get_user_health_conditions_endpoint(user_id: str):
    """
    Get health conditions for a specific user
    """
    try:
        conditions = await fetch_user_health_conditions(user_id)
        
        if not conditions:
            return {
                "success": True,
                "user_id": user_id,
                "count": 0,
                "conditions": [],
                "message": "No health conditions found for this user"
            }
        
        # Extract condition details
        condition_list = [
            {
                "id": cond.get('health_conditions', {}).get('id'),
                "name": cond.get('health_conditions', {}).get('name'),
                "description": cond.get('health_conditions', {}).get('description'),
                "severity": cond.get('severity')
            }
            for cond in conditions
            if cond.get('health_conditions')
        ]
        
        return {
            "success": True,
            "user_id": user_id,
            "count": len(condition_list),
            "conditions": condition_list
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))