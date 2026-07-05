# OpenClaw Kit

OpenClaw Kit is the public operational core for OpenClaw deployments: a compact, installable system for rules, routing, validation, recovery, observability, and DevOps foundations.

It is built to install cleanly, run predictably, and stay easy to extend without turning the core into a feature dump or leaking private machine state.

## What this repo contains

- System rules and operator contract
- Skill routing metadata and execution profiles
- Safe install and validation tooling
- DevOps templates for environment variables, cron, systemd, and shell entrypoints
- GitHub workflow, issue templates, and contribution hygiene
- A public skill set for bootstrap, operations, validation, recovery, observability, release, security, and plugin boundaries

## Public docs

- [Overview](docs/overview.md)
- [Install](docs/install.md)
- [Architecture](docs/architecture.md)
- [Conventions](docs/conventions.md)
- [Security](docs/security.md)
- [Recovery](docs/recovery.md)
- [Release](docs/release.md)
- [Plugins](docs/plugins.md)
- [Troubleshooting](docs/troubleshooting.md)

## Why it exists

- To make OpenClaw easy to install on a clean machine
- To keep operational rules separate from product-specific features
- To provide a stable public core with clear plugin boundaries
- To reduce setup drift across environments
- To give operators a reliable baseline they can extend with private overlays or plugins

## Quick start

```bash
bash install.sh --target "$HOME/.openclaw"
python3 tools/validate.py --path .
```

For the installed target, use the generated `bin/` entrypoints and keep local config in the target overlay.

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
- Validate before publish, install, or recovery
