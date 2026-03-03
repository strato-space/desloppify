"""Auto-resolution helpers for review re-import workflows."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from desloppify.state import utc_now


def auto_resolve_review_findings(
    state: dict[str, Any],
    *,
    new_ids: set[str],
    diff: dict[str, Any],
    note: str,
    should_resolve: Callable[[dict[str, Any]], bool],
    utc_now_fn=utc_now,
) -> None:
    """Auto-resolve stale open review findings that match a scope predicate."""
    diff.setdefault("auto_resolved", 0)
    for finding_id, finding in state.get("findings", {}).items():
        if finding_id in new_ids or finding.get("status") != "open":
            continue
        if not should_resolve(finding):
            continue
        finding["status"] = "auto_resolved"
        finding["resolved_at"] = utc_now_fn()
        finding["note"] = note
        diff["auto_resolved"] += 1
