You are a focused subagent reviewer for a single holistic investigation batch.

Repository root: /Users/peteromalley/Documents/desloppify
Blind packet: /Users/peteromalley/Documents/desloppify/.desloppify/review_packet_blind.json
Batch index: 12
Batch name: Full Codebase Sweep
Batch dimensions: naming_quality, logic_clarity, type_safety, contract_coherence, error_consistency, abstraction_fitness, ai_generated_debt, high_level_elegance, mid_level_elegance, low_level_elegance, cross_module_architecture, initialization_coupling, convention_outlier, dependency_health, test_strategy, api_surface_coherence, authorization_consistency, incomplete_migration, package_organization, design_coherence
Batch rationale: thorough default: evaluate cross-cutting quality across all production files

Mechanical scan evidence: The blind packet contains `holistic_context.scan_evidence` with aggregated signals from all mechanical detectors — including complexity hotspots, error hotspots, signal density index (files flagged by multiple detectors), boundary violations, and systemic patterns. Consult this section for investigative leads beyond the seed files.

Seed files (start here):
- .github/scripts/roslyn_stub.py
- desloppify/__init__.py
- desloppify/__main__.py
- desloppify/app/__init__.py
- desloppify/app/cli_support/__init__.py
- desloppify/app/cli_support/parser.py
- desloppify/app/cli_support/parser_groups.py
- desloppify/app/cli_support/parser_groups_admin.py
- desloppify/app/commands/__init__.py
- desloppify/app/commands/_show_terminal.py
- desloppify/app/commands/config_cmd.py
- desloppify/app/commands/detect.py
- desloppify/app/commands/dev_cmd.py
- desloppify/app/commands/dev_scaffold_templates.py
- desloppify/app/commands/exclude_cmd.py
- desloppify/app/commands/fix/__init__.py
- desloppify/app/commands/fix/apply_flow.py
- desloppify/app/commands/fix/cmd.py
- desloppify/app/commands/fix/options.py
- desloppify/app/commands/fix/review_flow.py
- desloppify/app/commands/helpers/__init__.py
- desloppify/app/commands/helpers/guardrails.py
- desloppify/app/commands/helpers/lang.py
- desloppify/app/commands/helpers/query.py
- desloppify/app/commands/helpers/queue_progress.py
- desloppify/app/commands/helpers/rendering.py
- desloppify/app/commands/helpers/runtime.py
- desloppify/app/commands/helpers/runtime_options.py
- desloppify/app/commands/helpers/score.py
- desloppify/app/commands/helpers/score_update.py
- desloppify/app/commands/helpers/state.py
- desloppify/app/commands/helpers/subjective.py
- desloppify/app/commands/langs.py
- desloppify/app/commands/move/__init__.py
- desloppify/app/commands/move/move.py
- desloppify/app/commands/move/move_apply.py
- desloppify/app/commands/move/move_directory.py
- desloppify/app/commands/move/move_language.py
- desloppify/app/commands/move/move_planning.py
- desloppify/app/commands/move/move_reporting.py
- desloppify/app/commands/next.py
- desloppify/app/commands/next_parts/__init__.py
- desloppify/app/commands/next_parts/output.py
- desloppify/app/commands/next_parts/render.py
- desloppify/app/commands/plan/__init__.py
- desloppify/app/commands/plan/_resolve.py
- desloppify/app/commands/plan/cluster_handlers.py
- desloppify/app/commands/plan/cmd.py
- desloppify/app/commands/plan/move_handlers.py
- desloppify/app/commands/plan/override_handlers.py
- desloppify/app/commands/plan/queue_render.py
- desloppify/app/commands/plan/synthesis_playbook.py
- desloppify/app/commands/plan/synthesize_handlers.py
- desloppify/app/commands/plan_cmd.py
- desloppify/app/commands/registry.py
- desloppify/app/commands/resolve/__init__.py
- desloppify/app/commands/resolve/apply.py
- desloppify/app/commands/resolve/cmd.py
- desloppify/app/commands/resolve/render.py
- desloppify/app/commands/resolve/selection.py
- desloppify/app/commands/review/__init__.py
- desloppify/app/commands/review/assessment_integrity.py
- desloppify/app/commands/review/batch.py
- desloppify/app/commands/review/batch_core.py
- desloppify/app/commands/review/batch_prompt_template.py
- desloppify/app/commands/review/batch_scoring.py
- desloppify/app/commands/review/batches.py
- desloppify/app/commands/review/entrypoint.py
- desloppify/app/commands/review/external.py
- desloppify/app/commands/review/helpers.py
- desloppify/app/commands/review/import_cmd.py
- desloppify/app/commands/review/import_helpers.py
- desloppify/app/commands/review/importing/__init__.py
- desloppify/app/commands/review/importing/modes.py
- desloppify/app/commands/review/merge.py
- desloppify/app/commands/review/packet_policy.py
- desloppify/app/commands/review/preflight.py
- desloppify/app/commands/review/prepare.py
- desloppify/app/commands/review/runner_helpers.py
- desloppify/app/commands/review/runtime/__init__.py

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
3. Return 0-20 high-quality findings for this batch (empty array allowed).
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
9a. For package_organization, ground scoring in objective structure signals from `holistic_context.structure` (root_files fan_in/fan_out roles, directory_profiles, coupling_matrix). Prefer thresholded evidence (for example: fan_in < 5 for root stragglers, import-affinity > 60%, directories > 10 files with mixed concerns).
9b. Suggestions must include a staged reorg plan (target folders, move order, and import-update/validation commands).
9c. Also consult `holistic_context.structure.flat_dir_findings` for directories flagged as overloaded, fragmented, or thin-wrapper patterns.
9d. For abstraction_fitness, use evidence from `holistic_context.abstractions`:
  - `delegation_heavy_classes`: classes where most methods forward to an inner object — entries include class_name, delegate_target, sample_methods, and line number.
  - `facade_modules`: re-export-only modules with high re_export_ratio — entries include samples (re-exported names) and loc.
  - `typed_dict_violations`: TypedDict fields accessed via .get()/.setdefault()/.pop() — entries include typed_dict_name, violation_type, field, and line number.
  - `complexity_hotspots`: files where mechanical analysis found extreme parameter counts, deep nesting, or disconnected responsibility clusters.
  Include `delegation_density`, `definition_directness`, and `type_discipline` alongside existing sub-axes in dimension_notes when evidence supports it.
9e. For initialization_coupling, use evidence from `holistic_context.scan_evidence.mutable_globals` and `holistic_context.errors.mutable_globals`. Investigate initialization ordering dependencies, coupling through shared mutable state, and whether state should be encapsulated behind a proper registry/context manager.
9f. For design_coherence, use evidence from `holistic_context.scan_evidence.signal_density` — files where multiple mechanical detectors fired. Investigate what design change would address multiple signals simultaneously. Check `scan_evidence.complexity_hotspots` for files with high responsibility cluster counts.
9g. For error_consistency, use evidence from `holistic_context.errors.exception_hotspots` — files with concentrated exception handling findings. Investigate whether error handling is designed or accidental. Check for broad catches masking specific failure modes.
9h. For cross_module_architecture, also consult `holistic_context.coupling.boundary_violations` for import paths that cross architectural boundaries, and `holistic_context.dependencies.deferred_import_density` for files with many function-level imports (proxy for cycle pressure).
9i. For convention_outlier, also consult `holistic_context.conventions.duplicate_clusters` for cross-file function duplication and `conventions.naming_drift` for directory-level naming inconsistency.
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
  "batch": "Full Codebase Sweep",
  "batch_index": 12,
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
