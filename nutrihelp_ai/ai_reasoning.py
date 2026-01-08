# """
# AI Reasoning Module - Enhanced for Better Meal Plans
# """

import pandas as pd
from typing import Dict, Optional, Tuple, List
from google import genai
from google.genai.types import GenerateContentConfig
# from config import GEMINI_API_KEY, GEMINI_MODEL
from config import GEMINI_API_KEY, GEMINI_MODEL

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)


def validate_profile(user_profile: Dict) -> Tuple[bool, str]:
    """
    STRICT VALIDATION ENGINE
    Checks if user answers logically match the required questions.
    Returns: (isValid: bool, ErrorMessage: str)
    """

    # 1. Validate Health Goal
    goal = user_profile.get('goal', '').lower()
    valid_goals = ['lose', 'weight', 'fat', 'gain',
                   'muscle', 'bulk', 'maintain', 'health', 'fitness']
    if len(goal) < 3 or goal in ['yes', 'no', 'ok', 'good', 'bad'] or not any(x in goal for x in valid_goals):
        return False, "Your health goal is unclear. Please answer with: 'Lose weight', 'Gain muscle', or 'Maintain health'."

    # 2. Validate Physical Activity
    activity = user_profile.get('sport', '').lower()
    valid_activities = ['gym', 'walk', 'run', 'yoga', 'swim', 'sport', 'none', 'sedentary',
                        'active', 'moderate', 'exercise', 'training', 'cricket', 'football', 'cycling']
    if len(activity) < 3 or not any(x in activity for x in valid_activities):
        return False, "Physical activity answer is invalid. Please specify: Gym, Walking, Running, Yoga, Swimming, etc."

    # 3. Validate Fitness Level
    level = user_profile.get('level', '').lower()
    valid_levels = ['begin', 'interm', 'advan', 'pro']
    if not any(x in level for x in valid_levels):
        return False, "Fitness level invalid. Please choose: Beginner, Intermediate, or Advanced."

    # 4. Validate Diet Preference
    diet = user_profile.get('diet', '').lower()
    valid_diets = ['veg', 'non', 'meat', 'egg', 'pesc', 'omni']
    if not any(x in diet for x in valid_diets):
        return False, "Diet preference unclear. Please choose: Vegetarian, Non-vegetarian, Vegan, or Eggetarian."

    # 5. Validate Condition (Explicitly allow 'none', 'no', etc.)
    cond = user_profile.get('condition', '').lower().strip()
    safe_words = ['none', 'no', 'nothing', 'na',
                  'n/a', 'no condition', 'nil', 'None']

    if cond in safe_words:
        pass
    elif len(cond) < 3 or cond in ['yes', 'ok', 'good', 'bad', 'sure']:
        return False, "Medical condition answer is invalid. Please state 'None' or a specific condition (e.g., Diabetes)."

    # 6. Validate Allergies
    allergies = user_profile.get('allergies', [])
    if isinstance(allergies, str):
        allergies = [allergies]

    for alg in allergies:
        alg_str = alg.lower().strip()
        safe_allergy_words = ['none', 'no', 'nothing', 'na', 'n/a']

        if alg_str in safe_allergy_words:
            continue

        if len(alg_str) < 3 or alg_str in ['yes', 'ok', 'food', 'good']:
            return False, "Allergy answer is invalid. Please state 'None' or specific foods (e.g., Peanuts, Dairy)."

    return True, "Profile Validated"


def generate_meal_plan(user_profile: Dict, data_loader, start_day: int = 1) -> str:
    """
    Generates a STRICT 6-Day Meal Plan WITH SPORT GEAR.
    Args:
        start_day: The day number to start generating from (default 1).
    """

    # --- STEP 1: STRICT VALIDATION ---
    is_valid, error_msg = validate_profile(user_profile)
    if not is_valid:
        print(f"[AI] ⛔ Validation Failed: {error_msg}")
        return f"ERROR: {error_msg}\nPlease provide a correct answer."

    # --- STEP 2: DATA PREPARATION ---

    # Get condition info
    condition_info = None
    if user_profile.get('condition') and user_profile['condition'].lower() not in ['none', 'no', 'nothing']:
        condition_info = data_loader.get_condition_info(
            user_profile['condition'])

    # Get Sport Gear Recommendations (NEW)
    sport_gear_list = data_loader.get_sport_gear(
        user_profile.get('sport', 'general'))

    # Filter recipes
    safe_recipes = data_loader.filter_by_allergies(
        user_profile.get('allergies', []))

    # Sort based on goal
    user_goal = user_profile.get('goal', '').lower()
    if 'muscle' in user_goal or 'gain' in user_goal:
        sorted_recipes = safe_recipes.sort_values(
            by='protein', ascending=False)
    elif 'loss' in user_goal:
        valid_cal = safe_recipes[safe_recipes['calories'] > 0]
        sorted_recipes = valid_cal.sort_values(by='calories', ascending=True)
    else:
        sorted_recipes = safe_recipes

    # Select top matches
    final_recipe_pool = sorted_recipes.head(25)

    # --- STEP 3: BUILD STRICT PROMPT ---
    prompt = _build_strict_prompt(
        user_profile, condition_info, final_recipe_pool, sport_gear_list, start_day)

    try:
        print(
            f"[AI] Generating Days {start_day} to {start_day + 5} + Gear Recommendations...")

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config=GenerateContentConfig(
                temperature=0.3,
                max_output_tokens=8000
            )
        )
        return response.text

    except Exception as e:
        print(f"[AI] ✗ Error: {e}")
        return "System Error: Unable to generate plan. Please try again."


