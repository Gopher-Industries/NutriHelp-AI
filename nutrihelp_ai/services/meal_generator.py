import json
import os
import re
from typing import Dict, List, Optional, Tuple

ALLERGY_MAP = {
    "nuts": ["contains_nuts", "contains_tree_nut", "contains_peanut"],
    "peanut": ["contains_peanut"],
    "tree_nut": ["contains_tree_nut"],
    "dairy": [
        "contains_dairy",
        "contains_milk",
        "contains_cheese",
        "contains_yoghurt",
        "contains_butter",
        "contains_cream",
        "contains_whey",
        "contains_casein",
        "contains_lactose",
    ],
    "milk": ["contains_milk", "contains_dairy"],
    "egg": ["contains_egg"],
    "soy": ["contains_soy"],
    "gluten": ["contains_gluten", "contains_wheat", "contains_barley", "contains_rye"],
    "wheat": ["contains_wheat", "contains_gluten"],
    "shellfish": ["contains_shellfish"],
    "fish": ["contains_fish"],
    "fruit": [
        "contains_fruit",
        "contains_apple",
        "contains_banana",
        "contains_citrus",
        "contains_orange",
        "contains_lemon",
        "contains_lime",
        "contains_grapefruit",
        "contains_strawberry",
        "contains_kiwi",
        "contains_peach",
        "contains_mango",
        "contains_pineapple",
    ],
    "sesame": ["contains_sesame", "contains_tahini"],
    "apple": ["contains_apple"],
    "banana": ["contains_banana"],
    "citrus": ["contains_citrus", "contains_orange", "contains_lemon", "contains_lime", "contains_grapefruit"],
    "strawberry": ["contains_strawberry"],
    "kiwi": ["contains_kiwi"],
}

CONDITION_MAP = {
    "diabetes": [
        "high_sugar",
        "high_gi",
        "added_sugar",
        "refined_carb",
        "sugary_drink",
        "dessert",
        "fried",
        "high_saturated_fat",
        "processed_meat",
        "high_salt",
    ],
    "cholesterol": ["high_fat", "fried", "high_saturated_fat"],
    "high_cholesterol": ["high_fat", "fried", "high_saturated_fat"],
    "hypertension": ["high_salt", "very_high_salt", "processed_meat", "pickled", "soy_sauce_heavy"],
    "high_blood_pressure": ["high_salt", "very_high_salt", "processed_meat", "pickled", "soy_sauce_heavy"],
    "kidney_disease": ["high_potassium", "high_phosphorus", "high_protein"],
    "ckd": ["high_potassium", "high_phosphorus", "high_protein"],
    "elderly": ["hard_food", "crunchy", "tough_meat", "very_high_salt", "fried", "very_spicy"],
}

CONDITION_PREFERENCE_MAP = {
    "diabetes": ["low_sugar", "low_gi", "high_fibre", "high_protein"],
    "cholesterol": ["heart_healthy", "low_fat", "high_fibre", "omega3_rich"],
    "high_cholesterol": ["heart_healthy", "low_fat", "high_fibre", "omega3_rich"],
    "hypertension": ["low_salt", "high_fibre", "heart_healthy"],
    "high_blood_pressure": ["low_salt", "high_fibre", "heart_healthy"],
    "kidney_disease": ["low_salt", "low_fat", "soft_food"],
    "ckd": ["low_salt", "low_fat", "soft_food"],
    "elderly": ["soft_food", "high_protein", "high_fibre"],
}

MEAL_TYPE_CALORIE_DISTRIBUTION = {
    "breakfast": 0.25,
    "lunch": 0.35,
    "dinner": 0.30,
    "snack": 0.10,
}

SORT_KEYS = {
    "balanced",
    "prep_time",
    "cook_time",
    "total_time",
    "high_protein",
    "high_fibre",
    "low_calories",
}


def detect_allergens(text: str) -> List[str]:
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
        "shellfish": [
            "shellfish",
            "shrimp",
            "prawn",
            "crab",
            "lobster",
            "clam",
            "clams",
            "mussel",
            "mussels",
            "oyster",
            "oysters",
            "scallop",
            "scallops",
        ],
        "sesame": ["sesame", "sesame seed", "sesame oil", "tahini", "hummus"],
        "apple": ["apple", "apples", "apple juice", "apple puree"],
        "banana": ["banana", "bananas", "banana powder"],
        "citrus": ["orange", "oranges", "lemon", "lemons", "lime", "limes", "grapefruit", "mandarin", "citrus"],
        "fruit": ["strawberry", "strawberries", "kiwi", "kiwi fruit", "peach", "peaches", "mango", "mangoes", "pineapple"],
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


