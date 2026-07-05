# Recovery

OpenClaw recovery is designed to be reversible and boring.

## Recovery goals

- Restore a valid install layout
- Recreate missing entrypoints
- Keep secrets untouched
- Avoid rewriting local overlays unless asked

## Recovery actions

- Re-run bootstrap in dry-run mode first
- Validate the repository and installed target
- Restore from the latest backup if the target is incomplete
- Reinstall missing rules, skills, tools, or templates

## Recovery rule

If a recovery action cannot be explained in one sentence, it is too large for the public core.

