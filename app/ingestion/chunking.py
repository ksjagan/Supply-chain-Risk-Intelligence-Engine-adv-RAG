from __future__ import annotations

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(documents: list[Document], chunk_size: int, chunk_overlap: int) -> list[Document]:
    """Split documents into retrieval chunks with enough overlap for context.

    Args:
        documents: Raw LangChain documents from Markdown files and CSV rows.
        chunk_size: Maximum characters per chunk.
        chunk_overlap: Characters repeated between adjacent chunks to preserve context.

    Returns:
        Chunked documents with stable `chunk_id` metadata.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    chunks = splitter.split_documents(documents)
    for index, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = f"CHUNK-{index:06d}"
    return chunks
