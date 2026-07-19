from src.retrieval.retriever import retrieve
from src.generation.prompt import build_prompt
from src.generation.llm import get_llm



def generate(question: str) -> str:
    documents = retrieve(question)

    messages = build_prompt(context_documents=documents, question=question)

    llm = get_llm()

    response = llm.invoke(messages)

    return response.content