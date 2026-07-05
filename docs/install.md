# Install

## Recommended flow

1. Clone the repository.
2. Review the manifest and the templates.
3. Run a dry-run install.
4. Validate the install target.
5. Copy the environment example into your local overlay.

## Example

```bash
bash install.sh --target "$HOME/.openclaw" --dry-run
bash install.sh --target "$HOME/.openclaw"
python3 tools/validate.py --path .
```

## Notes

- The public core does not ship customer data.
- The install process preserves existing files unless overwrite is explicit.
- Feature packs should be installed separately as plugins.

## Local paths

- `config/` for editable local settings
- `logs/` for runtime output
- `state/` for small machine-owned markers
- `backups/` for recovery artifacts

## Verification

After install, validate both the repository and the target install. The public repository should pass on its own, and the installed target should contain the generated entrypoints and runtime directories.
