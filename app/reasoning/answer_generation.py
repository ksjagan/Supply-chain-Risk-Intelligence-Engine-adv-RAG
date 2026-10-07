from __future__ import annotations

from langchain_core.documents import Document
from langchain_openai import ChatOpenAI

from app.config import settings


def format_evidence(results: list[tuple[Document, float]]) -> list[dict]:
    """Convert retrieval results into API-friendly evidence objects.

    Args:
        results: Ranked `(Document, score)` pairs.

    Returns:
        List of dictionaries with content preview, score, source, and metadata.
    """
    evidence = []
    for doc, score in results:
        evidence.append(
            {
                "content": doc.page_content[:900],
                "score": round(float(score), 4),
                "source": str(doc.metadata.get("source", "unknown")),
                "metadata": dict(doc.metadata),
            }
        )
    return evidence


def risk_score_from_evidence(results: list[tuple[Document, float]]) -> float:
    """Estimate a simple risk score from retrieved evidence text.

    Args:
        results: Ranked evidence chunks.

    Returns:
        Float between 0 and 0.98. This is a demo signal, not a statistical risk model.
    """
    text = "\n".join(doc.page_content.lower() for doc, _score in results)
    score = 0.25
    for term, weight in {
        "delayed": 0.14,
        "single_source_flag: yes": 0.18,
        "high": 0.1,
        "critical": 0.1,
        "compliance": 0.08,
        "capacity": 0.07,
        "congestion": 0.08,
        "no approved alternate": 0.14,
    }.items():
        if term in text:
            score += weight
    return round(min(score, 0.98), 2)


def generate_answer(question: str, results: list[tuple[Document, float]], strategy: str) -> str:
    """Generate a deterministic evidence-grounded answer.

    Args:
        question: Original user question.
        results: Ranked evidence chunks.
        strategy: Retrieval strategy name, shown in the response for demo clarity.

    Returns:
        Answer text with cited evidence snippets and a recommended action.
    """
    if not results:
        return "I could not find enough evidence in the generated company dataset to answer this question."

    if settings.use_openai_llm and settings.openai_api_key:
        evidence_text = "\n\n".join(
            f"Source: {doc.metadata.get('source', 'unknown')}\nScore: {score:.3f}\nText:\n{' '.join(doc.page_content.split())[:1200]}"
            for doc, score in results[:8]
        )
        prompt = f"""
You are a supply chain risk analyst. Answer the question using only the evidence below.
Include:
1. Direct answer
2. Key risk drivers
3. Affected suppliers/components/products if present
4. Recommended actions
5. Citations using source names

Question: {question}
Retrieval strategy: {strategy}

Evidence:
{evidence_text}
"""
        try:
            llm = ChatOpenAI(model=settings.openai_model, temperature=0, api_key=settings.openai_api_key)
            return llm.invoke(prompt).content
        except Exception:
            pass

    bullets = []
    for doc, score in results[:5]:
        source = doc.metadata.get("source", "unknown source")
        snippet = " ".join(doc.page_content.replace("#", "").split())[:320]
        bullets.append(f"- {snippet} [source: {source}, score: {score:.3f}]")

    return (
        f"Based on {strategy} retrieval, the strongest evidence suggests the risk should be reviewed through "
        "supplier performance, shipment delay, BOM dependency, and alternate-source coverage.\n\n"
        "Key evidence:\n"
        + "\n".join(bullets)
        + "\n\nRecommended action: validate affected products through the BOM table, prioritize high-revenue or tier_1 products, "
        "and check whether approved alternate suppliers exist before escalating mitigation."
    )
