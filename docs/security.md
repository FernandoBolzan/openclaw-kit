# Security

## Public-core rules

- No tokens in source control
- No personal handles in examples
- No live logs, scans, or exported profiles
- No private keys or cookie jars
- No feature-specific workflow data in the base repo

## Publishing checklist

- Verify the tree for personal markers
- Exclude runtime state and caches
- Keep sample configs placeholder-only
- Redact identifiers from docs and templates
- Run validation before release

## Hard limits

- No live tokens in tests
- No user profile exports in examples
- No product-specific automation data in the public core
- No hidden dependencies on private paths
