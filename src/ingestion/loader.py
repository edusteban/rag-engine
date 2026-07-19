from pathlib  import Path 
import hashlib

from langchain_core.documents import Document
from config import DOCS_PATH

def load_documents() -> list[Document]:
    return [_load_document(file) for file in Path(DOCS_PATH).rglob("*.txt")]

def _load_document(file: Path) -> Document:
    with open (file, "r", encoding="utf-8") as f:
        content = f.read()
        return Document(
            page_content=content, 
            metadata={
                "source": file.relative_to(DOCS_PATH).as_posix(),
                "file_name": file.name,
                "content_hash": _generate_doc_id(content)
                }
        )

def _generate_doc_id(content: str) -> str:
    content = " ".join(content.split())

    return hashlib.sha256(
        content.encode("utf-8")
    ).hexdigest()
