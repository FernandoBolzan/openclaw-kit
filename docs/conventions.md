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

## Failure policy

- Missing configuration is a hard error.
- Missing runtime state is a recoverable condition.
- Missing secrets is not recoverable inside the public core.
- If validation cannot explain a failure clearly, the tool should fail closed.

## Documentation policy

- Every public skill should explain purpose, workflow, rules, and related files.
- Every public doc should describe what is included, what is excluded, and why the boundary exists.
- Examples should be runnable or clearly marked as placeholders.
