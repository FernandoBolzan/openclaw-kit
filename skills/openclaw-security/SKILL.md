# OpenClaw Security

Use this skill for secrets hygiene, redaction, least-privilege checks, and public-release review.

## When to use

- Before publishing or tagging a release
- Before copying a tree into a public repository
- When reviewing templates, examples, or fixtures
- When a file may contain personal markers or live credentials

## Workflow

1. Search the tree for personal markers and secret patterns.
2. Confirm examples are placeholder-only.
3. Check that templates do not reference private paths.
4. Reject any file that contains live tokens, passwords, or cookies.
5. Re-run validation after cleanup.

## Rules

- Never commit tokens, passwords, or private keys.
- Never export personal data in the public core.
- Redact identifiers from examples and fixtures.
- Validate that templates stay placeholder-only.
- Assume anything not explicitly public should stay private.

## Security checks

- Secret scanning
- Personal marker scanning
- Template redaction review
- Public-core boundary review
- Release readiness review

## Related files

- `docs/security.md`
- `tools/validate.py`
- `manifest.json`
