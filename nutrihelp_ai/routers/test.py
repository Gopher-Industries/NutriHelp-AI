import json
import random
import re
import os

ALLERGY_MAP = {
    "nuts": ["contains_nuts", "contains_tree_nut", "contains_peanut"],
    "peanut": ["contains_peanut"],
    "tree_nut": ["contains_tree_nut"],
    "dairy": ["contains_dairy", "contains_milk", "contains_cheese", "contains_yoghurt", "contains_butter", "contains_cream", "contains_whey", "contains_casein", "contains_lactose"],
    "milk": ["contains_milk", "contains_dairy"],
    "egg": ["contains_egg"],
    "soy": ["contains_soy"],
    "gluten": ["contains_gluten", "contains_wheat", "contains_barley", "contains_rye"],
    "wheat": ["contains_wheat", "contains_gluten"],
    "shellfish": ["contains_shellfish"],
    "fish": ["contains_fish"],
    "fruit": ["contains_fruit", "contains_apple", "contains_banana", "contains_citrus", "contains_orange", "contains_lemon", "contains_lime", "contains_grapefruit", "contains_strawberry",
              "contains_kiwi", "contains_peach", "contains_mango", "contains_pineapple"],
    "sesame": ["contains_sesame", "contains_tahini"],
    "apple": ["contains_apple"],
    "banana": ["contains_banana"],
    "citrus": ["contains_citrus", "contains_orange", "contains_lemon", "contains_lime", "contains_grapefruit"],
    "strawberry": ["contains_strawberry"],
    "kiwi": ["contains_kiwi"],
}

CONDITION_MAP = {
    # Diabetes: avoid high sugar and high GI meals
    "diabetes": ["high_sugar", "high_gi", "added_sugar", "refined_carb", "sugary_drink", "dessert", "fried", "high_saturated_fat", "processed_meat", "high_salt"],
    # High cholesterol: avoid high fat (saturared and fried foods)
    "cholesterol": ["high_fat", "fried", "high_saturated_fat"],
    "high_cholesterol": ["high_fat", "fried", "high_saturated_fat"],
    # Hypertension
    "hypertension": ["high_salt", "very_high_salt", "processed_meat", "pickled", "soy_sauce_heavy"],
    "high_blood_pressure": ["high_salt", "very_high_salt", "processed_meat", "pickled", "soy_sauce_heavy"],
    # Kidney Disease
    "kidney_disease": ["high_potassium", "high_phosphorus", "high_protein"],
    "ckd": ["high_potassium", "high_phosphorus", "high_protein"],
    # Elderly condition rules
    "elderly": ["hard_food", "crunchy", "tough_meat", "very_high_salt", "fried", "very_spicy"]
}


def detect_allergens(text: str) -> list[str]:
    if not text:
        return []

    t = text.lower()

    keywords = {
        "dairy": ["milk", "cheese", "yoghurt", "yogurt", "butter", "cream", "whey", "casein", "lactose"],
        "egg": ["egg", "eggs", "albumen", "ovalbumin", "egg white", "egg yolk", "mayonaise", "mayonnaise"],
        "soy": ["soy", "soya", "soybean", "tofu", "edamame", "lecithin (soy)", "soy lecithin"],
        "gluten": ["gluten", "wheat", "barley", "rye", "malt", "flour"],
        "peanut": ["peanut", "groundnut", "peanut oil", "peanut butter"],
        "nuts": ["nuts", "almond", "cashew", "walnut", "hazelnut", "pistachio", "pecan", "macadamia"],
        "fish": ["fish", "salmon", "tuna", "cod", "anchovy", "sardine"],
        "shellfish": ["shellfish", "shrimp", "prawn", "crab", "lobster", "clam", "clams", "mussel", "mussels", "oyster", "oysters", "scallop", "scallops"],
        "sesame": ["sesame", "sesame seed", "sesame oil", "tahini", "hummus"],
        "apple": ["apple", "apples", "apple juice", "apple puree"],
        "banana": ["banana", "bananas", "banana powder"],
        "citrus": ["orange", "oranges", "lemon", "lemons", "lime", "limes", "grapefruit", "mandarin", "citrus"],
        "fruit": ["strawberry", "strawberries", "kiwi", "kiwi fruit", "peach", "peaches", "mango", "mangoes", "pineapple"]
    }

    found = set()
    for allergen, words in keywords.items():
        for w in words:
            if re.search(rf"\b{re.escape(w)}\b", t):
                found.add(allergen)
                break

    if "citrus" in found:
        found.add("fruit")

    found = [a for a in found if a in ALLERGY_MAP]

    return list(found)

