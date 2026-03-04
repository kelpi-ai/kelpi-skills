---
name: kelpi-getting-started
description: Guide a new Kelpi user from verified workspace access to their first live automation. Use when Codex needs to inspect workspace readiness, set up a sender, create the first template and flow, activate it safely, and continue into SDK integration for the official Kelpi MCP workflow.
---

# Kelpi Getting Started

Onboard a new Kelpi user by turning a connected workspace into one small live flow with the least friction possible.

## Start Small

Prefer the smallest credible first win:
- one sender decision
- one template or a very small set of templates
- one short flow
- one explicit activation step
- one SDK integration path

Do not design a large campaign system on the first pass unless the user asks for it.

## Opening Sequence

Read [references/workspace-readiness.md](references/workspace-readiness.md) first.

Use this order:
1. Call `kelpi_workspace_summary`.
2. Summarize what is already present.
3. Pick the shortest path to first value.

## First-Run Branches

If no sender is ready, use [references/sender-setup.md](references/sender-setup.md).

If the user needs a first automation, use [references/first-template-and-flow.md](references/first-template-and-flow.md).

If the flow is ready to go live, use [references/activation-and-sdk.md](references/activation-and-sdk.md).

## Keep The User Moving

- Ask for the goal in plain language if it is missing.
- If the user has no concrete use case, recommend a simple welcome flow first.
- Prefer one recommendation plus two alternatives, not an exhaustive list.
- Keep approval checkpoints crisp.
- Never activate a flow without explicit approval.

## Template And Flow Discipline

- Create templates before creating a flow that references them.
- Keep the first flow small enough that the user can review it quickly.
- Use targeted flow-step tools for edits after creation.
- Use the visual template editor only when the user wants copy or layout iteration.

## Finish The Loop

After activation, continue into SDK tracking instead of stopping at "flow created".

The ideal first-run outcome is:
1. workspace checked
2. sender chosen
3. flow created
4. flow activated
5. SDK path clear
