from __future__ import annotations

from langchain_core.documents import Document


def reciprocal_rank_fusion(result_sets: list[list[tuple[Document, float]]], k: int = 60) -> list[tuple[Document, float]]:
    """Merge ranked lists using reciprocal rank fusion.

    Args:
        result_sets: Ranked retrieval outputs from BM25, vector search, or query variants.
        k: Smoothing constant that controls how strongly top ranks are rewarded.

    Returns:
        Deduplicated `(Document, fused_score)` pairs sorted by fused score.
    """
    fused: dict[str, tuple[Document, float]] = {}
    for results in result_sets:
        for rank, (doc, _score) in enumerate(results, start=1):
            chunk_id = doc.metadata.get("chunk_id") or doc.metadata.get("source") or doc.page_content[:80]
            contribution = 1.0 / (k + rank)
            if chunk_id not in fused:
                fused[chunk_id] = (doc, contribution)
            else:
                existing_doc, existing_score = fused[chunk_id]
                fused[chunk_id] = (existing_doc, existing_score + contribution)
    return sorted(fused.values(), key=lambda item: item[1], reverse=True)
