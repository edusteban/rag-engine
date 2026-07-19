from pathlib  import Path 

from langchain_core.documents import Document
from config import DOCS_PATH

def load_documents() -> list[Document]:
    return [_load_document(file) for file in Path(DOCS_PATH).rglob("*.txt")]

def _load_document(file: str) -> Document:
    with open (file, "r", encoding="utf-8") as f:
        return Document(
            page_content=f.read(), 
            metadata={"source": file.relative_to(DOCS_PATH).as_posix()}
        )
    
