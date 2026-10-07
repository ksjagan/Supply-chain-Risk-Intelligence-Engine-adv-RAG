from __future__ import annotations

import json
from pathlib import Path

from app.evaluation.metrics import entity_recall
from app.reasoning.answer_generation import generate_answer
from app.retrieval.engine import SupplyChainRetrievalEngine


def run_small_eval(engine: SupplyChainRetrievalEngine, eval_path: Path, strategy: str = "hybrid_rerank", limit: int = 20) -> dict:
    questions = json.loads(eval_path.read_text(encoding="utf-8"))[:limit]
    rows = []
    for item in questions:
        results = engine.retrieve(item["question"], strategy=strategy, top_k=8)
        combined_text = "\n".join(doc.page_content for doc, _score in results)
        rows.append(
            {
                "question_id": item["question_id"],
                "question": item["question"],
                "entity_recall": entity_recall(combined_text, item.get("expected_entities", [])),
                "top_source": results[0][0].metadata.get("source", "none") if results else "none",
            }
        )
    avg = round(sum(row["entity_recall"] for row in rows) / max(1, len(rows)), 3)
    return {"strategy": strategy, "average_entity_recall": avg, "rows": rows}
