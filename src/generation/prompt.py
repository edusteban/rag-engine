from langchain_core.prompt_values import ChatPromptValue
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document


def build_prompt(context_documents: list[Document], question: str) -> ChatPromptValue:
    context = "\n\n".join(
        f"Source: {doc.metadata['source']}\n{doc.page_content}"
        for doc in context_documents
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant. Answer the user's questions using only the provided context. "
                "If the answer is not in the context, say that you don't know.",
            ),
            (
                "human",
                "Context:\n{context}\n\nQuestion:\n{question}",
            ),
        ]
    )

    return prompt.invoke(
        {
            "context": context,
            "question": question,
        }
    )