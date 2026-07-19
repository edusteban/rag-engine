from src.ingestion.ingester import ingest
from src.generation.generator import generate


def main():
    ingest()

    while True:
        question = input("> ")

        answer = generate(question)

        print(answer)


if __name__ == "__main__":
    main()