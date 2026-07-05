# Conventions

## Naming

- Files and directories use lowercase with hyphens where useful.
- Skills use a stable `skill-openclaw-*` naming pattern.
- Templates are grouped by target type: env, cron, and systemd.

## Environment variables

- Prefer `OPENCLAW_*` for runtime configuration.
- Keep secrets in a separate local file.
- Use `*_FILE` variables for secret file paths when possible.

## Behavioral defaults

- Dry-run first
- Preserve existing files
- Explicit confirmation for destructive actions
- Minimal context, maximal verification

