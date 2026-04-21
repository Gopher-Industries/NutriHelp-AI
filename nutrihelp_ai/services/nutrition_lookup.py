import re
from typing import Dict, Optional


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
}

MEAL_METADATA: Dict[str, Dict[str, Optional[str]]] = {
    "apple_pie": {
        "display_name": "Apple Pie",
        "cuisine": "Western",
        "about": "A baked dessert made with sweet apple filling inside a pastry crust.",
    },
    "bibimbap": {
        "display_name": "Bibimbap",
        "cuisine": "Korean",
        "about": "A Korean rice bowl usually served with vegetables, protein, chili paste, and often a fried egg.",
    },
    "caesar_salad": {
        "display_name": "Caesar Salad",
        "cuisine": "Western",
        "about": "A salad built around lettuce, croutons, parmesan, and a creamy Caesar-style dressing.",
    },
    "cheesecake": {
        "display_name": "Cheesecake",
        "cuisine": "Dessert",
        "about": "A rich dessert with a soft cheese filling over a biscuit or pastry base.",
    },
    "chicken_curry": {
        "display_name": "Chicken Curry",
        "cuisine": "South Asian",
        "about": "A chicken dish simmered in a seasoned sauce or gravy with spices and aromatics.",
    },
    "chicken_wings": {
        "display_name": "Chicken Wings",
        "cuisine": "Western",
        "about": "Small chicken wing pieces, usually fried or baked and coated with sauce or seasoning.",
    },
    "chocolate_cake": {
        "display_name": "Chocolate Cake",
        "cuisine": "Dessert",
        "about": "A sweet baked cake flavored with chocolate or cocoa.",
    },
    "club_sandwich": {
        "display_name": "Club Sandwich",
        "cuisine": "Western",
        "about": "A layered sandwich commonly filled with bread, meat, salad, and sauce.",
    },
    "donuts": {
        "display_name": "Donuts",
        "cuisine": "Dessert",
        "about": "Sweet fried dough pastries that may be glazed, sugared, or filled.",
    },
    "falafel": {
        "display_name": "Falafel",
        "cuisine": "Middle Eastern",
        "about": "Fried balls or patties made from seasoned chickpeas or fava beans.",
    },
    "fish_and_chips": {
        "display_name": "Fish and Chips",
        "cuisine": "British",
        "about": "A fried fish fillet served with hot chips, often with tartar sauce or lemon.",
    },
    "french_fries": {
        "display_name": "French Fries",
        "cuisine": "Western",
        "about": "Deep-fried potato strips usually served as a side or snack.",
    },
    "fried_rice": {
        "display_name": "Fried Rice",
        "cuisine": "Asian",
        "about": "Cooked rice stir-fried with oil, seasoning, vegetables, and sometimes egg or meat.",
    },
    "grilled_salmon": {
        "display_name": "Grilled Salmon",
        "cuisine": "Seafood",
        "about": "A salmon fillet cooked on a grill or pan, often served with light seasoning.",
    },
    "guacamole": {
        "display_name": "Guacamole",
        "cuisine": "Mexican",
        "about": "A mashed avocado dip often mixed with lime, onion, tomato, and herbs.",
    },
    "hamburger": {
        "display_name": "Hamburger",
        "cuisine": "Western",
        "about": "A sandwich built around a cooked meat patty inside a bun with toppings.",
    },
    "hot_dog": {
        "display_name": "Hot Dog",
        "cuisine": "Western",
        "about": "A sausage served in a split bun, usually with condiments.",
    },
    "hummus": {
        "display_name": "Hummus",
        "cuisine": "Middle Eastern",
        "about": "A smooth chickpea dip blended with tahini, lemon, and garlic.",
    },
    "ice_cream": {
        "display_name": "Ice Cream",
        "cuisine": "Dessert",
        "about": "A frozen dairy dessert that may be served in scoops, cups, or cones.",
    },
    "lasagna": {
        "display_name": "Lasagna",
        "cuisine": "Italian",
        "about": "A layered pasta bake with sauce, cheese, and meat or vegetables.",
    },
    "macaroni_and_cheese": {
        "display_name": "Macaroni and Cheese",
        "cuisine": "Western",
        "about": "Pasta coated in a cheese sauce, usually served hot as a bowl or bake.",
    },
    "nachos": {
        "display_name": "Nachos",
        "cuisine": "Mexican-inspired",
        "about": "Tortilla chips topped with cheese and often beans, salsa, meat, or sour cream.",
    },
    "omelette": {
        "display_name": "Omelette",
        "cuisine": "Breakfast",
        "about": "A beaten egg dish cooked in a pan, sometimes folded around fillings.",
    },
    "pad_thai": {
        "display_name": "Pad Thai",
        "cuisine": "Thai",
        "about": "A Thai stir-fried noodle dish often made with egg, protein, peanuts, and sauce.",
    },
    "pancakes": {
        "display_name": "Pancakes",
        "cuisine": "Breakfast",
        "about": "Flat griddled cakes usually served as a stack with syrup or toppings.",
    },
    "pho": {
        "display_name": "Pho",
        "cuisine": "Vietnamese",
        "about": "A Vietnamese noodle soup with broth, rice noodles, herbs, and usually sliced beef or chicken.",
    },
    "pizza": {
        "display_name": "Pizza",
        "cuisine": "Italian-inspired",
        "about": "A baked flatbread topped with sauce, cheese, and other ingredients.",
    },
    "ramen": {
        "display_name": "Ramen",
        "cuisine": "Japanese",
        "about": "A Japanese noodle soup built around wheat noodles, broth, toppings, and seasonings.",
    },
    "risotto": {
        "display_name": "Risotto",
        "cuisine": "Italian",
        "about": "A creamy rice dish cooked slowly with stock until tender.",
    },
    "sashimi": {
        "display_name": "Sashimi",
        "cuisine": "Japanese",
        "about": "Thinly sliced raw fish or seafood served without rice.",
    },
    "spaghetti_bolognese": {
        "display_name": "Spaghetti Bolognese",
        "cuisine": "Italian-inspired",
        "about": "Spaghetti served with a rich meat-based tomato sauce.",
    },
    "spaghetti_carbonara": {
        "display_name": "Spaghetti Carbonara",
        "cuisine": "Italian",
        "about": "Pasta coated in a sauce made from egg, cheese, and cured pork.",
    },
    "steak": {
        "display_name": "Steak",
        "cuisine": "Western",
        "about": "A cooked cut of beef, usually served as a main with sides.",
    },
    "sushi": {
        "display_name": "Sushi",
        "cuisine": "Japanese",
        "about": "Rice-based Japanese bites often paired with seafood, vegetables, or egg.",
    },
    "tacos": {
        "display_name": "Tacos",
        "cuisine": "Mexican",
        "about": "Folded or open tortillas filled with meat, vegetables, and sauces.",
    },
    "tiramisu": {
        "display_name": "Tiramisu",
        "cuisine": "Italian",
        "about": "A layered dessert made with coffee-soaked sponge, cream, and cocoa.",
    },
    "waffles": {
        "display_name": "Waffles",
        "cuisine": "Breakfast",
        "about": "Crisp grid-patterned batter cakes served with sweet or savory toppings.",
    },
}

