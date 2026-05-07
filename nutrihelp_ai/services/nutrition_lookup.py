import re
from typing import Dict, List, Optional


EXACT_LOOKUP: Dict[str, Dict[str, object]] = {
    "apple_pie": {"estimated_calories": 320, "serving_description": "1 slice"},
    "bibimbap": {"estimated_calories": 560, "serving_description": "1 bowl"},
    "caesar_salad": {"estimated_calories": 280, "serving_description": "1 bowl"},
    "cheesecake": {"estimated_calories": 430, "serving_description": "1 slice"},
    "chicken_curry": {"estimated_calories": 420, "serving_description": "1 bowl"},
    "chicken_wings": {"estimated_calories": 430, "serving_description": "6 wings"},
    "chocolate_cake": {"estimated_calories": 410, "serving_description": "1 slice"},
    "club_sandwich": {"estimated_calories": 520, "serving_description": "1 sandwich"},
    "donuts": {"estimated_calories": 260, "serving_description": "1 donut"},
    "falafel": {"estimated_calories": 330, "serving_description": "1 serving"},
    "fish_and_chips": {"estimated_calories": 680, "serving_description": "1 plate"},
    "french_fries": {"estimated_calories": 365, "serving_description": "1 medium serve"},
    "fried_rice": {"estimated_calories": 450, "serving_description": "1 plate"},
    "grilled_salmon": {"estimated_calories": 360, "serving_description": "1 fillet"},
    "guacamole": {"estimated_calories": 230, "serving_description": "1 small bowl"},
    "hamburger": {"estimated_calories": 520, "serving_description": "1 burger"},
    "hot_dog": {"estimated_calories": 330, "serving_description": "1 hot dog"},
    "hummus": {"estimated_calories": 180, "serving_description": "1 small bowl"},
    "ice_cream": {"estimated_calories": 275, "serving_description": "1 cup"},
    "lasagna": {"estimated_calories": 430, "serving_description": "1 slice"},
    "macaroni_and_cheese": {"estimated_calories": 460, "serving_description": "1 bowl"},
    "nachos": {"estimated_calories": 520, "serving_description": "1 plate"},
    "omelette": {"estimated_calories": 250, "serving_description": "1 omelette"},
    "pad_thai": {"estimated_calories": 540, "serving_description": "1 plate"},
    "pancakes": {"estimated_calories": 350, "serving_description": "3 pancakes"},
    "pho": {"estimated_calories": 380, "serving_description": "1 bowl"},
    "pizza": {"estimated_calories": 285, "serving_description": "1 slice"},
    "ramen": {"estimated_calories": 490, "serving_description": "1 bowl"},
    "risotto": {"estimated_calories": 420, "serving_description": "1 bowl"},
    "sashimi": {"estimated_calories": 220, "serving_description": "1 serving"},
    "spaghetti_bolognese": {"estimated_calories": 520, "serving_description": "1 plate"},
    "spaghetti_carbonara": {"estimated_calories": 610, "serving_description": "1 plate"},
    "steak": {"estimated_calories": 620, "serving_description": "1 steak"},
    "sushi": {"estimated_calories": 320, "serving_description": "1 roll set"},
    "tacos": {"estimated_calories": 300, "serving_description": "2 tacos"},
    "tiramisu": {"estimated_calories": 390, "serving_description": "1 slice"},
    "waffles": {"estimated_calories": 370, "serving_description": "2 waffles"},
    "avocado_toast": {"estimated_calories": 310, "serving_description": "1 slice"},
    "greek_salad": {"estimated_calories": 240, "serving_description": "1 bowl"},
    "quinoa_salad": {"estimated_calories": 320, "serving_description": "1 bowl"},
    "chickpea_salad": {"estimated_calories": 340, "serving_description": "1 bowl"},
    "tofu_stir_fry": {"estimated_calories": 410, "serving_description": "1 bowl"},
    "burrito_bowl": {"estimated_calories": 540, "serving_description": "1 bowl"},
    "overnight_oats": {"estimated_calories": 300, "serving_description": "1 jar"},
    "protein_smoothie": {"estimated_calories": 260, "serving_description": "1 glass"},
    "grilled_chicken_bowl": {"estimated_calories": 460, "serving_description": "1 bowl"},
    "lentil_soup": {"estimated_calories": 280, "serving_description": "1 bowl"},
    "salmon_bowl": {"estimated_calories": 520, "serving_description": "1 bowl"},
    "veggie_wrap": {"estimated_calories": 360, "serving_description": "1 wrap"},
    "bean_chili": {"estimated_calories": 390, "serving_description": "1 bowl"},
    "cottage_cheese_bowl": {"estimated_calories": 220, "serving_description": "1 bowl"},
    "chana_masala": {"estimated_calories": 430, "serving_description": "1 bowl"},
    "kimchi_bibimbap": {"estimated_calories": 570, "serving_description": "1 bowl"},
    "thai_basil_chicken": {"estimated_calories": 520, "serving_description": "1 plate"},
    "turkish_lentil_soup": {"estimated_calories": 290, "serving_description": "1 bowl"},
    "falafel_wrap": {"estimated_calories": 480, "serving_description": "1 wrap"},
    "shakshuka": {"estimated_calories": 360, "serving_description": "1 skillet serve"},
    "mojo_fish": {"estimated_calories": 510, "serving_description": "1 plate"},
    "black_bean_rice": {"estimated_calories": 520, "serving_description": "1 bowl"},
    "onigiri": {"estimated_calories": 190, "serving_description": "2 pieces"},
    "dal_khichdi": {"estimated_calories": 500, "serving_description": "1 bowl"},
}

