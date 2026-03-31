from nutrihelp_ai.services.active_ai_backend import GroqChromaBackend

backend = GroqChromaBackend(collection_name="aus_food_nutrition")

queries = [
    "How should the chatbot handle dietary preferences and allergies?",
    "What information should the recipe engine use when generating recipes?",
    "How should unclear detected ingredients be handled?",
    "What kind of prompt structure should the chatbot follow?",
    "What should I avoid if I have a nut allergy?",
    "Can NutriHelp adjust recipe suggestions for low-carb users?",
    "How should the chatbot respond when ingredients are unclear?"
]

for q in queries:
    print("\nQUERY:", q)
    results = backend.retrieve(q, n_results=2)
    print("RESULTS:", results)