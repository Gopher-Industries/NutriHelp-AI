from langchain.agents import AgentExecutor,create_tool_calling_agent,tool
from langchain_community.utilities import SerpAPIWrapper
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate   
import os
import requests
from dotenv import load_dotenv
load_dotenv()
serpapi_key = os.getenv("SERPAPI_API_KEY")
ninja_key = os.getenv("NINJA_API_KEY")

@tool
def search(query: str) -> str:
    """This tool is only used when you need to know real-time information or something you don't know."""
    serp = SerpAPIWrapper()
    return serp.run(query)

@tool
def get_info_from_local(query: str) -> str:
    """This tool is used to retrieve nutrition-related content from the local Qdrant vector store."""
    import os
    from langchain_qdrant import QdrantVectorStore
    from qdrant_client import QdrantClient
    from langchain_openai import OpenAIEmbeddings

    # Use the persistent Qdrant database directory within the project
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "qdrant_data"))
    client = QdrantClient(path=db_path)

    retriever_qr = QdrantVectorStore(client, "local_documents_demo", OpenAIEmbeddings())
    retriever = retriever_qr.as_retriever(search_type="mmr")
    results = retriever.get_relevant_documents(query)

    if not results:
        return "No relevant documents found."

    return "\n\n".join([doc.page_content[:500] for doc in results[:3]])


@tool
def get_nutrition_info(food: str) -> str:
    """Returns the nutritional information of the specified food per 100 grams, including calories, protein, carbs, and fat."""
    try:
        response = requests.get(
            f"https://api.api-ninjas.com/v1/nutrition?query={food}",
            headers={"X-Api-Key": os.environ["NINJA_API_KEY"]}
        )
        if response.status_code == 200:
            data = response.json()
            if not data:
                return f"No nutrition information found for {food}."
            item = data[0]
            return (
                f"Nutrition info per 100g of {food}:\n"
                f"- Calories: {item['calories']} kcal\n"
                f"- Protein: {item['protein_g']} g\n"
                f"- Carbohydrates: {item['carbohydrates_total_g']} g\n"
                f"- Fat: {item['fat_total_g']} g"
            )
        else:
            return "Request failed. Please check API usage limits or request format."
    except Exception as e:
        return f"An error occurred during the query: {str(e)}"

