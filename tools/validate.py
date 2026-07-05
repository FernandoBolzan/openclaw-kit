#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = [
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
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
    "docs/overview.md",
    "docs/release.md",
    "docs/plugins.md",
    "docs/recovery.md",
    "docs/troubleshooting.md",
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


def validate_json_files(root: Path) -> list[str]:
    errors: list[str] = []
    json_paths = [
        root / "manifest.json",
        root / "rules/router/skills-router.json",
        root / "rules/router/skill-aliases.json",
        root / "rules/router/skill-execution-profiles.json",
        root / "rules/router/skill-chains.json",
        root / "rules/router/skills-manifest.json",
    ]
    for path in json_paths:
        try:
            json.loads(load_text(path))
        except Exception as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
    return errors


def validate_skills(root: Path) -> list[str]:
    errors: list[str] = []
    for path in (root / "skills").rglob("SKILL.md"):
        text = load_text(path)
        if len(text.strip()) < 120:
            errors.append(f"{path.relative_to(root)}: too short")
        if "Use" not in text or "Rules" not in text:
            errors.append(f"{path.relative_to(root)}: missing Use/Rules sections")
    return errors


def validate_scripts(root: Path) -> list[str]:
    errors: list[str] = []
    scripts = [
        root / "tools" / "install.py",
        root / "tools" / "validate.py",
        root / "install.sh",
        *sorted((root / "templates" / "bin").glob("*")),
    ]
    for path in scripts:
        if path.suffix == ".py":
            result = subprocess.run(["python", "-B", "-m", "py_compile", str(path)], capture_output=True, text=True)
            if result.returncode != 0:
                errors.append(f"{path.relative_to(root)}: {result.stderr.strip()}")
        else:
            text = load_text(path)
            if not text.startswith("#!"):
                errors.append(f"{path.relative_to(root)}: missing shebang")
            if "set -euo pipefail" not in text and path.name != "openclaw-health":
                errors.append(f"{path.relative_to(root)}: missing safe shell guard")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate an OpenClaw Kit checkout.")
    parser.add_argument("--path", default=str(ROOT), help="Path to validate.")
    parser.add_argument("--installed-target", default="", help="Optional installed target to validate too.")
    args = parser.parse_args(argv)

    root = Path(args.path).resolve()
    missing = validate_required(root)
    hits = scan_forbidden(root)
    json_errors = validate_json_files(root)
    skill_errors = validate_skills(root)
    script_errors = validate_scripts(root)
    install_target = []
    if args.installed_target:
        target = Path(args.installed_target).expanduser().resolve()
        expected = [
            target / "rules",
            target / "skills",
            target / "tools",
            target / "bin",
            target / "config",
            target / "docs",
            target / "systemd",
            target / "cron",
            target / "logs",
            target / "state",
            target / "backups",
            target / "manifest.json",
            target / "config" / "openclaw.env.example",
            target / "config" / "openclaw.env",
            target / "bin" / "openclaw-bootstrap",
            target / "bin" / "openclaw-validate",
            target / "bin" / "openclaw-health",
            target / "bin" / "openclaw-backup",
            target / "bin" / "openclaw-release",
        ]
        for path in expected:
            if not path.exists():
                install_target.append(str(path))

    report = {
        "path": str(root),
        "missing": missing,
        "forbidden_hits": hits,
        "json_errors": json_errors,
        "skill_errors": skill_errors,
        "script_errors": script_errors,
        "missing_installed_paths": install_target,
        "ok": not missing and not hits and not json_errors and not skill_errors and not script_errors and not install_target,
    }
    print(json.dumps(report, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
