"""Payload parsing helpers for review import workflows."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from desloppify.intelligence.review.importing.contracts import (
    ReviewFindingPayload,
    ReviewImportPayload,
)


@dataclass(frozen=True)
class ReviewImportEnvelope:
    """Validated shared payload shape for review imports."""

    findings: list[ReviewFindingPayload]
    assessments: dict[str, Any] | None
    reviewed_files: list[str]


def extract_reviewed_files(data: list[dict] | dict) -> list[str]:
    """Parse optional reviewed-file list from import payload."""
    if not isinstance(data, dict):
        return []
    raw = data.get("reviewed_files")
    if not isinstance(raw, list):
        return []

    reviewed: list[str] = []
    seen: set[str] = set()
    for item in raw:
        if not isinstance(item, str):
            continue
        path = item.strip()
        if not path or path in seen:
            continue
        seen.add(path)
        reviewed.append(path)
    return reviewed


def parse_review_import_payload(
    data: ReviewImportPayload | dict[str, Any],
    *,
    mode_name: str,
) -> ReviewImportEnvelope:
    """Parse shared review import payload shape for per-file/holistic flows."""
    if not isinstance(data, dict):
        raise ValueError(f"{mode_name} review import payload must be a JSON object")

    if "findings" not in data:
        raise ValueError(f"{mode_name} review import payload must contain 'findings'")
    findings = data["findings"]
    if not isinstance(findings, list):
        raise ValueError(f"{mode_name} review import payload 'findings' must be a list")
    for idx, finding in enumerate(findings):
        if not isinstance(finding, dict):
            raise ValueError(
                f"{mode_name} review import payload 'findings[{idx}]' must be an object"
            )

    assessments = data.get("assessments")
    if assessments is not None and not isinstance(assessments, dict):
        raise ValueError(
            f"{mode_name} review import payload 'assessments' must be an object"
        )
    return ReviewImportEnvelope(
        findings=findings,
        assessments=assessments,
        reviewed_files=extract_reviewed_files(data),
    )


def normalize_review_confidence(value: object) -> str:
    """Normalize review confidence labels to high/medium/low."""
    confidence = str(value).strip().lower()
    return confidence if confidence in {"high", "medium", "low"} else "low"


def review_tier(confidence: str, *, holistic: bool) -> int:
    """Derive natural tier from review confidence and scope."""
    if confidence == "high":
        return 1 if holistic else 3
    if confidence == "medium":
        return 2 if holistic else 3
    return 3
