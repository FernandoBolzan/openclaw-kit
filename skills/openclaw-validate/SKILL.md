# OpenClaw Validate

Use this skill to verify that the repository and installed target are clean, complete, and safe.

## Use

- Run this skill before release, publish, or install.
- Use it after editing rules, skills, templates, or tooling.
- Use it whenever you suspect drift or missing files.

## Rules

- Validate the repository before the installed target.
- Fail closed on missing files, malformed JSON, or forbidden markers.
- Keep checks deterministic and explainable.
- Do not accept a target that only works on the current machine.

## Checks

- Required files exist
- No personal markers are present
- No feature-specific artifacts are bundled
- Install layout is consistent
