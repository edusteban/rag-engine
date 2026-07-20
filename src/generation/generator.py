from src.retrieval.retriever import retrieve
from src.generation.prompt import build_prompt

from langchain_ollama import ChatOllama
from collections.abc import Generator



def generate(question: str, llm: ChatOllama) -> str:
    documents = retrieve(question)

    prompt = build_prompt(context_documents=documents, question=question)

    response = llm.invoke(prompt)

    return response.content

def stream_generate(question: str, llm: ChatOllama, debug: bool) -> Generator:
    print("Searching documents...", flush=True)
    documents = retrieve(question)

    print("Generating answer...", flush=True)

    prompt = build_prompt(
        context_documents=documents,
        question=question
    )

    if debug:
        print("\n========== PROMPT ==========")
        print(prompt.to_string())
        print("==============================\n")

    for chunk in llm.stream(prompt):
        yield chunk.content