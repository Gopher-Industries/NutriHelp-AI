# NutriHelp-AI

FastAPI service for the NutriHelp project.

The active AI chatbot runtime in this repository is `Groq + Chroma`. Older Hugging Face, OpenAI, Redis, and Qdrant references still exist in legacy modules, but they are not the default runtime path.

## Active Backend Path

The current active backend path is:

- `run.py`
- `nutrihelp_ai/main.py`
- `nutrihelp_ai/services/active_ai_backend.py`

Runtime usage:

- Chatbot routes use `GroqChromaBackend`
- Health-plan routes use `HealthPlanService`
- Image nutrition enrichment uses `GroqChromaBackend`

Legacy compatibility modules:

- `nutrihelp_ai/services/nutribot/`
- `nutrihelp_ai/services/nutribot_rag.py`
- `nutrihelp_ai/agents/agent_hf.py`

These legacy modules are compatibility shims or older implementations. New backend changes should target `nutrihelp_ai/services/active_ai_backend.py`.

## Setup

### 1. Clone

```bash
git clone https://github.com/Gopher-Industries/NutriHelp-AI.git
cd NutriHelp-AI
```

### 2. Create a virtual environment

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create `.env` from `.env.example`:

```bash
cp .env.example .env
```

Required for the active Groq + Chroma backend:

```env
GROQ_API_KEY=
CHROMA_MODE=cloud
CHROMA_API_KEY=
CHROMA_TENANT=
CHROMA_DATABASE=
RAG_COLLECTION=aus_food_nutrition
```

Optional:

```env
GROQ_MODEL=llama-3.1-8b-instant
CHROMA_PATH=./.chroma
PORT=8000
```

Notes:

- Use `CHROMA_MODE=cloud` for Chroma Cloud.
- Use `CHROMA_MODE=local` with `CHROMA_PATH` for a local persistent Chroma store.
- `RAG_COLLECTION` should match the collection that contains the nutrition documents used for retrieval.

### 5. Run the API

```bash
python run.py
```

Local URLs:

- API root: `http://127.0.0.1:8000/`
- Health check: `http://127.0.0.1:8000/healthz`
- Swagger docs: `http://127.0.0.1:8000/docs`

## Main Endpoints

- `POST /ai-model/chatbot/chat`
- `POST /ai-model/chatbot/chat_with_rag`
- `POST /ai-model/medical-report/retrieve`
- `POST /ai-model/medical-report/plan/generate`
- `POST /ai-model/image-analysis/image-analysis`
- `POST /ai-model/image-analysis/multi-image-analysis`
- `GET /ai-model/chatbot-finetune/healthz`
- `POST /ai-model/chatbot-finetune/chat`

## Environment Variables

### Active chatbot runtime

- `GROQ_API_KEY`: required for Groq chat completions
- `GROQ_MODEL`: optional default model name
- `CHROMA_MODE`: `cloud` or `local`
- `CHROMA_API_KEY`: required when `CHROMA_MODE=cloud`
- `CHROMA_TENANT`: required when `CHROMA_MODE=cloud`
- `CHROMA_DATABASE`: required when `CHROMA_MODE=cloud`
- `CHROMA_PATH`: used when `CHROMA_MODE=local`
- `RAG_COLLECTION`: Chroma collection used by chat and health-plan retrieval
- `PORT`: optional API port override

### Other env vars used elsewhere in the repo

These are not part of the active Groq + Chroma chatbot runtime:

- `JWT_TOKEN`
- `SUPABASE_URL`
- `SUPABASE_ANON_KEY`
- `GMAIL_USER`
- `GMAIL_APP_PASSWORD`
- `HF_SPACE_URL`
- `HF_SPACE_KEY`

## Maintenance Notes

- Keep chatbot backend changes inside `nutrihelp_ai/services/active_ai_backend.py`.
- Treat `nutrihelp_ai/services/nutribot/` and `nutrihelp_ai/services/nutribot_rag.py` as legacy compatibility layers.
- Do not add new setup guidance for OpenAI, Redis, or Qdrant unless those become active runtime dependencies again.
