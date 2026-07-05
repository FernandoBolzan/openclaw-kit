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
- JSON manifests parse successfully
- Skill files contain a clear use case and rules
- Shell entrypoints have safe guards and executable headers
- Python tooling compiles without syntax errors

## Failure signals

- Missing required files
- Unexpected private markers
- Broken JSON
- Missing install paths
- Incomplete or ambiguous skill files
- Scripts that cannot run in a clean install target

## Related files

- `tools/validate.py`
- `manifest.json`
- `rules/router/skills-manifest.json`
