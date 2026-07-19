from langchain_core.documents import Document

from src.vectorstore.chroma import get_vectorstore


def retrieve(query: str, k: int = 5) -> list[Document]:
    vectorstore = get_vectorstore()

    if vectorstore._collection.count() == 0:
        raise RuntimeError(
            "Vectorstore is empty. Run ingestion first."
        )
    
    results = vectorstore.similarity_search(
        query,
        k=k
    )

    return results