# Load meals from JSON file
def meal_library():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, "meal_library.json")
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def normalise_list_input(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        parts = [v.strip() for v in value.split(",")]
        return [p for p in parts if p]
    return []


def _coerce_optional_int(value) -> Optional[int]:
    if value is None:
        return None
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        return None
    return parsed if parsed >= 0 else None


def _normalize_string_list(values: List[str]) -> List[str]:
    return [str(v).strip().lower() for v in values if str(v).strip()]


def _meal_tags_lower(meal: Dict[str, object]) -> List[str]:
    return _normalize_string_list(meal.get("tags", []))


def _meal_allergens_lower(meal: Dict[str, object]) -> List[str]:
    return _normalize_string_list(meal.get("allergens", []))


def _meal_categories_lower(meal: Dict[str, object]) -> List[str]:
    return _normalize_string_list(meal.get("food_categories", []))


def _meal_cuisines_lower(meal: Dict[str, object]) -> List[str]:
    raw = []
    if meal.get("cuisine"):
        raw.append(meal.get("cuisine"))
    if meal.get("region"):
        raw.append(meal.get("region"))
    raw.extend(meal.get("tags", []))
    raw.extend(meal.get("food_categories", []))
    return _normalize_string_list(raw)


def _meal_seasons_lower(meal: Dict[str, object]) -> List[str]:
    seasons = _normalize_string_list(meal.get("seasonal_tags", []))
    if not seasons:
        seasons = ["all-season"]
    if "all_season" in seasons and "all-season" not in seasons:
        seasons.append("all-season")
    return seasons


def _meal_contains_allergen(meal: Dict[str, object], allergy: str) -> bool:
    tags = set(_meal_tags_lower(meal))
    allergens = set(_meal_allergens_lower(meal))
    mapped_tags = set(ALLERGY_MAP.get(allergy, []))
    return bool(allergy in allergens or mapped_tags.intersection(tags) or mapped_tags.intersection(allergens))


# Filter by allergies
def filter_allergy(meals, allergies):
    result = []
    allergies_lowercase = _normalize_string_list(allergies)

    for meal in meals:
        has_allergy = any(_meal_contains_allergen(meal, allergy) for allergy in allergies_lowercase)
        if not has_allergy:
            result.append(meal)
    return result


# Filter by health condition
def filter_condition(meals, conditions):
    result = []
    conditions_lowercase = _normalize_string_list(conditions)

    for meal in meals:
        bad = False
        meal_tags = set(_meal_tags_lower(meal))

        for condition in conditions_lowercase:
            bad_tags = CONDITION_MAP.get(condition, [])
            if any(tag in meal_tags for tag in bad_tags):
                bad = True
                break

            sodium = meal.get("sodium_mg", 0) or 0
            if condition in {"hypertension", "high_blood_pressure"} and sodium > 800:
                bad = True
                break

        if not bad:
            result.append(meal)

    return result


# Filter by texture requirement
def filter_texture(meals, text):
    text = (text or "normal").lower()

    if text != "soft":
        return meals

    return [meal for meal in meals if "soft_food" in _meal_tags_lower(meal)]


def filter_budget(meals, budget):
    budget = str(budget or "medium").lower()

    if budget == "low":
        preferred_orders = [["cost_low"], ["cost_low", "cost_medium"], ["cost_low", "cost_medium", "cost_high"]]
    elif budget == "medium":
        preferred_orders = [["cost_medium"], ["cost_medium", "cost_low"], ["cost_medium", "cost_low", "cost_high"]]
    else:
        return meals

    for allowed in preferred_orders:
        filtered = [meal for meal in meals if any(cost_tag in _meal_tags_lower(meal) for cost_tag in allowed)]
        if filtered:
            return filtered

    return meals


def filter_cuisine(meals: List[Dict[str, object]], preferred_cuisines: List[str]) -> List[Dict[str, object]]:
    cuisines = _normalize_string_list(preferred_cuisines)
    if not cuisines:
        return meals

    filtered = [meal for meal in meals if any(c in _meal_cuisines_lower(meal) for c in cuisines)]
    return filtered or meals


def filter_season(meals: List[Dict[str, object]], preferred_seasons: List[str]) -> List[Dict[str, object]]:
    seasons = _normalize_string_list(preferred_seasons)
    if not seasons:
        return meals

    filtered = [
        meal
        for meal in meals
        if "all-season" in _meal_seasons_lower(meal)
        or "all_season" in _meal_seasons_lower(meal)
        or any(s in _meal_seasons_lower(meal) for s in seasons)
    ]
    return filtered or meals


def filter_time(
    meals: List[Dict[str, object]],
    *,
    max_prep_time_minutes: Optional[int],
    max_total_time_minutes: Optional[int],
) -> List[Dict[str, object]]:
    if max_prep_time_minutes is None and max_total_time_minutes is None:
        return meals

    def _ok(meal: Dict[str, object]) -> bool:
        prep = int(meal.get("prep_time_minutes", 9999) or 9999)
        total = int(meal.get("total_time_minutes", prep + int(meal.get("cook_time_minutes", 0) or 0)) or 9999)
        if max_prep_time_minutes is not None and prep > max_prep_time_minutes:
            return False
        if max_total_time_minutes is not None and total > max_total_time_minutes:
            return False
        return True

    filtered = [meal for meal in meals if _ok(meal)]
    return filtered or meals


def _condition_boost_score(meal: Dict[str, object], conditions_lower: List[str]) -> float:
    meal_tags = set(_meal_tags_lower(meal))
    score = 0.0
    for condition in conditions_lower:
        preferred_tags = CONDITION_PREFERENCE_MAP.get(condition, [])
        score += sum(8.0 for tag in preferred_tags if tag in meal_tags)

    sodium = float(meal.get("sodium_mg", 0) or 0)
    if any(c in {"hypertension", "high_blood_pressure"} for c in conditions_lower) and sodium > 500:
        score -= min(20.0, (sodium - 500) / 40.0)

    return score


def _meal_calorie_score(meal: Dict[str, object], target_calories: float) -> float:
    calories = float(meal.get("calories", 0) or 0)
    distance = abs(calories - target_calories)
    return max(0.0, 50.0 - (distance * 0.25))


def _variety_bonus(meal: Dict[str, object], used_categories: set) -> float:
    categories = set(_meal_categories_lower(meal))
    if not categories:
        return 0.0
    if categories.isdisjoint(used_categories):
        return 8.0
    overlap = len(categories.intersection(used_categories))
    return max(0.0, 5.0 - (overlap * 2.0))


def _culture_season_bonus(
    meal: Dict[str, object],
    preferred_cuisines: List[str],
    preferred_seasons: List[str],
) -> float:
    score = 0.0
    cuisines = set(_meal_cuisines_lower(meal))
    seasons = set(_meal_seasons_lower(meal))

    for cuisine in preferred_cuisines:
        if cuisine in cuisines:
            score += 4.0
    for season in preferred_seasons:
        if season in seasons or "all-season" in seasons:
            score += 2.5

    return score


def _sort_preference_bonus(meal: Dict[str, object], sort_by: str) -> float:
    if sort_by == "prep_time":
        return max(0.0, 12.0 - (int(meal.get("prep_time_minutes", 60) or 60) * 0.35))
    if sort_by == "cook_time":
        return max(0.0, 10.0 - (int(meal.get("cook_time_minutes", 60) or 60) * 0.25))
    if sort_by == "total_time":
        return max(0.0, 14.0 - (int(meal.get("total_time_minutes", 90) or 90) * 0.22))
    if sort_by == "high_protein":
        return float(meal.get("protein_g", 0) or 0) * 0.35
    if sort_by == "high_fibre":
        return float(meal.get("fibre_g", 0) or 0) * 0.6
    if sort_by == "low_calories":
        return max(0.0, 20.0 - (float(meal.get("calories", 0) or 0) * 0.03))
    return 0.0


def _score_meal(
    meal: Dict[str, object],
    target_calories: float,
    remaining_calories: int,
    conditions_lower: List[str],
    used_categories: set,
    preferred_cuisines: List[str],
    preferred_seasons: List[str],
    sort_by: str,
) -> float:
    calories = int(meal.get("calories", 0) or 0)
    if calories > remaining_calories:
        return -1.0

    score = _meal_calorie_score(meal, target_calories)
    score += _condition_boost_score(meal, conditions_lower)
    score += _variety_bonus(meal, used_categories)
    score += _culture_season_bonus(meal, preferred_cuisines, preferred_seasons)
    score += _sort_preference_bonus(meal, sort_by)

    if "processed_food" in _meal_tags_lower(meal) or "fast_food" in _meal_categories_lower(meal):
        score -= 6.0

    return score


def _pick_best_meal(
    meals: List[Dict[str, object]],
    *,
    target_calories: float,
    remaining_calories: int,
    conditions_lower: List[str],
    used_categories: set,
    excluded_ids: set,
    preferred_cuisines: List[str],
    preferred_seasons: List[str],
    sort_by: str,
) -> Optional[Dict[str, object]]:
    candidates = [m for m in meals if m.get("id") not in excluded_ids]
    scored: List[Tuple[float, Dict[str, object]]] = []

    for meal in candidates:
        score = _score_meal(
            meal,
            target_calories=target_calories,
            remaining_calories=remaining_calories,
            conditions_lower=conditions_lower,
            used_categories=used_categories,
            preferred_cuisines=preferred_cuisines,
            preferred_seasons=preferred_seasons,
            sort_by=sort_by,
        )
        if score >= 0:
            scored.append((score, meal))

    if not scored:
        return None

    scored.sort(
        key=lambda x: (
            x[0],
            -int(x[1].get("total_time_minutes", 0) or 0) if sort_by == "total_time" else x[1].get("protein_g", 0),
            -int(x[1].get("prep_time_minutes", 0) or 0) if sort_by == "prep_time" else x[1].get("fibre_g", 0),
        ),
        reverse=True,
    )
    return scored[0][1]


def _apply_selection(plan_obj: Dict[str, object], slot: str, meal: Optional[Dict[str, object]], remaining_calories: int, used_ids: set, used_categories: set) -> int:
    plan_obj[slot] = meal
    if meal:
        remaining_calories -= int(meal.get("calories", 0) or 0)
        used_ids.add(meal.get("id"))
        used_categories.update(_meal_categories_lower(meal))
    return remaining_calories


def _build_nutrition_summary(plan_obj: Dict[str, object]) -> Dict[str, float]:
    meals = [plan_obj.get("breakfast"), plan_obj.get("lunch"), plan_obj.get("dinner")] + list(plan_obj.get("snacks", []))
    summary = {
        "protein_g": 0.0,
        "carbs_g": 0.0,
        "fat_g": 0.0,
        "fibre_g": 0.0,
        "sodium_mg": 0.0,
    }

    for meal in meals:
        if not meal:
            continue
        summary["protein_g"] += float(meal.get("protein_g", 0) or 0)
        summary["carbs_g"] += float(meal.get("carbs_g", 0) or 0)
        summary["fat_g"] += float(meal.get("fat_g", 0) or 0)
        summary["fibre_g"] += float(meal.get("fibre_g", 0) or 0)
        summary["sodium_mg"] += float(meal.get("sodium_mg", 0) or 0)

    return {k: round(v, 1) for k, v in summary.items()}


def _build_rationale(meal: Optional[Dict[str, object]], conditions_lower: List[str]) -> str:
    if not meal:
        return "No meal matched the current constraints for this slot."

    tags = set(_meal_tags_lower(meal))
    reasons = []
    if "high_protein" in tags:
        reasons.append("supports protein needs")
    if "high_fibre" in tags:
        reasons.append("adds fibre for satiety")
    if "low_salt" in tags:
        reasons.append("keeps sodium controlled")
    if "low_sugar" in tags or "low_gi" in tags:
        reasons.append("helps with glucose-friendly choices")
    if "heart_healthy" in tags or "omega3_rich" in tags:
        reasons.append("supports heart health")

    for condition in conditions_lower:
        preferred = CONDITION_PREFERENCE_MAP.get(condition, [])
        if any(p in tags for p in preferred):
            reasons.append(f"aligned with {condition.replace('_', ' ')} preferences")
            break

    if not reasons:
        reasons.append("fits current calorie and filtering constraints")

    return "; ".join(dict.fromkeys(reasons)) + "."


# Build the plan
def plan(user, all_meals):
    if user is None:
        user = {}

    raw_allergies = user.get("allergies", [])
    raw_conditions = user.get("conditions", [])

    allergies = normalise_list_input(raw_allergies)
    conditions = normalise_list_input(raw_conditions)

    label_text = user.get("label_text", "")
    detected_allergies = detect_allergens(label_text)

    allergies = list(set(_normalize_string_list(allergies + detected_allergies)))
    conditions_lower = _normalize_string_list(conditions)

    texture = user.get("texture") or "normal"
    budget = user.get("budget") or "medium"
    calories = user.get("calories_target") or 2000

    preferred_cuisines = _normalize_string_list(
        normalise_list_input(user.get("preferred_cuisines") or user.get("cuisines") or [])
    )
    preferred_seasons = _normalize_string_list(
        normalise_list_input(user.get("preferred_seasons") or user.get("season") or [])
    )

    max_prep_time_minutes = _coerce_optional_int(user.get("max_prep_time_minutes"))
    max_total_time_minutes = _coerce_optional_int(user.get("max_total_time_minutes"))
    sort_by = str(user.get("sort_by") or "balanced").strip().lower()
    if sort_by not in SORT_KEYS:
        sort_by = "balanced"

    filtered = filter_allergy(all_meals, allergies)
    filtered = filter_condition(filtered, conditions_lower)
    filtered = filter_texture(filtered, texture)

    if "elderly" in conditions_lower:
        soft_meals = [meal for meal in filtered if "soft_food" in _meal_tags_lower(meal)]
        if soft_meals:
            filtered = soft_meals

    filtered = filter_budget(filtered, budget)
    filtered = filter_cuisine(filtered, preferred_cuisines)
    filtered = filter_season(filtered, preferred_seasons)
    filtered = filter_time(
        filtered,
        max_prep_time_minutes=max_prep_time_minutes,
        max_total_time_minutes=max_total_time_minutes,
    )

    breakfasts = [m for m in filtered if m.get("meal_type") == "breakfast"]
    lunches = [m for m in filtered if m.get("meal_type") == "lunch"]
    dinners = [m for m in filtered if m.get("meal_type") == "dinner"]
    snacks = [m for m in filtered if m.get("meal_type") == "snack"]

    remaining_calories = int(calories)
    used_ids = set()
    used_categories = set()

    plan_obj: Dict[str, object] = {
        "breakfast": None,
        "lunch": None,
        "dinner": None,
        "snacks": [],
    }

    breakfast_target = calories * MEAL_TYPE_CALORIE_DISTRIBUTION["breakfast"]
    lunch_target = calories * MEAL_TYPE_CALORIE_DISTRIBUTION["lunch"]
    dinner_target = calories * MEAL_TYPE_CALORIE_DISTRIBUTION["dinner"]
    snack_target = calories * MEAL_TYPE_CALORIE_DISTRIBUTION["snack"]

    breakfast = _pick_best_meal(
        breakfasts,
        target_calories=breakfast_target,
        remaining_calories=remaining_calories,
        conditions_lower=conditions_lower,
        used_categories=used_categories,
        excluded_ids=used_ids,
        preferred_cuisines=preferred_cuisines,
        preferred_seasons=preferred_seasons,
        sort_by=sort_by,
    )
    remaining_calories = _apply_selection(plan_obj, "breakfast", breakfast, remaining_calories, used_ids, used_categories)

    lunch = _pick_best_meal(
        lunches,
        target_calories=lunch_target,
        remaining_calories=remaining_calories,
        conditions_lower=conditions_lower,
        used_categories=used_categories,
        excluded_ids=used_ids,
        preferred_cuisines=preferred_cuisines,
        preferred_seasons=preferred_seasons,
        sort_by=sort_by,
    )
    remaining_calories = _apply_selection(plan_obj, "lunch", lunch, remaining_calories, used_ids, used_categories)

    dinner = _pick_best_meal(
        dinners,
        target_calories=dinner_target,
        remaining_calories=remaining_calories,
        conditions_lower=conditions_lower,
        used_categories=used_categories,
        excluded_ids=used_ids,
        preferred_cuisines=preferred_cuisines,
        preferred_seasons=preferred_seasons,
        sort_by=sort_by,
    )

    if dinner is None:
        soft_dinners = [m for m in dinners if "soft_food" in _meal_tags_lower(m)]
        dinner = _pick_best_meal(
            soft_dinners,
            target_calories=dinner_target,
            remaining_calories=remaining_calories,
            conditions_lower=conditions_lower,
            used_categories=used_categories,
            excluded_ids=used_ids,
            preferred_cuisines=preferred_cuisines,
            preferred_seasons=preferred_seasons,
            sort_by=sort_by,
        )

        if dinner is None and plan_obj["lunch"] is not None:
            lunch_item = plan_obj["lunch"]
            lunch_calories = int(lunch_item.get("calories", 0) or 0)
            if lunch_calories <= remaining_calories:
                dinner = lunch_item

    remaining_calories = _apply_selection(plan_obj, "dinner", dinner, remaining_calories, used_ids, used_categories)

    snack_candidates = sorted(
        snacks,
        key=lambda m: (
            _score_meal(
                m,
                target_calories=max(snack_target / 2, 80),
                remaining_calories=remaining_calories,
                conditions_lower=conditions_lower,
                used_categories=used_categories,
                preferred_cuisines=preferred_cuisines,
                preferred_seasons=preferred_seasons,
                sort_by=sort_by,
            ),
            m.get("protein_g", 0),
            m.get("fibre_g", 0),
        ),
        reverse=True,
    )

    def _add_snack_candidate(snack: Dict[str, object], require_new_category: bool) -> bool:
        nonlocal remaining_calories

        if len(plan_obj["snacks"]) >= 2:
            return False
        if snack.get("id") in used_ids:
            return False

        snack_calories = int(snack.get("calories", 0) or 0)
        if snack_calories > remaining_calories:
            return False

        snack_categories = set(_meal_categories_lower(snack))
        if require_new_category and snack_categories and not snack_categories.isdisjoint(used_categories):
            return False

        plan_obj["snacks"].append(snack)
        remaining_calories -= snack_calories
        used_ids.add(snack.get("id"))
        used_categories.update(snack_categories)
        return True

    for snack in snack_candidates:
        if len(plan_obj["snacks"]) >= 2:
            break
        _add_snack_candidate(snack, require_new_category=True)

    if len(plan_obj["snacks"]) == 0:
        for snack in snack_candidates:
            if len(plan_obj["snacks"]) >= 2:
                break
            _add_snack_candidate(snack, require_new_category=False)

    total_calories = 0
    if plan_obj["breakfast"] is not None:
        total_calories += int(plan_obj["breakfast"].get("calories", 0) or 0)
    if plan_obj["lunch"] is not None:
        total_calories += int(plan_obj["lunch"].get("calories", 0) or 0)
    if plan_obj["dinner"] is not None:
        total_calories += int(plan_obj["dinner"].get("calories", 0) or 0)
    for snack in plan_obj["snacks"]:
        total_calories += int(snack.get("calories", 0) or 0)

    nutrition_summary = _build_nutrition_summary(plan_obj)

    plan_obj["total_calories"] = total_calories
    plan_obj["target_calories"] = calories
    plan_obj["allergies_used"] = allergies
    plan_obj["detected_allergies_from_label"] = detected_allergies
    plan_obj["budget_used"] = budget
    plan_obj["conditions_used"] = conditions_lower
    plan_obj["remaining_calories"] = remaining_calories
    plan_obj["daily_nutrition_summary"] = nutrition_summary
    plan_obj["variety_score"] = len(used_categories)
    plan_obj["sorting_used"] = sort_by
    plan_obj["cuisine_filter_used"] = preferred_cuisines
    plan_obj["season_filter_used"] = preferred_seasons
    plan_obj["max_prep_time_minutes_used"] = max_prep_time_minutes
    plan_obj["max_total_time_minutes_used"] = max_total_time_minutes
    plan_obj["meal_rationales"] = {
        "breakfast": _build_rationale(plan_obj.get("breakfast"), conditions_lower),
        "lunch": _build_rationale(plan_obj.get("lunch"), conditions_lower),
        "dinner": _build_rationale(plan_obj.get("dinner"), conditions_lower),
        "snacks": [_build_rationale(snack, conditions_lower) for snack in plan_obj.get("snacks", [])],
    }

    return plan_obj


if __name__ == "__main__":
    meals = meal_library()
    user_profile = {
        "name": "Week 9 quick Asian",
        "label_text": "",
        "allergies": [],
        "conditions": [],
        "budget": "medium",
        "texture": "normal",
        "calories_target": 1800,
        "preferred_cuisines": ["asian"],
        "preferred_seasons": ["winter"],
        "max_prep_time_minutes": 20,
        "max_total_time_minutes": 45,
        "sort_by": "prep_time",
    }

    print("\n=== TEST: Week 9 filtering/sorting ===")
    result = plan(user_profile, meals)
    print(json.dumps(result, indent=2, ensure_ascii=False))
