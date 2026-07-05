# OpenClaw Observability

Use this skill for logs, health checks, state markers, diagnostics, and operational visibility.

## When to use

- Inspecting a failed install or run
- Confirming a service is alive
- Reviewing state markers after a scheduled job
- Designing log output for a new tool or script
- Triage after a recovery or release step

## Workflow

1. Check the current runtime state and recent logs.
2. Identify whether the issue is config, state, or execution.
3. Reduce the signal to a short, actionable status line.
4. Record only what operators need to know.
5. Validate again after the fix.

## Rules

- Prefer structured outputs.
- Keep logs short and actionable.
- Separate runtime state from source control.
- Treat missing health signals as failures until proven otherwise.
- Avoid noisy logs that hide the real fault.

## Observability surface

- Health checks
- State markers
- Runtime logs
- Backup or recovery evidence
- Validation summaries

## Related files

- `docs/troubleshooting.md`
- `docs/recovery.md`
- `templates/systemd/openclaw-health.service`
- `templates/systemd/openclaw-health.timer`
