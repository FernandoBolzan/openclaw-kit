# OpenClaw Recovery

Use this skill when a target install is incomplete, drifted, or partially broken.

## When to use

- A required entrypoint is missing
- An install target is partially copied
- The layout no longer matches the manifest
- A local config file exists but the core files are damaged

## Workflow

1. Identify the missing or broken path.
2. Verify whether the issue is in the repo or the installed target.
3. Recreate only the missing files or directories.
4. Keep local secrets, overlays, and runtime state untouched.
5. Re-run validation after repair.

## Rules

- Prefer the smallest reversible repair.
- Recreate only missing files or directories.
- Do not overwrite local secrets or overlays.
- Revalidate after repair.
- Stop if the fix would rewrite private data.

## Recovery outputs

- Restored install layout
- Recreated entrypoints or directories
- Validation result after repair
- Clear note about what changed

## Related files

- `docs/recovery.md`
- `tools/install.py`
- `tools/validate.py`
