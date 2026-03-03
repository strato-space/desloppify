You are a focused subagent reviewer for a single holistic investigation batch.

Repository root: /Users/peteromalley/Documents/desloppify
Blind packet: /Users/peteromalley/Documents/desloppify/.desloppify/review_packet_blind.json
Batch index: 2
Batch name: Conventions & Errors
Batch dimensions: mid_level_elegance
Batch rationale: naming drift, behavioral outliers, mixed error strategies, exception hotspots, duplicate clusters

Mechanical scan evidence: The blind packet contains `holistic_context.scan_evidence` with aggregated signals from all mechanical detectors — including complexity hotspots, security hotspots, signal density index (files flagged by multiple detectors), private crossings, and systemic patterns. Consult this section for investigative leads beyond the seed files.

Seed files (start here):
- desloppify/app/commands/dev_scaffold_templates.py
- desloppify/app/commands/registry.py
- desloppify/app/commands/_show_terminal.py
- desloppify/app/commands/viz_cmd.py
- desloppify/app/commands/fix/options.py
- desloppify/app/commands/helpers/lang.py
- desloppify/app/commands/helpers/runtime.py
- desloppify/app/commands/helpers/score.py
- desloppify/app/commands/move/move_language.py
- desloppify/app/commands/move/move_planning.py
- desloppify/app/commands/move/move_reporting.py
- desloppify/app/commands/plan/_resolve.py
- desloppify/app/commands/plan/synthesis_playbook.py
- desloppify/app/commands/plan/cmd.py
- desloppify/app/commands/plan/synthesis/shared.py
- desloppify/app/commands/plan/synthesis/organize.py
- desloppify/app/commands/resolve/render.py
- desloppify/app/commands/show/formatting.py
- desloppify/app/commands/show/payload.py
- desloppify/app/commands/status_parts/strict_target.py
- desloppify/app/output/tree_text.py
- desloppify/app/output/visualize.py
- desloppify/scoring.py
- desloppify/state.py
- desloppify/engine/_plan/epic_synthesis.py
- desloppify/engine/_plan/stale_dimensions.py
- desloppify/engine/detectors/base.py
- desloppify/engine/detectors/dupes.py
- desloppify/engine/detectors/gods.py
- desloppify/engine/detectors/passthrough.py
- desloppify/engine/detectors/signature.py
- desloppify/intelligence/review/_context/patterns.py
- desloppify/intelligence/review/feedback_contract.py
- desloppify/intelligence/review/finding_merge.py
- desloppify/intelligence/review/policy.py
- desloppify/intelligence/review/context_holistic/mechanical.py
- desloppify/intelligence/review/context_holistic/readers.py
- desloppify/intelligence/review/importing/contracts.py
- desloppify/languages/_framework/base/phase_builders.py
- desloppify/languages/_framework/contract_validation.py
- desloppify/languages/_framework/policy.py
- desloppify/languages/_framework/registry_state.py
- desloppify/languages/_framework/runtime.py
- desloppify/languages/_framework/generic_parts/tool_spec.py
- desloppify/languages/_framework/treesitter/_cache.py
- desloppify/languages/_framework/treesitter/_specs.py
- desloppify/languages/_framework/treesitter/phases.py
- desloppify/languages/_framework/treesitter/_normalize.py
- desloppify/languages/csharp/commands.py
- desloppify/languages/csharp/move.py
- desloppify/languages/python/extractors.py
- desloppify/languages/python/review.py
- desloppify/languages/python/detectors/complexity.py
- desloppify/languages/python/detectors/dict_keys_visitor.py
- desloppify/languages/python/detectors/unused.py
- desloppify/languages/python/detectors/facade.py
- desloppify/languages/python/detectors/import_linter_adapter.py
- desloppify/languages/python/detectors/bandit_adapter.py
- desloppify/languages/python/detectors/private_imports.py
- desloppify/languages/python/detectors/ruff_smells.py
- desloppify/languages/python/detectors/smells.py
- desloppify/languages/python/detectors/uncalled.py
- desloppify/languages/typescript/commands.py
- desloppify/languages/typescript/extractors.py
- desloppify/languages/typescript/move.py
- desloppify/languages/typescript/review.py
- desloppify/languages/typescript/detectors/contracts.py
- desloppify/languages/typescript/detectors/_smell_detectors.py
- desloppify/languages/typescript/detectors/_smell_helpers.py
- desloppify/languages/typescript/detectors/facade.py
- desloppify/languages/typescript/detectors/deps_runtime.py
- desloppify/languages/typescript/detectors/exports.py
- desloppify/languages/typescript/detectors/knip_adapter.py
- desloppify/languages/typescript/detectors/security.py
- desloppify/languages/typescript/fixers/common.py
- desloppify/languages/typescript/fixers/fixer_io.py
- desloppify/languages/typescript/fixers/import_rewrite.py
- desloppify/languages/typescript/fixers/syntax_scan.py
- desloppify/languages/csharp/_parse_helpers.py
- desloppify/app/commands/fix/apply_flow.py

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
9j. Workflow integrity checks: when reviewing orchestration/queue/review flows,
    explicitly look for loop-prone patterns and blind spots:
    - repeated stale/reopen churn without clear exit criteria or gating,
    - packet/batch data being generated but dropped before prompt execution,
    - ranking/triage logic that can starve target-improving work,
    - reruns happening before existing open review work is drained.
    If found, propose concrete guardrails and where to implement them.
11. Ignore prior chat context and any target-threshold assumptions.
12. Do not edit repository files.
13. Return ONLY valid JSON, no markdown fences.

Scope enums:
- impact_scope: "local" | "module" | "subsystem" | "codebase"
- fix_scope: "single_edit" | "multi_file_refactor" | "architectural_change"

Output schema:
{
  "batch": "Conventions & Errors",
  "batch_index": 2,
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
