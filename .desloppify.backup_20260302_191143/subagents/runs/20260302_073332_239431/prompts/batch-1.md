You are a focused subagent reviewer for a single holistic investigation batch.

Repository root: /Users/peteromalley/Documents/desloppify
Blind packet: /Users/peteromalley/Documents/desloppify/.desloppify/review_packets/review_packet_blind_20260302_073332_239431.json
Batch index: 1
Batch name: Abstractions & Dependencies
Batch dimensions: low_level_elegance
Batch rationale: abstraction hotspots (wrappers/interfaces/param bags/delegation-heavy classes/facade modules/TypedDict violations), dep cycles

Mechanical scan evidence: The blind packet contains `holistic_context.scan_evidence` with aggregated signals from all mechanical detectors — including complexity hotspots, security hotspots, signal density index (files flagged by multiple detectors), private crossings, and systemic patterns. Consult this section for investigative leads beyond the seed files.

Seed files (start here):
- desloppify/engine/_work_queue/helpers.py
- desloppify/intelligence/review/_prepare/helpers.py
- desloppify/languages/typescript/fixers/common.py
- desloppify/engine/planning/common.py
- desloppify/app/commands/review/helpers.py
- desloppify/app/commands/scan/scan_workflow.py
- desloppify/engine/planning/synthesis.py
- desloppify/core/_internal/coercions.py
- desloppify/core/_internal/text_utils.py
- desloppify/core/registry.py
- desloppify/core/source_discovery.py
- desloppify/intelligence/review/_context/models.py
- desloppify/languages/typescript/detectors/deps.py
- desloppify/app/commands/helpers/query.py
- desloppify/core/source_scan_api.py
- desloppify/core/subjective_dimensions.py
- desloppify/engine/policy/zones.py
- desloppify/languages/_framework/generic.py
- desloppify/app/commands/scan/scan_reporting_subjective.py
- desloppify/engine/_scoring/results/core.py
- desloppify/engine/_scoring/subjective/core.py
- desloppify/engine/detectors/patterns/security.py
- desloppify/intelligence/review/dimensions/__init__.py
- desloppify/intelligence/review/dimensions/metadata.py
- desloppify/languages/_framework/base/shared_phases.py
- desloppify/app/commands/scan/scan.py
- desloppify/languages/python/detectors/smells_ast/_node_detectors.py
- desloppify/languages/python/detectors/smells_ast/_tree_context_detectors.py
- desloppify/languages/python/detectors/smells_ast/_tree_safety_detectors.py
- desloppify/languages/python/detectors/smells_ast/_tree_quality_detectors_types.py
- desloppify/languages/python/detectors/smells_ast/_tree_quality_detectors.py
- desloppify/languages/python/detectors/smells_ast/__init__.py
- desloppify/languages/python/detectors/smells_ast/_dispatch.py
- desloppify/languages/python/detectors/smells_ast/_tree_safety_detectors_runtime.py
- desloppify/languages/typescript/phases.py
- desloppify/languages/typescript/__init__.py
- desloppify/intelligence/review/prepare_batches.py
- desloppify/languages/python/__init__.py
- desloppify/languages/python/phases.py
- desloppify/languages/csharp/__init__.py
- desloppify/intelligence/review/prepare.py
- desloppify/languages/python/detectors/dict_keys_visitor.py
- desloppify/app/commands/review/batch.py
- desloppify/app/output/scorecard_parts/left_panel.py
- desloppify/intelligence/review/importing/holistic.py
- desloppify/app/commands/review/batch_merge.py
- desloppify/app/commands/review/runner_parallel.py
- desloppify/app/commands/review/coordinator.py
- desloppify/intelligence/review/importing/shared.py
- desloppify/app/commands/review/external.py
- desloppify/app/commands/review/batches.py
- desloppify/app/commands/next_parts/render.py
- desloppify/app/commands/review/batch_core.py
- desloppify/app/commands/review/batches_runtime.py
- desloppify/app/commands/review/runner_helpers.py
- desloppify/app/commands/scan/scan_wontfix.py
- desloppify/engine/_state/merge_history.py
- desloppify/app/commands/review/runner_process.py
- desloppify/intelligence/narrative/action_engine.py
- desloppify/app/commands/review/runner_packets.py
- desloppify/languages/typescript/detectors/security.py
- desloppify/app/commands/review/import_cmd.py
- desloppify/languages/_framework/runtime.py
- desloppify/languages/typescript/detectors/props.py
- desloppify/app/cli_support/parser_groups.py
- desloppify/app/cli_support/parser_groups_admin.py
- desloppify/app/commands/fix/apply_flow.py
- desloppify/app/commands/fix/options.py
- desloppify/app/commands/fix/review_flow.py
- desloppify/app/commands/plan/synthesis/organize.py
- desloppify/app/commands/plan/synthesis/reflect.py
- desloppify/app/commands/resolve/render.py
- desloppify/engine/detectors/security/filters.py
- desloppify/engine/detectors/test_coverage/discovery.py
- desloppify/engine/detectors/test_coverage/metrics.py
- desloppify/engine/work_queue.py
- desloppify/intelligence/narrative/__init__.py
- desloppify/intelligence/narrative/dimensions.py
- desloppify/intelligence/narrative/phase.py
- desloppify/intelligence/review/context_holistic/__init__.py

