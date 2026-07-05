#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = [
    "README.md",
    "LICENSE",
    "manifest.json",
    "rules/rules.md",
    "rules/maestro.md",
    "rules/router/skills-router.json",
    "rules/router/skill-aliases.json",
    "rules/router/skill-execution-profiles.json",
    "rules/router/skill-chains.json",
    "rules/router/skills-manifest.json",
    "tools/install.py",
    "tools/validate.py",
]

FORBIDDEN_PATTERNS = [
    re.compile(r"fernandobolzan", re.IGNORECASE),
    re.compile(r"26258162670434070"),
    re.compile(r"EAAT[0-9A-Za-z_-]{20,}"),
    re.compile(r"threads\.com/@fernandobolzan\.pro", re.IGNORECASE),
    re.compile(r"contact@fernandobolzan\.com", re.IGNORECASE),
]


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def validate_required(root: Path) -> list[str]:
    missing = []
    for rel in REQUIRED_PATHS:
        if not (root / rel).exists():
            missing.append(rel)
    return missing


def scan_forbidden(root: Path) -> list[str]:
    hits: list[str] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.relative_to(root).as_posix() == "tools/validate.py":
            continue
        if any(part in {".git", ".venv", "__pycache__", ".omx"} for part in path.parts):
            continue
        try:
            text = load_text(path)
        except Exception:
            continue
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.search(text):
                hits.append(f"{path.relative_to(root)}: {pattern.pattern}")
    return hits


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate an OpenClaw Kit checkout.")
    parser.add_argument("--path", default=str(ROOT), help="Path to validate.")
    args = parser.parse_args(argv)

    root = Path(args.path).resolve()
    missing = validate_required(root)
    hits = scan_forbidden(root)

    report = {
        "path": str(root),
        "missing": missing,
        "forbidden_hits": hits,
        "ok": not missing and not hits,
    }
    print(json.dumps(report, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
