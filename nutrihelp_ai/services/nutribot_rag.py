import os, json, re
from typing import Any, Dict, List, Optional
from dotenv import load_dotenv

from groq import Groq
import chromadb

load_dotenv()

# ----------------- Config -----------------
GROQ_API_KEY   = os.getenv("GROQ_API_KEY")
GROQ_MODEL     = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

# If you really want cloud, set CHROMA_MODE=cloud and provide API key + tenant + database
CHROMA_MODE     = os.getenv("CHROMA_MODE", "local")  # "local" | "cloud"
CHROMA_PATH     = os.getenv("CHROMA_PATH", "./.chroma")  # for local persistent
CHROMA_TENANT   = os.getenv("CHROMA_TENANT")
CHROMA_DATABASE = os.getenv("CHROMA_DATABASE")
CHROMA_API_KEY  = os.getenv("CHROMA_API_KEY")

RAG_COLLECTION  = os.getenv("RAG_COLLECTION", "aus_food_nutrition")


def _require_env(name: str, value: Optional[str]):
    if not value:
        raise RuntimeError(f"Missing required env var: {name}")


STRICT_SCHEMA_EXAMPLE = {
    "suggestion": "string",
    "weekly_plan": [
        {
            "week": 1,
            "target_calories_per_day": 2000,
            "focus": "string",
            "workouts": ["string"],
            "meal_notes": "string",
            "reminders": ["string"]
        }
    ]
}


class RAG:
    def __init__(self, collection_name: str = RAG_COLLECTION):
        self.collection_name = collection_name
        self._client = None
        self._col = None

    def _ensure_client(self):
        if self._client is not None and self._col is not None:
            return

        if CHROMA_MODE.lower() == "cloud":
            _require_env("CHROMA_API_KEY", CHROMA_API_KEY)
            _require_env("CHROMA_TENANT", CHROMA_TENANT)
            _require_env("CHROMA_DATABASE", CHROMA_DATABASE)
            self._client = chromadb.CloudClient(
                tenant=CHROMA_TENANT,
                database=CHROMA_DATABASE,
                api_key=CHROMA_API_KEY,
            )
        else:
            # Local persistent storage (recommended for development)
            self._client = chromadb.PersistentClient(path=CHROMA_PATH)

        self._col = self._client.get_or_create_collection(name=self.collection_name)

    def add_documents(self, docs: List[str]) -> int:
        self._ensure_client()
        start = self._col.count()
        for i, d in enumerate(docs):
            self._col.upsert(ids=[f"id{start+i}"], documents=[d])
        return self._col.count()

    def retrieve(self, query: str, n_results: int = 4) -> List[str]:
        self._ensure_client()
        # Gracefully handle empty collection
        try:
            count = self._col.count()
            if count == 0:
                return []
        except Exception:
            # If count isn’t supported for some reason, still attempt query
            pass

        res = self._col.query(query_texts=[query], n_results=n_results)
        return res.get("documents", [[]])[0]


class NutriBotRAGService:
    def __init__(self, rag: Optional[RAG] = None):
        self.rag = rag or RAG()
        self._groq = None

    def _groq_client(self):
        if self._groq is None:
            _require_env("GROQ_API_KEY", GROQ_API_KEY)
            self._groq = Groq(api_key=GROQ_API_KEY)
        return self._groq

    @staticmethod
    def _force_json(text: str) -> Dict[str, Any]:
        # Extract first {...}; fix common trailing commas; fallback
        m = re.search(r"\{.*\}", text, flags=re.DOTALL)
        raw = m.group(0) if m else text
        raw = re.sub(r",(\s*[\]}])", r"\1", raw)
        try:
            return json.loads(raw)
        except Exception:
            return {"suggestion": raw.strip(), "weekly_plan": []}

    def _build_prompt(self, analyzed_health_condition: Dict[str, Any], n_results: int = 4) -> str:
        condition_json = json.dumps(analyzed_health_condition, ensure_ascii=False)
        schema_json = json.dumps(STRICT_SCHEMA_EXAMPLE, ensure_ascii=False, indent=2)

        user_task = (
            "Generate a 4-weekly diet & workout plan for the user. "
            "Return STRICT JSON only, no extra text."
        )
        ctx_snips = self.rag.retrieve(
            query=f"{user_task}\nUser condition: {condition_json}",
            n_results=n_results,
        )
        ctx_joined = "\n- " + "\n- ".join(ctx_snips) if ctx_snips else ""

        return (
            "You are a nutrition and fitness assistant.\n"
            "RULES:\n"
            "1) Output MUST be valid JSON only, no prose or code fences.\n"
            "2) Follow this schema exactly (keys and types):\n"
            f"{schema_json}\n"
            "3) Provide realistic numeric values. 'week' starts at 1.\n"
            "4) 'target_calories_per_day' must be an integer.\n"
            "5) Keep 'workouts' as concise bullet-like strings.\n\n"
            f"USER CONDITION JSON:\n{condition_json}\n\n"
            "RAG CONTEXT (use to ground recommendations and Australian nutrition norms):\n"
            f"{ctx_joined}\n"
        )

    def generate_plan(
        self,
        analyzed_health_condition: Dict[str, Any],
        n_results: int = 4,
        max_tokens: int = 1200,
        temperature: float = 0.2,
    ) -> Dict[str, Any]:
        prompt = self._build_prompt(analyzed_health_condition, n_results=n_results)
        client = self._groq_client()
        resp = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You output strictly valid JSON."},
                {"role": "user", "content": prompt},
            ],
            model=GROQ_MODEL,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        out = (resp.choices[0].message.content or "").strip()
        data = self._force_json(out)
        data.setdefault("suggestion", "")
        data.setdefault("weekly_plan", [])
        return data
