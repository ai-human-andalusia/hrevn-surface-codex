# HREVN Trust Layer for Codex

**Un solo núcleo. Tres superficies. Mismo resultado verificable.**

OpenAI changes the bundle.  
Anthropic changes the skill.  
Google changes the middleware.  
HREVN does not change its truth.

This repo is the Codex-facing HREVN surface: a skills-first plugin bundle with
a local helper bridge to the live managed runtime and an optional public MCP
path.

Public package:

- `https://pypi.org/project/hrevn-codex-cli/`

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
- a thin helper bridge to `https://api.hrevn.com`
- an optional MCP path through `hrevn-mcp-server`

## What it is not yet
- not a live marketplace listing
- not the private HREVN runtime
- not the private commercial toolkit

## Quick Start

```bash
pipx install hrevn-codex-cli
export HREVN_API_BASE_URL="https://api.hrevn.com"
export HREVN_API_KEY="replace-me"
hrevn-codex health-check
hrevn-codex self-test
hrevn-codex baseline
```

If you want the repo checkout instead, use:

```bash
git clone https://github.com/ai-human-andalusia/hrevn-surface-codex
cd hrevn-surface-codex
pipx install .
```

If `pipx` is not available, a local fallback is:

```bash
python3 -m pip install .
```

## Recommended first test

Start with:

```bash
hrevn-codex self-test
```

Then run:

```bash
hrevn-codex baseline
```

The self-test separates setup and auth problems from product issues. The
baseline check then validates the public runtime bridge before moving on to
broader Codex workflow use.

## Alpha runtime path

Current default alpha path:

- Codex skills
- local helper
- `https://api.hrevn.com`

This is intentional. MCP is available, but it is not required for the first
working Codex test.

## Optional MCP path

If you want Codex to discover HREVN as MCP tools instead of only through skills
plus the helper script, use:

- `https://github.com/ai-human-andalusia/hrevn-mcp-server`

See:
- `docs/mcp/MCP_USAGE.md`
- `.mcp.json`
- `docs/CODEX_ALPHA_TESTING.md`

## Included
- `.codex-plugin/plugin.json`
- `.mcp.json`
- `pyproject.toml`
- `skills/hrevn-baseline-check/SKILL.md`
- `skills/hrevn-sign-on-complete/SKILL.md`
- `skills/hrevn-verify-bundle/SKILL.md`
- `docs/integration/MANAGED_API_USAGE.md`
- `scripts/hrevn_managed_api.py`
- `src/hrevn_codex_cli/...`
- `examples/*.json`
- `docs/references/*`
- `docs/mcp/MCP_READINESS_NOTE.md`

## Managed Runtime Bridge
The live managed endpoint is:
- `https://api.hrevn.com`

Current path:
- skills-first bundle now
- managed API helper bridge now
- MCP available as a secondary path

## Current status
This is a public Codex plugin candidate with a real technical alpha testing
path. The supported first path is skills plus local helper plus the live
managed runtime. MCP is available, but it is not the default runtime path in
this alpha.

## Rule
This bundle should not reimplement HREVN semantics locally.
It should present the runtime cleanly inside the Codex ecosystem.
