"""Audience-oriented facade for scan terminal output reporting."""

from __future__ import annotations

from .. import scan_reporting_summary as _summary_mod

show_diff_summary = _summary_mod.show_diff_summary
show_score_delta = _summary_mod.show_score_delta
show_strict_target_progress = _summary_mod.show_strict_target_progress

__all__ = [
    "show_diff_summary",
    "show_score_delta",
    "show_strict_target_progress",
]
