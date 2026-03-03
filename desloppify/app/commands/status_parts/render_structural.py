"""Structural-area reporting helpers for status output."""

from __future__ import annotations

from collections import defaultdict

from desloppify import state as state_mod
from desloppify.core.output_api import colorize
from desloppify.core.paths_api import get_area


def collect_structural_areas(
    state: dict,
) -> list[tuple[str, list]] | None:
    """Collect T3/T4 structural findings grouped by area."""
    findings = state_mod.path_scoped_findings(
        state.get("findings", {}), state.get("scan_path")
    )
    structural = [
        finding
        for finding in findings.values()
        if finding["tier"] in (3, 4) and finding["status"] in ("open", "wontfix")
    ]
    if len(structural) < 5:
        return None

    areas: dict[str, list] = defaultdict(list)
    for finding in structural:
        area = get_area(str(finding.get("file", "")))
        areas[area].append(finding)
    if len(areas) < 2:
        return None

    return sorted(areas.items(), key=lambda pair: -sum(f["tier"] for f in pair[1]))


def build_area_rows(
    sorted_areas: list[tuple[str, list]],
    *,
    max_areas: int = 15,
) -> list[list[str]]:
    """Build table rows from sorted area findings."""
    rows: list[list[str]] = []
    for area, area_findings in sorted_areas[:max_areas]:
        t3 = sum(1 for finding in area_findings if finding["tier"] == 3)
        t4 = sum(1 for finding in area_findings if finding["tier"] == 4)
        open_count = sum(1 for finding in area_findings if finding["status"] == "open")
        debt_count = sum(1 for finding in area_findings if finding["status"] == "wontfix")
        weight = sum(finding["tier"] for finding in area_findings)
        rows.append(
            [
                area,
                str(len(area_findings)),
                f"T3:{t3} T4:{t4}",
                str(open_count),
                str(debt_count),
                str(weight),
            ]
        )
    return rows


def render_area_workflow(
    sorted_areas: list[tuple[str, list]],
    *,
    max_areas: int = 15,
) -> None:
    """Print overflow count and workflow instructions for structural work."""
    remaining = len(sorted_areas) - max_areas
    if remaining > 0:
        print(colorize(f"\n  ... and {remaining} more areas", "dim"))

    print(colorize("\n  Workflow:", "dim"))
    print(colorize("    1. desloppify show <area> --status wontfix --top 50", "dim"))
    print(
        colorize(
            "    2. Create tasks/<date>-<area-name>.md with decomposition plan",
            "dim",
        )
    )
    print(
        colorize("    3. Farm each task doc to a sub-agent for implementation", "dim")
    )
    print()


__all__ = [
    "build_area_rows",
    "collect_structural_areas",
    "render_area_workflow",
]

