import argparse

from src.ingestion.ingester import ingest
from src.interfaces.chat import chat
from src.vectorstore.chroma import reset_vectorstore


def reset():
    confirmation = input(
        "This will delete the current vectorstore. "
        "Are you sure? [y/N]: "
    )
    if confirmation.lower() != "y":
        print("Reset cancelled.")
        return
    
    reset_vectorstore()
    print("Vectorstore reset successfully.")

def main():

    parser = argparse.ArgumentParser(
        description="RAG Engine"
    )

    parser.add_argument(
        "command",
        choices=["ingest", "chat", "reset"]
    )

    args = parser.parse_args()

    if args.command == "ingest":
        ingest()
        print("Documents ingested successfully")

    elif args.command == "chat":
        chat()

    elif args.command == "reset":
        reset()

if __name__ == "__main__":
    main()