from __future__ import annotations

import streamlit as st

from app.config import settings
from app.intelligence.query_tools import generate_query_variants, rewrite_query
from app.reasoning.answer_generation import format_evidence, generate_answer, risk_score_from_evidence
from app.reasoning.multi_hop import multi_hop_answer, multi_query_retrieve
from app.retrieval.engine import SupplyChainRetrievalEngine


st.set_page_config(
    page_title="Supply Chain Risk Intelligence Engine",
    page_icon="",
    layout="wide",
)


@st.cache_resource(show_spinner="Building retrieval indexes from company data...")
def load_engine() -> SupplyChainRetrievalEngine:
    return SupplyChainRetrievalEngine(settings.data_dir)


def run_pipeline(question: str, strategy: str, top_k: int) -> dict:
    engine = load_engine()
    if strategy == "multi_hop":
        result = multi_hop_answer(engine, question, top_k=top_k)
        return {
            "answer": result["answer"],
            "rewritten_query": result["rewritten_query"],
            "query_variants": result["query_variants"],
            "hops": result["hops"],
            "evidence": format_evidence(result["results"]),
            "risk_score": result["risk_score"],
        }

    if strategy == "multi_query":
        variants, results = multi_query_retrieve(engine, question, top_k=top_k)
        return {
            "answer": generate_answer(question, results, strategy),
            "rewritten_query": rewrite_query(question),
            "query_variants": variants,
            "hops": [],
            "evidence": format_evidence(results),
            "risk_score": risk_score_from_evidence(results),
        }

    query = rewrite_query(question) if strategy in {"hybrid", "hybrid_rerank"} else question
    results = engine.retrieve(query, strategy=strategy, top_k=top_k)
    return {
        "answer": generate_answer(question, results, strategy),
        "rewritten_query": query if query != question else None,
        "query_variants": generate_query_variants(question) if strategy == "hybrid_rerank" else [],
        "hops": [],
        "evidence": format_evidence(results),
        "risk_score": risk_score_from_evidence(results),
    }


st.title("Supply Chain Risk Intelligence Engine")
st.caption("Hybrid retrieval, reranking, query transformation, and multi-hop reasoning over synthetic enterprise supply chain data.")

try:
    stats = load_engine().stats()
    cols = st.columns(5)
    cols[0].metric("Documents", stats.get("documents", 0))
    cols[1].metric("Chunks", stats.get("chunks", 0))
    cols[2].metric("Shipments", stats.get("shipments", 0))
    cols[3].metric("Suppliers", stats.get("suppliers", 0))
    cols[4].metric("Eval Questions", stats.get("eval_questions", 0))
except Exception as exc:
    st.error("Company data is not ready. Run `python data/generate_data.py` after installing Python dependencies.")
    st.exception(exc)
    st.stop()


with st.sidebar:
    st.header("Retrieval Controls")
    strategy = st.selectbox(
        "Strategy",
        ["multi_hop", "multi_query", "hybrid_rerank", "hybrid", "vector", "bm25"],
        index=0,
        help="Choose the retrieval strategy to compare quality and evidence coverage.",
    )
    top_k = st.slider(
        "Top K Evidence Chunks",
        min_value=3,
        max_value=20,
        value=8,
        help="Controls how many final evidence chunks are shown after retrieval and reranking.",
    )

    st.divider()
    st.subheader("Demo Questions")
    demo_questions = [
        "Which products are most exposed to delayed semiconductor shipments from Malaysia?",
        "Which suppliers create single-source risk for high-revenue products?",
        "What components are affected by Vietnam port congestion?",
        "Which suppliers have both poor delivery performance and compliance risk?",
        "What are the biggest supply chain risks for the Orion product line?",
    ]
    selected_demo = st.radio("Pick one", demo_questions, label_visibility="collapsed")


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Ask a supply chain risk question, then switch retrieval strategies to compare the evidence quality.",
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


question = st.chat_input("Ask about supplier risk, shipment delays, product exposure, or compliance issues")

if st.button("Use selected demo question"):
    question = selected_demo

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Retrieving evidence and building risk answer..."):
            result = run_pipeline(question, strategy, top_k)
        st.markdown(result["answer"])

    st.session_state.messages.append({"role": "assistant", "content": result["answer"]})

    st.divider()
    left, right = st.columns([0.35, 0.65])

    with left:
        st.subheader("Risk Signal")
        st.metric("Evidence Risk Score", result["risk_score"])
        if result["rewritten_query"]:
            st.text_area("Rewritten Query", result["rewritten_query"], height=110)

        if result["query_variants"]:
            st.write("Query Variants")
            for variant in result["query_variants"]:
                st.code(variant, language="text")

        if result["hops"]:
            st.write("Multi-Hop Trace")
            for hop in result["hops"]:
                with st.expander(f"Hop {hop['hop']}"):
                    st.write(hop["query"])
                    st.write("Top sources")
                    st.write(hop["top_sources"])

    with right:
        st.subheader("Retrieved Evidence")
        for index, item in enumerate(result["evidence"], start=1):
            with st.expander(f"{index}. {item['source']} · score {item['score']}"):
                st.write(item["content"])
                st.json(item["metadata"])
