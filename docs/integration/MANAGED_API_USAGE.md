# HREVN Codex -> Managed API

## Goal
Connect the Codex plugin surface to the same HREVN managed runtime used by all other surfaces.

## Current path
- plugin bundle as public entry
- skills-first invocation model
- managed API as runtime bridge
- MCP later when the shared tooling bridge is mature

## Required environment

```bash
export HREVN_API_BASE_URL="https://api.hrevn.com"
export HREVN_API_KEY="replace-me"
```

Public managed endpoint:
- `https://api.hrevn.com`

## First useful call

### Baseline check
`POST /v1/baseline-check`

Example request:

```json
{
  "task_type": "ai_workflow",
  "profile": "eu_readiness_profile",
  "record": {
    "human_oversight": {},
    "risk_register": {},
    "evidence_lifecycle": {}
  },
  "metadata": {
    "surface": "codex"
  }
}
```

Example `curl`:

```bash
curl -s -X POST "https://api.hrevn.com/v1/baseline-check" \
  -H "Authorization: Bearer ${HREVN_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @examples/baseline_check_request.json
```

## Bundle operations
- `POST /v1/generate-bundle`
- `POST /v1/verify-bundle`
- `GET /v1/bundles/{bundle_id}/download`

## Local helper for Codex

This bundle now includes:
- installable CLI package `hrevn-codex-cli`
- `scripts/hrevn_managed_api.py`

Minimal usage:

```bash
pipx install hrevn-codex-cli
export HREVN_API_KEY="replace-me"
hrevn-codex health-check
hrevn-codex self-test
hrevn-codex baseline
```

Generate a bundle:

```bash
hrevn-codex generate-bundle --input examples/generate_bundle_request.json
```

## Rule
The Codex surface should not reimplement HREVN semantics locally.
It should call the managed runtime and present the result cleanly inside Codex.
