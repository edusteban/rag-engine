# RAG Engine

A production-oriented Retrieval-Augmented Generation (RAG) engine built with **LangChain**, **ChromaDB** and **Ollama**.

This project implements a complete local RAG pipeline with incremental document ingestion, semantic retrieval and LLM-based answer generation.

## Features

- Document ingestion pipeline
- Configurable document chunking
- Local embeddings generation with Ollama
- Persistent vector storage using ChromaDB
- Incremental document synchronization:
  - New documents are added
  - Modified documents are updated
  - Deleted documents are removed
- Semantic retrieval
- Local LLM inference with Ollama
- Streaming responses
- Command-line interface

---

## Architecture

```text
                         Documents
                             |
                             v
                    Ingestion Pipeline
                             |
             +---------------+---------------+
             |                               |
        Document Loader                Text Splitter
             |                               |
             +---------------+---------------+
                             |
                             v
                       Embeddings
                             |
                             v
                         ChromaDB
                             |
                             v

User Question
        |
        v
    Retriever
        |
        v
 Retrieved Context
        |
        v
  Prompt Construction
        |
        v
      Ollama LLM
        |
        v
   Generated Answer
```

---

## Project Structure

```text
rag-engine
│
├── data
│   └── documents
│
├── src
│   │
│   ├── ingestion
│   │   ├── loader.py
│   │   ├── splitter.py
│   │   ├── models.py
│   │   └── ingester.py
│   │
│   ├── vectorstore
│   │   └── chroma.py
│   │
│   ├── retrieval
│   │   └── retriever.py
│   │
│   ├── generation
│   │   ├── llm.py
│   │   ├── prompt.py
│   │   └── generator.py
│   │
│   ├── interfaces
│   │   └── chat.py
│   │
│   ├── cli.py
│   │
│   └── config.py
│
├── requirements.txt
└── README.md
```

---

## How It Works

### Document Ingestion

Documents placed inside:

```text
data/documents/
```

are processed by the ingestion pipeline.

Each document goes through:

1. Document loading
2. Text splitting into chunks
3. Embedding generation
4. Vector storage in ChromaDB

Each chunk contains metadata such as:

- Source document
- Content hash
- Chunk identifier

---

### Incremental Synchronization

The ingestion pipeline keeps the vector database synchronized with the document collection.

Changes are detected using content hashes:

| Change | Action |
|---|---|
| New document | Add chunks |
| Modified document | Replace existing chunks |
| Deleted document | Remove chunks |

Running ingestion multiple times without document changes does not recreate the index.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd rag-engine
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Requirements

This project uses Ollama for local LLM inference.

Install Ollama:

https://ollama.com/

Download the required models:

```bash
ollama pull qwen3:8b
ollama pull nomic-embed-text
```

---

## Configuration

Configuration is defined in:

```text
src/config.py
```

Example:

```python
LLM_MODEL = "qwen3:8b"

EMBEDDING_MODEL = "nomic-embed-text"

CHROMA_PATH = "data/chroma_db"
```

---

## Usage

### Ingest Documents

Run the ingestion pipeline:

```bash
python src/cli.py ingest
```

Example output:

```text
Ingestion summary:
  Added: 5
  Updated: 1
  Deleted: 0
```

---

### Chat

Start the RAG assistant:

```bash
python src/cli.py chat
```

Example:

```text
RAG Engine ready
Type 'exit' to quit

> What is Ollama?

Searching documents...
Generating answer...

Ollama is a tool that allows running large language models locally...
```

Responses are generated using streaming.

---

## Technologies

- Python
- LangChain
- ChromaDB
- Ollama
- Vector embeddings
- Retrieval-Augmented Generation

---

## Future Improvements

Possible extensions:

- REST API with FastAPI
- Docker deployment
- Automated document watchers
- Retrieval evaluation pipeline
- Hybrid search (BM25 + embeddings)
- Reranking models
- Multi-user support

---

## License

MIT License