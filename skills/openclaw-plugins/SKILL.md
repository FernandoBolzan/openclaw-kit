# OpenClaw Plugins

Use this skill to manage optional overlays and plugin packs without weakening the public core.

## When to use

- Packaging an optional feature set
- Defining a new boundary between public and private content
- Auditing whether a feature belongs in the core or in a plugin
- Installing an extension pack on top of a clean OpenClaw base

## Workflow

1. Classify the feature as core or optional.
2. Move product-specific behavior out of the public repo if it depends on private data.
3. Declare the plugin's own config and state paths.
4. Keep the plugin install path independent from the base install.
5. Revalidate the base repo after plugin changes.

## Rules

- Keep the public core stable.
- Isolate feature-specific code into plugins.
- Document each plugin boundary clearly.
- Do not leak user-specific data into shared templates.
- Make plugins optional, not implicit dependencies.

## Plugin boundary

- Public: rules, routing, validation, recovery, release, security, observability
- Private: customer data, live state, feature automations, account-specific overlays

## Related files

- `docs/plugins.md`
- `rules/router/skills-manifest.json`
- `rules/router/skill-chains.json`
