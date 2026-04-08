# Codex Alpha Testing

## Public repos

- `https://github.com/ai-human-andalusia/hrevn-surface-codex`
- `https://github.com/ai-human-andalusia/hrevn-mcp-server`

## Live backend

- `https://api.hrevn.com`

## Codex alpha API key

Use a dedicated alpha key issued out-of-band for your test environment.
Do not commit live keys into `.mcp.json`, shell history, or repo docs.

## Preferred path

Codex -> HREVN MCP server -> `https://api.hrevn.com`

## Install

```bash
git clone https://github.com/ai-human-andalusia/hrevn-mcp-server
cd hrevn-mcp-server
pip install -e .
```

If you install into a virtualenv, launch Codex from that same activated
environment. Otherwise `hrevn-mcp-server` may not be available in the `PATH`
that Codex sees.

## Verify MCP first

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

## Codex config

The plugin already includes:
- `./.mcp.json`

Replace the placeholder API key with your issued alpha key.

If `hrevn-mcp-server` is not found, run:

```bash
which hrevn-mcp-server
```

and replace the `command` value in `.mcp.json` with that absolute path.

## First test

In Codex, prefer the MCP tool:
- `baseline_check`

with:
- `examples/baseline_check_request.json`

## Fallback path

If MCP is not available, the local helper still works:

```bash
export HREVN_API_KEY="replace-with-issued-alpha-key"
python3 scripts/hrevn_managed_api.py baseline-check \
  --input examples/baseline_check_request.json
```
