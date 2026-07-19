from langchain_core.documents import Document
from langchain_chroma import Chroma

from src.ingestion.loader import load_documents
from src.ingestion.splitter import split_documents
from src.vectorstore.chroma import get_vectorstore
from src.ingestion.models import VectorstoreChanges

def ingest() -> None:
    documents = load_documents()

    if not documents:
        raise RuntimeError(
            "No documents found to ingest."
        )
        
    chunks = split_documents(documents)

    vectorstore = get_vectorstore()

    _update_vectorstore(vectorstore, chunks)
    

def _update_vectorstore(vectorstore: Chroma, chunks: list[Document]) -> None:
    changes = _get_vectorstore_changes(vectorstore, chunks)
    
    _delete_documents(
        vectorstore, 
        changes.to_delete | changes.to_update
    )

    _add_documents(
        vectorstore,
        chunks,
        changes.to_add | changes.to_update
    )

    print("\nIngestion summary:")
    print(f"  Added: {len(changes.to_add)}")
    print(f"  Updated: {len(changes.to_update)}")
    print(f"  Deleted: {len(changes.to_delete)}")


def _get_vectorstore_changes(
    vectorstore: Chroma,
    chunks: list[Document]
) -> VectorstoreChanges:

    existing_hashes = _get_hashes_dic(
        vectorstore.get()["metadatas"]
    )

    new_hashes = _get_hashes_dic(
        [chunk.metadata for chunk in chunks]
    )

    to_add = new_hashes.keys() - existing_hashes.keys()

    to_delete = existing_hashes.keys() - new_hashes.keys()

    to_update = {
        source
        for source, content_hash in new_hashes.items()
        if source in existing_hashes
        and existing_hashes[source] != content_hash
    }

    return VectorstoreChanges(
        to_add=set(to_add),
        to_delete=set(to_delete),
        to_update=to_update
    )

def _delete_documents(vectorstore: Chroma, sources: set[str]) -> None:
    for source in sources:
        vectorstore.delete(
            where={
                "source": source
            }
        )

def _add_documents(vectorstore: Chroma, chunks: list[Document], sources: set[str]) -> None:
    chunks_to_add = [
        chunk
        for chunk in chunks
        if chunk.metadata["source"] in sources
    ]

    if not chunks_to_add:
        return
    
    vectorstore.add_documents(
        chunks_to_add
    )


def _get_hashes_dic(metadatas: list[dict]) -> dict[str, str]:
    return {
        metadata["source"]: metadata["content_hash"]
        for metadata in metadatas
    }
