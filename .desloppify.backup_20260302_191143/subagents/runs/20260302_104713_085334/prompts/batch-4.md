You are a focused subagent reviewer for a single holistic investigation batch.

Repository root: /Users/peteromalley/Documents/desloppify
Blind packet: /Users/peteromalley/Documents/desloppify/.desloppify/review_packets/review_packet_blind_20260302_104713_085334.json
Batch index: 4
Batch name: Design coherence — Mechanical Concern Signals
Batch dimensions: design_coherence
Batch rationale: mechanical detectors identified structural patterns needing judgment; concern types: design_concern, duplication_design, mixed_responsibilities, systemic_pattern; truncated to 80 files from 90 candidates

Mechanical scan evidence: The blind packet contains `holistic_context.scan_evidence` with aggregated signals from all mechanical detectors — including complexity hotspots, security hotspots, signal density index (files flagged by multiple detectors), private crossings, and systemic patterns. Consult this section for investigative leads beyond the seed files.

Seed files (start here):
- desloppify/app/commands/review/runner_failures.py
- desloppify/app/commands/review/runner_parallel.py
- desloppify/intelligence/narrative/core.py
- desloppify/intelligence/review/context_holistic/mechanical.py
- desloppify/languages/_framework/base/types.py
- desloppify/languages/_framework/registry_state.py
- desloppify/languages/python/detectors/deps.py
- desloppify/languages/typescript/extractors.py
- desloppify/app/commands/fix/review_flow.py
- desloppify/app/commands/helpers/score_update.py
- desloppify/app/commands/next.py
- desloppify/app/commands/plan/cluster_handlers.py
- desloppify/app/commands/review/batch_merge.py
- desloppify/app/commands/review/external.py
- desloppify/app/commands/review/import_cmd.py
- desloppify/app/commands/show/cmd.py
- desloppify/core/source_discovery.py
- desloppify/engine/hook_registry.py
- desloppify/intelligence/review/__init__.py
- desloppify/intelligence/review/dimensions/data.py
- desloppify/languages/csharp/__init__.py
- desloppify/languages/csharp/_parse_helpers.py
- desloppify/languages/csharp/deps/cli.py
- desloppify/languages/csharp/detectors/deps.py
- desloppify/languages/dart/__init__.py
- desloppify/languages/dart/commands.py
- desloppify/languages/dart/detectors/deps.py
- desloppify/languages/dart/extractors.py
- desloppify/languages/dart/phases.py
- desloppify/languages/gdscript/extractors.py
- desloppify/languages/go/__init__.py
- desloppify/languages/python/commands.py
- desloppify/languages/python/detectors/private_imports.py
- desloppify/languages/python/detectors/ruff_smells.py
- desloppify/languages/python/detectors/smells.py
- desloppify/languages/python/move.py
- desloppify/languages/python/phases.py
- desloppify/languages/typescript/detectors/exports.py
- desloppify/languages/typescript/detectors/react.py
- desloppify/languages/typescript/fixers/if_chain.py
- desloppify/app/cli_support/parser_groups_admin.py
- desloppify/app/commands/fix/apply_flow.py
- desloppify/app/commands/next_parts/render.py
- desloppify/app/commands/plan/override_handlers.py
- desloppify/app/commands/plan/synthesis/shared.py
- desloppify/app/commands/resolve/render.py
- desloppify/app/commands/review/batch.py
- desloppify/app/commands/review/batch_core.py
- desloppify/app/commands/review/batches_scope.py
- desloppify/app/commands/review/coordinator.py
- desloppify/app/commands/review/import_output.py
- desloppify/app/commands/review/import_policy.py
- desloppify/app/commands/review/runner_helpers.py
- desloppify/app/commands/review/runner_process.py
- desloppify/app/commands/scan/scan_reporting_dimensions.py
- desloppify/app/commands/scan/scan_reporting_subjective.py
- desloppify/app/commands/scan/scan_workflow.py
- desloppify/app/commands/show/scope.py
- desloppify/app/commands/status_parts/render.py
- desloppify/core/registry.py
- desloppify/core/subjective_dimensions.py
- desloppify/engine/_plan/epic_synthesis.py
- desloppify/engine/_plan/operations.py
- desloppify/engine/_plan/schema.py
- desloppify/engine/_plan/stale_dimensions.py
- desloppify/engine/_state/schema.py
- desloppify/engine/_work_queue/helpers.py
- desloppify/engine/_work_queue/ranking.py
- desloppify/engine/concerns.py
- desloppify/engine/detectors/coverage/mapping.py
- desloppify/intelligence/review/context_holistic/budget.py
- desloppify/intelligence/review/context_holistic/selection.py
- desloppify/intelligence/review/importing/holistic.py
- desloppify/intelligence/review/importing/shared.py
- desloppify/intelligence/review/prepare.py
- desloppify/intelligence/review/selection.py
- desloppify/languages/_framework/base/shared_phases.py
- desloppify/languages/_framework/commands_base.py
- desloppify/languages/_framework/finding_factories.py
- desloppify/languages/_framework/generic.py

