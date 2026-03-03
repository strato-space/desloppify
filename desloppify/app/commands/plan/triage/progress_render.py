"""Progress rendering helpers for triage command handlers."""

from __future__ import annotations

from desloppify.app.commands.helpers.display import short_finding_id
from desloppify.app.commands.plan.triage_playbook import (
    TRIAGE_STAGE_DEPENDENCIES,
    TRIAGE_STAGE_LABELS,
    TRIAGE_CMD_CLUSTER_ENRICH_COMPACT,
)
from desloppify.core.output import colorize

from desloppify.app.commands.plan.triage.stage_helpers import (
    _manual_clusters_with_findings,
    _triage_coverage,
    _unenriched_clusters,
)


def _print_stage_progress(stages: dict, plan: dict | None = None) -> None:
    """Print the 4-stage progress indicator."""
    print(colorize("  Stages:", "dim"))
    for stage_name, label in TRIAGE_STAGE_LABELS:
        if stage_name in stages:
            print(colorize(f"    \u2713 {label}", "green"))
        elif TRIAGE_STAGE_DEPENDENCIES[stage_name].issubset(stages):
            print(colorize(f"    \u2192 {label} (current)", "yellow"))
        else:
            print(colorize(f"    \u25cb {label}", "dim"))

    if plan and "reflect" in stages and "organize" not in stages:
        gaps = _unenriched_clusters(plan)
        manual = _manual_clusters_with_findings(plan)
        if not manual:
            print(
                colorize(
                    "\n    No manual clusters yet. Create clusters and enrich them.",
                    "yellow",
                )
            )
        elif gaps:
            print(colorize(f"\n    {len(gaps)} cluster(s) need enrichment:", "yellow"))
            for name, missing in gaps:
                print(colorize(f"      {name}: missing {', '.join(missing)}", "yellow"))
            print(
                colorize(
                    f"      Fix: {TRIAGE_CMD_CLUSTER_ENRICH_COMPACT}",
                    "dim",
                )
            )
        else:
            print(colorize(f"\n    All {len(manual)} manual cluster(s) enriched.", "green"))


def _print_progress(plan: dict, open_findings: dict) -> None:
    """Show cluster state and unclustered findings."""
    clusters = plan.get("clusters", {})
    _print_active_clusters(clusters)
    unclustered = _collect_unclustered_findings(clusters, open_findings)
    _print_unclustered_findings(plan, open_findings, unclustered)


def _print_active_clusters(clusters: dict[str, dict]) -> None:
    """Print current clusters that contain findings."""
    active_clusters = {name: cluster for name, cluster in clusters.items() if cluster.get("finding_ids")}
    if not active_clusters:
        return
    print(colorize("\n  Current clusters:", "cyan"))
    for name, cluster in active_clusters.items():
        count = len(cluster.get("finding_ids", []))
        desc = cluster.get("description") or ""
        tag_str = _cluster_tag_summary(cluster)
        desc_str = f" \u2014 {desc}" if desc else ""
        print(f"    {name}: {count} items{tag_str}{desc_str}")


def _cluster_tag_summary(cluster: dict) -> str:
    """Build compact tag summary for one cluster row."""
    steps = cluster.get("action_steps", [])
    auto = cluster.get("auto", False)
    tags: list[str] = []
    tags.append("auto" if auto else "manual")
    tags.append("desc" if cluster.get("description") else "no desc")
    if steps:
        tags.append(f"{len(steps)} steps")
    elif not auto:
        tags.append("no steps")
    return f" [{', '.join(tags)}]"


def _collect_unclustered_findings(clusters: dict[str, dict], open_findings: dict) -> list[str]:
    """Return finding IDs that are not attached to any cluster."""
    all_clustered: set[str] = set()
    for cluster in clusters.values():
        all_clustered.update(cluster.get("finding_ids", []))
    return [finding_id for finding_id in open_findings if finding_id not in all_clustered]


def _print_unclustered_findings(
    plan: dict,
    open_findings: dict,
    unclustered: list[str],
) -> None:
    """Print unclustered findings summary or all-clustered confirmation."""
    if unclustered:
        print(colorize(f"\n  {len(unclustered)} findings not yet in a cluster:", "yellow"))
        for finding_id in unclustered[:10]:
            finding = open_findings[finding_id]
            dim = (
                (finding.get("detail", {}) or {}).get("dimension", "")
                if isinstance(finding.get("detail"), dict)
                else ""
            )
            short = short_finding_id(finding_id)
            print(f"    [{short}] [{dim}] {finding.get('summary', '')}")
        if len(unclustered) > 10:
            print(colorize(f"    ... and {len(unclustered) - 10} more", "dim"))
        return
    if open_findings:
        organized, total, _ = _triage_coverage(plan)
        print(colorize(f"\n  All {organized}/{total} findings are in clusters.", "green"))
