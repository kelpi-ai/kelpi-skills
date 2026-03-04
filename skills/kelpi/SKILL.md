---
name: kelpi
description: Route Kelpi setup and onboarding requests to the right workflow. Use when Codex needs to help a user connect the official Kelpi MCP endpoint, authenticate, verify workspace access, troubleshoot first-run setup, or guide a new user from connection through their first live Kelpi flow.
---

# Kelpi

Route broad Kelpi requests into the smallest workflow that will finish the task quickly.

## Route First

Read [references/routing.md](references/routing.md) first.

Use `kelpi-mcp-setup` when the user needs to:
- connect Kelpi to an MCP client
- use the official hosted MCP endpoint
- authenticate or re-authenticate
- verify that Kelpi tools are working
- troubleshoot first-run setup

Use `kelpi-getting-started` when the user needs to:
- inspect a newly connected workspace
- choose a first sender or sending domain
- create a first template or flow
- activate a first flow
- wire up SDK tracking after activation

If the request spans both, do setup first and then hand off to getting started.

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

## Use References Selectively

Read [references/tool-map.md](references/tool-map.md) only when you need a reminder of the current MCP surface.
