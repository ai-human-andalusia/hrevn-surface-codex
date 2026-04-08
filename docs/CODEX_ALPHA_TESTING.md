# Codex Alpha Testing

## Public repos

- `https://github.com/ai-human-andalusia/hrevn-surface-codex`
- `https://github.com/ai-human-andalusia/hrevn-mcp-server`

## Live backend

- `https://api.hrevn.com`

## Codex alpha API key

Use a dedicated alpha key issued out-of-band for your test environment.
Do not commit live keys into `.mcp.json`, shell history, or repo docs.

## Supported first path

Codex skills -> local helper -> `https://api.hrevn.com`

## Setup

```bash
git clone https://github.com/ai-human-andalusia/hrevn-surface-codex
cd hrevn-surface-codex
python3 -m venv .venv
source .venv/bin/activate
```

Then export:

```bash
export HREVN_API_BASE_URL="https://api.hrevn.com"
export HREVN_API_KEY="replace-with-issued-alpha-key"
```

Open Codex from that same repo and same environment.

## Preflight

Run this first:

```bash
python3 scripts/hrevn_managed_api.py self-test
```

Expected result:
- `self_test: ok`
- `auth: ok`
- a real `check_id`
- a real `checked_at`

## First test

```bash
python3 scripts/hrevn_managed_api.py baseline-check \
  --input examples/baseline_check_request.json
```

Expected result:
- a real `BaselineResult`
- returned from `https://api.hrevn.com`
- not a mock and not a textual explanation

## Optional MCP path

If you want to test MCP in parallel, use:
- `https://github.com/ai-human-andalusia/hrevn-mcp-server`

Then:

```bash
git clone https://github.com/ai-human-andalusia/hrevn-mcp-server
cd hrevn-mcp-server
pip install -e .
```

If you install into a virtualenv, launch Codex from that same activated
environment. Otherwise `hrevn-mcp-server` may not be available in the `PATH`
that Codex sees.

Verify MCP before opening Codex:

```bash
HREVN_API_BASE_URL=https://api.hrevn.com \
HREVN_API_KEY=replace-with-issued-alpha-key \
hrevn-mcp-server --version

HREVN_API_BASE_URL=https://api.hrevn.com \
HREVN_API_KEY=replace-with-issued-alpha-key \
hrevn-mcp-server --list-tools

HREVN_API_BASE_URL=https://api.hrevn.com \
HREVN_API_KEY=replace-with-issued-alpha-key \
hrevn-mcp-server --self-test
```

The plugin already includes:
- `./.mcp.json`

Replace the placeholder API key there with your issued alpha key.

If `hrevn-mcp-server` is not found, run:

```bash
which hrevn-mcp-server
```

and replace the `command` value in `.mcp.json` with that absolute path.
