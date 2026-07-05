# OpenClaw Bootstrap

Use this skill to install the public OpenClaw core into a clean target directory and verify that the target is ready for local use.

## When to use

- First install on a fresh machine
- Reinstall after drift or partial corruption
- Prepare a new workspace for plugin overlays
- Rebuild a target that should contain only the public core

## Input

- Repository path
- Target path for the install
- Optional override paths for config, logs, state, and backups

## Workflow

1. Inspect the target path before writing anything.
2. Run a dry-run install if the target already exists.
3. Copy rules, skills, tools, docs, templates, and manifest files.
4. Create local runtime directories for config, logs, state, and backups.
5. Seed placeholder config from `openclaw.env.example`.
6. Run validation on both the repository and the installed target.

## Rules

- Prefer dry-run first.
- Preserve existing files unless overwrite is explicit.
- Never copy live state, logs, or secrets from a personal machine.
- Treat feature-specific packs as optional plugins, not core content.
- Fail closed if the target layout does not match the manifest.

## Output

- Installed OpenClaw public core
- Local config scaffold
- Runtime directories for operational use
- Validation result for the installed target

## Related files

- `tools/install.py`
- `tools/validate.py`
- `templates/env/openclaw.env.example`
- `docs/install.md`
