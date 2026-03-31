""" AI Reasoning Module - Enhanced for Better Meal Plans """
from config import GEMINI_API_KEY, GEMINI_MODEL
import pandas as pd
from typing import Dict, Optional, Tuple, List
from google import genai

# Initialize client ONCE
client = genai.Client(api_key=GEMINI_API_KEY)


def validate_profile(user_profile: Dict) -> Tuple[bool, str]:
    """
    STRICT VALIDATION ENGINE
    """
    goal = user_profile.get('goal', '').lower()
    valid_goals = ['lose', 'weight', 'fat', 'gain',
                   'muscle', 'bulk', 'maintain', 'health', 'fitness']
    if len(goal) < 3 or goal in ['yes', 'no', 'ok', 'good', 'bad'] or not any(x in goal for x in valid_goals):
        return False, "Your health goal is unclear. Please answer with: Lose weight, Gain muscle, or Maintain health."

    activity = user_profile.get('sport', '').lower()
    valid_activities = ['gym', 'walk', 'run', 'yoga', 'swim', 'sport', 'none', 'sedentary',
                        'active', 'moderate', 'exercise', 'training', 'cricket', 'football', 'cycling']
    if len(activity) < 3 or not any(x in activity for x in valid_activities):
        return False, "Physical activity answer is invalid."

    level = user_profile.get('level', '').lower()
    valid_levels = ['begin', 'interm', 'advan', 'pro']
    if not any(x in level for x in valid_levels):
        return False, "Fitness level invalid."

    diet = user_profile.get('diet', '').lower()
    valid_diets = ['veg', 'non', 'meat', 'egg', 'pesc', 'omni']
    if not any(x in diet for x in valid_diets):
        return False, "Diet preference unclear."

    # FIXED: More flexible medical condition validation
    cond = user_profile.get('condition', '').lower().strip()
    safe_indicators = ['none', 'no', 'not', 'nothing',
                       'na', 'n/a', 'nil', 'healthy', 'fine']

    # Check if it's a "no condition" response
    has_safe_word = any(word in cond for word in safe_indicators)

    # If it contains safe words, accept it
    if has_safe_word:
        pass  # Valid response
    # If it's too short or generic (but doesn't say "no condition"), reject
    elif len(cond) < 3 or cond in ['yes', 'ok', 'good', 'bad']:
        return False, "Medical condition answer is invalid. Please state 'None' or a specific condition (e.g., diabetes, hypertension)."
    # Otherwise, assume it's a specific condition name, which is valid

    # FIXED: Better allergy validation
    allergies = user_profile.get('allergies', [])

    # Handle string input
    if isinstance(allergies, str):
        allergies = [a.strip() for a in allergies.split(',') if a.strip()]

    # Filter out empty strings and clean up
    cleaned_allergies = []
    for alg in allergies:
        cleaned = str(alg).strip()
        if cleaned:
            cleaned_allergies.append(cleaned)

    # If no allergies, that's fine
    if not cleaned_allergies:
        return True, "Profile Validated"

    # Check each allergy
    safe_allergy_words = ['none', 'no', 'nothing', 'na', 'n/a', 'nil']
    for alg in cleaned_allergies:
        a = alg.lower().strip()

        # Skip if it's a "no allergy" indicator
        if a in safe_allergy_words:
            continue

        # If it's too short or too generic, reject
        if len(a) < 2 or a in ['yes', 'ok', 'i', 'a']:
            return False, f"Allergy answer '{alg}' is invalid. Please state 'None' or specific allergies (e.g., peanuts, dairy, gluten)."

    return True, "Profile Validated"


