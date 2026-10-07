from __future__ import annotations

import re
import json

from langchain_openai import ChatOpenAI

from app.config import settings


COUNTRIES = ["Malaysia", "Vietnam", "China", "Taiwan", "South Korea", "India", "Mexico", "Poland", "Germany", "Turkey"]
RISK_WORDS = ["delay", "risk", "compliance", "single-source", "shortage", "congestion", "quality", "capacity", "export"]


def extract_entities(question: str) -> dict[str, list[str]]:
    """Extract obvious business entities from a user question.

    Args:
        question: Natural-language supply chain question from the user.

    Returns:
        Dictionary containing country names, operational IDs, and capitalized phrases.
    """
    countries = [country for country in COUNTRIES if country.lower() in question.lower()]
    ids = re.findall(r"\b(?:SUP|CMP|PRD|SHP|PO)-\d+\b", question, flags=re.IGNORECASE)
    capitalized = re.findall(r"\b[A-Z][A-Za-z]+(?:\s[A-Z][A-Za-z]+){0,3}\b", question)
    return {
        "countries": countries,
        "ids": [item.upper() for item in ids],
        "phrases": sorted(set(capitalized))[:8],
    }


def rewrite_query(question: str) -> str:
    """Rewrite a question into a stronger retrieval query.

    Args:
        question: Original user question.

    Returns:
        A retrieval-focused query. When `USE_OPENAI_LLM=true`, an OpenAI model writes
        the query. Otherwise a deterministic domain expansion is used.
    """
    if settings.use_openai_llm and settings.openai_api_key:
        try:
            llm = ChatOpenAI(model=settings.openai_model, temperature=0, api_key=settings.openai_api_key)
            prompt = (
                "Rewrite this supply chain risk question as one high-recall retrieval query. "
                "Include relevant terms for suppliers, shipments, BOM, components, products, "
                "single-source exposure, compliance, incidents, and business impact when useful. "
                "Return only the rewritten query.\n\n"
                f"Question: {question}"
            )
            return llm.invoke(prompt).content.strip()
        except Exception:
            pass

    entities = extract_entities(question)
    intent_terms = [word for word in RISK_WORDS if word in question.lower()]
    additions = ["supplier", "component", "product", "shipment", "BOM", "evidence"]
    if "products" in question.lower() or "product" in question.lower():
        additions.extend(["bill of materials", "single source", "revenue impact"])
    if "compliance" in question.lower():
        additions.extend(["audit", "certification", "screening"])
    entity_text = " ".join(entities["countries"] + entities["ids"] + entities["phrases"])
    return f"{question} {entity_text} {' '.join(intent_terms)} {' '.join(additions)}".strip()


def generate_query_variants(question: str) -> list[str]:
    """Generate diverse query variants for multi-query retrieval.

    Args:
        question: Original user question.

    Returns:
        Search variants targeting different evidence types such as incidents, risk
        reports, logistics memos, BOM rows, and compliance reviews.
    """
    if settings.use_openai_llm and settings.openai_api_key:
        try:
            llm = ChatOpenAI(model=settings.openai_model, temperature=0, api_key=settings.openai_api_key)
            prompt = (
                "Create 5 diverse retrieval queries for the supply chain risk question. "
                "Return JSON only: {\"queries\": [\"...\"]}. Queries should target shipments, "
                "supplier profiles, BOM/product impact, compliance, incidents, logistics risk, "
                "and alternate supplier coverage when relevant.\n\n"
                f"Question: {question}"
            )
            parsed = json.loads(llm.invoke(prompt).content)
            queries = [str(item).strip() for item in parsed.get("queries", []) if str(item).strip()]
            if queries:
                return queries[:5]
        except Exception:
            pass

    rewritten = rewrite_query(question)
    variants = [
        rewritten,
        f"{question} delayed shipments supplier component product impact",
        f"{question} risk report incident report logistics memo compliance review",
        f"{question} single-source supplier alternate supplier bill of materials",
        f"{question} procurement mitigation operational exposure",
    ]
    seen: set[str] = set()
    unique: list[str] = []
    for variant in variants:
        compact = " ".join(variant.split())
        if compact.lower() not in seen:
            unique.append(compact)
            seen.add(compact.lower())
    return unique


def decompose_question(question: str) -> list[str]:
    """Break a complex question into retrieval hops.

    Args:
        question: Original user question.

    Returns:
        Ordered sub-questions for multi-hop retrieval. Each hop targets a different
        part of the supply chain reasoning chain.
    """
    if settings.use_openai_llm and settings.openai_api_key:
        try:
            llm = ChatOpenAI(model=settings.openai_model, temperature=0, api_key=settings.openai_api_key)
            prompt = (
                "Decompose this supply chain risk question into 4 retrieval sub-questions. "
                "Return JSON only: {\"hops\": [\"...\"]}. The hops should cover entity detection, "
                "risk evidence, BOM/product mapping, and mitigation/alternate supplier coverage.\n\n"
                f"Question: {question}"
            )
            parsed = json.loads(llm.invoke(prompt).content)
            hops = [str(item).strip() for item in parsed.get("hops", []) if str(item).strip()]
            if hops:
                return hops[:4]
        except Exception:
            pass

    return [
        f"Identify the suppliers, countries, components, and products mentioned in: {question}",
        f"Find shipment delays, incidents, risk reports, and compliance issues related to: {question}",
        f"Map affected suppliers and components to finished products using BOM data for: {question}",
        f"Find alternate supplier coverage and business impact evidence for: {question}",
    ]
