from __future__ import annotations

import math
import re
import json
import hashlib
from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from rank_bm25 import BM25Okapi

from app.config import settings
from app.ingestion.chunking import chunk_documents
from app.ingestion.loaders import load_markdown_documents, load_tables, table_rows_as_documents
from app.retrieval.fusion import reciprocal_rank_fusion


TOKEN_PATTERN = re.compile(r"[A-Za-z0-9_\-]+")


def tokenize(text: str) -> list[str]:
    """Split text into normalized tokens for BM25 and fallback reranking.

    Args:
        text: Raw document or query text.

    Returns:
        Lowercase alphanumeric tokens. Hyphenated IDs such as SUP-0001 are preserved.
    """
    return [token.lower() for token in TOKEN_PATTERN.findall(text)]


def cosine_scores(query_vector: list[float], matrix: np.ndarray) -> np.ndarray:
    """Compute cosine similarity between one query vector and all chunk vectors.

    Args:
        query_vector: Embedding vector for the user query.
        matrix: Two-dimensional array of chunk embeddings.

    Returns:
        One score per chunk where larger means more semantically similar.
    """
    query = np.asarray(query_vector, dtype=np.float32)
    query_norm = np.linalg.norm(query)
    matrix_norms = np.linalg.norm(matrix, axis=1)
    denominator = np.maximum(matrix_norms * query_norm, 1e-12)
    return matrix.dot(query) / denominator


