# Kelpi Routing

Route by user intent, not by tool names.

## Use `kelpi-mcp-setup`

Choose setup when the user says things like:
- "set up Kelpi"
- "connect Kelpi MCP"
- "add Kelpi to Claude Code"
- "use https://app.kelpi.ai/api/mcp"
- "log in to Kelpi"
- "Kelpi tools are not working"

Order:
1. Connect the hosted HTTP endpoint.
2. Complete auth.
3. Verify with `kelpi_status`.
4. Inspect workspace state with `kelpi_workspace_summary`.
5. Offer the next step: first template/flow onboarding.

## Use `kelpi-getting-started`

Choose getting started when the user says things like:
- "help me onboard Kelpi"
- "set up my first flow"
- "create a welcome flow"
- "create my first template"
- "get my sender set up"
- "activate my first automation"
- "set up the SDK"

Order:
1. Check workspace state.
2. Resolve sender readiness.
3. Design the first small flow.
4. Create resources after approval.
5. Activate only after explicit approval.
6. Continue into SDK tracking.

## Ambiguous Requests

If the user asks for "Kelpi setup" or "help me get started" and it is unclear whether MCP is already connected:
- assume setup first
- verify quickly
- move into getting started without making the user restate the goal
