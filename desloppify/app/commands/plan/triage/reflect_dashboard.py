"""Reflect-stage dashboard rendering helpers."""

from __future__ import annotations

from desloppify.core.output import colorize
from desloppify.engine.planning.triage import detect_recurring_patterns


def _print_reflect_dashboard(si: object, plan: dict) -> None:
    """Show completed clusters, resolved findings, and recurring patterns."""
    completed = getattr(si, "completed_clusters", [])
    resolved = getattr(si, "resolved_findings", {})
    open_findings = getattr(si, "open_findings", {})

    _print_completed_clusters(completed)
    _print_resolved_findings(resolved)
    recurring = _print_recurring_patterns(open_findings, resolved)
    if not recurring and not completed and not resolved:
        print(colorize("\n  First triage — no prior work to compare against.", "dim"))
        print(colorize("  Focus your reflect report on your strategy:", "yellow"))
        print(
            colorize(
                "  - How will you resolve contradictions you identified in observe?",
                "dim",
            )
        )
        print(colorize("  - Which findings will you cluster together vs defer?", "dim"))
        print(colorize("  - What's the overall arc of work and why?", "dim"))


def _print_completed_clusters(completed: list[dict]) -> None:
    """Print completed cluster context for reflect stage."""
    if not completed:
        return
    print(colorize("\n  Previously completed clusters:", "cyan"))
    for cluster in completed[:10]:
        name = cluster.get("name", "?")
        count = len(cluster.get("finding_ids", []))
        thesis = cluster.get("thesis", "")
        print(f"    {name}: {count} findings")
        if thesis:
            print(colorize(f"      {thesis}", "dim"))
        for step in cluster.get("action_steps", [])[:3]:
            print(colorize(f"      - {step}", "dim"))
    if len(completed) > 10:
        print(colorize(f"    ... and {len(completed) - 10} more", "dim"))


def _print_resolved_findings(resolved: dict[str, dict]) -> None:
    """Print resolved findings delta since last triage."""
    if not resolved:
        return
    print(colorize(f"\n  Resolved findings since last triage: {len(resolved)}", "cyan"))
    for finding_id, finding in sorted(resolved.items())[:10]:
        status = finding.get("status", "")
        summary = finding.get("summary", "")
        detail = finding.get("detail", {}) if isinstance(finding.get("detail"), dict) else {}
        dim = detail.get("dimension", "")
        print(f"    [{status}] [{dim}] {summary}")
        print(colorize(f"      {finding_id}", "dim"))
    if len(resolved) > 10:
        print(colorize(f"    ... and {len(resolved) - 10} more", "dim"))


def _print_recurring_patterns(open_findings: dict, resolved: dict[str, dict]) -> bool:
    """Print recurring pattern diagnostics for reflect stage."""
    recurring = detect_recurring_patterns(open_findings, resolved)
    if not recurring:
        return False
    print(colorize("\n  Recurring patterns detected:", "yellow"))
    for dim, info in sorted(recurring.items()):
        resolved_count = len(info["resolved"])
        open_count = len(info["open"])
        label = "potential loop" if open_count >= resolved_count else "root cause unaddressed"
        print(
            colorize(
                f"    {dim}: {resolved_count} resolved, {open_count} still open \u2014 {label}",
                "yellow",
            )
        )
    return True
