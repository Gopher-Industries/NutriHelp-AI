# # ============================================================================
# # FILE 2: data_loader.py
# # Loads and manages all nutrition data from CSV
# # ============================================================================


import pandas as pd
from typing import List, Dict, Optional


class NutritionDataLoader:
    """Manages all nutrition, recipe, health condition, and sport gear data"""

    def __init__(self):
        self.conditions = None
        self.allergies = None
        self.recipes = None
        self.ingredients = None
        self.recipe_ingredients = None
        self.categories = None
        self.sport_gear = None  # NEW

    def load_all_data(self):
        """Load all nutrition and sport data"""
        try:
            print("[Data] Loading database...")

            self.conditions = self._load_conditions()
            self.allergies = self._load_allergies()
            self.recipes = self._load_recipes()
            self.ingredients = self._load_ingredients()
            self.recipe_ingredients = self._load_recipe_ingredients()
            self.categories = self._load_categories()

            # --- NEW: Load Sport Gear Data ---
            self.sport_gear = self._load_sport_gear()
            print(
                f"[Data] ✓ Loaded gear data for {len(self.sport_gear)} sports")

            print("[Data] ✓ All data loaded successfully!\n")
            return True

        except Exception as e:
            print(f"[Data] ✗ Error loading data: {e}")
            return False

    # =========================================================================
    #  NEW: SPORT GEAR DATA
    # =========================================================================
    def _load_sport_gear(self) -> Dict[str, List[str]]:
        """Returns a dictionary of sports and recommended gear"""
        return {
            'gym': [
                'Flat-soled shoes (Converse/Metcons) for stability',
                'Weightlifting Belt (for heavy compounds)',
                'Wrist Wraps (for pressing movements)',
                'Shaker Bottle',
                'Gym Towel'
            ],
            'running': [
                'Proper Running Shoes (Gait analysis recommended)',
                'Moisture-wicking Socks (prevent blisters)',
                'Running Watch/Tracker (Garmin/Apple)',
                'High-visibility vest (night running)',
                'Anti-chafe balm'
            ],
            'yoga': [
                'Non-slip Yoga Mat (4mm+ thickness)',
                'Yoga Blocks (Cork or Foam)',
                'Yoga Strap (for flexibility)',
                'Form-fitting, breathable clothing',
                'Microfiber Towel'
            ],
            'swimming': [
                'Anti-fog Goggles',
                'Silicone Swim Cap',
                'Chlorine-resistant Swimsuit',
                'Ear Plugs & Nose Clip',
                'Microfiber Quick-dry Towel'
            ],
            'walking': [
                'Supportive Walking Shoes with arch support',
                'Pedometer or Step Counter',
                'Breathable layers (weather appropriate)',
                'Small backpack or waist pack',
                'Sun protection (Hat/SPF)'
            ],
            'cycling': [
                'Padded Cycling Shorts (Bibs)',
                'Helmet (MIPS safety standard)',
                'Cycling Shoes (Clipless)',
                'Water Bottle Cage',
                'Bike Lights (Front & Rear)'
            ],
            'football': [
                'Football Cleats/Boots',
                'Shin Guards',
                'Compression Socks',
                'Hydration Bottle',
                'Breathable Jersey'
            ],
            'cricket': [
                'Cricket Spikes/Shoes',
                'Sun Hat/Cap',
                'White Athletic Wear',
                'Personal Abdominal Guard (Box)',
                'Sunscreen'
            ],
            'general': [
                'Comfortable Athletic Shoes',
                'Water Bottle (1L+)',
                'Sweat Towel',
                'Smart Watch/Fitness Tracker',
                'Wireless Earbuds'
            ]
        }

    def get_sport_gear(self, sport_name: str) -> List[str]:
        """Get gear list based on sport name (fuzzy match)"""
        if not self.sport_gear:
            return []

        sport = sport_name.lower()

        # Simple keyword matching
        if 'gym' in sport or 'weight' in sport or 'lift' in sport:
            return self.sport_gear['gym']
        elif 'run' in sport or 'jog' in sport:
            return self.sport_gear['running']
        elif 'yoga' in sport or 'pilates' in sport:
            return self.sport_gear['yoga']
        elif 'swim' in sport or 'pool' in sport:
            return self.sport_gear['swimming']
        elif 'walk' in sport:
            return self.sport_gear['walking']
        elif 'cycle' in sport or 'bike' in sport:
            return self.sport_gear['cycling']
        elif 'football' in sport or 'soccer' in sport:
            return self.sport_gear['football']
        elif 'cricket' in sport:
            return self.sport_gear['cricket']

        return self.sport_gear['general']

    # =========================================================================
    #  EXISTING DATA METHODS (Kept exactly as they were)
    # =========================================================================
    def _load_conditions(self) -> pd.DataFrame:
        conditions_data = {
            'condition_id': list(range(1, 131)),
            'name': ['Diabetes', 'Hypertension', 'Celiac Disease', 'Lactose Intolerance',
                     'Anemia', 'Osteoporosis', 'Gout', 'IBS', 'High Cholesterol',
                     'Kidney Disease', 'Arthritis', 'Asthma', 'Bronchitis',
                     'Chronic Fatigue Syndrome', 'Depression', 'Anxiety Disorder',
                     'Obesity', 'Migraine', 'Eczema', 'Psoriasis', 'Acid Reflux',
                     'Diverticulitis', 'Ulcerative Colitis', 'Crohn\'s Disease',
                     'Hyperthyroidism', 'Hypothyroidism', 'Parkinson\'s Disease',
                     'Alzheimer\'s Disease', 'Multiple Sclerosis', 'Rheumatoid Arthritis'
                     ] + ['Other Condition'] * 100,
            'recommended_foods': [
                ['Whole Grains', 'Leafy Greens', 'Lean Proteins'],
                ['Low-sodium Foods', 'Bananas', 'Beets'],
                ['Rice', 'Quinoa', 'Gluten-free Oats'],
                ['Almond Milk', 'Soy Milk', 'Lactose-free Products'],
                ['Red Meat', 'Spinach', 'Iron-fortified Cereal'],
                ['Dairy Products', 'Leafy Greens', 'Sardines'],
                ['Low-fat Dairy', 'Vegetables', 'Cherries'],
                ['Low-FODMAP Foods', 'Rice', 'Carrots'],
                ['Oats', 'Nuts', 'Fatty Fish'],
                ['Cauliflower', 'Blueberries', 'Egg Whites'],
                ['Fish oils', 'Turmeric', 'Green Tea'],
                ['Antioxidant-rich Fruits', 'Leafy Greens', 'Omega-3 Sources'],
                ['Warm Herbal Teas', 'Honey', 'Ginger'],
                ['Complex Carbohydrates', 'Lean Proteins', 'Nuts'],
                ['Omega-3 Rich Foods', 'Leafy Greens', 'Berries'],
                ['Chamomile Tea', 'Whole Grains', 'Bananas'],
                ['Fruits', 'Vegetables', 'Lean Proteins'],
                ['Magnesium-Rich Foods', 'Ginger', 'Dark Leafy Greens'],
                ['Anti-inflammatory Foods', 'Fruits', 'Vegetables'],
                ['Omega-3 Rich Foods', 'Fruits', 'Vegetables'],
                ['Oatmeal', 'Ginger', 'Aloe Vera Juice'],
                ['High-Fiber Foods', 'Fruits', 'Vegetables'],
                ['Probiotic Foods', 'Bone Broth', 'Easily Digestible Fruits'],
                ['Lean Proteins', 'Cooked Vegetables', 'Rice'],
                ['Calcium-Rich Foods', 'High-Quality Proteins', 'Antioxidants'],
                ['Whole Grains', 'Lean Proteins', 'Fruits'],
                ['Fiber-Rich Foods', 'Antioxidants', 'Omega-3 Foods'],
                ['Mediterranean Diet Foods', 'Leafy Greens', 'Berries'],
                ['Vitamin D Rich Foods', 'Omega-3 Sources', 'Fruits'],
                ['Fish Oils', 'Nuts', 'Antioxidant-Rich Vegetables']
            ] + [['Balanced Diet', 'Whole Foods', 'Fresh Produce']] * 100,
            'restricted_foods': [
                ['Refined Sugar', 'White Bread', 'Sweetened Beverages'],
                ['Salted Snacks', 'Processed Meats', 'Pickles'],
                ['Wheat', 'Barley', 'Rye'],
                ['Milk', 'Cheese', 'Yogurt'],
                ['Calcium-rich Foods during iron meals'],
                ['Caffeine', 'Soft Drinks'],
                ['Red Meat', 'Seafood', 'Alcohol'],
                ['Onions', 'Garlic', 'Lentils'],
                ['Fried Foods', 'Trans Fats', 'Full-fat Dairy'],
                ['Sodium-rich Foods', 'Potassium-rich Foods', 'Red Meat'],
                ['Processed Foods', 'Sugar', 'Saturated Fats'],
                ['Dairy in sensitive cases', 'Processed Foods', 'Sulfites'],
                ['Cold Drinks', 'Smoking'],
                ['Caffeinated Beverages', 'Processed Sugars', 'High Fat Foods'],
                ['High Sugar', 'Caffeine', 'Alcohol'],
                ['Caffeine', 'Sugar', 'Processed Food'],
                ['Sugary Snacks', 'Fried Foods', 'Sodas'],
                ['Alcohol', 'Chocolate', 'Caffeine'],
                ['Dairy', 'Nuts', 'Eggs'],
                ['Alcohol', 'Red Meat', 'Dairy'],
                ['Coffee', 'Chocolate', 'Spicy Foods'],
                ['Processed Foods', 'Red Meat', 'Refined Grains'],
                ['Spicy Foods', 'Caffeine', 'High-Fiber Raw Veggies'],
                ['Dairy', 'High-Fiber Foods', 'Processed Foods'],
                ['Iodine-Rich Foods', 'Caffeine', 'Processed Snacks'],
                ['Excess Soy Products',
                    'Cruciferous Vegetables in excess', 'Processed Foods'],
                ['High Sugar Foods', 'Saturated Fats', 'Processed Snacks'],
                ['Saturated Fats', 'Sugar', 'Processed Foods'],
                ['Saturated Fats', 'Processed Foods', 'Refined Sugars'],
                ['Red Meat', 'Processed Foods', 'Sugars']
            ] + [['Processed Foods', 'Excessive Sugar', 'Trans Fats']] * 100,
            'severity_level': ['high', 'high', 'high', 'medium', 'medium',
                               'medium', 'high', 'medium', 'high', 'high',
                               'medium', 'medium', 'medium', 'high', 'high',
                               'medium', 'high', 'high', 'medium', 'medium',
                               'medium', 'medium', 'high', 'high', 'medium',
                               'medium', 'high', 'high', 'high', 'high'] + ['medium'] * 100
        }
        return pd.DataFrame(conditions_data)

    def _load_allergies(self) -> pd.DataFrame:
        allergies_data = {
            'id': list(range(1, 27)),
            'name': [
                'Peanuts', 'Shrimp', 'Gluten', 'Dairy', 'Eggs', 'Soy',
                'Fish', 'Shellfish', 'Tree Nuts', 'Wheat', 'Sesame', 'Corn',
                'Legumes', 'Seeds', 'Coconut', 'Alcohol', 'Sulfites',
                'Spices', 'Vegetables', 'Fruits', 'Meat', 'Herbs',
                'Grains', 'Oils', 'Additives', 'Not categorized'
            ]
        }
        return pd.DataFrame(allergies_data)

    def _load_recipes(self) -> pd.DataFrame:
        recipes_data = {
            'id': [18, 19, 22, 23, 25, 26, 27, 28, 34, 82],
            'recipe_name': [
                'Tomato Pesto Chicken Pasta', 'Spanish Tortilla', 'Quinoa Salmon Bowl',
                'Quinoa Salmon Bowl v2', 'Vegetable Curry', 'Saffron Rice',
                'Vegetable Rice', 'Vegetable Curry Deluxe', 'Pasta Puttanesca', 'Classic Spaghetti'
            ],
            'cuisine_id': [5, 6, 14, 14, 2, 1, 1, 1, 2, 2],
            'total_servings': [3, 4, 3, 3, 3, 2, 0, 3, 1, 1],
            'preparation_time': [45, 15, 30, 30, 23, 23, 50, 70, 70, 70],
            'calories': [2704.97, 0, 1328.66, 1306.76, 5.75, 39, 2.6, 11.7, 0, 0],
            'protein': [23.31, 0, 87.84, 92.2, 0.44, 0.81, 0.05, 0.31, 0, 0],
            'carbohydrates': [144.13, 0, 112.46, 112.2, 1.14, 8.46, 0.56, 2.14, 0, 0],
            'fat': [242.31, 0, 57.32, 51.24, 0.06, 0.08, 0.01, 0.25, 0, 0],
            'fiber': [8.78, 0, 16.82, 19.7, 0.46, 0.12, 0.01, 0.36, 0, 0],
            'difficulty_level': ['medium', 'easy', 'easy', 'easy', 'easy',
                                 'easy', 'easy', 'medium', 'medium', 'easy']
        }
        return pd.DataFrame(recipes_data)

    def _load_ingredients(self) -> pd.DataFrame:
        ingredients_data = {
            'id': ['salmon-001', 'yogurt-001', 'almond-001', 'chicken-001',
                   'apple-001', 'banana-001', 'broccoli-001', 'egg-001',
                   'rice-001', 'oats-001'],
            'name': ['Salmon', 'Greek Yogurt', 'Almonds', 'Chicken Breast',
                     'Apple', 'Banana', 'Broccoli', 'Eggs', 'Brown Rice', 'Oatmeal'],
            'category': ['Fish', 'Dairy', 'Nuts', 'Meat', 'Fruits', 'Fruits',
                         'Vegetables', 'Dairy', 'Grains', 'Grains'],
            'calories_per_100g': [208, 59, 579, 165, 52, 89, 34, 155, 111, 68],
            'protein': [25, 10, 21, 31, 0.3, 1.1, 2.8, 13, 2.6, 2.4],
            'carbs': [0, 3.6, 22, 0, 14, 23, 7, 1.1, 23, 12],
            'fat': [12, 0.4, 50, 3.6, 0.2, 0.3, 0.4, 11, 0.9, 1.4],
            'fiber': [0, 0, 12, 0, 2.4, 2.6, 2.6, 0, 1.8, 1.7]
        }
        return pd.DataFrame(ingredients_data)

    def _load_recipe_ingredients(self) -> pd.DataFrame:
        recipe_ing_data = {
            'recipe_id': [22, 22, 22, 23, 23, 23, 25, 25, 26, 27],
            'ingredient_name': ['Salmon', 'Quinoa', 'Broccoli', 'Salmon',
                                'Quinoa', 'Brown Rice', 'Curry Powder', 'Vegetables',
                                'Saffron', 'Rice'],
            'amount': [300, 200, 150, 300, 200, 150, 20, 200, 2, 250]
        }
        return pd.DataFrame(recipe_ing_data)

    def _load_categories(self) -> pd.DataFrame:
        categories_data = {
            'id': list(range(9, 17)),
            'name': ['Main Course', 'Appetizer', 'Dessert', 'Breakfast',
                     'Lunch', 'Dinner', 'Snack', 'Beverage'],
            'description': [
                'Primary dish of a meal', 'Starter dishes',
                'Sweet dishes served after main course', 'Morning meals',
                'Midday meals', 'Evening meals',
                'Light meals between main meals', 'Drinks and cocktails'
            ]
        }
        return pd.DataFrame(categories_data)

    def get_condition_info(self, condition_name: str) -> Optional[Dict]:
        if self.conditions is None:
            return None
        condition = self.conditions[self.conditions['name'].str.lower(
        ) == condition_name.lower()]
        if condition.empty:
            return None
        return {
            'name': condition.iloc[0]['name'],
            'recommended': condition.iloc[0]['recommended_foods'],
            'restricted': condition.iloc[0]['restricted_foods'],
            'severity': condition.iloc[0]['severity_level']
        }

    def search_recipes(self, query: str = '', max_results: int = 10) -> pd.DataFrame:
        if self.recipes is None:
            return pd.DataFrame()
        if not query:
            return self.recipes.head(max_results)
        mask = self.recipes['recipe_name'].str.contains(
            query, case=False, na=False)
        return self.recipes[mask].head(max_results)

    def filter_by_allergies(self, allergy_list: List[str]) -> pd.DataFrame:
        return self.recipes

    def get_high_protein_recipes(self, min_protein: float = 20) -> pd.DataFrame:
        if self.recipes is None:
            return pd.DataFrame()
        return self.recipes[self.recipes['protein'] >= min_protein]

    def get_low_calorie_recipes(self, max_calories: float = 500) -> pd.DataFrame:
        if self.recipes is None:
            return pd.DataFrame()
        return self.recipes[(self.recipes['calories'] > 0) & (self.recipes['calories'] <= max_calories)]
