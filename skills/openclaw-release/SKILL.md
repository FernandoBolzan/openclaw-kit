# OpenClaw Release

Use this skill when preparing a public cut of OpenClaw Kit or a plugin-compatible version of it.

## When to use

- Before tagging a release
- Before pushing a public branch
- After a documentation or install-flow change
- When writing a changelog entry or release note

## Workflow

1. Validate the repository.
2. Validate the installed target.
3. Confirm there are no personal markers or secret values.
4. Review the changelog and the README for accuracy.
5. Tag or publish only from a clean tree.

## Rules

- Validate the repository before tagging a release.
- Confirm no personal markers are present.
- Ensure docs describe the current layout and install flow.
- Keep release notes short and factual.
- Do not release a tree that has not been installed and validated end to end.

## Release outputs

- Changelog entry
- Clean tag or release branch
- Validation result
- Public documentation snapshot

## Related files

- `CHANGELOG.md`
- `docs/release.md`
- `tools/validate.py`