# Load meals form JSON file


def meal_library():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, "meal_library.json")
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def normalise_list_input(value):
    # None -> []
    if value is None:
        return []
    # list -> same list
    if isinstance(value, list):
        return value
    # string "a,b"  -> ["a", "b"]
    # string "a" -> ["a"]
    if isinstance(value, str):
        # split by comma if needed
        parts = [v.strip() for v in value.split(",")]
        return [p for p in parts if p]  # remove empty strings
    # any other weird type
    return []

# Filter by allergies


def filter_allergy(meals, allergies):

    result = []

    allergies_lowercase = []
    for a in allergies:
        allergies_lowercase.append(a.lower())

    for meal in meals:
        has_allergy = False

        for allergy in allergies_lowercase:
            if allergy in ALLERGY_MAP:
                to_avoid = ALLERGY_MAP[allergy]
            else:
                to_avoid = []

            for tag in to_avoid:
                if tag in meal["tags"]:
                    has_allergy = True
                    break

            if has_allergy:
                break

        if not has_allergy:
            result.append(meal)
    return result

# Filter by health condition


def filter_condition(meals, conditions):
    result = []

    conditions_lowercase = []
    for c in conditions:
        conditions_lowercase.append(c.lower())

    for meal in meals:
        bad = False

        for condition in conditions_lowercase:
            if condition in CONDITION_MAP:
                bad_tag = CONDITION_MAP[condition]
            else:
                bad_tag = []

            for tag in bad_tag:
                if tag in meal["tags"]:
                    bad = True
                    break

            if bad:
                break

        if not bad:
            result.append(meal)

    return result

# Filter by texture requirement


def filter_texture(meals, text):
    if text is None:
        text = "normal"

    text = text.lower()

    # We filter only if user needs soft food
    if text != "soft":
        return meals

    soft_meals = []
    for meal in meals:
        if "soft_food" in meal["tags"]:
            soft_meals.append(meal)

    return soft_meals


def filter_budget(meals, budget):
    if budget is None:
        budget = "medium"
    budget = str(budget).lower()

    # preference order (fallback)
    if budget == "low":
        preferred_orders = [["cost_low"], ["cost_low", "cost_medium"], [
            "cost_low", "cost_medium", "cost_high"]]
    elif budget == "medium":
        preferred_orders = [["cost_medium"], ["cost_medium", "cost_low"], [
            "cost_medium", "cost_low", "cost_high"]]
    else:
        # high budget: no need to restrict
        return meals

    # Try strict first, then relax
    for allowed in preferred_orders:
        filtered = []
        for meal in meals:
            tags = meal.get("tags", [])
            if any(cost_tag in tags for cost_tag in allowed):
                filtered.append(meal)
        if len(filtered) > 0:
            return filtered

    # if no cost tags exist at all, return original
    return meals


def pick_meal_under_calories(meals, remaining_calories):
    valid_meals = [m for m in meals if m.get(
        "calories", 0) <= remaining_calories]
    if not valid_meals:
        return None
    return random.choice(valid_meals)


