#!/usr/bin/env python3
"""Compatibility wrapper for the installable Codex CLI."""

from hrevn_codex_cli.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