MEAL_METADATA: Dict[str, Dict[str, Optional[str]]] = {
    "apple_pie": {"display_name": "Apple Pie", "cuisine": "Western", "about": "A baked dessert made with sweet apple filling inside a pastry crust."},
    "bibimbap": {"display_name": "Bibimbap", "cuisine": "Korean", "about": "A Korean rice bowl with vegetables, protein, and chili paste."},
    "caesar_salad": {"display_name": "Caesar Salad", "cuisine": "Western", "about": "A lettuce-based salad with croutons and creamy dressing."},
    "cheesecake": {"display_name": "Cheesecake", "cuisine": "Dessert", "about": "A rich dessert with a cream cheese filling and crust."},
    "chicken_curry": {"display_name": "Chicken Curry", "cuisine": "South Asian", "about": "Chicken simmered in a seasoned spiced sauce."},
    "grilled_salmon": {"display_name": "Grilled Salmon", "cuisine": "Seafood", "about": "A salmon fillet grilled and served as a protein-rich main."},
    "hummus": {"display_name": "Hummus", "cuisine": "Middle Eastern", "about": "A chickpea and tahini dip with garlic and lemon."},
    "omelette": {"display_name": "Omelette", "cuisine": "Breakfast", "about": "A folded egg dish often served with vegetables or cheese."},
    "pho": {"display_name": "Pho", "cuisine": "Vietnamese", "about": "A Vietnamese noodle soup with aromatic broth and herbs."},
    "sushi": {"display_name": "Sushi", "cuisine": "Japanese", "about": "Rice-based Japanese bites with seafood or vegetables."},
    "avocado_toast": {"display_name": "Avocado Toast", "cuisine": "Breakfast", "about": "Wholegrain toast topped with smashed avocado and seasoning."},
    "greek_salad": {"display_name": "Greek Salad", "cuisine": "Mediterranean", "about": "A fresh salad of cucumber, tomato, olives, and feta."},
    "quinoa_salad": {"display_name": "Quinoa Salad", "cuisine": "Healthy Fusion", "about": "A whole-grain bowl with vegetables and herbs."},
    "tofu_stir_fry": {"display_name": "Tofu Stir Fry", "cuisine": "Asian", "about": "Tofu and vegetables quickly cooked in a wok-style sauce."},
    "burrito_bowl": {"display_name": "Burrito Bowl", "cuisine": "Mexican-inspired", "about": "A layered rice bowl with beans, vegetables, and protein."},
    "overnight_oats": {"display_name": "Overnight Oats", "cuisine": "Breakfast", "about": "Cold soaked oats with milk or yoghurt, fruit, and seeds."},
    "protein_smoothie": {"display_name": "Protein Smoothie", "cuisine": "Beverage", "about": "A blended drink with fruit, milk, and protein-rich ingredients."},
    "lentil_soup": {"display_name": "Lentil Soup", "cuisine": "Comfort Food", "about": "A hearty soup made from lentils and vegetables."},
    "bean_chili": {"display_name": "Bean Chili", "cuisine": "Tex-Mex", "about": "A tomato-based bean stew with spices."},
    "chana_masala": {"display_name": "Chana Masala", "cuisine": "Indian", "about": "A tomato-onion chickpea curry seasoned with warming spices."},
    "kimchi_bibimbap": {"display_name": "Kimchi Bibimbap", "cuisine": "Korean", "about": "Rice bowl with kimchi, vegetables, and protein."},
    "thai_basil_chicken": {"display_name": "Thai Basil Chicken", "cuisine": "Thai", "about": "Stir-fried chicken with basil, garlic, and chili."},
    "turkish_lentil_soup": {"display_name": "Turkish Lentil Soup", "cuisine": "Turkish", "about": "A silky red lentil soup with citrus and spices."},
    "falafel_wrap": {"display_name": "Falafel Wrap", "cuisine": "Middle Eastern", "about": "A pita wrap with falafel, herbs, and tahini sauce."},
    "shakshuka": {"display_name": "Shakshuka", "cuisine": "Mediterranean", "about": "Eggs poached in a spiced tomato-pepper sauce."},
    "mojo_fish": {"display_name": "Mojo Fish", "cuisine": "Cuban", "about": "Fish marinated with citrus-garlic mojo and herbs."},
    "black_bean_rice": {"display_name": "Black Bean Rice", "cuisine": "Latin American", "about": "Rice and black beans cooked with aromatic spices."},
    "onigiri": {"display_name": "Onigiri", "cuisine": "Japanese", "about": "Japanese rice balls often wrapped in seaweed."},
    "dal_khichdi": {"display_name": "Dal Khichdi", "cuisine": "Indian", "about": "Comforting rice and lentil one-pot dish."},
}

