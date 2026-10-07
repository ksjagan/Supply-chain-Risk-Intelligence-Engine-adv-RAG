from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    data_dir: Path = Path(os.getenv("DATA_DIR", "data/company_data"))
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    openai_embedding_model: str = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
    reranker_model_name: str = os.getenv("RERANKER_MODEL_NAME", "cross-encoder/ms-marco-MiniLM-L-6-v2")
    use_openai_llm: bool = os.getenv("USE_OPENAI_LLM", "false").lower() == "true"
    chunk_size: int = 900
    chunk_overlap: int = 140
    retrieval_k: int = 8
    candidate_k: int = 30


settings = Settings()