class SupplyChainRetrievalEngine:
    """Production-style in-memory retrieval engine for the API and Streamlit app."""

    def __init__(self, data_dir: Path | None = None) -> None:
        """Load company data, create chunks, build BM25, and load OpenAI embeddings.

        Args:
            data_dir: Folder containing `documents/`, `tables/`, `eval/`, and `manifest.json`.
                When omitted, the path comes from `DATA_DIR` in `.env`.

        Raises:
            RuntimeError: If `OPENAI_API_KEY` is missing. The project intentionally uses
                OpenAI embeddings for dense retrieval.
        """
        self.data_dir = data_dir or settings.data_dir
        if not settings.openai_api_key:
            raise RuntimeError("OPENAI_API_KEY is required because dense retrieval uses OpenAI embeddings.")
        self.tables = load_tables(self.data_dir)
        raw_docs = load_markdown_documents(self.data_dir) + table_rows_as_documents(self.tables)
        self.chunks = chunk_documents(raw_docs, settings.chunk_size, settings.chunk_overlap)
        self.texts = [doc.page_content for doc in self.chunks]
        self.tokens = [tokenize(text) for text in self.texts]
        self.bm25 = BM25Okapi(self.tokens)
        self.embedding_client = OpenAIEmbeddings(model=settings.openai_embedding_model, api_key=settings.openai_api_key)
        self.embedding_matrix = self._load_or_create_embedding_matrix()

    def _embedding_cache_path(self) -> Path:
        """Return the cache path for OpenAI chunk embeddings.

        Args:
            None.

        Returns:
            A path under `data/company_data/cache/` keyed by embedding model and chunk hash.
        """
        digest = hashlib.sha256()
        digest.update(settings.openai_embedding_model.encode("utf-8"))
        for doc in self.chunks:
            digest.update(str(doc.metadata.get("chunk_id", "")).encode("utf-8"))
            digest.update(doc.page_content.encode("utf-8"))
        cache_dir = self.data_dir / "cache"
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir / f"openai_embeddings_{digest.hexdigest()[:16]}.json"

    def _load_or_create_embedding_matrix(self) -> np.ndarray:
        """Load cached chunk embeddings or create them with OpenAI.

        Args:
            None.

        Returns:
            A NumPy matrix shaped `(number_of_chunks, embedding_dimensions)`.
        """
        cache_path = self._embedding_cache_path()
        if cache_path.exists():
            payload = json.loads(cache_path.read_text(encoding="utf-8"))
            return np.asarray(payload["embeddings"], dtype=np.float32)

        embeddings = self.embedding_client.embed_documents(self.texts)
        cache_path.write_text(
            json.dumps(
                {
                    "model": settings.openai_embedding_model,
                    "chunk_count": len(self.chunks),
                    "embeddings": embeddings,
                }
            ),
            encoding="utf-8",
        )
        return np.asarray(embeddings, dtype=np.float32)

    def stats(self) -> dict[str, Any]:
        """Return dataset and index statistics for health checks and the UI.

        Args:
            None.

        Returns:
            Manifest counts plus runtime chunk count, table names, and embedding model.
        """
        manifest_path = self.data_dir / "manifest.json"
        manifest = {}
        if manifest_path.exists():
            import json

            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        return {
            **manifest,
            "chunks": len(self.chunks),
            "tables": sorted(self.tables.keys()),
            "embedding_model": settings.openai_embedding_model,
        }

    def vector_search(self, query: str, top_k: int = 8) -> list[tuple[Document, float]]:
        """Retrieve semantically similar chunks using OpenAI embeddings.

        Args:
            query: User question or rewritten search query.
            top_k: Number of highest-scoring chunks to return.

        Returns:
            Ranked `(Document, score)` pairs where score is cosine similarity.
        """
        query_vector = self.embedding_client.embed_query(query)
        scores = cosine_scores(query_vector, self.embedding_matrix)
        indexes = np.argsort(scores)[::-1][:top_k]
        return [(self.chunks[int(index)], float(scores[int(index)])) for index in indexes if scores[int(index)] > 0]

    def bm25_search(self, query: str, top_k: int = 8) -> list[tuple[Document, float]]:
        """Retrieve chunks using BM25 lexical search.

        Args:
            query: User question or rewritten search query.
            top_k: Number of highest-scoring chunks to return.

        Returns:
            Ranked `(Document, score)` pairs where score is BM25 relevance.
        """
        scores = self.bm25.get_scores(tokenize(query))
        indexes = np.argsort(scores)[::-1][:top_k]
        return [(self.chunks[int(index)], float(scores[int(index)])) for index in indexes if scores[int(index)] > 0]

    def hybrid_search(self, query: str, top_k: int = 8, candidate_k: int | None = None) -> list[tuple[Document, float]]:
        """Combine OpenAI vector search and BM25 using reciprocal rank fusion.

        Args:
            query: User question or rewritten search query.
            top_k: Final number of fused chunks to return.
            candidate_k: Number of candidates each retriever contributes before fusion.
                Larger values improve recall before reranking, at the cost of more work.

        Returns:
            Ranked fused `(Document, score)` pairs.
        """
        limit = candidate_k or max(top_k * 4, settings.candidate_k)
        vector_results = self.vector_search(query, limit)
        bm25_results = self.bm25_search(query, limit)
        return reciprocal_rank_fusion([vector_results, bm25_results])[:top_k]

    def rerank(self, query: str, candidates: list[tuple[Document, float]], top_k: int = 8) -> list[tuple[Document, float]]:
        """Rerank retrieved candidates.

        Args:
            query: Original user question. Using the original question keeps ranking
                aligned with the user's intent after broad retrieval.
            candidates: Candidate chunks from hybrid or multi-query retrieval.
            top_k: Number of final evidence chunks to return.

        Returns:
            Reranked `(Document, score)` pairs.
        """
        if settings.use_openai_llm and settings.openai_api_key:
            return self.llm_rerank(query, candidates, top_k)
        return self.heuristic_rerank(query, candidates, top_k)

    def heuristic_rerank(self, query: str, candidates: list[tuple[Document, float]], top_k: int = 8) -> list[tuple[Document, float]]:
        """Fast local reranker used when LLM reranking is disabled.

        Args:
            query: Original user question.
            candidates: Candidate chunks with base retrieval scores.
            top_k: Number of final chunks to return.

        Returns:
            Reranked `(Document, score)` pairs based on overlap, exactness, and evidence type.
        """
        query_terms = set(tokenize(query))
        reranked: list[tuple[Document, float]] = []
        for doc, base_score in candidates:
            doc_terms = tokenize(doc.page_content)
            counts = Counter(doc_terms)
            overlap = sum(counts[term] for term in query_terms)
            exact_bonus = 0.2 if query.lower() in doc.page_content.lower() else 0.0
            metadata_bonus = 0.08 if doc.metadata.get("document_type") in {"incident_reports", "risk_reports", "structured_row"} else 0.0
            length_penalty = 1.0 / math.sqrt(max(1, len(doc_terms) / 120))
            score = float(base_score) + (overlap * 0.035 * length_penalty) + exact_bonus + metadata_bonus
            reranked.append((doc, score))
        return sorted(reranked, key=lambda item: item[1], reverse=True)[:top_k]

    def llm_rerank(self, query: str, candidates: list[tuple[Document, float]], top_k: int = 8) -> list[tuple[Document, float]]:
        """Use an OpenAI chat model to choose the most relevant evidence chunks.

        Args:
            query: Original user question.
            candidates: Candidate chunks to evaluate. Only the first 20 are sent to control cost.
            top_k: Number of selected chunks to return.

        Returns:
            LLM-selected `(Document, score)` pairs. If parsing fails, falls back to the
            local heuristic reranker.
        """
        short_list = candidates[:20]
        evidence = [
            {
                "index": index,
                "source": doc.metadata.get("source", "unknown"),
                "text": " ".join(doc.page_content.split())[:900],
            }
            for index, (doc, _score) in enumerate(short_list)
        ]
        prompt = (
            "You are reranking evidence for a supply chain risk question. "
            "Return JSON only with this shape: {\"ranking\": [{\"index\": 0, \"score\": 0.95, \"reason\": \"...\"}]}.\n"
            f"Question: {query}\n"
            f"Evidence candidates:\n{json.dumps(evidence, indent=2)}"
        )
        try:
            llm = ChatOpenAI(model=settings.openai_model, temperature=0, api_key=settings.openai_api_key)
            content = llm.invoke(prompt).content
            parsed = json.loads(content)
            selected: list[tuple[Document, float]] = []
            for item in parsed.get("ranking", [])[:top_k]:
                index = int(item["index"])
                if 0 <= index < len(short_list):
                    selected.append((short_list[index][0], float(item.get("score", 0.0))))
            return selected or self.heuristic_rerank(query, candidates, top_k)
        except Exception:
            return self.heuristic_rerank(query, candidates, top_k)

    def retrieve(self, query: str, strategy: str = "hybrid_rerank", top_k: int = 8) -> list[tuple[Document, float]]:
        """Run one named retrieval strategy.

        Args:
            query: User question or transformed query.
            strategy: One of `vector`, `bm25`, `hybrid`, or `hybrid_rerank`.
            top_k: Number of final evidence chunks to return.

        Returns:
            Ranked `(Document, score)` pairs from the selected retrieval strategy.
        """
        if strategy == "vector":
            return self.vector_search(query, top_k)
        if strategy == "bm25":
            return self.bm25_search(query, top_k)
        if strategy == "hybrid":
            return self.hybrid_search(query, top_k)
        candidates = self.hybrid_search(query, max(settings.candidate_k, top_k * 4))
        return self.rerank(query, candidates, top_k)
