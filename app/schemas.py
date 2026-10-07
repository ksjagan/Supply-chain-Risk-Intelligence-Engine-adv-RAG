from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


RetrievalStrategy = Literal["vector", "bm25", "hybrid", "hybrid_rerank", "multi_query", "multi_hop"]


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=3)
    strategy: RetrievalStrategy = "multi_hop"
    top_k: int = Field(default=8, ge=1, le=20)


class EvidenceItem(BaseModel):
    content: str
    score: float
    source: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class ChatResponse(BaseModel):
    answer: str
    strategy: str
    rewritten_query: str | None = None
    query_variants: list[str] = Field(default_factory=list)
    hops: list[dict[str, Any]] = Field(default_factory=list)
    evidence: list[EvidenceItem] = Field(default_factory=list)
    risk_score: float | None = None
