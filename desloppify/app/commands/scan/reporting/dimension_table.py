"""Audience-oriented facade for scan dimension table reporting."""

from __future__ import annotations

from .. import scan_reporting_dimensions as _dimensions_mod

show_dimension_deltas = _dimensions_mod.show_dimension_deltas
show_score_model_breakdown = _dimensions_mod.show_score_model_breakdown
show_scorecard_subjective_measures = _dimensions_mod.show_scorecard_subjective_measures

__all__ = [
    "show_dimension_deltas",
    "show_score_model_breakdown",
    "show_scorecard_subjective_measures",
]
