from langchain_ollama import ChatOllama
from config import LLM_MODEL, LLM_TEMPERATURE

def get_llm() -> ChatOllama:
    return ChatOllama(
        model=LLM_MODEL,
        temperature=LLM_TEMPERATURE
    )
    