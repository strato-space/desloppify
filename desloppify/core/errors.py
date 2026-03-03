"""Shared custom exception types used across command flows."""

from __future__ import annotations


class PlanLoadError(Exception):
    """Recoverable failure while parsing or validating plan persistence data."""


__all__ = ["PlanLoadError"]
