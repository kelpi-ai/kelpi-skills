---
name: kelpi
description: Set up and onboard new Kelpi users through the official hosted MCP endpoint. Use when Codex needs to connect Kelpi MCP, guide authentication, verify workspace access, troubleshoot first-run setup, inspect workspace readiness, set up a sender, create a first flow, activate it safely, or continue into SDK integration.
---

# Kelpi

Guide the user from first connection through first live flow without splitting them across multiple installed skills.

## Default Path

Use this order unless the user clearly asks for a narrower task:
1. connect Kelpi MCP
2. authenticate and verify access
3. inspect workspace readiness
4. resolve sender readiness
5. design and create one small flow
6. activate only after explicit approval
7. continue into SDK setup

## Keep First-Run Experience Smooth

- Prefer the official hosted endpoint only: `https://app.kelpi.ai/api/mcp`.
- Do not start with a long tool catalog.
- Do not dump every onboarding option up front.
- Lead with the next concrete step, then continue.
- Treat first success as the goal:
  1. connect
  2. verify access
  3. inspect workspace
  4. launch one small flow

## Setup Workflow

For connection, auth, and verification:
- read [references/hosted-http-endpoint.md](references/hosted-http-endpoint.md)
- then read [references/auth-and-verification.md](references/auth-and-verification.md)
- use [references/troubleshooting.md](references/troubleshooting.md) only if setup fails

## Onboarding Workflow

After setup succeeds:
- read [references/workspace-readiness.md](references/workspace-readiness.md)
- use [references/sender-setup.md](references/sender-setup.md) if sender readiness is missing
- use [references/first-template-and-flow.md](references/first-template-and-flow.md) for the first flow
- use [references/activation-and-sdk.md](references/activation-and-sdk.md) once the flow is ready to go live

## Use References Selectively

Read [references/tool-map.md](references/tool-map.md) only when you need a reminder of the current MCP surface.