# Build the plan
def plan(user, all_meals):
    if user is None:
        user = {}

    # FALLBACK LOGIC FOR LIMITED INPUT
    # allergies or conditions can be missing, string, or list
    raw_allergies = user.get("allergies", [])
    raw_conditions = user.get("conditions", [])

    allergies = normalise_list_input(raw_allergies)
    conditions = normalise_list_input(raw_conditions)

    label_text = user.get("label_text", "")
    detected_allergies = detect_allergens(label_text)

    # Combine user allergies + detected allergies
    allergies = allergies + detected_allergies
    allergies = list(set([a.lower() for a in allergies]))

    # texture: default to "normal" if missing or empty
    texture = user.get("texture") or "normal"

    budget = user.get("budget") or "medium"

    # calories_target: default to 2000 if not given
    calories = user.get("calories_target")
    if calories is None:
        calories = 2000

    # Apply filters step by step
    filtered = filter_allergy(all_meals, allergies)
    filtered = filter_condition(filtered, conditions)
    filtered = filter_texture(filtered, texture)

    conditions_lower = [str(c).lower() for c in conditions]
    if "elderly" in conditions_lower:
        soft_meals = [
            meal for meal in filtered if "soft_food" in meal.get("tags", [])]
        if len(soft_meals) > 0:
            filtered = soft_meals

    filtered = filter_budget(filtered, budget)

    # Split meals by type
    breakfasts = []
    lunches = []
    dinners = []
    snacks = []

    for meal in filtered:
        if meal["meal_type"] == "breakfast":
            breakfasts.append(meal)
        elif meal["meal_type"] == "lunch":
            lunches.append(meal)
        elif meal["meal_type"] == "dinner":
            dinners.append(meal)
        elif meal["meal_type"] == "snack":
            snacks.append(meal)

    # Pick one meal for each main meal, and up to 2 snacks
    remaining_calories = calories

    plan = {
        "breakfast": None,
        "lunch": None,
        "dinner": None,
        "snacks": []
    }

    # Pick breakfast
    plan["breakfast"] = pick_meal_under_calories(
        breakfasts, remaining_calories)
    if plan["breakfast"]:
        remaining_calories -= plan["breakfast"]["calories"]

    # Pick lunch
    plan["lunch"] = pick_meal_under_calories(lunches, remaining_calories)
    if plan["lunch"]:
        remaining_calories -= plan["lunch"]["calories"]

    # Pick dinner
    plan["dinner"] = pick_meal_under_calories(dinners, remaining_calories)
    if plan["dinner"]:
        remaining_calories -= plan["dinner"]["calories"]

    # Dinner fallback — MUST respect remaining calories
    if plan["dinner"] is None:
        soft_dinners = [m for m in dinners if "soft_food" in m.get("tags", [])]
        plan["dinner"] = pick_meal_under_calories(
            soft_dinners, remaining_calories)

        # Reuse lunch ONLY if it fits remaining calories
        if plan["dinner"] is None and plan["lunch"] is not None:
            if plan["lunch"]["calories"] <= remaining_calories:
                plan["dinner"] = plan["lunch"]
                remaining_calories -= plan["lunch"]["calories"]

    for snack in snacks:
        if len(plan["snacks"]) >= 2:
            break
        if snack["calories"] <= remaining_calories:
            plan["snacks"].append(snack)
            remaining_calories -= snack["calories"]

    # Calculate total calories
    total_calories = 0

    if plan["breakfast"] is not None:
        total_calories += plan["breakfast"]["calories"]
    if plan["lunch"] is not None:
        total_calories += plan["lunch"]["calories"]
    if plan["dinner"] is not None:
        total_calories += plan["dinner"]["calories"]

    for snack in plan["snacks"]:
        total_calories += snack["calories"]

    plan["total_calories"] = total_calories
    plan["target_calories"] = calories

    plan["allergies_used"] = allergies
    plan["detected_allergies_from_label"] = detected_allergies
    plan["budget_used"] = budget

    return plan


if __name__ == "__main__":
    meals = meal_library()

    # Test 1: Dairy allergy
    user_dairy_allergy = {
        "name": "Test Dairy Allergy",
        "label_text": "",
        "allergies": [],
        "conditions": [],
        "budget": "medium",
        "texture": "normal",
        "calories_target": 1500
    }

    print("\n=== TEST 1: Dairy Allergy ===")
    result1 = plan(user_dairy_allergy, meals)
    print(json.dumps(result1, indent=2, ensure_ascii=False))
