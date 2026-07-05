# Plugins

Plugins are optional overlays that extend OpenClaw without modifying the public core.

## Plugin boundary

- Public core: rules, routing, validation, recovery, and operational templates
- Private overlay: product-specific automations, account data, live state, and secrets

## Plugin rules

- Plugins must be installable without editing the core
- Plugins must declare their own config and state paths
- Plugins must never require private data in the public repository

