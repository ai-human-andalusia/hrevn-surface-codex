---
name: hrevn-sign-on-complete
description: Wrap a critical action with HREVN State Guard so Codex can run baseline before execution and emit an AER afterward.
---

# HREVN Sign on Complete

## Use this skill when
- a critical action should leave a structured tamper-evident trail
- the user wants one-line adoption via `@hrevn.sign_on_complete`
- a workflow needs pre-check + action receipt + failure trail

## Do not use this skill when
- the action is trivial and has no real consequence
- the user only wants conceptual discussion

## Required behavior
1. Route through the State Guard engine.
2. Keep the layering:
   - `@hrevn.sign_on_complete`
   - `HREVNStateGuard`
   - `RealBaselineRunner`
   - `BaselineEngine`
3. Do not duplicate profile detection logic in the wrapper.
4. Prefer the real baseline engine by default.
5. Keep mock runners only as explicit fallback for development.

## Runtime bridge
When the managed runtime is available:
1. run baseline first against `https://api.hrevn.com`
2. execute the consequential action
3. generate the HREVN bundle through the managed runtime

The Codex bundle should stay thin. It should not duplicate issuance or bundle
semantics locally.

## Canonical references
- `references/CODEX_HANDOFF_STATE_GUARD_CONNECTED_STACK.md`
- `references/CODEX_SIGN_ON_COMPLETE_NOTE.md`
- `references/HREVN_CORE_NAMING_DECISIONS.md`
