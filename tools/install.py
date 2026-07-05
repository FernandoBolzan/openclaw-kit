#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGET = Path.home() / ".openclaw"
COPY_DIRS = ("rules", "skills", "tools", "docs")
INSTALL_MAP = {
    "manifest.json": "manifest.json",
    "templates/env": "config",
    "templates/cron": "cron",
    "templates/systemd": "systemd",
    "templates/bin": "bin",
}


def expand_target(value: str) -> Path:
    expanded = os.path.expandvars(os.path.expanduser(value))
    return Path(expanded).resolve()


def copy_tree(src: Path, dst: Path, overwrite: bool, dry_run: bool) -> list[str]:
    copied: list[str] = []
    for path in src.rglob("*"):
        rel = path.relative_to(src)
        target = dst / rel
        if any(part in {".git", "__pycache__", ".venv"} for part in path.parts):
            continue
        if path.suffix in {".pyc", ".pyo", ".pyd"}:
            continue
        if path.is_dir():
            if dry_run:
                continue
            target.mkdir(parents=True, exist_ok=True)
            continue
        if target.exists() and not overwrite:
            continue
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
        copied.append(str(target))
    return copied


def install_entrypoints(target: Path, overwrite: bool, dry_run: bool) -> list[str]:
    summary: list[str] = []
    for src_rel, dst_rel in INSTALL_MAP.items():
        src = ROOT / src_rel
        dst = target / dst_rel
        if src.is_dir():
            summary.extend(copy_tree(src, dst, overwrite, dry_run))
            continue
        if src.exists() and (overwrite or not dst.exists()):
            if not dry_run:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
            summary.append(str(dst))
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Install the public OpenClaw core.")
    parser.add_argument("--target", default=str(DEFAULT_TARGET), help="Install target directory.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files.")
    parser.add_argument("--dry-run", action="store_true", help="Show actions without writing.")
    args = parser.parse_args(argv)

    target = expand_target(args.target)
    payload_root = target
    summary: list[str] = []

    for name in COPY_DIRS:
        src = ROOT / name
        dst = payload_root / name
        if src.exists():
            summary.extend(copy_tree(src, dst, args.overwrite, args.dry_run))

    summary.extend(install_entrypoints(payload_root, args.overwrite, args.dry_run))

    if not args.dry_run:
        for folder in ("logs", "state", "backups"):
            (target / folder).mkdir(parents=True, exist_ok=True)

        config_example = target / "config" / "openclaw.env.example"
        config_file = target / "config" / "openclaw.env"
        if config_example.exists() and not config_file.exists():
            shutil.copy2(config_example, config_file)
            summary.append(str(config_file))

        marker = target / "state" / "openclaw-kit"
        marker.mkdir(parents=True, exist_ok=True)
        (marker / "installed-from.json").write_text(
            json.dumps(
                {
                    "source": str(ROOT),
                    "target": str(target),
                    "installed": sorted(summary),
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

    print(json.dumps({"dry_run": args.dry_run, "target": str(target), "files": summary}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
