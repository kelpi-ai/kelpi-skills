---
name: kelpi-mcp-setup
description: Connect and verify Kelpi's official hosted MCP server for new users. Use when Codex needs to add the Kelpi MCP endpoint, guide authentication, confirm that Kelpi tools are working, or troubleshoot first-run connection issues for `https://app.kelpi.ai/api/mcp`.
---

# Kelpi MCP Setup

Connect the user to Kelpi's hosted MCP endpoint with the fewest steps possible, then verify that the workspace is reachable.

## Default Path

Treat Kelpi's official MCP setup path as:
- endpoint: `https://app.kelpi.ai/api/mcp`
- first verification tool: `kelpi_status`
- first workspace inspection tool: `kelpi_workspace_summary`

Prefer the hosted HTTP endpoint. Do not suggest stdio or package installation unless the user explicitly asks for an alternative setup path.

## Run Minimal Onboarding

Make first-run setup feel short:
1. Help the user add the hosted endpoint to their MCP client.
2. Help the user authenticate.
3. Call `kelpi_status`.
4. Call `kelpi_workspace_summary`.
5. Summarize what is ready and name the next best action.

Do not start by explaining every Kelpi tool.

## Client Handling

If the user is using Claude Code, use the simple two-step path from [references/hosted-http-endpoint.md](references/hosted-http-endpoint.md).

If the user is using another MCP client:
- ask only if the client is needed to produce the exact add/connect command
- otherwise provide the same hosted URL and an equivalent HTTP MCP configuration

## Verification Rules

After connection, prefer this verification sequence:
1. `kelpi_status`
2. `kelpi_workspace_summary`

If auth is missing or expired, resolve auth before doing anything else.

Use [references/auth-and-verification.md](references/auth-and-verification.md) for the normal sequence and [references/troubleshooting.md](references/troubleshooting.md) for failure handling.

## Smooth Handoff

When setup is complete, do not stop at "connected".

Offer the next step in one sentence:
- "Kelpi is connected. I can inspect the workspace and help you launch your first flow next."