KEYWORD_FALLBACKS = (
    (
        "salad",
        {
            "estimated_calories": 220,
            "serving_description": "1 bowl",
            "cuisine": None,
            "about": "A mixed bowl of vegetables and toppings, usually served cold or lightly dressed.",
        },
    ),
    (
        "soup",
        {
            "estimated_calories": 180,
            "serving_description": "1 bowl",
            "cuisine": None,
            "about": "A broth-based or blended dish served as a bowl or starter.",
        },
    ),
    (
        "cake",
        {
            "estimated_calories": 410,
            "serving_description": "1 slice",
            "cuisine": "Dessert",
            "about": "A baked dessert that is usually served in slices.",
        },
    ),
    (
        "pie",
        {
            "estimated_calories": 320,
            "serving_description": "1 slice",
            "cuisine": "Dessert",
            "about": "A baked pastry dish with a sweet or savory filling.",
        },
    ),
    (
        "sandwich",
        {
            "estimated_calories": 480,
            "serving_description": "1 sandwich",
            "cuisine": "Western",
            "about": "A handheld meal made with bread and a filling.",
        },
    ),
    (
        "burger",
        {
            "estimated_calories": 520,
            "serving_description": "1 burger",
            "cuisine": "Western",
            "about": "A sandwich built around a patty inside a bun.",
        },
    ),
    (
        "rice",
        {
            "estimated_calories": 450,
            "serving_description": "1 plate",
            "cuisine": "Asian-inspired",
            "about": "A rice-based meal that can vary widely by toppings and seasoning.",
        },
    ),
    (
        "pasta",
        {
            "estimated_calories": 500,
            "serving_description": "1 plate",
            "cuisine": "Italian-inspired",
            "about": "A pasta dish served with sauce, protein, or vegetables.",
        },
    ),
    (
        "noodle",
        {
            "estimated_calories": 450,
            "serving_description": "1 bowl",
            "cuisine": "Asian-inspired",
            "about": "A noodle-based dish that may be served dry or in broth.",
        },
    ),
    (
        "fries",
        {
            "estimated_calories": 365,
            "serving_description": "1 medium serve",
            "cuisine": "Western",
            "about": "A fried potato side dish or snack.",
        },
    ),
    (
        "ice_cream",
        {
            "estimated_calories": 275,
            "serving_description": "1 cup",
            "cuisine": "Dessert",
            "about": "A frozen dessert typically served by scoop or cup.",
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
    "bun bo": "bun_bo",
    "bun bo hue": "bun_bo_hue",
}


class NutritionLookupService:
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

    def build_recommendation(
        self,
        nutrition: Dict[str, object],
        *,
        is_unclear: bool = False,
    ) -> str:
        if is_unclear:
            return "Try uploading a clearer, closer image for a more reliable result."

        calories = nutrition.get("estimated_calories")
        if calories is None:
            return "Nutrition data is not available for this class yet. Treat the result as a guide only."

        calories = int(calories)
        if calories >= 600:
            return "This looks like a more calorie-dense serving. Portion size and sides will change the total substantially."
        if calories <= 250:
            return "This looks like a lighter serving. Pair it with protein or fibre if you want it to be more filling."
        return "Use the calorie estimate as a guide only. Recipe and serving size can shift the total."

    def _build_available(
        self,
        normalized: str,
        data: Dict[str, object],
        *,
        source: str,
        display_name: Optional[str] = None,
    ) -> Dict[str, object]:
        metadata = MEAL_METADATA.get(normalized, {})
        return {
            "display_name": metadata.get("display_name") or display_name or self._humanize_label(normalized),
            "about": metadata.get("about") or data.get("about"),
            "cuisine": metadata.get("cuisine") or data.get("cuisine"),
            "estimated_calories": int(data["estimated_calories"]),
            "serving_description": data.get("serving_description"),
            "source": source,
            "available": True,
        }

    def _unavailable(
        self,
        *,
        label: Optional[str] = None,
        normalized: Optional[str] = None,
    ) -> Dict[str, object]:
        base_label = normalized or self._normalize_label(label)
        return {
            "display_name": self._display_name(label, base_label),
            "about": None,
            "cuisine": None,
            "estimated_calories": None,
            "serving_description": None,
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
