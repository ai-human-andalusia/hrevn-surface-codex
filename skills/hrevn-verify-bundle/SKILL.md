---
name: hrevn-verify-bundle
description: Inspect HREVN baseline, receipt, manifest and related artifacts, explain what happened, and clarify whether the evidence trail is verified or merely described.
---

# HREVN Verify Bundle

## Use this skill when
- the user wants to inspect an HREVN receipt or execution trail
- you need to explain baseline, snapshot, receipt and manifest artifacts
- you want to verify the shape and meaning of an HREVN artifact bundle

## Do not use this skill when
- no HREVN artifacts exist
- the user only wants a conceptual overview

## Combination with other HREVN skills
- Usually third in sequence
- Use after baseline + sign-on-complete when artifacts exist
- Can be used alone only if HREVN artifacts already exist

## Required behavior
1. Inspect available artifacts:
   - baseline JSON
   - snapshot JSON
   - receipt JSON
   - manifest JSON
   - JSONL log stream
2. Summarize:
   - run id
   - profile
   - policy
   - readiness
   - success/failure
   - evidence hash
3. Be explicit about verified vs merely described information.

## Runtime bridge
When a bundle zip exists locally, prefer the managed verifier path:

```bash
python3 scripts/hrevn_managed_api.py verify-bundle \
  --source /absolute/path/to/bundle.zip
```

Use the managed result to separate:
- verified bundle integrity
- described but not verified narrative

## Canonical references
- `references/HREVN_STATE_GUARD_RECEIPT_SCHEMA_V1_2.json`
- `references/README_STATE_GUARD_V1_2.md`
- `references/HREVN_CORE_NAMING_DECISIONS.md`
