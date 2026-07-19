import argparse

from src.ingestion.ingester import ingest
from src.interfaces.chat import chat

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