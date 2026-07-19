from langchain_chroma import Chroma
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