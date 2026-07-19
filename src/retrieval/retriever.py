from langchain_core.documents import Document

from src.vectorstore.chroma import get_vectorstore


def retrieve(query: str, k: int = 5) -> list[Document]:
    vectorstore = get_vectorstore()

    results = vectorstore.similarity_search(
        query,
        k=k
    )

    return results