# NutriHelp Food image recognition

Summary after discussion with Acting Company Director (Dr Bahareh)  
Contributed by: Chin Tho (John) Leong (T3 2023)

## Terminologies:

- Food = any edible raw/process item (e.g. fruit, Pizza)
- Ingredient = edible items use in making a dish or food (e.g. spices, vegetables).

Steps to take in developing this feature:

1. Step one – Research on ML to recognise the food
2. Step two – Build the ML
3. Step three – If the food is a cooked food, the identified food will refer to databases for ingredients and look up for volume or portion of each ingredient.
4. Step Three – nutrition facts lookup. (Reference Database)

## STEP ONE – Build ML to recognise the food

- Research:

  - Existing literature on food/image recognition.
  - Look for open Sample dataset for model training.
  - List out all possible ML model to use and find out the pros and cons.

## STEP TWO – Build ML

- Code and build all researched models based on simple object and image recognition (simple food or ingredient (Fruits/vegetable/meat)).

## STEP THREE - Identify ingredients from an identified dish/food

- Any dish identify by the ML will need to reference a Recipe database to retrieve all related ingredients, and portion or volume of the dish.

## STEP FOUR – Retrieve Nutrition facts.

- All identified food/dishes will reference a nutrition fact database to retrieve all related nutritional facts. (e.g. Food Remedy API)
