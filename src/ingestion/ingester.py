from langchain_core.documents import Document

from src.ingestion.loader import load_documents
from src.ingestion.splitter import split_documents
from src.vectorstore.chroma import get_vectorstore

def ingest() -> None:
    documents = load_documents()
    chunks = split_documents(documents)

    vectorstore = get_vectorstore()

    vectorstore.reset_collection()
    

    vectorstore.add_documents(chunks)
    

