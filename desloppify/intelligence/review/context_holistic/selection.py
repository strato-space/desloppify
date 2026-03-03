"""File selection and context section builders for holistic review."""

from __future__ import annotations

from pathlib import Path

from desloppify.engine.policy.zones import EXCLUDED_ZONE_VALUES
from .selection_contexts import (
    api_surface_context as _api_surface_context,
    architecture_context as _architecture_context,
    coupling_context as _coupling_context,
    dependencies_context as _dependencies_context,
    error_strategy_context as _error_strategy_context,
    naming_conventions_context as _naming_conventions_context,
    sibling_behavior_context as _sibling_behavior_context,
    testing_context as _testing_context,
)
from .selection_contexts import (
    api_surface_context as _api_surface_context,
    architecture_context as _architecture_context,
    coupling_context as _coupling_context,
    dependencies_context as _dependencies_context,
    error_strategy_context as _error_strategy_context,
    naming_conventions_context as _naming_conventions_context,
    sibling_behavior_context as _sibling_behavior_context,
    testing_context as _testing_context,
)


def select_holistic_files(path: Path, lang: object, files: list[str] | None) -> list[str]:
    selected = files if files is not None else (lang.file_finder(path) if lang.file_finder else [])
    if not selected:
        return []

    zone_map = getattr(lang, "zone_map", None)
    if zone_map is None:
        return selected

    filtered: list[str] = []
    for filepath in selected:
        try:
            zone = zone_map.get(filepath)
            zone_value = getattr(zone, "value", str(zone))
        except (AttributeError, KeyError, TypeError, ValueError):
            zone_value = "production"
        if zone_value in EXCLUDED_ZONE_VALUES:
            continue
        filtered.append(filepath)
    return filtered


__all__ = [
    "select_holistic_files",
    "_api_surface_context",
    "_architecture_context",
    "_coupling_context",
    "_dependencies_context",
    "_error_strategy_context",
    "_naming_conventions_context",
    "_sibling_behavior_context",
    "_testing_context",
]


__all__ = [
    "_api_surface_context",
    "_architecture_context",
    "_coupling_context",
    "_dependencies_context",
    "_error_strategy_context",
    "_naming_conventions_context",
    "_sibling_behavior_context",
    "_testing_context",
    "select_holistic_files",
]