def generate_meal_plan(user_profile: Dict, data_loader, start_day: int = 1) -> str:
    is_valid, error_msg = validate_profile(user_profile)
    if not is_valid:
        return f"ERROR: {error_msg}"

    # Handle condition info
    condition_str = user_profile.get('condition', '').lower().strip()
    condition_info = None
    safe_condition_indicators = ['none', 'no', 'not',
                                 'nothing', 'na', 'n/a', 'nil', 'healthy', 'fine']

    if condition_str and not any(word in condition_str for word in safe_condition_indicators):
        if data_loader:
            condition_info = data_loader.get_condition_info(
                user_profile['condition'])

    # Get sport gear
    sport_gear_list = []
    if data_loader:
        sport_gear_list = data_loader.get_sport_gear(
            user_profile.get('sport', 'general'))

    # Filter recipes by allergies
    safe_recipes = None
    if data_loader:
        safe_recipes = data_loader.filter_by_allergies(
            user_profile.get('allergies', []))

    # Sort recipes based on goal
    if safe_recipes is not None and not safe_recipes.empty:
        user_goal = user_profile.get('goal', '').lower()
        if 'muscle' in user_goal or 'gain' in user_goal:
            sorted_recipes = safe_recipes.sort_values(
                by='protein', ascending=False)
        elif 'loss' in user_goal or 'lose' in user_goal:
            sorted_recipes = safe_recipes[safe_recipes['calories'] > 0].sort_values(
                by='calories')
        else:
            sorted_recipes = safe_recipes

        final_recipe_pool = sorted_recipes.head(25)
    else:
        final_recipe_pool = pd.DataFrame()

    prompt = _build_strict_prompt(
        user_profile, condition_info, final_recipe_pool, sport_gear_list, start_day
    )

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config={
                "temperature": 0.3,
                "max_output_tokens": 8000
            }
        )
        return response.text.strip()

    except Exception as e:
        return f"System Error: {type(e).__name__}: {str(e)}"


def _build_strict_prompt(user_profile: Dict, condition_info: Optional[Dict],
                         available_recipes: pd.DataFrame, sport_gear: List[str], start_day: int) -> str:
    recipe_text = "Standard healthy options."
    if not available_recipes.empty:
        recipe_text = "; ".join(
            f"{row['recipe_name']} ({row['calories']:.0f} cal)"
            for _, row in available_recipes.iterrows()
        )

    cond_str = "None"
    if condition_info:
        cond_str = (
            f"{condition_info['name']} "
            f"Must Eat: {', '.join(condition_info['recommended'])} "
            f"Avoid: {', '.join(condition_info['restricted'])}"
        )

    gear_str = ", ".join(
        sport_gear) if sport_gear else "Standard Athletic Wear"
    end_day = start_day + 6

    # Clean up allergies for display
    allergies = user_profile.get('allergies', [])
    if isinstance(allergies, str):
        allergies = [allergies]
    allergy_display = ', '.join([str(a).strip()
                                for a in allergies if str(a).strip()])
    if not allergy_display:
        allergy_display = "None"

    return f"""
ROLE: Strict Clinical Nutrition & Sports Engine.
TASK: Generate a {start_day}-Day to {end_day}-Day Meal Plan + Sport Gear Checklist.

USER DATA:
Goal: {user_profile.get('goal')}
Activity: {user_profile.get('sport')}
Level: {user_profile.get('level')}
Diet: {user_profile.get('diet')}
Condition: {cond_str}
Allergies: {allergy_display}

AVAILABLE RECIPES:
{recipe_text}
RECOMMENDED SPORT GEAR:
{gear_str}

RULES:
1. Generate exactly 7 days (Day {start_day} to Day {end_day})
2. Plain text only. No markdown formatting.
3. Each day must include: Breakfast, Mid-Morning Snack, Lunch, Evening Snack, Dinner
4. Respect dietary restrictions: {user_profile.get('diet')}
5. Avoid all allergies: {allergy_display}
6. Calories should align with goal: {user_profile.get('goal')}

FORMAT:
Day {start_day}
Breakfast: [meal details with calories]
Mid-Morning Snack: [snack details]
Lunch: [meal details with calories]
Evening Snack: [snack details]
Dinner: [meal details with calories]
Total Calories: [number]

...continue for all 7 days...

Day {end_day}
[same format]

SPORT GEAR CHECKLIST FOR {user_profile.get('sport')}:
{gear_str}
"""


def get_quick_nutrition_advice(question: str) -> str:
    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=f"Answer strictly in plain text: {question}",
            config={
                "temperature": 0.5,
                "max_output_tokens": 300
            }
        )
        return response.text.strip()
    except Exception:
        return "Service unavailable."
