from src.generation.generator import stream_generate
from src.generation.llm import get_llm


def chat(debug: bool = False):
    llm = get_llm()
    print("RAG Engine ready")
    print("Type 'exit' to quit\n")

    while True:
        question = input("> ")
        
        if not question.strip():
            continue

        if question.lower() == "exit":
            break
        

        for token in stream_generate(question, llm, debug=debug):
            print(token, end="", flush=True)

        print("\n")