Task requirements:
1. Read the blind packet and follow `system_prompt` constraints exactly.
1a. If previously flagged issues are listed above, use them as context for your review.
    Verify whether each still applies to the current code. Do not re-report fixed or
    wontfix issues. Use them as starting points to look deeper — inspect adjacent code
    and related modules for defects the prior review may have missed.
1b. If mechanical concern signals are listed above, explicitly confirm or refute them.
    Report confirmed defects under the most impacted batch dimension.
    If refuting, include clear counter-evidence in `dimension_notes`.
1c. Think structurally: when you spot multiple individual issues that share a common
    root cause (missing abstraction, duplicated pattern, inconsistent convention),
    explain the deeper structural issue in the finding, not just the surface symptom.
    If the pattern is significant enough, report the structural issue as its own finding
    with appropriate fix_scope ('multi_file_refactor' or 'architectural_change') and
    use `root_cause_cluster` to connect related symptom findings together.
2. Start with the seed files, then freely explore additional repository files likely to surface material issues.
2a. Prioritize high-signal leads: unexplored/lightly reviewed files, historical issue areas, and hotspot neighbors (high coupling, god modules, large files, churn seams).
2b. Keep exploration targeted — follow strongest evidence paths first instead of attempting exhaustive coverage.
2c. Keep findings and scoring scoped to this batch's listed dimensions.
2d. Respect scope controls in the blind packet config: do not include files/directories marked by `exclude`, `ignore`, or zone overrides that classify files as non-production (test/config/generated/vendor).
3. Return 0-10 high-quality findings for this batch (empty array allowed).
3a. Do not suppress real defects to keep scores high; report every material issue you can support with evidence.
3b. Do not default to 100. Reserve 100 for genuinely exemplary evidence in this batch.
4. Score/finding consistency is required: broader or more severe findings MUST lower dimension scores.
4a. Any dimension scored below 85.0 MUST include explicit feedback: add at least one finding with the same `dimension` and a non-empty actionable `suggestion`.
5. Every finding must include `related_files` with at least 2 files when possible.
6. Every finding must include `dimension`, `identifier`, `summary`, `evidence`, `suggestion`, and `confidence`.
7. Every finding must include `impact_scope` and `fix_scope`.
8. Every scored dimension MUST include dimension_notes with concrete evidence.
9. If a dimension score is >85.0, include `issues_preventing_higher_score` in dimension_notes.
10. Use exactly one decimal place for every assessment and abstraction sub-axis score.
11. Ignore prior chat context and any target-threshold assumptions.
12. Do not edit repository files.
13. Return ONLY valid JSON, no markdown fences.

Scope enums:
- impact_scope: "local" | "module" | "subsystem" | "codebase"
- fix_scope: "single_edit" | "multi_file_refactor" | "architectural_change"

Output schema:
{
  "batch": "Abstractions & Dependencies",
  "batch_index": 1,
  "assessments": {"<dimension>": <0-100 with one decimal place>},
  "dimension_notes": {
    "<dimension>": {
      "evidence": ["specific code observations"],
      "impact_scope": "local|module|subsystem|codebase",
      "fix_scope": "single_edit|multi_file_refactor|architectural_change",
      "confidence": "high|medium|low",
      "issues_preventing_higher_score": "required when score >85.0",
      "sub_axes": {"abstraction_leverage": 0-100, "indirection_cost": 0-100, "interface_honesty": 0-100, "delegation_density": 0-100, "definition_directness": 0-100, "type_discipline": 0-100}  // required for abstraction_fitness when evidence supports it; all one decimal place
    }
  },
  "findings": [{
    "dimension": "<dimension>",
    "identifier": "short_id",
    "summary": "one-line defect summary",
    "related_files": ["relative/path.py"],
    "evidence": ["specific code observation"],
    "suggestion": "concrete fix recommendation",
    "confidence": "high|medium|low",
    "impact_scope": "local|module|subsystem|codebase",
    "fix_scope": "single_edit|multi_file_refactor|architectural_change",
    "root_cause_cluster": "optional_cluster_name_when_supported_by_history"
  }],
  "retrospective": {
    "root_causes": ["optional: concise root-cause hypotheses"],
    "likely_symptoms": ["optional: identifiers that look symptom-level"],
    "possible_false_positives": ["optional: prior concept keys likely mis-scoped"]
  }
}
