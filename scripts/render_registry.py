#!/usr/bin/env python3
"""Render the endpoint registry into the documents that describe it.

registry/adp-registry.json is the one list of ADP levels, page requirements
and endpoints. The specification, the README, the audit tool and the reference
implementation all read it. This script writes the tables between the
``<!-- registry:NAME:start -->`` and ``<!-- registry:NAME:end -->`` markers.

    python scripts/render_registry.py           # rewrite the documents
    python scripts/render_registry.py --check   # exit 1 if any are stale
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "registry" / "adp-registry.json"
DOCUMENTS = ["README.md", "SPECIFICATION.md"]
STATUSES = {"required", "recommended", "optional"}


def load() -> dict:
    registry = json.loads(REGISTRY.read_text())
    levels = {entry["level"] for entry in registry["levels"]}
    seen_ids, seen_paths = set(), set()
    for endpoint in registry["endpoints"]:
        paths = [endpoint["path"], *endpoint.get("aliases", [])]
        if endpoint["id"] in seen_ids:
            raise SystemExit(f"duplicate id: {endpoint['id']}")
        if endpoint["level"] not in levels:
            raise SystemExit(f"unknown level on {endpoint['path']}")
        if endpoint["status"] not in STATUSES:
            raise SystemExit(f"unknown status on {endpoint['path']}")
        for path in paths:
            if path in seen_paths:
                raise SystemExit(f"duplicate path: {path}")
            seen_paths.add(path)
        seen_ids.add(endpoint["id"])
    for entry in registry["retired"]:
        if entry["path"] in seen_paths:
            raise SystemExit(f"retired path is still listed: {entry['path']}")
    return registry


def levels_table(registry: dict) -> str:
    rows = ["| Level | Name | Status | What it is |", "|---|---|---|---|"]
    for entry in registry["levels"]:
        rows.append(
            f"| {entry['level']} | {entry['name']} | {entry['status'].capitalize()} "
            f"| {entry['summary']} |"
        )
    return "\n".join(rows)


def page_table(registry: dict) -> str:
    rows = ["| Requirement | Status | Rule |", "|---|---|---|"]
    for entry in registry["page_requirements"]:
        rule = entry["description"].replace("<", "`<").replace(">", ">`")
        rows.append(f"| `{entry['id']}` | {entry['status'].capitalize()} | {rule} |")
    return "\n".join(rows)


def endpoints_table(registry: dict) -> str:
    rows = ["| Level | Path | Status | Purpose |", "|---|---|---|---|"]
    for endpoint in registry["endpoints"]:
        rows.append(
            f"| {endpoint['level']} | `{endpoint['path']}` "
            f"| {endpoint['status'].capitalize()} | {endpoint['description']} |"
        )
    return "\n".join(rows)


def retired_table(registry: dict) -> str:
    rows = ["| Path | Retired in | Use instead | Why |", "|---|---|---|---|"]
    for entry in registry["retired"]:
        replacement = f"`{entry['replacement']}`" if entry["replacement"] else "Nothing"
        rows.append(
            f"| `{entry['path']}` | {entry['since']} | {replacement} | {entry['reason']} |"
        )
    return "\n".join(rows)


RENDERERS = {
    "levels": levels_table,
    "page": page_table,
    "endpoints": endpoints_table,
    "retired": retired_table,
}


def render(text: str, registry: dict) -> str:
    for name, renderer in RENDERERS.items():
        pattern = re.compile(
            rf"(<!-- registry:{name}:start -->\n).*?(\n<!-- registry:{name}:end -->)",
            re.DOTALL,
        )
        text = pattern.sub(
            lambda match, table=renderer(registry): match.group(1) + table + match.group(2),
            text,
        )
    return text


def main() -> int:
    check = "--check" in sys.argv
    registry = load()
    stale = []
    for name in DOCUMENTS:
        path = ROOT / name
        current = path.read_text()
        rendered = render(current, registry)
        if rendered != current:
            stale.append(name)
            if not check:
                path.write_text(rendered)
    if check and stale:
        print("Out of date with registry/adp-registry.json: " + ", ".join(stale))
        print("Run: python scripts/render_registry.py")
        return 1
    print("Registry tables are current." if not stale else "Rewrote: " + ", ".join(stale))
    return 0


if __name__ == "__main__":
    sys.exit(main())