NUTRITION_DETAILS: Dict[str, Dict[str, object]] = {
    "grilled_salmon": {
        "protein_g": 34.0,
        "carbs_g": 0.0,
        "fat_g": 22.0,
        "fibre_g": 0.0,
        "sugar_g": 0.0,
        "sodium_mg": 90.0,
        "micronutrients": {"omega3_g": 2.3, "selenium_mcg": 36, "potassium_mg": 490},
        "vitamins": ["vitamin_d", "vitamin_b12", "vitamin_b6"],
        "minerals": ["selenium", "phosphorus", "potassium"],
        "allergens": ["fish"],
        "food_categories": ["seafood", "high_protein", "heart_healthy"],
    },
    "hummus": {
        "protein_g": 5.0,
        "carbs_g": 14.0,
        "fat_g": 8.0,
        "fibre_g": 6.0,
        "sugar_g": 0.5,
        "sodium_mg": 170.0,
        "micronutrients": {"iron_mg": 2.2, "folate_mcg": 55, "magnesium_mg": 40},
        "vitamins": ["folate", "vitamin_b6"],
        "minerals": ["iron", "magnesium", "zinc"],
        "allergens": ["sesame"],
        "food_categories": ["dip", "plant_based", "legume"],
    },
    "omelette": {
        "protein_g": 18.0,
        "carbs_g": 2.0,
        "fat_g": 19.0,
        "fibre_g": 0.0,
        "sugar_g": 1.5,
        "sodium_mg": 320.0,
        "micronutrients": {"choline_mg": 290, "selenium_mcg": 24, "vitamin_d_iu": 110},
        "vitamins": ["vitamin_b12", "vitamin_d", "vitamin_a"],
        "minerals": ["selenium", "phosphorus", "iron"],
        "allergens": ["egg"],
        "food_categories": ["breakfast", "high_protein", "egg_based"],
    },
    "sushi": {
        "protein_g": 12.0,
        "carbs_g": 43.0,
        "fat_g": 5.0,
        "fibre_g": 2.0,
        "sugar_g": 5.0,
        "sodium_mg": 410.0,
        "micronutrients": {"iodine_mcg": 45, "selenium_mcg": 20, "omega3_g": 0.6},
        "vitamins": ["vitamin_b12", "folate"],
        "minerals": ["iodine", "selenium", "manganese"],
        "allergens": ["fish", "soy"],
        "food_categories": ["japanese", "rice_based", "seafood"],
    },
    "avocado_toast": {
        "protein_g": 8.0,
        "carbs_g": 31.0,
        "fat_g": 16.0,
        "fibre_g": 8.0,
        "sugar_g": 3.0,
        "sodium_mg": 260.0,
        "micronutrients": {"potassium_mg": 490, "vitamin_e_mg": 2.1, "folate_mcg": 80},
        "vitamins": ["vitamin_e", "folate", "vitamin_k"],
        "minerals": ["potassium", "magnesium"],
        "allergens": ["gluten", "wheat"],
        "food_categories": ["breakfast", "whole_grain", "healthy_fat"],
    },
    "greek_salad": {
        "protein_g": 7.0,
        "carbs_g": 12.0,
        "fat_g": 17.0,
        "fibre_g": 4.0,
        "sugar_g": 6.0,
        "sodium_mg": 430.0,
        "micronutrients": {"vitamin_c_mg": 24, "vitamin_k_mcg": 51, "calcium_mg": 180},
        "vitamins": ["vitamin_c", "vitamin_k", "vitamin_a"],
        "minerals": ["calcium", "potassium"],
        "allergens": ["dairy"],
        "food_categories": ["salad", "mediterranean", "vegetarian"],
    },
    "quinoa_salad": {
        "protein_g": 11.0,
        "carbs_g": 44.0,
        "fat_g": 9.0,
        "fibre_g": 7.0,
        "sugar_g": 4.0,
        "sodium_mg": 210.0,
        "micronutrients": {"iron_mg": 3.4, "magnesium_mg": 118, "potassium_mg": 420},
        "vitamins": ["folate", "vitamin_b6"],
        "minerals": ["iron", "magnesium", "potassium"],
        "allergens": [],
        "food_categories": ["salad", "whole_grain", "plant_based"],
    },
    "tofu_stir_fry": {
        "protein_g": 20.0,
        "carbs_g": 32.0,
        "fat_g": 16.0,
        "fibre_g": 6.0,
        "sugar_g": 6.0,
        "sodium_mg": 520.0,
        "micronutrients": {"calcium_mg": 260, "iron_mg": 3.6, "vitamin_c_mg": 34},
        "vitamins": ["vitamin_c", "vitamin_k", "folate"],
        "minerals": ["calcium", "iron", "magnesium"],
        "allergens": ["soy"],
        "food_categories": ["asian", "plant_protein", "stir_fry"],
    },
    "burrito_bowl": {
        "protein_g": 24.0,
        "carbs_g": 62.0,
        "fat_g": 18.0,
        "fibre_g": 12.0,
        "sugar_g": 6.0,
        "sodium_mg": 690.0,
        "micronutrients": {"iron_mg": 4.8, "potassium_mg": 840, "folate_mcg": 180},
        "vitamins": ["folate", "vitamin_c"],
        "minerals": ["iron", "potassium", "magnesium"],
        "allergens": [],
        "food_categories": ["mexican", "rice_bowl", "high_fibre"],
    },
    "overnight_oats": {
        "protein_g": 10.0,
        "carbs_g": 44.0,
        "fat_g": 9.0,
        "fibre_g": 8.0,
        "sugar_g": 9.0,
        "sodium_mg": 120.0,
        "micronutrients": {"iron_mg": 2.9, "magnesium_mg": 82, "calcium_mg": 200},
        "vitamins": ["vitamin_b1", "vitamin_b6", "vitamin_d"],
        "minerals": ["iron", "magnesium", "calcium"],
        "allergens": ["dairy"],
        "food_categories": ["breakfast", "whole_grain", "high_fibre"],
    },
    "protein_smoothie": {
        "protein_g": 22.0,
        "carbs_g": 22.0,
        "fat_g": 7.0,
        "fibre_g": 4.0,
        "sugar_g": 14.0,
        "sodium_mg": 180.0,
        "micronutrients": {"potassium_mg": 520, "calcium_mg": 260, "vitamin_c_mg": 20},
        "vitamins": ["vitamin_c", "vitamin_b12", "vitamin_d"],
        "minerals": ["potassium", "calcium", "phosphorus"],
        "allergens": ["dairy"],
        "food_categories": ["beverage", "high_protein", "post_workout"],
    },
    "lentil_soup": {
        "protein_g": 14.0,
        "carbs_g": 38.0,
        "fat_g": 6.0,
        "fibre_g": 12.0,
        "sugar_g": 4.0,
        "sodium_mg": 360.0,
        "micronutrients": {"iron_mg": 5.0, "folate_mcg": 160, "potassium_mg": 680},
        "vitamins": ["folate", "vitamin_b1", "vitamin_b6"],
        "minerals": ["iron", "potassium", "magnesium"],
        "allergens": [],
        "food_categories": ["soup", "legume", "high_fibre"],
    },
    "bean_chili": {
        "protein_g": 16.0,
        "carbs_g": 48.0,
        "fat_g": 9.0,
        "fibre_g": 13.0,
        "sugar_g": 8.0,
        "sodium_mg": 430.0,
        "micronutrients": {"iron_mg": 5.3, "potassium_mg": 790, "vitamin_c_mg": 28},
        "vitamins": ["vitamin_c", "folate"],
        "minerals": ["iron", "potassium", "magnesium"],
        "allergens": [],
        "food_categories": ["stew", "legume", "plant_based"],
    },
    "chana_masala": {
        "protein_g": 17.0,
        "carbs_g": 54.0,
        "fat_g": 11.0,
        "fibre_g": 12.0,
        "sugar_g": 7.0,
        "sodium_mg": 390.0,
        "micronutrients": {"iron_mg": 5.7, "folate_mcg": 170, "potassium_mg": 760},
        "vitamins": ["folate", "vitamin_c", "vitamin_b6"],
        "minerals": ["iron", "potassium", "magnesium"],
        "allergens": [],
        "food_categories": ["indian", "curry", "legume"],
    },
    "kimchi_bibimbap": {
        "protein_g": 23.0,
        "carbs_g": 66.0,
        "fat_g": 17.0,
        "fibre_g": 8.0,
        "sugar_g": 8.0,
        "sodium_mg": 680.0,
        "micronutrients": {"iron_mg": 3.9, "calcium_mg": 190, "vitamin_c_mg": 24},
        "vitamins": ["vitamin_c", "vitamin_k", "folate"],
        "minerals": ["iron", "calcium", "potassium"],
        "allergens": ["soy"],
        "food_categories": ["korean", "rice_bowl", "fermented_food"],
    },
    "thai_basil_chicken": {
        "protein_g": 33.0,
        "carbs_g": 42.0,
        "fat_g": 19.0,
        "fibre_g": 4.0,
        "sugar_g": 6.0,
        "sodium_mg": 620.0,
        "micronutrients": {"iron_mg": 2.5, "potassium_mg": 640, "vitamin_b6_mg": 0.7},
        "vitamins": ["vitamin_b6", "niacin"],
        "minerals": ["iron", "potassium", "phosphorus"],
        "allergens": ["soy"],
        "food_categories": ["thai", "stir_fry", "high_protein"],
    },
    "turkish_lentil_soup": {
        "protein_g": 11.0,
        "carbs_g": 36.0,
        "fat_g": 7.0,
        "fibre_g": 10.0,
        "sugar_g": 4.0,
        "sodium_mg": 340.0,
        "micronutrients": {"iron_mg": 4.5, "folate_mcg": 140, "potassium_mg": 620},
        "vitamins": ["folate", "vitamin_b1"],
        "minerals": ["iron", "potassium", "magnesium"],
        "allergens": [],
        "food_categories": ["turkish", "soup", "legume"],
    },
    "falafel_wrap": {
        "protein_g": 16.0,
        "carbs_g": 55.0,
        "fat_g": 17.0,
        "fibre_g": 10.0,
        "sugar_g": 5.0,
        "sodium_mg": 560.0,
        "micronutrients": {"iron_mg": 4.0, "folate_mcg": 130, "magnesium_mg": 80},
        "vitamins": ["folate", "vitamin_b6"],
        "minerals": ["iron", "magnesium", "zinc"],
        "allergens": ["gluten", "wheat", "sesame"],
        "food_categories": ["middle_eastern", "wrap", "plant_based"],
    },
    "shakshuka": {
        "protein_g": 20.0,
        "carbs_g": 18.0,
        "fat_g": 21.0,
        "fibre_g": 5.0,
        "sugar_g": 7.0,
        "sodium_mg": 410.0,
        "micronutrients": {"lycopene_mg": 10, "iron_mg": 2.8, "calcium_mg": 150},
        "vitamins": ["vitamin_a", "vitamin_c", "vitamin_b12"],
        "minerals": ["iron", "calcium", "potassium"],
        "allergens": ["egg"],
        "food_categories": ["mediterranean", "egg_based", "high_protein"],
    },
    "mojo_fish": {
        "protein_g": 32.0,
        "carbs_g": 18.0,
        "fat_g": 16.0,
        "fibre_g": 3.0,
        "sugar_g": 4.0,
        "sodium_mg": 300.0,
        "micronutrients": {"omega3_g": 1.2, "selenium_mcg": 28, "potassium_mg": 610},
        "vitamins": ["vitamin_b12", "vitamin_d", "vitamin_c"],
        "minerals": ["selenium", "potassium", "phosphorus"],
        "allergens": ["fish"],
        "food_categories": ["cuban", "seafood", "heart_healthy"],
    },
    "black_bean_rice": {
        "protein_g": 18.0,
        "carbs_g": 72.0,
        "fat_g": 9.0,
        "fibre_g": 13.0,
        "sugar_g": 4.0,
        "sodium_mg": 390.0,
        "micronutrients": {"iron_mg": 5.4, "potassium_mg": 860, "folate_mcg": 180},
        "vitamins": ["folate", "vitamin_b1"],
        "minerals": ["iron", "potassium", "magnesium"],
        "allergens": [],
        "food_categories": ["latin_american", "rice_bowl", "legume"],
    },
    "onigiri": {
        "protein_g": 5.0,
        "carbs_g": 40.0,
        "fat_g": 2.0,
        "fibre_g": 2.0,
        "sugar_g": 1.0,
        "sodium_mg": 210.0,
        "micronutrients": {"iodine_mcg": 40, "folate_mcg": 18, "potassium_mg": 140},
        "vitamins": ["vitamin_b1"],
        "minerals": ["iodine", "potassium"],
        "allergens": ["soy"],
        "food_categories": ["japanese", "snack", "rice_based"],
    },
    "dal_khichdi": {
        "protein_g": 19.0,
        "carbs_g": 68.0,
        "fat_g": 10.0,
        "fibre_g": 10.0,
        "sugar_g": 3.0,
        "sodium_mg": 320.0,
        "micronutrients": {"iron_mg": 4.7, "magnesium_mg": 108, "potassium_mg": 580},
        "vitamins": ["folate", "vitamin_b1", "vitamin_b6"],
        "minerals": ["iron", "magnesium", "potassium"],
        "allergens": [],
        "food_categories": ["indian", "one_pot", "comfort_food"],
    },
}

