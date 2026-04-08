---
name: hrevn-baseline-check
description: Run an HREVN baseline check before critical or governance-sensitive actions to determine profile, readiness, missing blocks, risk flags and next step.
---

# HREVN Baseline Check

## Use this skill when
- a workflow needs a pre-flight governance or integrity check
- a task may fall under `eu_readiness_profile`, `mica_readiness_profile`, or `agentic_finance_profile`
- you want to know what is missing before executing a consequential action
- you need a structured `BaselineResult`

## Do not use this skill when
- the task is trivial and not consequential
- the user only wants a generic explanation with no structured assessment

## Required behavior
1. Respect explicit `profile` first.
2. Otherwise apply BC1 profile detection.
3. Compute:
   - `profile_detected`
   - `missing_required_blocks`
   - `risk_flags`
   - `readiness_level`
   - `recommended_next_step`
4. Build `remedy_payload` only from missing required blocks.
5. Do not invent profiles or legal conclusions.

## Runtime bridge
When `HREVN_API_KEY` is available, prefer the managed runtime:

```bash
python3 scripts/hrevn_managed_api.py baseline-check \
  --input examples/baseline_check_request.json
```

Use `https://api.hrevn.com` as the default managed endpoint unless the user has
configured a different `HREVN_API_BASE_URL`.

In this alpha, the default supported path is the local helper bridge. If Codex
also has HREVN MCP configured, the `baseline_check` MCP tool is available as an
optional secondary path.

## Canonical references
- `references/HREVN_BC1_PROFILE_DETECTION_TABLE.md`
- `references/HREVN_BASELINE_DECISION_RULES.md`
- `references/HREVN_CORE_NAMING_DECISIONS.md`

## Output naming
Use:
- `BaselineResult` for the pre-flight assessment
- reserve `AER` for the post-action evidence receipt
