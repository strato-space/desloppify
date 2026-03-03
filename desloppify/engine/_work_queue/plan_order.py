"""Plan-order and cluster-collapse helpers for work queues."""

from __future__ import annotations

from desloppify.state import StateModel


def new_item_ids(state: StateModel) -> set[str]:
    """Return finding IDs added in the most recent scan."""
    scan_history = state.get("scan_history", [])
    if not scan_history:
        return set()
    threshold = scan_history[-1].get("timestamp", "")
    if not threshold:
        return set()
    return {
        finding_id
        for finding_id, finding in state.get("findings", {}).items()
        if finding.get("first_seen", "") >= threshold
    }


def apply_plan_order(
    items: list[dict],
    plan: dict,
    *,
    include_skipped: bool = False,
    cluster: str | None = None,
    new_ids: set[str] | None = None,
) -> list[dict]:
    """Reorder items according to the living plan."""
    queue_order: list[str] = plan.get("queue_order", [])
    skipped_map: dict = plan.get("skipped", {})
    skipped_ids: set[str] = set(skipped_map.keys())
    overrides: dict = plan.get("overrides", {})
    clusters: dict = plan.get("clusters", {})
    active_cluster = plan.get("active_cluster")

    by_id: dict[str, dict] = {}
    for item in items:
        by_id[item["id"]] = item

    for item_id, item in by_id.items():
        override = overrides.get(item_id, {})
        if override.get("description"):
            item["plan_description"] = override["description"]
        if override.get("note"):
            item["plan_note"] = override["note"]
        if override.get("cluster"):
            cluster_name = override["cluster"]
            cluster_data = clusters.get(cluster_name, {})
            item["plan_cluster"] = {
                "name": cluster_name,
                "description": cluster_data.get("description"),
                "total_items": len(cluster_data.get("finding_ids", [])),
            }

    ordered: list[dict] = []
    ordered_ids: set[str] = set()
    for finding_id in queue_order:
        if finding_id in by_id and finding_id not in skipped_ids:
            ordered.append(by_id[finding_id])
            ordered_ids.add(finding_id)

    skipped_items: list[dict] = []
    remaining_existing: list[dict] = []
    remaining_new: list[dict] = []
    _new = new_ids or set()
    for item in items:
        item_id = item["id"]
        if item_id in ordered_ids:
            continue
        if item_id in skipped_ids:
            skipped_items.append(item)
        elif item_id in _new:
            remaining_new.append(item)
        else:
            remaining_existing.append(item)

    result = ordered + remaining_existing + remaining_new

    # Triage stage IDs can appear in queue_order, so plan ordering may
    # scramble their dependency order.  Re-sort just the stage items
    # in-place to restore unblocked-before-blocked invariant.
    stage_entries = [
        (i, item) for i, item in enumerate(result)
        if item.get("kind") == "workflow_stage"
    ]
    if len(stage_entries) > 1:
        sorted_stages = sorted(
            [item for _, item in stage_entries],
            key=lambda it: (
                1 if it.get("is_blocked") else 0,
                int(it.get("stage_index", 0)),
            ),
        )
        for (idx, _), replacement in zip(stage_entries, sorted_stages):
            result[idx] = replacement

    if include_skipped:
        result = result + skipped_items

    for position, item in enumerate(result):
        item["queue_position"] = position + 1
        if item["id"] in skipped_ids:
            item["plan_skipped"] = True
            skip_entry = skipped_map.get(item["id"])
            if skip_entry:
                item["plan_skip_kind"] = skip_entry.get("kind", "temporary")
                skip_reason = skip_entry.get("reason")
                if skip_reason:
                    item["plan_skip_reason"] = skip_reason

    effective_cluster = cluster or active_cluster
    if effective_cluster:
        cluster_data = clusters.get(effective_cluster, {})
        cluster_member_ids = set(cluster_data.get("finding_ids", []))
        if cluster_member_ids:
            result = [item for item in result if item["id"] in cluster_member_ids]
    return result


def action_type_for_detector(detector: str) -> str:
    """Look up the action_type for a detector from the registry."""
    try:
        from desloppify.core.registry import DETECTORS

        meta = DETECTORS.get(detector)
        if meta:
            return meta.action_type
    except ImportError as exc:
        _ = exc
    return "manual_fix"


def _build_cluster_meta(
    cluster_name: str, members: list[dict], cluster_data: dict
) -> dict:
    """Build a cluster meta-item from its member items."""
    detector = members[0].get("detector", "") if members else ""
    action = cluster_data.get("action") or ""
    if "desloppify fix" in action:
        action_type = "auto_fix"
    elif "desloppify move" in action:
        action_type = "reorganize"
    else:
        action_type = action_type_for_detector(detector)
        if action_type == "auto_fix" and "desloppify fix" not in action:
            action_type = "refactor"

    stored_desc = cluster_data.get("description") or ""
    total_in_cluster = len(cluster_data.get("finding_ids", []))
    if stored_desc and total_in_cluster != len(members):
        summary = stored_desc.replace(str(total_in_cluster), str(len(members)))
    else:
        summary = stored_desc or f"{len(members)} findings"

    primary_command = cluster_data.get("action")
    if not primary_command:
        primary_command = f"desloppify next --cluster {cluster_name} --count 10"

    estimated_impact = max(
        (m.get("estimated_impact", 0.0) for m in members), default=0.0
    )

    return {
        "id": cluster_name,
        "kind": "cluster",
        "action_type": action_type,
        "summary": summary,
        "members": members,
        "member_count": len(members),
        "primary_command": primary_command,
        "cluster_name": cluster_name,
        "cluster_auto": True,
        "cluster_optional": bool(cluster_data.get("optional")),
        "confidence": "high",
        "detector": detector,
        "file": "",
        "estimated_impact": estimated_impact,
    }


def collapse_clusters(items: list[dict], plan: dict) -> list[dict]:
    """Replace cluster member items with single cluster meta-items.

    Walks the list in order: the first member of each collapsed cluster is
    replaced with its meta-item, subsequent members are skipped.  This
    preserves the ordering established by sort + plan-order.
    """
    clusters = plan.get("clusters", {})
    if not clusters:
        return items

    fid_to_cluster: dict[str, str] = {}
    for name, cluster in clusters.items():
        if not cluster.get("auto"):
            continue
        for finding_id in cluster.get("finding_ids", []):
            fid_to_cluster[finding_id] = name

    if not fid_to_cluster:
        return items

    # Collect members per cluster (preserving encounter order)
    cluster_members: dict[str, list[dict]] = {}
    for item in items:
        cname = fid_to_cluster.get(item.get("id", ""))
        if cname:
            cluster_members.setdefault(cname, []).append(item)

    # Build meta-items only for clusters with 2+ members in the queue
    meta_items: dict[str, dict] = {}
    for cname, members in cluster_members.items():
        if len(members) < 2:
            continue
        meta_items[cname] = _build_cluster_meta(
            cname, members, clusters.get(cname, {})
        )

    # Walk in order: replace first member of each collapsed cluster
    # with its meta-item, skip subsequent members
    seen_clusters: set[str] = set()
    result: list[dict] = []
    for item in items:
        cname = fid_to_cluster.get(item.get("id", ""))
        if cname and cname in meta_items:
            if cname not in seen_clusters:
                seen_clusters.add(cname)
                result.append(meta_items[cname])
            # skip individual member
        else:
            result.append(item)
    return result


__all__ = [
    "apply_plan_order",
    "collapse_clusters",
    "new_item_ids",
]
