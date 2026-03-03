"""Shared compatibility behavior for typed detector adapters."""

from __future__ import annotations

from typing import Protocol

from desloppify.languages._framework.base.types import DetectorCoverageStatus


class CoverageStatusLike(Protocol):
    """Minimal status contract used by compatibility wrappers."""

    def coverage(self) -> DetectorCoverageStatus | None: ...


def entries_or_none_on_degradation(
    *,
    entries: list[dict],
    status: CoverageStatusLike,
) -> list[dict] | None:
    """Return entries when coverage is intact, otherwise preserve legacy ``None``."""
    if status.coverage() is None:
        return entries
    return None


__all__ = ["entries_or_none_on_degradation"]