KEYWORD_FALLBACKS = (
    (
        "salad",
        {
            "estimated_calories": 220,
            "serving_description": "1 bowl",
            "cuisine": None,
            "about": "A mixed bowl of vegetables and toppings.",
            "protein_g": 8.0,
            "carbs_g": 18.0,
            "fat_g": 10.0,
            "fibre_g": 5.0,
            "sugar_g": 4.0,
            "sodium_mg": 280.0,
            "food_categories": ["salad"],
        },
    ),
    (
        "soup",
        {
            "estimated_calories": 180,
            "serving_description": "1 bowl",
            "cuisine": None,
            "about": "A broth-based or blended dish.",
            "protein_g": 8.0,
            "carbs_g": 20.0,
            "fat_g": 6.0,
            "fibre_g": 3.0,
            "sugar_g": 3.0,
            "sodium_mg": 420.0,
            "food_categories": ["soup"],
        },
    ),
    (
        "cake",
        {
            "estimated_calories": 410,
            "serving_description": "1 slice",
            "cuisine": "Dessert",
            "about": "A baked dessert usually served in slices.",
            "protein_g": 5.0,
            "carbs_g": 55.0,
            "fat_g": 18.0,
            "fibre_g": 1.5,
            "sugar_g": 35.0,
            "sodium_mg": 320.0,
            "food_categories": ["dessert"],
        },
    ),
    (
        "sandwich",
        {
            "estimated_calories": 480,
            "serving_description": "1 sandwich",
            "cuisine": "Western",
            "about": "A handheld meal made with bread and filling.",
            "protein_g": 20.0,
            "carbs_g": 45.0,
            "fat_g": 22.0,
            "fibre_g": 4.0,
            "sugar_g": 6.0,
            "sodium_mg": 700.0,
            "food_categories": ["sandwich"],
        },
    ),
)

