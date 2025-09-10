# nutrihelp_ai/agents/agent_groq.py
from dotenv import load_dotenv
import os

try:
    import chromadb
except Exception:
    chromadb = None

try:
    from groq import Groq
except Exception:
    Groq = None

class AgentGroq:
    def __init__(self, collection_name="aus_food_nutrition"):
        load_dotenv()
        groq_key = os.getenv("GROQ_API_KEY")
        self.llm_client = Groq(api_key=groq_key) if Groq and groq_key else None

        chroma_key = os.getenv("CHROMA_API_KEY")
        if chromadb and chroma_key:
            try:
                client = chromadb.CloudClient(
                    tenant="a0123436-2e87-4752-8983-73168aafe2e9",
                    database="nutribot",
                    api_key=chroma_key,
                )
                self.collection = client.get_or_create_collection(name=collection_name)
            except Exception:
                self.collection = None
        else:
            self.collection = None

        self.count = self.collection.count() if self.collection else 0

    def _safe_reply(self, prompt: str) -> str:
        return f"[offline] {prompt}"

    def _chat(self, prompt: str, model: str):
        if not self.llm_client:
            return self._safe_reply(prompt)
        try:
            r = self.llm_client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=model,
            )
            return r.choices[0].message.content
        except Exception:
            return self._safe_reply(prompt)

    def run_agent(self, prompt, model="llama-3.1-8b-instant"):
        return self._chat(prompt, model)

    async def run_agent_ws(self, prompt, model="llama-3.1-8b-instant"):
        return self._chat(prompt, model)

    def generate_with_rag(self, prompt, model="llama-3.1-8b-instant"):
        return self._chat(prompt, model)
