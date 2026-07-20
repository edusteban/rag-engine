from langchain_chroma import Chroma
from langchain_core.documents import Document
 
from langchain_ollama import OllamaEmbeddings

from config import EMBEDDING_MODEL, CHROMA_PATH, CHROMA_COLLECTION_NAME, CHUNK_OVERLAP, CHUNK_SIZE

def get_current_config() -> dict:
    return {
        "embedding_model": EMBEDDING_MODEL,
        "chunk_size": CHUNK_SIZE,
        "chunk_overlap": CHUNK_OVERLAP
    }


def get_vectorstore() -> Chroma:
    embeddings = OllamaEmbeddings(
        model=EMBEDDING_MODEL
    )
    vectorstore = Chroma(
        collection_name=CHROMA_COLLECTION_NAME,
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings,
        collection_metadata=get_current_config()
    )

    return vectorstore

def reset_vectorstore() -> None:
    vectorstore = get_vectorstore()

    vectorstore.delete_collection()

def vectorstore_config_changed(vectorstore: Chroma) -> bool:
    stored_metadata = vectorstore._collection.metadata

    return stored_metadata != get_current_config()

def delete_documents(vectorstore: Chroma, sources: set[str]) -> None:
    if not sources:
        return

    vectorstore.delete(
        where={
            "source": {
                "$in": list(sources)
            }
        }
    )

def add_documents(vectorstore: Chroma, documents: list[Document]) -> None:
    if not documents:
        return

    vectorstore.add_documents(documents)