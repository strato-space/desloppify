# External Blind Review Session

Session id: ext_20260302_000342_f3c2c0fa
Session token: 8e09c168279bfffa18f3e565787a3630
Blind packet: /Users/peteromalley/Documents/desloppify/.desloppify/review_packet_blind.json
Template output: /Users/peteromalley/Documents/desloppify/.desloppify/external_review_sessions/ext_20260302_000342_f3c2c0fa/review_result.template.json
Claude launch prompt: /Users/peteromalley/Documents/desloppify/.desloppify/external_review_sessions/ext_20260302_000342_f3c2c0fa/claude_launch_prompt.md
Expected reviewer output: /Users/peteromalley/Documents/desloppify/.desloppify/external_review_sessions/ext_20260302_000342_f3c2c0fa/review_result.json

Happy path:
1. Open the Claude launch prompt file and paste it into a context-isolated subagent task.
2. Reviewer writes JSON output to the expected reviewer output path.
3. Submit with the printed --external-submit command.

Reviewer output requirements:
1. Return JSON with top-level keys: session, assessments, findings.
2. session.id must be `ext_20260302_000342_f3c2c0fa`.
3. session.token must be `8e09c168279bfffa18f3e565787a3630`.
4. Include findings with required schema fields (dimension/identifier/summary/related_files/evidence/suggestion/confidence).
5. Use the blind packet only (no score targets or prior context).
