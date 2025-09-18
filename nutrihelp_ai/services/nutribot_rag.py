import os, json, re
from typing import Any, Dict, List, Optional
from dotenv import load_dotenv

from groq import Groq
import chromadb

load_dotenv()

# ----------------- Config -----------------
GROQ_API_KEY   = os.getenv("GROQ_API_KEY")
GROQ_MODEL     = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

CHROMA_MODE     = os.getenv("CHROMA_MODE", "local")
CHROMA_PATH     = os.getenv("CHROMA_PATH", "./.chroma")
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
    ],
    "progress_analysis": "string"
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
        try:
            count = self._col.count()
            if count == 0:
                return []
        except Exception:
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
        # Try to extract outermost JSON object
        m = re.search(r"\{[\s\S]*\}\s*$", text)
        raw = m.group(0) if m else text

        # Remove trailing commas before ] or }
        raw = re.sub(r",(\s*[\]}])", r"\1", raw)

        try:
            data = json.loads(raw)
        except Exception:
            # Last resort: wrap as suggestion
            return {"suggestion": str(text).strip(), "weekly_plan": [], "progress_analysis": ""}

        # If suggestion accidentally contains JSON, try to pull it up
        if isinstance(data.get("suggestion"), str) and "{" in data["suggestion"] and "}" in data["suggestion"]:
            try:
                inner = json.loads(data["suggestion"])
                # If inner has expected keys, merge; otherwise, keep original text
                if isinstance(inner, dict):
                    for k in ("suggestion", "weekly_plan", "progress_analysis"):
                        if k in inner and k not in data:
                            data[k] = inner[k]
                    # And make suggestion a plain sentence
                    if isinstance(data.get("suggestion"), dict):
                        data["suggestion"] = "See plan and reminders below."
            except Exception:
                pass

        return data


    def _build_prompt(
        self,
        analyzed_health_condition: Dict[str, Any],
        n_results: int = 4,
        num_weeks: int = 4,   # <— added
    ) -> str:
        condition_json = json.dumps(analyzed_health_condition, ensure_ascii=False, indent=2)
        schema_json = json.dumps(STRICT_SCHEMA_EXAMPLE, ensure_ascii=False, indent=2)

        user_task = (
            f"Generate a {num_weeks}-week diet & workout plan and analyze progress across reports. "
            "If multiple reports are given, compare them and include improvement/no-improvement notes "
            "in the 'progress_analysis' field. Return STRICT JSON only."
        )
        ctx_snips = self.rag.retrieve(
            query=f"{user_task}\nUser condition history: {condition_json}",
            n_results=n_results,
        )
        ctx_joined = "\n- " + "\n- ".join(ctx_snips) if ctx_snips else ""

        return (
            "You are a nutrition and fitness assistant.\n"
            "OUTPUT RULES (READ CAREFULLY):\n"
            "1) Output MUST be a single valid JSON object. No prose, no code fences.\n"
            "2) Allowed top-level keys ONLY: \"suggestion\", \"weekly_plan\", \"progress_analysis\".\n"
            "3) Types:\n"
            "   - suggestion: string (one sentence). It MUST NOT contain JSON or braces.\n"
            "   - weekly_plan: array of exactly {n} objects, with keys:\n"
            "       week (int 1..{n}), target_calories_per_day (int), focus (string: Weight Loss|Muscle Gain|Endurance),\n"
            "       workouts (array of strings), meal_notes (string), reminders (array of strings)\n"
            "   - progress_analysis: string (short paragraph)\n"
            "4) Keep workouts/reminders as short bullet-like strings.\n"
            "5) Use realistic AU norms (hydration, calories, macros) when relevant.\n"
            "6) Do not include any extra keys anywhere.\n"
            "7) Produce exactly {n} items in weekly_plan with weeks numbered 1..{n}.\n"
            "\nSTRICT SHAPE EXAMPLE (TYPES ONLY, NOT CONTENT):\n"
            f"{schema_json}\n"
            "\nUSER CONDITION HISTORY:\n"
            f"{condition_json}\n"
            "\nRAG CONTEXT (Australian norms):\n"
            f"{ctx_joined}\n"
        )


    def generate_plan(
        self,
        analyzed_health_condition: Dict[str, Any],
        n_results: int = 4,
        max_tokens: int = 1200,
        temperature: float = 0.2,
        num_weeks: int = 8,
    ) -> Dict[str, Any]:
        prompt = self._build_prompt(
            analyzed_health_condition,
            n_results=n_results,
            num_weeks=num_weeks,  # <— passed through
        )
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
        clean = _enforce_schema(data, num_weeks=num_weeks)
        return clean



# ───────────────────────── Schema Enforcer helpers ─────────────────────────
ALLOWED_FOCUS = {"Weight Loss", "Muscle Gain", "Endurance"}
CAL_MIN, CAL_MAX = 1200, 3500  # sensible guardrails

def _clean_str(x) -> str:
    return str(x).strip()

def _clean_str_list(xs):
    if isinstance(xs, list):
        return [_clean_str(s) for s in xs if str(s).strip()]
    if isinstance(xs, str):
        return [_clean_str(xs)] if xs.strip() else []
    return []

def _coerce_int(x, default: int) -> int:
    try:
        v = int(float(x))
        return max(CAL_MIN, min(CAL_MAX, v))
    except Exception:
        return default

def _normalize_week_item(i: int, item: dict) -> dict:
    week = i + 1
    target = _coerce_int(item.get("target_calories_per_day", 1700), 1900)
    focus = item.get("focus", "Weight Loss")
    focus = focus if focus in ALLOWED_FOCUS else "Weight Loss"
    workouts = _clean_str_list(item.get("workouts", []))
    meal_notes = _clean_str(item.get("meal_notes", ""))
    reminders = _clean_str_list(item.get("reminders", []))

    if workouts and ":" not in workouts[0]:
        days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        workouts = [f"{days[j%7]}: {w}" for j, w in enumerate(workouts)]

    return {
        "week": week,
        "target_calories_per_day": target,
        "focus": focus,
        "workouts": workouts[:7] or [
            "Monday: 30 minutes brisk walking",
            "Wednesday: Rest day",
            "Friday: 20 minutes strength training"
        ],
        "meal_notes": meal_notes or "Eat 3 main meals and 2 snacks, include lean protein, whole grains, and healthy fats.",
        "reminders": reminders[:6] or ["Drink 8 glasses of water daily", "Limit sugary drinks and fast food"],
    }

def _enforce_schema(data: dict, num_weeks: int) -> dict:
    out = {
        "suggestion": _clean_str(data.get("suggestion", "")),
        "weekly_plan": [],
        "progress_analysis": _clean_str(data.get("progress_analysis", "")),
    }

    if "{" in out["suggestion"] and "}" in out["suggestion"]:
        out["suggestion"] = "Increase daily water intake to 2 liters and consume 5 servings of fruits and vegetables."

    wp = data.get("weekly_plan", [])
    wp = wp if isinstance(wp, list) else []

    norm_items = []
    for i in range(num_weeks):
        base = wp[i] if i < len(wp) and isinstance(wp[i], dict) else {}
        norm_items.append(_normalize_week_item(i, base))
    out["weekly_plan"] = norm_items

    if not out["progress_analysis"]:
        out["progress_analysis"] = (
            "Progress trend: steady adherence recommended. Track weight, BMI, and blood pressure weekly."
        )

    return out
# ───────────────────────── End helpers ─────────────────────────