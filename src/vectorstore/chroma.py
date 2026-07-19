from langchain_chroma import Chroma
from langchain_core.documents import Document
 
from langchain_ollama import OllamaEmbeddings

from config import EMBEDDING_MODEL, CHROMA_PATH, CHROMA_COLLECTION_NAME

def get_vectorstore() -> Chroma:
    embeddings = OllamaEmbeddings(
        model=EMBEDDING_MODEL
    )
    vectorstore = Chroma(
        collection_name=CHROMA_COLLECTION_NAME,
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )

    return vectorstore

def delete_documents(vectorstore: Chroma, sources: set[str]) -> None:
    for source in sources:
        vectorstore.delete(
            where={
                "source": source
            }
        )

def add_documents(vectorstore: Chroma, documents: list[Document]) -> None:
    if not documents:
        return

    vectorstore.add_documents(documents)