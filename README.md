# OpenClaw Kit

OpenClaw Kit is the operational core for OpenClaw deployments: rules, routing, validation, recovery, observability, and DevOps templates that can be installed safely into a fresh environment.

It is intentionally not a product-specific automation pack.

## What this repo contains

- System rules and operator contract
- Skill routing metadata
- Safe install and validation tooling
- DevOps templates for env, cron, and systemd
- GitHub workflow and contribution hygiene

## What this repo does not contain

- Threads automations
- IAPRO or other client-specific workflows
- Personal data, profiles, tokens, or exports
- Runtime state, logs, caches, or backups from a live machine

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

## Safety model

- Dry-run by default for destructive actions
- Preserve existing files unless overwrite is explicit
- Keep secrets outside the repository
- Keep personal overlays outside the public core

