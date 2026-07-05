# Overview

OpenClaw Kit provides the public operational layer for OpenClaw.

The kit is organized around a few stable ideas:

## Core

The public rules, routing metadata, and validation contracts that define how OpenClaw behaves.

## Operations

Templates and tooling for install, environment setup, cron, and systemd-based runtime management.

## Safety

Repository hygiene, dry-run behavior, validation gates, and strict separation between public core and private overlays.

## Extensibility

Optional skills and plugin boundaries that let the system grow without coupling the core to a specific workflow.

## Release discipline

The kit includes validation, recovery, and release guidance so public changes stay small, auditable, and reversible.

## Result

A small, reproducible, and operator-friendly foundation that can be installed and adapted without inheriting personal machine state.

## Included artifacts

- Public rules and routing metadata
- Public skills for bootstrap, operations, security, plugins, validation, observability, release, and recovery
- Installable templates for env, cron, systemd, and shell entrypoints
- Validation tooling and release checks

## Excluded artifacts

- Personal machine data
- Live tokens or private keys
- Customer or workspace specific state
- Product-only features that depend on private overlays
