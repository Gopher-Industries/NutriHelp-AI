from pathlib import Path
from nutrihelp_ai.services.active_ai_backend import GroqChromaBackend

BASE_DIR = Path(__file__).resolve().parent
DOC_DIR = BASE_DIR / "nutrihelp_ai" / "data" / "rag_sources"

files = [
    DOC_DIR / "week9_recipe_engine_context.txt",
    DOC_DIR / "week9_chatbot_prompt_guide.txt",
]

docs = []
for file_path in files:
    print("Checking:", file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        docs.append(f.read().strip())

backend = GroqChromaBackend(collection_name="aus_food_nutrition")

before_count = backend.collection_count()
after_count = backend.add_documents(docs)

print("Before count:", before_count)
print("After count:", after_count)
print("Added documents:", len(docs))