from langchain_core.documents import Document

from src.vectorstore.chroma import get_vectorstore
from config import RETRIEVER_TOP_K

def retrieve(query: str) -> list[Document]:
    vectorstore = get_vectorstore()

    if vectorstore._collection.count() == 0:
        raise RuntimeError(
            "Vectorstore is empty. Run ingestion first."
        )
    
    results = vectorstore.similarity_search(
        query,
        k=RETRIEVER_TOP_K
    )

    return results