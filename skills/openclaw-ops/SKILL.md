# OpenClaw Ops

Use this skill for operational tasks such as cron, systemd, backups, logs, runtime checks, and recovery support.

## When to use

- Setting up scheduled jobs
- Managing runtime entrypoints
- Inspecting logs and state markers
- Creating or rotating backups
- Rebuilding missing operational files

## Workflow

1. Confirm the target layout exists.
2. Inspect the current config and runtime state.
3. Make the smallest reversible change that solves the issue.
4. Re-run validation or a health check after each change.
5. Record the outcome in logs or state markers when appropriate.

## Rules

- Keep operations idempotent.
- Use lock files when concurrent execution is possible.
- Keep destructive actions behind explicit confirmation.
- Prefer small, reversible changes.
- Separate source-controlled templates from local runtime files.

## Operational scope

- Cron jobs and timers
- Systemd services and health checks
- Backups and restore points
- Runtime logs and diagnostics
- Install target repair

## Related files

- `templates/cron/openclaw.cron.example`
- `templates/systemd/openclaw.service`
- `templates/systemd/openclaw-health.service`
- `templates/systemd/openclaw-health.timer`
- `docs/recovery.md`
