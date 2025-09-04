from dotenv import load_dotenv
import os

try:
    import chromadb
except:
    chromadb = None

try:
    from groq import Groq
except:
    Groq = None


class AgentClass:
    def __init__(self, collection_name="aus_food_nutrition"):
        load_dotenv()

        # Init Groq
        groq_key = os.environ.get('GROQ_API_KEY')

        self.llm_client = Groq(api_key=groq_key) if Groq and groq_key else None

        # Init Chroma
        chroma_key = os.environ.get("CHROMA_API_KEY")
        if chromadb and chroma_key:
            try:
                client = chromadb.CloudClient(
                    tenant="a0123436-2e87-4752-8983-73168aafe2e9",
                    database="nutribot",
                    api_key=chroma_key,
                )
                self.collection = client.get_or_create_collection(name=collection_name)
            except:
                self.collection = None
        else:
            self.collection = None

        self.count = self.collection.count() if self.collection else 0

    def _safe_reply(self, prompt: str) -> str:
        return f"I'm currently unavailable."

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

    def generate_with_rag(self, prompt, n_results=5, model="llama-3.1-8b-instant"):
        res = self.collection.query(query_texts=[prompt], n_results=n_results)
        retrieved_contexts = res.get("documents", [[]])[0]
        prompt = prompt + f"\nUse this as context for answering: {retrieved_contexts}"
        return self._chat(prompt, model)
    
    def add_documents(self, docs):
        for doc in docs:
            _id = f"id{self.count}"
            self.collection.upsert(ids=[_id], documents=[doc])
            self.count += 1