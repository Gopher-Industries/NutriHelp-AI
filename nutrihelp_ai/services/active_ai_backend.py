import json
import logging
import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from urllib import error as urllib_error
from urllib import request as urllib_request

from dotenv import find_dotenv, load_dotenv

logger = logging.getLogger(__name__)

try:
    import chromadb
except Exception:
    chromadb = None

try:
    from groq import Groq
except Exception:
    Groq = None


def _load_project_env() -> Optional[Path]:
    """Load .env in a cross-platform way for Linux/Windows execution contexts."""
    candidates: List[Path] = []

    env_override = os.getenv("NUTRIHELP_ENV_FILE", "").strip()
    if env_override:
        candidates.append(Path(env_override).expanduser())

    project_root = Path(__file__).resolve().parents[2]
    candidates.append(project_root / ".env")

    cwd = Path.cwd()
    candidates.append(cwd / ".env")

    discovered = find_dotenv(filename=".env", usecwd=True)
    if discovered:
        candidates.append(Path(discovered))

    seen = set()
    for candidate in candidates:
        normalized = str(candidate.resolve()) if candidate.exists() else str(candidate)
        normalized_key = normalized.lower() if os.name == "nt" else normalized
        if normalized_key in seen:
            continue
        seen.add(normalized_key)

        if candidate.is_file():
            load_dotenv(dotenv_path=candidate, override=False)
            logger.info("Loaded environment variables from %s", candidate)
            return candidate

    logger.warning(
        "No .env file found. Checked: %s. Chat may be unavailable if GROQ_API_KEY is missing.",
        ", ".join(str(path) for path in candidates),
    )
    return None


_LOADED_ENV_PATH = _load_project_env()


def _env_float(name: str, default: float) -> float:
    raw = os.getenv(name, "").strip()
    if not raw:
        return default
    try:
        return float(raw)
    except ValueError:
        logger.warning("Invalid float value for %s=%r; falling back to %s", name, raw, default)
        return default


def _env_int(name: str, default: int) -> int:
    raw = os.getenv(name, "").strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        logger.warning("Invalid integer value for %s=%r; falling back to %s", name, raw, default)
        return default


