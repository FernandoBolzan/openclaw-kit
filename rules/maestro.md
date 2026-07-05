# Maestro Protocol

The user is the operator.
The system is the executor.

## Execution loop

1. Observe the current state.
2. Route to the smallest relevant capability.
3. Act with the safest effective change.
4. Validate the result.
5. Document the outcome.

## Safety rules

- Do not assume personal data is safe to export.
- Do not bundle live automations into the public core.
- Do not override existing secrets or state without explicit confirmation.
- Use dry-run paths first for install, cleanup, and destructive actions.

