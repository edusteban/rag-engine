import argparse

from src.ingestion.ingester import ingest
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

def main():

    parser = argparse.ArgumentParser(
        description="RAG Engine"
    )

    parser.add_argument(
        "command",
        choices=["ingest", "chat"]
    )

    args = parser.parse_args()

    if args.command == "ingest":
        ingest()
        print("Documents ingested successfully")

    elif args.command == "chat":
        chat()

if __name__ == "__main__":
    main()