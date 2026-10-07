from __future__ import annotations

from pathlib import Path

import pandas as pd
from langchain_core.documents import Document


def load_markdown_documents(data_dir: Path) -> list[Document]:
    """Load generated Markdown business documents into LangChain Documents.

    Args:
        data_dir: Root company data folder containing the `documents/` directory.

    Returns:
        LangChain `Document` objects with page content and source metadata.
    """
    documents: list[Document] = []
    for path in sorted((data_dir / "documents").rglob("*.md")):
        relative = path.relative_to(data_dir).as_posix()
        category = path.parent.name
        text = path.read_text(encoding="utf-8")
        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": relative,
                    "document_type": category,
                    "file_name": path.name,
                },
            )
        )
    return documents


def load_tables(data_dir: Path) -> dict[str, pd.DataFrame]:
    """Load structured supply chain CSV tables.

    Args:
        data_dir: Root company data folder containing the `tables/` directory.

    Returns:
        Dictionary mapping table names, such as `shipments`, to pandas DataFrames.
    """
    tables: dict[str, pd.DataFrame] = {}
    for path in sorted((data_dir / "tables").glob("*.csv")):
        tables[path.stem] = pd.read_csv(path)
    return tables


def table_rows_as_documents(tables: dict[str, pd.DataFrame]) -> list[Document]:
    """Turn structured rows into searchable text while preserving metadata.

    Args:
        tables: Dictionary of table names to DataFrames.

    Returns:
        One LangChain `Document` per table row so structured records can be retrieved
        together with unstructured reports.
    """
    docs: list[Document] = []
    for table_name, frame in tables.items():
        for index, row in frame.iterrows():
            values = row.dropna().to_dict()
            text = "\n".join(f"{key}: {value}" for key, value in values.items())
            docs.append(
                Document(
                    page_content=f"Table: {table_name}\n{text}",
                    metadata={
                        "source": f"tables/{table_name}.csv#{index}",
                        "document_type": "structured_row",
                        "table": table_name,
                        "row_index": int(index),
                    },
                )
            )
    return docs