@dataclass(frozen=True)
class ActiveAISettings:
    groq_api_key: str = field(default_factory=lambda: os.getenv("GROQ_API_KEY", ""))
    groq_model: str = field(default_factory=lambda: os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"))
    chroma_mode: str = field(default_factory=lambda: os.getenv("CHROMA_MODE", "cloud"))
    chroma_path: str = field(default_factory=lambda: os.getenv("CHROMA_PATH", "./.chroma"))
    chroma_api_key: str = field(default_factory=lambda: os.getenv("CHROMA_API_KEY", ""))
    chroma_tenant: str = field(default_factory=lambda: os.getenv("CHROMA_TENANT", ""))
    chroma_database: str = field(default_factory=lambda: os.getenv("CHROMA_DATABASE", ""))
    rag_collection: str = field(default_factory=lambda: os.getenv("RAG_COLLECTION", "aus_food_nutrition"))
    rag_n_results: int = field(default_factory=lambda: _env_int("RAG_N_RESULTS", 5))
    rag_distance_threshold: float = field(default_factory=lambda: _env_float("RAG_DISTANCE_THRESHOLD", 0.8))
    rag_relaxed_distance_threshold: float = field(default_factory=lambda: _env_float("RAG_RELAXED_DISTANCE_THRESHOLD", 1.6))
    groq_temperature: float = field(default_factory=lambda: _env_float("GROQ_TEMPERATURE", 0.0))
    groq_top_p: float = field(default_factory=lambda: _env_float("GROQ_TOP_P", 1.0))

    def missing_chat_env(self) -> List[str]:
        return ["GROQ_API_KEY"] if not self.groq_api_key else []

    def missing_chroma_env(self) -> List[str]:
        if self.chroma_mode.lower() != "cloud":
            return []

        missing = []
        if not self.chroma_api_key:
            missing.append("CHROMA_API_KEY")
        if not self.chroma_tenant:
            missing.append("CHROMA_TENANT")
        if not self.chroma_database:
            missing.append("CHROMA_DATABASE")
        return missing


def _safe_reply() -> str:
    return "Nutribot is currently unavailable."


GROUNDING_SYSTEM_PROMPT = (
    "You are NutriBot, a nutrition assistant.\n"
    "Strict grounding rules (follow exactly):\n"
    "1) Use ONLY the information provided in the context below.\n"
    "2) Answer ONLY using the provided context.\n"
    "3) Do not add information not present in the context.\n"
    "4) Do not rephrase, embellish, or expand unnecessarily.\n"
    "5) Be concise and direct.\n"
    "6) If the context is insufficient, reply exactly: 'I don\'t have enough information on that topic in my knowledge base.'"
)

DOMAIN_CHAT_SYSTEM_PROMPT = (
    "You are NutriBot, the NutriHelp assistant.\n"
    "You only help with nutrition, meals, food choices, healthy eating, calorie guidance, nutrients, "
    "dietary habits, food scanning follow-up, and user health goals related to diet and lifestyle.\n"
    "If the user asks something outside that scope, do not answer it as a general-purpose assistant. "
    "Instead, briefly explain that you focus on nutrition, meals, and healthy eating, then invite the user "
    "to ask a food or nutrition question.\n"
    "Keep replies concise, practical, and friendly."
)


class GroqChromaBackend:
    def __init__(
        self,
        collection_name: Optional[str] = None,
        settings: Optional[ActiveAISettings] = None,
    ):
        self.settings = settings or ActiveAISettings()
        self.collection_name = collection_name or self.settings.rag_collection
        self._groq_client = None
        self._collection = None
        self._count = None

    def _chat_unavailable_reason(self) -> str:
        missing = self.settings.missing_chat_env()
        if missing:
            return f"missing configuration: {', '.join(missing)}"
        if not Groq:
            return "groq package not installed/importable"
        return "unknown client initialization issue"

    def _domain_redirect_reply(self) -> str:
        return (
            "I'm here to help with nutrition, meals, healthy eating, and your food-related health goals. "
            "Try asking about foods, calories, nutrients, meal ideas, or diet guidance."
        )

    def _is_social_prompt(self, prompt: str) -> bool:
        clean = (prompt or "").strip().lower()
        if not clean:
            return False
        social_patterns = [
            r"^(hi|hello|hey|good morning|good afternoon|good evening)\b",
            r"^(thanks|thank you|thx)\b",
            r"^(how are you|how are you doing)\b",
        ]
        return any(re.search(pattern, clean) for pattern in social_patterns)

    def _is_nutrition_domain_prompt(self, prompt: str) -> bool:
        clean = (prompt or "").strip().lower()
        if not clean:
            return False

        nutrition_keywords = [
            "nutrition",
            "nutrient",
            "calorie",
            "protein",
            "carb",
            "fat",
            "fibre",
            "fiber",
            "vitamin",
            "mineral",
            "iron",
            "calcium",
            "sodium",
            "cholesterol",
            "food",
            "meal",
            "diet",
            "healthy eating",
            "weight loss",
            "weight gain",
            "breakfast",
            "lunch",
            "dinner",
            "snack",
            "recipe",
            "ingredient",
            "serving",
            "portion",
            "scan",
            "dish",
            "older adults",
            "seniors",
            "exercise",
            "gym",
            "hydration",
            "water",
            "diabetes",
            "blood pressure",
        ]
        return any(keyword in clean for keyword in nutrition_keywords)

    def _chat_with_domain_guard(self, prompt: str, model: Optional[str] = None) -> str:
        if self._is_social_prompt(prompt):
            return self.chat(prompt, model=model, system_prompt=DOMAIN_CHAT_SYSTEM_PROMPT)
        if not self._is_nutrition_domain_prompt(prompt):
            logger.info("Domain guard redirected out-of-scope prompt")
            return self._domain_redirect_reply()
        return self.chat(prompt, model=model, system_prompt=DOMAIN_CHAT_SYSTEM_PROMPT)

    def _get_groq_client(self):
        if self._groq_client is not None:
            return self._groq_client

        if not Groq:
            logger.warning("groq import failed; will attempt HTTP fallback if API key is configured.")
            return None

        missing = self.settings.missing_chat_env()
        if missing:
            logger.warning("Missing Groq configuration: %s", ", ".join(missing))
            return None

        try:
            self._groq_client = Groq(api_key=self.settings.groq_api_key)
        except Exception as exc:
            logger.error("Failed to initialize Groq client: %s", exc)
            self._groq_client = None
        return self._groq_client

    def _chat_via_http(
        self,
        prompt: str,
        model: Optional[str] = None,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
    ) -> str:
        model_name = model or self.settings.groq_model
        temp = self.settings.groq_temperature if temperature is None else temperature
        messages = [{"role": "user", "content": prompt}]
        if system_prompt:
            messages.insert(0, {"role": "system", "content": system_prompt})
        payload = {
            "messages": messages,
            "model": model_name,
            "temperature": temp,
            "top_p": self.settings.groq_top_p,
        }
        req = urllib_request.Request(
            url="https://api.groq.com/openai/v1/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.settings.groq_api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )

        try:
            with urllib_request.urlopen(req, timeout=30) as resp:
                response_data = json.loads(resp.read().decode("utf-8"))
            return response_data.get("choices", [{}])[0].get("message", {}).get("content") or _safe_reply()
        except urllib_error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="ignore") if hasattr(exc, "read") else ""
            logger.error("Groq HTTP fallback failed with status %s: %s", exc.code, body)
            return _safe_reply()
        except Exception as exc:
            logger.error("Groq HTTP fallback request failed: %s", exc)
            return _safe_reply()

    def _build_chroma_client(self):
        if not chromadb:
            logger.warning("chromadb import failed; active RAG backend unavailable.")
            return None

        if self.settings.chroma_mode.lower() == "cloud":
            missing = self.settings.missing_chroma_env()
            if missing:
                logger.warning("Missing Chroma Cloud configuration: %s", ", ".join(missing))
                return None
            return chromadb.CloudClient(
                tenant=self.settings.chroma_tenant,
                database=self.settings.chroma_database,
                api_key=self.settings.chroma_api_key,
            )

        return chromadb.PersistentClient(path=self.settings.chroma_path)

    def _get_collection(self):
        if self._collection is not None:
            return self._collection

        client = self._build_chroma_client()
        if client is None:
            return None

        try:
            self._collection = client.get_or_create_collection(name=self.collection_name)
        except Exception as exc:
            logger.error("Failed to initialize Chroma collection '%s': %s", self.collection_name, exc)
            self._collection = None
        return self._collection

    def collection_count(self) -> int:
        if self._count is not None:
            return self._count

        collection = self._get_collection()
        if collection is None:
            self._count = 0
            return self._count

        try:
            self._count = collection.count()
        except Exception as exc:
            logger.error("Failed to count Chroma documents: %s", exc)
            self._count = 0
        return self._count

    def chat(
        self,
        prompt: str,
        model: Optional[str] = None,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
    ) -> str:
        client = self._get_groq_client()
        model_name = model or self.settings.groq_model
        temp = self.settings.groq_temperature if temperature is None else temperature
        messages = [{"role": "user", "content": prompt}]
        if system_prompt:
            messages.insert(0, {"role": "system", "content": system_prompt})

        if client is None:
            missing = self.settings.missing_chat_env()
            if missing:
                logger.error("Chat unavailable (%s)", self._chat_unavailable_reason())
                return _safe_reply()

            logger.info("Using Groq HTTP fallback client for model=%s", model_name)
            return self._chat_via_http(
                prompt=prompt,
                model=model_name,
                system_prompt=system_prompt,
                temperature=temp,
            )

        try:
            response = client.chat.completions.create(
                messages=messages,
                model=model_name,
                temperature=temp,
                top_p=self.settings.groq_top_p,
            )
            content = response.choices[0].message.content
            if not content:
                logger.warning("Groq chat response had empty content; returning safe reply.")
                return _safe_reply()
            return content
        except Exception as exc:
            logger.error("Groq chat request failed for model=%s: %s", model_name, exc)
            if not self.settings.missing_chat_env():
                logger.info("Retrying chat via Groq HTTP fallback.")
                return self._chat_via_http(
                    prompt=prompt,
                    model=model_name,
                    system_prompt=system_prompt,
                    temperature=temp,
                )
            return _safe_reply()

    def run_agent(self, prompt: str, model: Optional[str] = None) -> str:
        return self._chat_with_domain_guard(prompt, model=model)

    async def run_agent_ws(self, prompt: str, model: Optional[str] = None) -> str:
        return self._chat_with_domain_guard(prompt, model=model)

    def retrieve(self, query: str, n_results: int = 4) -> List[str]:
        collection = self._get_collection()
        if collection is None:
            return []

        try:
            if self.collection_count() == 0:
                return []
            result = collection.query(query_texts=[query], n_results=n_results)
            return result.get("documents", [[]])[0]
        except Exception as exc:
            logger.error("Chroma query failed: %s", exc)
            return []

    def retrieve_ranked(self, query: str, n_results: Optional[int] = None) -> List[tuple[str, float]]:
        collection = self._get_collection()
        if collection is None:
            return []

        limit = n_results or self.settings.rag_n_results
        fetch_limit = max(limit, limit * 3)

        try:
            if self.collection_count() == 0:
                return []
            result = collection.query(query_texts=[query], n_results=fetch_limit)
            documents = result.get("documents", [[]])[0]
            distances = result.get("distances", [[]])[0]
        except Exception as exc:
            logger.error("Chroma ranked query failed: %s", exc)
            return []

        ranked: List[tuple[str, float]] = []
        seen_documents = set()
        for document, distance in zip(documents, distances):
            if not document or distance is None:
                continue
            normalized = " ".join(document.split()).strip().lower()
            if normalized in seen_documents:
                continue
            seen_documents.add(normalized)
            ranked.append((document, float(distance)))
            if len(ranked) >= limit:
                break

        distance_summary = [round(distance, 3) for _, distance in ranked]
        query_preview = query.replace("\n", " ").strip()[:80]
        logger.info(
            "RAG retrieval summary (collection=%s query=%r candidates=%s distances=%s)",
            self.collection_name,
            query_preview,
            len(ranked),
            distance_summary,
        )
        return ranked

    def _looks_like_meta_context(self, document: str) -> bool:
        lowered = document.lower()
        meta_markers = [
            "structured prompting approach",
            "content-type: application/json",
            "json body",
            "example successful response",
            "the recipe engine does not work directly",
            "langchain",
            "redis memory",
            "serp",
            "openai models",
        ]
        return any(marker in lowered for marker in meta_markers)

    def retrieve_with_threshold(self, query: str, n_results: int = 5, distance_threshold: float = 0.8) -> List[str]:
        ranked = self.retrieve_ranked(query=query, n_results=n_results)
        return [document for document, distance in ranked if distance <= distance_threshold]

    def retrieve_for_rag(
        self,
        query: str,
        n_results: Optional[int] = None,
        distance_threshold: Optional[float] = None,
        relaxed_distance_threshold: Optional[float] = None,
    ) -> List[str]:
        limit = n_results or self.settings.rag_n_results
        strict_threshold = (
            self.settings.rag_distance_threshold
            if distance_threshold is None
            else distance_threshold
        )
        relaxed_threshold = (
            self.settings.rag_relaxed_distance_threshold
            if relaxed_distance_threshold is None
            else relaxed_distance_threshold
        )

        if relaxed_threshold < strict_threshold:
            relaxed_threshold = strict_threshold

        ranked = self.retrieve_ranked(query=query, n_results=limit)
        if not ranked:
            return []

        filtered_ranked = [
            (document, distance)
            for document, distance in ranked
            if not self._looks_like_meta_context(document)
        ]
        if len(filtered_ranked) != len(ranked):
            logger.info(
                "RAG retrieval filtered low-value contexts=%s",
                len(ranked) - len(filtered_ranked),
            )
        ranked = filtered_ranked
        if not ranked:
            logger.info("RAG retrieval produced only filtered meta-contexts; treating as no context")
            return []

        strict_contexts = [document for document, distance in ranked if distance <= strict_threshold]
        if strict_contexts:
            logger.info(
                "RAG retrieval accepted strict contexts=%s threshold=%.2f",
                len(strict_contexts),
                strict_threshold,
            )
            return strict_contexts

        relaxed_contexts = [document for document, distance in ranked if distance <= relaxed_threshold]
        if relaxed_contexts:
            logger.info(
                "RAG retrieval accepted relaxed contexts=%s strict=%.2f relaxed=%.2f",
                len(relaxed_contexts),
                strict_threshold,
                relaxed_threshold,
            )
            return relaxed_contexts

        logger.info(
            "RAG retrieval found no contexts within strict=%.2f or relaxed=%.2f",
            strict_threshold,
            relaxed_threshold,
        )
        return []

    def _build_grounded_user_prompt(self, contexts: List[str], question: str) -> str:
        joined_context = "\n\n".join(contexts)
        return (
            f"CONTEXT:\n{joined_context}\n\n"
            f"QUESTION: {question}\n\n"
            "Answer using only the provided context."
        )

    def generate_with_rag(
        self,
        prompt: str,
        n_results: Optional[int] = None,
        model: Optional[str] = None,
        distance_threshold: Optional[float] = None,
        relaxed_distance_threshold: Optional[float] = None,
    ) -> str:
        contexts = self.retrieve_for_rag(
            query=prompt,
            n_results=n_results,
            distance_threshold=distance_threshold,
            relaxed_distance_threshold=relaxed_distance_threshold,
        )
        if not contexts:
            logger.warning("RAG fallback triggered - no relevant context found for: %s", prompt)
            return (
                "I'm sorry, I could not find relevant nutrition information for your question. "
                "Please try asking about specific foods, nutrients, or dietary guidelines "
                "for Australian seniors."
            )

        grounded_prompt = self._build_grounded_user_prompt(contexts, prompt)
        return self.chat(
            grounded_prompt,
            model=model,
            system_prompt=GROUNDING_SYSTEM_PROMPT,
            temperature=0.0,
        )

    def _is_weak_rag_response(self, response: str) -> bool:
        if not response:
            return True

        clean = response.strip()
        if not clean:
            return True

        lowered = clean.lower()
        hard_weak_markers = [
            "i don't know",
            "i do not know",
            "unable to verify",
            "unable to answer",
            "unable to confirm",
            "cannot verify",
            "not enough information",
            "insufficient information",
            "no relevant nutrition information",
            "knowledge base",
        ]

        if any(marker in lowered for marker in hard_weak_markers):
            return True

        very_short = len(clean) < 20
        has_nutritional_signal = bool(re.search(r"\d|%|serving|vegetable|fruit|diet|nutrition|guideline", clean, re.IGNORECASE))
        return very_short and not has_nutritional_signal

    def chat_with_rag_fallback(self, prompt: str, model: Optional[str] = None) -> str:
        logger.info("AI07 chat_with_rag_fallback called (prompt_len=%s)", len(prompt or ""))
        try:
            contexts = self.retrieve_for_rag(
                query=prompt,
                n_results=self.settings.rag_n_results,
                distance_threshold=self.settings.rag_distance_threshold,
                relaxed_distance_threshold=self.settings.rag_relaxed_distance_threshold,
            )
            logger.info(
                "AI07 retrieval complete (contexts=%s strict=%.2f relaxed=%.2f)",
                len(contexts),
                self.settings.rag_distance_threshold,
                self.settings.rag_relaxed_distance_threshold,
            )

            # AI07 step 1: no contexts -> fallback to regular chat
            if not contexts:
                logger.info("AI07 fallback to chat (no RAG context)")
                return self._chat_with_domain_guard(prompt, model=model)

            # AI07 step 2: generate RAG answer when contexts exist
            grounded_prompt = self._build_grounded_user_prompt(contexts, prompt)
            rag_response = self.chat(
                grounded_prompt,
                model=model,
                system_prompt=GROUNDING_SYSTEM_PROMPT,
                temperature=0.0,
            )

            # AI07 step 3: weak RAG response -> fallback to regular chat
            if self._is_weak_rag_response(rag_response):
                logger.info("AI07 fallback to chat (weak RAG response)")
                fallback = self._chat_with_domain_guard(prompt, model=model)
                if fallback == _safe_reply():
                    logger.error("AI07 fallback chat also unavailable. Root issue likely: %s", self._chat_unavailable_reason())
                return fallback

            return rag_response
        except Exception:
            logger.exception("AI07 RAG fallback pipeline failed, using chat fallback")
            return self._chat_with_domain_guard(prompt, model=model)

    def add_documents(self, docs: List[str]) -> int:
        collection = self._get_collection()
        if collection is None:
            logger.warning("Chroma collection missing; cannot add documents.")
            return self.collection_count()

        start = self.collection_count()
        for offset, document in enumerate(docs):
            try:
                collection.upsert(ids=[f"id{start + offset}"], documents=[document])
            except Exception as exc:
                logger.error("Failed to upsert document %s: %s", start + offset, exc)

        self._count = None
        return self.collection_count()

    def run_agent_dynamic(self, prompt: str, model: Optional[str] = None) -> Dict[str, Any]:
        response = self.generate_with_rag(prompt, model=model) if self._get_collection() else self.chat(prompt, model=model)
        try:
            data = json.loads(response)
        except json.JSONDecodeError:
            return {"calories": None, "recommendation": response}

        data.setdefault("calories", None)
        data.setdefault("recommendation", "")
        return data


STRICT_SCHEMA_EXAMPLE = {
    "suggestion": "string",
    "weekly_plan": [
        {
            "week": 1,
            "target_calories_per_day": 2000,
            "focus": "string",
            "workouts": ["string"],
            "meal_notes": "string",
            "reminders": ["string"],
        }
    ],
    "progress_analysis": "string",
}

ALLOWED_FOCUS = {"Weight Loss", "Muscle Gain", "Endurance"}
CAL_MIN = 1200
CAL_MAX = 3500


def _clean_str(value: Any) -> str:
    return str(value).strip()


def _clean_str_list(values: Any) -> List[str]:
    if isinstance(values, list):
        return [_clean_str(item) for item in values if str(item).strip()]
    if isinstance(values, str) and values.strip():
        return [_clean_str(values)]
    return []


def _coerce_int(value: Any, default: int) -> int:
    try:
        parsed = int(float(value))
        return max(CAL_MIN, min(CAL_MAX, parsed))
    except Exception:
        return default


def _normalize_week_item(index: int, item: Dict[str, Any]) -> Dict[str, Any]:
    focus = item.get("focus", "Weight Loss")
    focus = focus if focus in ALLOWED_FOCUS else "Weight Loss"
    workouts = _clean_str_list(item.get("workouts", []))
    meal_notes = _clean_str(item.get("meal_notes", ""))
    reminders = _clean_str_list(item.get("reminders", []))

    if workouts and ":" not in workouts[0]:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        workouts = [f"{days[offset % 7]}: {workout}" for offset, workout in enumerate(workouts)]

    return {
        "week": index + 1,
        "target_calories_per_day": _coerce_int(item.get("target_calories_per_day", 1900), 1900),
        "focus": focus,
        "workouts": workouts[:7] or [
            "Monday: 30 minutes brisk walking",
            "Wednesday: Rest day",
            "Friday: 20 minutes strength training",
        ],
        "meal_notes": meal_notes or "Eat 3 main meals and 2 snacks, include lean protein, whole grains, and healthy fats.",
        "reminders": reminders[:6] or ["Drink 8 glasses of water daily", "Limit sugary drinks and fast food"],
    }


def _force_json(text: str) -> Dict[str, Any]:
    match = re.search(r"\{[\s\S]*\}\s*$", text)
    raw = match.group(0) if match else text
    raw = re.sub(r",(\s*[\]}])", r"\1", raw)

    try:
        data = json.loads(raw)
    except Exception:
        return {"suggestion": str(text).strip(), "weekly_plan": [], "progress_analysis": ""}

    if isinstance(data.get("suggestion"), str) and "{" in data["suggestion"] and "}" in data["suggestion"]:
        try:
            inner = json.loads(data["suggestion"])
        except Exception:
            inner = None
        if isinstance(inner, dict):
            for key in ("suggestion", "weekly_plan", "progress_analysis"):
                if key in inner and key not in data:
                    data[key] = inner[key]

    return data


def _enforce_schema(data: Dict[str, Any], num_weeks: int) -> Dict[str, Any]:
    suggestion = _clean_str(data.get("suggestion", ""))
    if "{" in suggestion and "}" in suggestion:
        suggestion = "Increase daily water intake to 2 liters and consume 5 servings of fruits and vegetables."

    weekly_plan = data.get("weekly_plan", [])
    weekly_plan = weekly_plan if isinstance(weekly_plan, list) else []

    normalized_items = []
    for index in range(num_weeks):
        base = weekly_plan[index] if index < len(weekly_plan) and isinstance(weekly_plan[index], dict) else {}
        normalized_items.append(_normalize_week_item(index, base))

    progress_analysis = _clean_str(data.get("progress_analysis", ""))
    if not progress_analysis:
        progress_analysis = "Progress trend: steady adherence recommended. Track weight, BMI, and blood pressure weekly."

    return {
        "suggestion": suggestion,
        "weekly_plan": normalized_items,
        "progress_analysis": progress_analysis,
    }


class HealthPlanService:
    def __init__(self, backend: Optional[GroqChromaBackend] = None):
        self.backend = backend or GroqChromaBackend()

    def _build_prompt(
        self,
        analyzed_health_condition: Dict[str, Any],
        n_results: int = 4,
        num_weeks: int = 4,
    ) -> str:
        condition_json = json.dumps(analyzed_health_condition, ensure_ascii=False, indent=2)
        schema_json = json.dumps(STRICT_SCHEMA_EXAMPLE, ensure_ascii=False, indent=2)

        user_task = (
            f"Generate a {num_weeks}-week diet & workout plan and analyze progress across reports. "
            "If multiple reports are given, compare them and include improvement/no-improvement notes "
            "in the 'progress_analysis' field. Return STRICT JSON only."
        )
        contexts = self.backend.retrieve(
            query=f"{user_task}\nUser condition history: {condition_json}",
            n_results=n_results,
        )
        joined_context = "\n- " + "\n- ".join(contexts) if contexts else ""

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
            f"{joined_context}\n"
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
            analyzed_health_condition=analyzed_health_condition,
            n_results=n_results,
            num_weeks=num_weeks,
        )

        client = self.backend._get_groq_client()
        if client is None:
            raise RuntimeError("Groq backend is not configured.")

        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You output strictly valid JSON."},
                {"role": "user", "content": prompt},
            ],
            model=self.backend.settings.groq_model,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        output = (response.choices[0].message.content or "").strip()
        return _enforce_schema(_force_json(output), num_weeks=num_weeks)
