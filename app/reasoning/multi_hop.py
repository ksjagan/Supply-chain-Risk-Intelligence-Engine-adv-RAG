from __future__ import annotations

from langchain_core.documents import Document

from app.intelligence.query_tools import decompose_question, generate_query_variants, rewrite_query
from app.reasoning.answer_generation import generate_answer, risk_score_from_evidence
from app.retrieval.engine import SupplyChainRetrievalEngine
from app.retrieval.fusion import reciprocal_rank_fusion


def multi_query_retrieve(engine: SupplyChainRetrievalEngine, question: str, top_k: int) -> tuple[list[str], list[tuple[Document, float]]]:
    """Run multi-query retrieval for a business question.

    Args:
        engine: Retrieval engine with BM25, OpenAI vector search, hybrid search, and reranking.
        question: Original user question.
        top_k: Number of final evidence chunks to return.

    Returns:
        Query variants and reranked evidence chunks.
    """
    variants = generate_query_variants(question)
    result_sets = [engine.retrieve(variant, "hybrid_rerank", top_k=top_k) for variant in variants]
    fused = reciprocal_rank_fusion(result_sets)
    reranked = engine.rerank(question, fused, top_k)
    return variants, reranked


def multi_hop_answer(engine: SupplyChainRetrievalEngine, question: str, top_k: int = 8) -> dict:
    """Run multi-hop retrieval and synthesize a cited risk answer.

    Args:
        engine: Retrieval engine used for every hop.
        question: Original user question.
        top_k: Number of final evidence chunks to return.

    Returns:
        Dictionary containing answer text, rewritten query, query variants, hop trace,
        retrieved results, and risk score.
    """
    rewritten = rewrite_query(question)
    hops = []
    all_results: list[list[tuple[Document, float]]] = []
    for hop_index, sub_question in enumerate(decompose_question(question), start=1):
        hop_query = f"{sub_question} {rewritten}"
        results = engine.retrieve(hop_query, "hybrid_rerank", top_k=top_k)
        hops.append(
            {
                "hop": hop_index,
                "query": hop_query,
                "top_sources": [doc.metadata.get("source", "unknown") for doc, _score in results[:3]],
            }
        )
        all_results.append(results)
    fused = reciprocal_rank_fusion(all_results)
    reranked = engine.rerank(question, fused, top_k)
    return {
        "answer": generate_answer(question, reranked, "multi_hop"),
        "rewritten_query": rewritten,
        "query_variants": generate_query_variants(question),
        "hops": hops,
        "results": reranked,
        "risk_score": risk_score_from_evidence(reranked),
    }
