# nutrihelp_ai/agents/agent_hf.py
import os
from typing import Optional, Dict, Any
from dotenv import load_dotenv

try:
    import chromadb
except Exception:
    chromadb = None

import httpx

def _alpaca_template(instruction: str, input_: str = "") -> str:
    if input_:
        return f"Instruction: {instruction}\nInput: {input_}\nResponse:"
    return f"Instruction: {instruction}\nResponse:"

class AgentHF:
    """
    Calls your Hugging Face Space hosting the fine-tuned NutriBot.
    Keep the same public methods as your original AgentClass.
    """
    def __init__(self, collection_name: str = "aus_food_nutrition"):
        load_dotenv()

        # HF Space base URL, e.g. https://ngtuanphong-nutribot.hf.space
        self.api_base = os.getenv("NUTRIBOT_API_URL", "http://localhost:7860")
        # Optional Bearer token if your Space requires it (private Space)
        self.api_key = os.getenv("NUTRIBOT_API_KEY", "")
        self.headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}

        # Optional: Chroma Cloud (same behavior as your old class)
        chroma_key = os.getenv("CHROMA_API_KEY")
        if chromadb and chroma_key:
            try:
                client = chromadb.CloudClient(
                    tenant=os.getenv("CHROMA_TENANT", "a0123436-2e87-4752-8983-73168aafe2e9"),
                    database=os.getenv("CHROMA_DATABASE", "nutribot"),
                    api_key=chroma_key,
                )
                self.collection = client.get_or_create_collection(name=collection_name)
            except Exception:
                self.collection = None
        else:
            self.collection = None

        self.count = self.collection.count() if self.collection else 0

        # default decoding
        self.default_gen = {
            "max_tokens": int(os.getenv("NUTRIBOT_MAX_TOKENS", "384")),
            "temperature": float(os.getenv("NUTRIBOT_TEMPERATURE", "0.7")),
            "top_p": float(os.getenv("NUTRIBOT_TOP_P", "0.9")),
            "repetition_penalty": float(os.getenv("NUTRIBOT_REP_PENALTY", "1.05")),
        }

        # choose "alpaca" or "chat"
        self.mode = os.getenv("NUTRIBOT_MODE", "alpaca").lower()

    def _safe_reply(self, prompt: str) -> str:
        return f"[offline] {prompt}"

    def _chat_alpaca(self, instruction: str, input_text: str = "", gen: Optional[Dict[str, Any]] = None) -> str:
        payload = dict(self.default_gen)
        if gen:
            payload.update({k: v for k, v in gen.items() if k in self.default_gen})
        payload.update({"instruction": instruction, "input": input_text})
        try:
            r = httpx.post(
                f"{self.api_base}/v1/alpaca/completions",
                json=payload,
                headers=self.headers,
                timeout=int(os.getenv("NUTRIBOT_TIMEOUT", "60")),
            )
            r.raise_for_status()
            data = r.json()
            return data["choices"][0]["text"]
        except Exception:
            return self._safe_reply(_alpaca_template(instruction, input_text))

    def _chat_standard(self, prompt: str, gen: Optional[Dict[str, Any]] = None) -> str:
        payload = dict(self.default_gen)
        if gen:
            payload.update({k: v for k, v in gen.items() if k in self.default_gen})
        payload.update({"messages": [{"role": "user", "content": prompt}]})
        try:
            r = httpx.post(
                f"{self.api_base}/v1/chat/completions",
                json=payload,
                headers=self.headers,
                timeout=int(os.getenv("NUTRIBOT_TIMEOUT", "60")),
            )
            r.raise_for_status()
            data = r.json()
            return data["choices"][0]["message"]["content"]
        except Exception:
            return self._safe_reply(prompt)

    def _chat(self, prompt: str, model: Optional[str], **gen) -> str:
        # Use the Alpaca route by default to match training
        if self.mode == "alpaca":
            return self._chat_alpaca(instruction=prompt, input_text="", gen=gen)
        return self._chat_standard(prompt=prompt, gen=gen)

    def run_agent(self, prompt: str, model: str = "ft-tinyllama-1.1b", **gen) -> str:
        return self._chat(prompt, model, **gen)

    async def run_agent_ws(self, prompt: str, model: str = "ft-tinyllama-1.1b", **gen) -> str:
        # simple async wrapper using httpx.AsyncClient if you need websockets later
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._chat, prompt, model, **gen)

    def generate_with_rag(self, prompt: str, model: str = "ft-tinyllama-1.1b", **gen) -> str:
        # For strict alignment with training, keep prompt as the instruction body
        # If you later inject retrieval, add it to the Alpaca "Input:" field:
        # return self._chat_alpaca(instruction=prompt, input_text=context, gen=gen)
        return self._chat(prompt, model, **gen)
