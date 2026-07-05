# Architecture

OpenClaw Kit separates the system into four layers:

## 1. Core

Rules, routing, validation, and operational contracts.

## 2. Templates

Environment, cron, and systemd examples that users copy into their own machines.

## 3. Plugins

Optional feature packs that stay outside the public core.

## 4. Local overlay

Private machine-specific settings, secrets, logs, caches, and runtime state.

## Principle

If something identifies a user, a customer, or a live deployment, it does not belong in the public core.

