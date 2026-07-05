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

