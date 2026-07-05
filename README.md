# OpenClaw Kit

OpenClaw Kit is the operational core for OpenClaw deployments: a compact system for rules, routing, validation, recovery, observability, and DevOps foundations.

It is built to install cleanly, run predictably, and stay easy to extend without turning the core into a feature dump.

## What this repo contains

- System rules and operator contract
- Skill routing metadata and execution profiles
- Safe install and validation tooling
- DevOps templates for environment variables, cron, systemd, and shell entrypoints
- GitHub workflow, issue templates, and contribution hygiene
- A public skill set for bootstrap, operations, validation, recovery, observability, release, security, and plugin boundaries

## Why it exists

- To make OpenClaw easy to install on a clean machine
- To keep operational rules separate from product-specific features
- To provide a stable public core with clear plugin boundaries
- To reduce setup drift across environments

## Quick start

```bash
bash install.sh --target "$HOME/.openclaw"
python3 tools/validate.py --path .
```

## Layout

```text
openclaw-kit/
  rules/
  skills/
  templates/
  tools/
  docs/
  .github/
```

## Design principles

- Dry-run first, then commit to changes intentionally
- Preserve existing files unless overwrite is explicit
- Keep secrets outside the repository
- Keep personal overlays separate from the public core
- Favor compact rules, stable paths, and reversible operations
- Prefer defaults that are safe on a fresh install
