from src.retrieval.retriever import retrieve
from src.generation.prompt import build_prompt

from langchain_ollama import ChatOllama
from collections.abc import Generator



def generate(question: str, llm: ChatOllama) -> str:
    documents = retrieve(question)

    messages = build_prompt(context_documents=documents, question=question)

    response = llm.invoke(messages)

    return response.content

def stream_generate(question: str, llm: ChatOllama) -> Generator:
    print("Searching documents...", flush=True)
    documents = retrieve(question)

    print("Generating answer...", flush=True)

    messages = build_prompt(
        context_documents=documents,
        question=question
    )

    for chunk in llm.stream(messages):
        yield chunk.content