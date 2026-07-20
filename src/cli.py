import argparse

from src.ingestion.ingester import ingest
from src.interfaces.chat import chat
from src.vectorstore.chroma import reset_vectorstore


def add_ingest_parser(subparsers) -> None:
    subparsers.add_parser(
        "ingest",
        help="Ingest documents into the vector store.",
    )


def add_chat_parser(subparsers) -> None:
    chat_parser = subparsers.add_parser(
        "chat",
        help="Start an interactive chat session.",
    )

    chat_parser.add_argument(
        "--debug",
        action="store_true",
        help="Show retrieval and prompt information.",
    )


def add_reset_parser(subparsers) -> None:
    reset_parser = subparsers.add_parser(
        "reset",
        help="Delete the vector store.",
    )

    reset_parser.add_argument(
        "--force",
        action="store_true",
        help="Skip confirmation prompt.",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="RAG Engine"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    add_ingest_parser(subparsers)
    add_chat_parser(subparsers)
    add_reset_parser(subparsers)

    return parser

def reset(skip_confirmation: bool = False):
    if not skip_confirmation:
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
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "ingest":
        ingest()
        print("Documents ingested successfully")

    elif args.command == "chat":
        chat(debug=args.debug)

    elif args.command == "reset":
        reset(skip_confirmation=args.force)


if __name__ == "__main__":
    main()