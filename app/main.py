from __future__ import annotations

from functools import lru_cache

from fastapi import FastAPI

from app.config import settings
from app.evaluation.runner import run_small_eval
from app.intelligence.query_tools import generate_query_variants, rewrite_query
from app.reasoning.answer_generation import format_evidence, generate_answer, risk_score_from_evidence
from app.reasoning.multi_hop import multi_hop_answer, multi_query_retrieve
from app.retrieval.engine import SupplyChainRetrievalEngine
from app.schemas import ChatRequest, ChatResponse


app = FastAPI(title="Supply Chain Risk Intelligence Engine")


@lru_cache(maxsize=1)
def get_engine() -> SupplyChainRetrievalEngine:
    return SupplyChainRetrievalEngine(settings.data_dir)


@app.get("/")
def home() -> dict:
    return {
        "name": "Supply Chain Risk Intelligence Engine",
        "ui": "Run the Streamlit app with: streamlit run streamlit_app.py",
        "docs": "/docs",
    }


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/stats")
def stats() -> dict:
    return get_engine().stats()


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    engine = get_engine()
    if request.strategy == "multi_hop":
        result = multi_hop_answer(engine, request.question, request.top_k)
        return ChatResponse(
            answer=result["answer"],
            strategy=request.strategy,
            rewritten_query=result["rewritten_query"],
            query_variants=result["query_variants"],
            hops=result["hops"],
            evidence=format_evidence(result["results"]),
            risk_score=result["risk_score"],
        )
    if request.strategy == "multi_query":
        variants, results = multi_query_retrieve(engine, request.question, request.top_k)
        return ChatResponse(
            answer=generate_answer(request.question, results, request.strategy),
            strategy=request.strategy,
            rewritten_query=rewrite_query(request.question),
            query_variants=variants,
            evidence=format_evidence(results),
            risk_score=risk_score_from_evidence(results),
        )
    query = rewrite_query(request.question) if request.strategy in {"hybrid", "hybrid_rerank"} else request.question
    results = engine.retrieve(query, request.strategy, request.top_k)
    return ChatResponse(
        answer=generate_answer(request.question, results, request.strategy),
        strategy=request.strategy,
        rewritten_query=query if query != request.question else None,
        query_variants=generate_query_variants(request.question) if request.strategy == "hybrid_rerank" else [],
        evidence=format_evidence(results),
        risk_score=risk_score_from_evidence(results),
    )


@app.post("/retrieve/{strategy}")
def retrieve(strategy: str, request: ChatRequest) -> dict:
    engine = get_engine()
    results = engine.retrieve(request.question, strategy, request.top_k)
    return {"strategy": strategy, "evidence": format_evidence(results)}


@app.post("/evaluate")
def evaluate(strategy: str = "hybrid_rerank", limit: int = 20) -> dict:
    return run_small_eval(get_engine(), settings.data_dir / "eval" / "eval_questions.json", strategy=strategy, limit=limit)
