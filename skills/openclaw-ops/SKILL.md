# OpenClaw Ops

Use this skill for operational tasks such as cron, systemd, backups, logs, and recovery.

## Rules

- Keep operations idempotent.
- Use lock files when concurrent execution is possible.
- Keep destructive actions behind explicit confirmation.
- Prefer small, reversible changes.