LABEL_ALIASES = {
    "apple pie": "apple_pie",
    "caesar salad": "caesar_salad",
    "chicken curry": "chicken_curry",
    "chicken wings": "chicken_wings",
    "chocolate cake": "chocolate_cake",
    "club sandwich": "club_sandwich",
    "fish and chips": "fish_and_chips",
    "french fries": "french_fries",
    "fried rice": "fried_rice",
    "grilled salmon": "grilled_salmon",
    "hot dog": "hot_dog",
    "ice cream": "ice_cream",
    "macaroni and cheese": "macaroni_and_cheese",
    "pad thai": "pad_thai",
    "spaghetti bolognese": "spaghetti_bolognese",
    "spaghetti carbonara": "spaghetti_carbonara",
    "avocado toast": "avocado_toast",
    "greek salad": "greek_salad",
    "quinoa salad": "quinoa_salad",
    "tofu stir fry": "tofu_stir_fry",
    "overnight oats": "overnight_oats",
    "protein smoothie": "protein_smoothie",
    "burrito bowl": "burrito_bowl",
    "bean chili": "bean_chili",
    "chana masala": "chana_masala",
    "kimchi bibimbap": "kimchi_bibimbap",
    "thai basil chicken": "thai_basil_chicken",
    "turkish lentil soup": "turkish_lentil_soup",
    "falafel wrap": "falafel_wrap",
    "black bean rice": "black_bean_rice",
    "mojo fish": "mojo_fish",
    "dal khichdi": "dal_khichdi",
}


