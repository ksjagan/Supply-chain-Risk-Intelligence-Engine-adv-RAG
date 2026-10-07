from __future__ import annotations


def entity_recall(answer_text: str, expected_entities: list[str]) -> float:
    if not expected_entities:
        return 0.0
    lower = answer_text.lower()
    hits = sum(1 for entity in expected_entities if str(entity).lower() in lower)
    return round(hits / len(expected_entities), 3)
