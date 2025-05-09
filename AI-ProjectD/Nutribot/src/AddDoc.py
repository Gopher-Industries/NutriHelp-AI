import tempfile
import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from fastapi import UploadFile
import fitz  # PyMuPDF
from langchain.schema import Document

class AddDocClass:
    def __init__(self) -> None:
        self.embeddings = OpenAIEmbeddings()
        self.loader = lambda urls: WebBaseLoader(urls)
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=50)

        # Create a persistent path inside the project folder
        self.persist_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "qdrant_data"))
        os.makedirs(self.persist_dir, exist_ok=True)  # Ensure folder exists

        client = QdrantClient(path=self.persist_dir)
        collection_name = "local_documents_demo"

        # Create collection if not exists
        collections = client.get_collections().collections
        if not any(collection.name == collection_name for collection in collections):
            client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
            )

        self.qdrant = QdrantVectorStore(
            client=client,
            collection_name=collection_name,
            embedding=self.embeddings,
        )

    async def add_urls(self, urls: list) -> dict:
        loader = self.loader(urls)
        docs = loader.load()
        documents = self.splitter.split_documents(docs)
        self.qdrant.add_documents(documents)
        return {"ok": "URLs added successfully"}
    
    async def add_pdf(self, file: UploadFile) -> dict:
        # Read the content of a PDF file
        content = await file.read()
        text = ""
        with fitz.open(stream=content, filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()

        # Convert into Document objects and split into segments
        docs = [Document(page_content=text)]
        split_docs = self.splitter.split_documents(docs)

        # Add to the Qdrant vector database
        self.qdrant.add_documents(split_docs)
        return {"ok": f"{file.filename} uploaded and indexed."}