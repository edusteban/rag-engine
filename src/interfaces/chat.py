from src.generation.generator import generate


def chat():
    print("RAG Engine ready")
    print("Type 'exit' to quit\n")
    
    while True:
        question = input("> ")
        
        if not question.strip():
            continue

        if question.lower() == "exit":
            break


        answer = generate(question)

        print("\nAnswer:")
        print(answer)
        print()