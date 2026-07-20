from pathlib  import Path 
import hashlib

from config import DOCS_PATH
from langchain_core.documents import Document

from src.ingestion.loaders import load_txt, load_docx, load_pdf, load_md

def load_documents() -> list[Document]:
    documents = []

    for path in Path(DOCS_PATH).rglob("*"):
        if not path.is_file():
            continue

        documents.extend(_load_document(path))

    return documents

def _load_document(path: Path) -> list[Document]:
    match path.suffix.lower():
        case ".txt":
            documents = load_txt(path)

        case ".pdf":
            documents = load_pdf(path)

        case ".md":
            documents = load_md(path)

        case ".docx":
            documents = load_docx(path)

        case _:
            return []
    
    return _add_metadata(documents, path= path)

def _add_metadata(documents: list[Document], path: Path) -> list[Document]:
    for document in documents:
        document.metadata["source"] = path.relative_to(DOCS_PATH).as_posix()
        document.metadata["file_name"] = path.name
        document.metadata["content_hash"] = _generate_doc_id(document.page_content)
    
    return documents

def _generate_doc_id(content: str) -> str:
    content = " ".join(content.split())

    return hashlib.sha256(
        content.encode("utf-8")
    ).hexdigest()