class NutritionLookupService:
    def unavailable(self, label: Optional[str] = None, *, source: str = "unavailable") -> Dict[str, object]:
        nutrition = self._unavailable(label=label)
        nutrition["source"] = source
        return nutrition

    def lookup(self, label: Optional[str]) -> Dict[str, object]:
        if not label:
            return self._unavailable()

        normalized = self._normalize_label(label)
        display_name = self._display_name(label, normalized)

        if normalized in EXACT_LOOKUP:
            return self._build_available(
                normalized,
                EXACT_LOOKUP[normalized],
                source="curated_lookup",
                display_name=display_name,
            )

        for keyword, data in KEYWORD_FALLBACKS:
            if keyword in normalized:
                return self._build_available(
                    normalized,
                    data,
                    source="category_heuristic",
                    display_name=display_name,
                )

        return self._unavailable(label=label, normalized=normalized)

    def build_recommendation(self, nutrition: Dict[str, object], *, is_unclear: bool = False) -> str:
        if is_unclear:
            return "Try uploading a clearer, closer image for a more reliable result."

        if not nutrition.get("available"):
            return "Nutrition data is not available for this class yet. Treat the result as a guide only."

        calories = int(nutrition.get("estimated_calories") or 0)
        protein = float(nutrition.get("protein_g") or 0)
        fibre = float(nutrition.get("fibre_g") or 0)
        sodium = float(nutrition.get("sodium_mg") or 0)
        sugar = float(nutrition.get("sugar_g") or 0)
        categories = [str(c).lower() for c in nutrition.get("food_categories", [])]

        tips: List[str] = []
        if calories >= 600:
            tips.append("This is a calorie-dense serving, so consider a smaller portion or lighter sides")
        elif calories <= 250:
            tips.append("This is a lighter serving and can be paired with protein or fibre-rich sides")

        if protein >= 20:
            tips.append("good protein contribution")
        if fibre >= 6:
            tips.append("strong fibre content for satiety")
        if sodium >= 600:
            tips.append("sodium appears high, so balance with lower-salt meals across the day")
        if sugar >= 20:
            tips.append("added sweetness may be high, especially for glucose management")

        if "dessert" in categories:
            tips.append("best treated as an occasional meal or shared portion")
        if "heart_healthy" in categories or "seafood" in categories:
            tips.append("can fit heart-friendly patterns depending on preparation")

        if not tips:
            tips.append("Use this estimate as a guide since recipe and portion sizes vary")

        return "; ".join(tips) + "."

    def _build_available(
        self,
        normalized: str,
        data: Dict[str, object],
        *,
        source: str,
        display_name: Optional[str] = None,
    ) -> Dict[str, object]:
        metadata = MEAL_METADATA.get(normalized, {})
        details = NUTRITION_DETAILS.get(normalized, {})

        return {
            "display_name": metadata.get("display_name") or display_name or self._humanize_label(normalized),
            "about": metadata.get("about") or data.get("about"),
            "cuisine": metadata.get("cuisine") or data.get("cuisine"),
            "estimated_calories": int(data["estimated_calories"]),
            "serving_description": data.get("serving_description"),
            "protein_g": float(details.get("protein_g", data.get("protein_g", 0)) or 0),
            "carbs_g": float(details.get("carbs_g", data.get("carbs_g", 0)) or 0),
            "fat_g": float(details.get("fat_g", data.get("fat_g", 0)) or 0),
            "fibre_g": float(details.get("fibre_g", data.get("fibre_g", 0)) or 0),
            "sugar_g": float(details.get("sugar_g", data.get("sugar_g", 0)) or 0),
            "sodium_mg": float(details.get("sodium_mg", data.get("sodium_mg", 0)) or 0),
            "micronutrients": details.get("micronutrients", data.get("micronutrients", {})),
            "vitamins": details.get("vitamins", data.get("vitamins", [])),
            "minerals": details.get("minerals", data.get("minerals", [])),
            "allergens": details.get("allergens", data.get("allergens", [])),
            "food_categories": details.get("food_categories", data.get("food_categories", [])),
            "source": source,
            "available": True,
        }

    def _unavailable(self, *, label: Optional[str] = None, normalized: Optional[str] = None) -> Dict[str, object]:
        base_label = normalized or self._normalize_label(label)
        return {
            "display_name": self._display_name(label, base_label),
            "about": None,
            "cuisine": None,
            "estimated_calories": None,
            "serving_description": None,
            "protein_g": None,
            "carbs_g": None,
            "fat_g": None,
            "fibre_g": None,
            "sugar_g": None,
            "sodium_mg": None,
            "micronutrients": {},
            "vitamins": [],
            "minerals": [],
            "allergens": [],
            "food_categories": [],
            "source": "unavailable",
            "available": False,
        }

    def _normalize_label(self, label: Optional[str]) -> str:
        text = str(label or "").strip().lower()
        if not text:
            return ""

        text = LABEL_ALIASES.get(text, text)
        text = re.sub(r"[^a-z0-9\s_-]+", "", text)
        text = re.sub(r"[\s-]+", "_", text)
        return LABEL_ALIASES.get(text, text)

    def _display_name(self, raw_label: Optional[str], normalized: str) -> str:
        metadata = MEAL_METADATA.get(normalized, {})
        if metadata.get("display_name"):
            return str(metadata["display_name"])

        if raw_label and str(raw_label).strip():
            return self._humanize_label(str(raw_label).strip())

        return self._humanize_label(normalized)

    def _humanize_label(self, label: str) -> str:
        if not label:
            return "Unknown Dish"
        return label.replace("_", " ").strip().title()
