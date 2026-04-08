# MCP_READINESS_NOTE.md

This bundle started skills-first and now includes a first concrete MCP path.

## Current state
- local helper path still works
- public MCP server now exists
- `.mcp.json` is now included
- Codex can move from helper-first to MCP-first testing

## Rule
- keep runtime truth in the managed API and HREVN core
- treat MCP as an interoperability layer, not a second backend
- prefer MCP tools when Codex has the server configured

## Current next step
Keep refining:
- Codex-specific MCP install UX
- mapping between Codex surface and HREVN canonical receipts
- later removal of duplicated helper instructions if MCP becomes the default path