def _build_strict_prompt(user_profile: Dict, condition_info: Optional[Dict],
                         available_recipes: pd.DataFrame, sport_gear: List[str], start_day: int) -> str:

    # Format Recipe String
    recipe_text = "Standard healthy options."
    if len(available_recipes) > 0:
        r_list = [f"{row['recipe_name']} ({row['calories']:.0f} cal)" for _,
                  row in available_recipes.iterrows()]
        recipe_text = "; ".join(r_list)

    # Format Condition String
    cond_str = "None"
    if condition_info:
        cond_str = f"{condition_info['name']}\n   (Must Eat: {', '.join(condition_info['recommended'])})\n   (Avoid: {', '.join(condition_info['restricted'])})"

    # Format Sport Gear String
    gear_str = ", ".join(
        sport_gear) if sport_gear else "Standard Athletic Wear"

    # Calculate End Day
    end_day = start_day + 5

    prompt = f"""
    ROLE: Strict Clinical Nutrition & Sports Engine.
    TASK: Generate a {start_day}-Day to {end_day}-Day Meal Plan + Sport Gear Checklist.

    USER DATA (VALIDATED):
    - Goal: {user_profile.get('goal')}
    - Activity: {user_profile.get('sport')}
    - Level: {user_profile.get('level')}
    - Diet: {user_profile.get('diet')}
    - Condition: {cond_str}
    - Allergies: {user_profile.get('allergies')}

    AVAILABLE RECIPES: {recipe_text}
    
    RECOMMENDED SPORT GEAR: {gear_str}

    ==================================================
    CRITICAL GENERATION RULES:
    1. Generate EXACTLY 6 DAYS (Day {start_day} to Day {end_day}).
    2. DO NOT STOP GENERATING UNTIL DAY {end_day} IS COMPLETE.
    3. Start directly with Day {start_day}.
    4. PLAIN TEXT ONLY. NO Markdown, NO Emojis, NO Bullets.
    5. Each day MUST include: Breakfast, Mid-Morning Snack, Lunch, Evening Snack, Dinner.
    6. Include Calorie counts and Prep Time for main meals.
    7. AFTER DAY {end_day}, ADD A "SPORT GEAR CHECKLIST" SECTION based on the data provided above.
    ==================================================

    OUTPUT TEMPLATE (Must follow strict format):

    Day {start_day}
    Breakfast: [Meal] | [Cal] cal | [Time] min
    Mid-Morning Snack: [Meal] | [Cal] cal
    Lunch: [Meal] | [Cal] cal | [Time] min
    Evening Snack: [Meal] | [Cal] cal
    Dinner: [Meal] | [Cal] cal | [Time] min

    Day {start_day + 1}
    (Repeat Format)

    ...

    Day {end_day}
    (Repeat Format)
    

    SPORT GEAR CHECKLIST
    (List the recommended gear items provided in the prompt)

    (STOP GENERATION HERE)
    """
    return prompt


def get_quick_nutrition_advice(question: str) -> str:
    """Quick Q&A - Text Only"""
    try:
        print("started quick qna......")
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=f"Answer strictly in plain text (no markdown): {question}",
            config=GenerateContentConfig(
                temperature=0.5, max_output_tokens=300)
        )
        print(f"[AI] Quick Q&A Response: {response.text}")
        return response.text
    except Exception as e:
        print(f"[AI] ✗ Quick Q&A Error: {e}")
        return "Service unavailable."
