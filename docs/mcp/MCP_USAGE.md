# HREVN Codex MCP Usage

## Goal

Expose the same live HREVN runtime to Codex through MCP tools instead of only
through skill guidance plus the local helper script.

## Companion server

Use the public MCP server repo:
- `https://github.com/ai-human-andalusia/hrevn-mcp-server`

It exposes:
- `baseline_check`
- `profile_validate`
- `generate_bundle`
- `verify_bundle`

All four tools call the same managed backend:
- `https://api.hrevn.com`

## Install the MCP server

```bash
git clone https://github.com/ai-human-andalusia/hrevn-mcp-server
cd hrevn-mcp-server
pip install -e .
```

If you install into a virtualenv, launch Codex from that same activated
environment. Otherwise `hrevn-mcp-server` may not be available in the `PATH`
that Codex sees.

## Codex MCP config

This plugin includes:
- `./.mcp.json`

Update the `HREVN_API_KEY` value before use.

If the command is not found, run:

```bash
which hrevn-mcp-server
```

and replace the `command` value in `.mcp.json` with that absolute path.

## Verify before Codex

```bash
hrevn-mcp-server --version
hrevn-mcp-server --list-tools
hrevn-mcp-server --self-test
```

## Recommended first test

In Codex, prefer the MCP tool:
- `baseline_check`

using:
- `examples/baseline_check_request.json`

The helper script remains available as a fallback path.
