"""State access helpers for review import workflows."""

from __future__ import annotations

from typing import Any


def _review_file_cache(state: dict[str, Any]) -> dict:
    """Access ``state["review_cache"]["files"]``, creating if absent."""
    return state.setdefault("review_cache", {}).setdefault("files", {})


def _lang_potentials(state: dict[str, Any], lang_name: str) -> dict:
    """Access ``state["potentials"][lang_name]``, creating if absent."""
    return state.setdefault("potentials", {}).setdefault(lang_name, {})
