# HREVN Trust Layer for Codex

**Un solo núcleo. Tres superficies. Mismo resultado verificable.**

OpenAI changes the bundle.  
Anthropic changes the skill.  
Google changes the middleware.  
HREVN does not change its truth.

This repo is the Codex-facing HREVN surface: a skills-first plugin bundle with a live bridge to the managed runtime.

## Why HREVN

AI agents and multi-step workflows fail in ambiguous ways. When a sequence is
interrupted, neither the user nor the system can always determine with
certainty what completed, what failed mid-execution, and where work can safely
resume. Without a verifiable record, context is reconstructed from memory or
chat history, wasting tokens, repeating work, and leaving no reliable trail.

HREVN adds a structured evidence layer: baseline checks before consequential
steps, tamper-evident receipts after execution, and manifests that allow
workflows to continue from the last verified point rather than restarting from
scratch.

For teams operating in regulated or high-stakes environments, HREVN also
supports evidentiary discipline: structured records of what ran, under what
authority, and when it stopped. This is particularly relevant for AI systems
that may fall within EU regulatory timelines in 2026 and beyond. HREVN does
not make a system legally compliant, but it provides structured, verifiable
evidence that compliance, audit, and governance processes can use.

In Codex-driven workflows, HREVN adds structured receipts and state manifests
so interrupted sessions can resume from a verified checkpoint rather than
repeating completed work.

## What it is
- a Codex-facing plugin bundle
- a skills-first public surface
- a thin bridge to `https://api.hrevn.com`
- MCP-ready for a later iteration

## What it is not yet
- not a full MCP server package
- not a live marketplace listing
- not the private HREVN runtime
- not the private commercial toolkit

## Quick Start

```bash
export HREVN_API_KEY="replace-me"
python3 scripts/hrevn_managed_api.py baseline-check \
  --input examples/baseline_check_request.json
```

## Recommended first test

Start with:

```bash
python3 scripts/hrevn_managed_api.py baseline-check \
  --input examples/baseline_check_request.json
```

That validates the public runtime bridge before moving on to broader Codex workflow use.

## Included
- `.codex-plugin/plugin.json`
- `skills/hrevn-baseline-check/SKILL.md`
- `skills/hrevn-sign-on-complete/SKILL.md`
- `skills/hrevn-verify-bundle/SKILL.md`
- `docs/integration/MANAGED_API_USAGE.md`
- `scripts/hrevn_managed_api.py`
- `examples/*.json`
- `docs/references/*`
- `docs/mcp/MCP_READINESS_NOTE.md`

## Managed Runtime Bridge
The live managed endpoint is:
- `https://api.hrevn.com`

Current path:
- skills-first bundle now
- managed API bridge now
- MCP later

## Current status
This is a public Codex bundle candidate with a real runtime bridge.
It is intentionally ahead on workflow clarity and behind on MCP packaging, by design.

## Rule
This bundle should not reimplement HREVN semantics locally.
It should present the runtime cleanly inside the Codex ecosystem.
