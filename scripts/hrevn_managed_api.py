#!/usr/bin/env python3
"""Small helper for calling the public HREVN managed runtime from Codex."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


DEFAULT_BASE_URL = "https://api.hrevn.com"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Call the HREVN managed API.")
    parser.add_argument(
        "--base-url",
        default=os.environ.get("HREVN_API_BASE_URL", DEFAULT_BASE_URL),
        help="Managed API base URL. Defaults to HREVN_API_BASE_URL or https://api.hrevn.com.",
    )
    parser.add_argument(
        "--api-key",
        default=os.environ.get("HREVN_API_KEY"),
        help="API key. Defaults to HREVN_API_KEY.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("self-test", help="Validate environment, auth, and baseline reachability.")

    baseline = subparsers.add_parser("baseline-check")
    baseline.add_argument("--input", required=True, help="Path to baseline request JSON.")

    generate = subparsers.add_parser("generate-bundle")
    generate.add_argument("--input", required=True, help="Path to generate request JSON.")

    verify = subparsers.add_parser("verify-bundle")
    verify.add_argument("--source", required=True, help="Absolute path to the bundle zip.")

    download = subparsers.add_parser("download-bundle")
    download.add_argument("--bundle-id", required=True, help="Bundle identifier to download.")
    download.add_argument("--output", help="Optional path to save the downloaded bundle.")

    return parser


def require_api_key(api_key: str | None) -> str:
    if api_key:
        return api_key
    raise SystemExit("HREVN_API_KEY is required")


def read_json(path: str) -> object:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def request_json(base_url: str, api_key: str, path: str, payload: object) -> object:
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        f"{base_url.rstrip('/')}{path}",
        data=data,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode("utf-8"))


def download_bundle(base_url: str, api_key: str, bundle_id: str) -> bytes:
    request = urllib.request.Request(
        f"{base_url.rstrip('/')}/v1/bundles/{urllib.parse.quote(bundle_id)}/download",
        headers={"Authorization": f"Bearer {api_key}"},
    )
    with urllib.request.urlopen(request) as response:
        return response.read()


def self_test_payload() -> object:
    return {
        "task_type": "ai_workflow",
        "profile": "eu_readiness_profile",
        "record": {
            "human_oversight": {},
            "risk_register": {},
            "evidence_lifecycle": {},
        },
        "metadata": {
            "surface": "codex",
            "source": "self_test",
        },
    }


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    api_key = require_api_key(args.api_key)

    try:
        if args.command == "self-test":
            result = request_json(
                args.base_url,
                api_key,
                "/v1/baseline-check",
                self_test_payload(),
            )
            print(
                json.dumps(
                    {
                        "self_test": "ok",
                        "base_url": args.base_url,
                        "auth": "ok",
                        "baseline_result": result.get("result"),
                        "profile_detected": result.get("profile_detected"),
                        "readiness_level": result.get("readiness_level"),
                        "check_id": result.get("check_id"),
                        "checked_at": result.get("checked_at"),
                    },
                    indent=2,
                )
            )
            return 0

        if args.command == "baseline-check":
            result = request_json(
                args.base_url,
                api_key,
                "/v1/baseline-check",
                read_json(args.input),
            )
            print(json.dumps(result, indent=2))
            return 0

        if args.command == "generate-bundle":
            result = request_json(
                args.base_url,
                api_key,
                "/v1/generate-bundle",
                read_json(args.input),
            )
            print(json.dumps(result, indent=2))
            return 0

        if args.command == "verify-bundle":
            result = request_json(
                args.base_url,
                api_key,
                "/v1/verify-bundle",
                {"source": args.source},
            )
            print(json.dumps(result, indent=2))
            return 0

        if args.command == "download-bundle":
            payload = download_bundle(args.base_url, api_key, args.bundle_id)
            if args.output:
                Path(args.output).write_bytes(payload)
                print(args.output)
            else:
                sys.stdout.buffer.write(payload)
            return 0

    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        print(f"HREVN managed API error {exc.code}: {detail}", file=sys.stderr)
        return 1
    except urllib.error.URLError as exc:
        print(f"HREVN managed API connection failed: {exc}", file=sys.stderr)
        return 1

    parser.error(f"Unsupported command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