Mechanical concern signals (detector synthesis hypotheses):
Treat each as a hypothesis: confirm or refute with direct code evidence.
  - [design_concern] desloppify/app/commands/review/runner_failures.py
    summary: Design signals from props, structural
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: props, structural
    evidence: [structural] Needs decomposition: large (339 LOC)
  - [design_concern] desloppify/app/commands/review/runner_parallel.py
    summary: Design signals from smells, structural
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: smells, structural
    evidence: [structural] Needs decomposition: large (471 LOC)
  - [design_concern] desloppify/intelligence/narrative/core.py
    summary: Design signals from smells, structural
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: smells, structural
    evidence: [structural] Needs decomposition: large (393 LOC)
  - [design_concern] desloppify/intelligence/review/context_holistic/mechanical.py
    summary: Design signals from smells, structural
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: smells, structural
    evidence: [structural] Needs decomposition: large (605 LOC)
  - [design_concern] desloppify/languages/_framework/base/types.py
    summary: Design signals from cycles, structural
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: cycles, structural
    evidence: [structural] Needs decomposition: large (359 LOC)
  - [design_concern] desloppify/languages/_framework/registry_state.py
    summary: Design signals from global_mutable_config
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: global_mutable_config
    evidence: [global_mutable_config] Module-level mutable '_registry' (line 35) modified from 2 site(s)
  - [design_concern] desloppify/languages/python/detectors/deps.py
    summary: Design signals from smells, structural
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: smells, structural
    evidence: [structural] Needs decomposition: large (306 LOC) / complexity score 30
  - [design_concern] desloppify/languages/typescript/extractors.py
    summary: Design signals from structural, uncalled_functions
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: structural, uncalled_functions
    evidence: [structural] Needs decomposition: complexity score 40
  - (+4 more concern signals)

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
6. Every finding must include canonical contract fields: `dimension`, `identifier`, `summary`, `confidence`, `suggestion`, `related_files`, `evidence`.
6a. `confidence` must be one of: high|low|medium.
7. Every finding must provide `impact_scope` and `fix_scope` directly, or rely on dimension_notes defaults.
8. Every scored dimension MUST include dimension_notes with concrete evidence.
9. If a dimension score is >85.0, include `issues_preventing_higher_score` in dimension_notes.
10. Use exactly one decimal place for every assessment and abstraction sub-axis score.
9f. For design_coherence, use evidence from `holistic_context.scan_evidence.signal_density` — files where multiple mechanical detectors fired. Investigate what design change would address multiple signals simultaneously. Check `scan_evidence.complexity_hotspots` for files with high responsibility cluster counts.
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
  "batch": "Design coherence — Mechanical Concern Signals",
  "batch_index": 4,
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
