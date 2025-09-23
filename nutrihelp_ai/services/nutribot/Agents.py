from dotenv import load_dotenv
import os
import logging
import json

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
load_dotenv()

try:
    import chromadb
except Exception as e:
    chromadb = None
    logging.warning("chromadb import failed: %s", e)

try:
    from groq import Groq
except Exception as e:
    Groq = None
    logging.warning("groq import failed: %s", e)

def _mask_presence(v: str | None) -> str:
    """Return a safe presence string."""
    if not v:
        return "(missing)"
    return f"loaded ({len(v)} chars)"


class AgentClass:
    def __init__(self, collection_name="aus_food_nutrition"):
        groq_key = os.getenv("GROQ_API_KEY")
        chroma_key = os.getenv("CHROMA_API_KEY")

        logging.info("GROQ_API_KEY: %s", _mask_presence(groq_key))
        logging.info("CHROMA_API_KEY: %s", _mask_presence(chroma_key))

        # --- Init Groq ---
        self.llm_client = None
        if Groq and groq_key:
            try:
                self.llm_client = Groq(api_key=groq_key)
            except Exception as e:
                logging.error("Failed to init Groq client: %s", e)

        # --- Init Chroma ---
        self.collection = None
        if chromadb and chroma_key:
            try:
                client = chromadb.CloudClient(
                    tenant="a0123436-2e87-4752-8983-73168aafe2e9",
                    database="nutribot",
                    api_key=chroma_key,
                )
                self.collection = client.get_or_create_collection(name=collection_name)
            except Exception as e:
                logging.error("Failed to init Chroma client/collection: %s", e)

        self.count = self.collection.count() if self.collection else 0

    def _safe_reply(self, prompt: str) -> str:
        return f"Nutribot is currently unavailable."

    def _chat(self, prompt: str, model: str):
        if not self.llm_client:
            return self._safe_reply(prompt)
        try:
            r = self.llm_client.chat.completions.create(
                messages=[
                    {"role": "user", "content": prompt},
                    ],
                model=model,
            )
            return r.choices[0].message.content
        except:
            return self._safe_reply(prompt)

    def run_agent(self, prompt, model="llama-3.1-8b-instant"):
        return self._chat(prompt, model)

    async def run_agent_ws(self, prompt, model="llama-3.1-8b-instant"):
        return self._chat(prompt, model)

    def generate_with_rag(self, prompt, n_results=5, model="llama-3.1-8b-instant", distance_threshold=0.8):
        if not self.collection:
            logging.warning("Chroma collection missing; falling back to plain chat.")
            return self._chat(prompt, model)
        
        try:
            res = self.collection.query(query_texts=[prompt], n_results=n_results)
            docs = res.get("documents", [[]])[0]
            distances = res.get("distances", [[]])[0]

            filtered_docs = []
            for doc, distance in zip(docs, distances):
                if distance <= distance_threshold:
                    filtered_docs.append(doc)
            retrieved_contexts = filtered_docs if filtered_docs else []
        except Exception as e:
            logging.error("Chroma query failed: %s", e)
            retrieved_contexts = []
        prompt = prompt + f"\nUse this as context for answering: {retrieved_contexts}"
        return self._chat(prompt, model)
    
    def add_documents(self, docs):
        if not self.collection:
            logging.warning("Chroma collection missing; cannot add documents.")
            return
        for doc in docs:
            _id = f"id{self.count}"
            try:
                self.collection.upsert(ids=[_id], documents=[doc])
                self.count += 1
            except Exception as e:
                logging.error("Failed to upsert doc %s: %s", _id, e)


        # -------------------------
    # Food image classfier 
    # -------------------------
    def run_agent_dynamic(self, prompt, model="llama-3.1-8b-instant"):
        """
        Runs the LLM and ensures the output is a dict with 'calories' and 'recommendation'.
        Falls back to default structure if parsing fails.
        """
        # Use RAG if Chroma collection exists
        response_str = self.generate_with_rag(prompt, model=model) if self.collection else self.run_agent(prompt, model=model)

        try:
            # Try parsing JSON output from LLM
            nutrition_data = json.loads(response_str)
            # Ensure keys exist
            nutrition_data.setdefault("calories", None)
            nutrition_data.setdefault("recommendation", "")
            return nutrition_data
        except json.JSONDecodeError:
            # Fallback: return the raw text as 'recommendation'
            return {"calories": None, "recommendation": response_str}
