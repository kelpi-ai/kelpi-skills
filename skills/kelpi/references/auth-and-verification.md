# Auth And Verification

Use this order.

## Standard Sequence

1. Ensure the MCP server entry points at `https://app.kelpi.ai/api/mcp`.
2. Have the user complete auth.
3. Call `kelpi_status`.
4. If `kelpi_status` works, call `kelpi_workspace_summary`.
5. Summarize:
   - workspace name
   - whether a sender exists
   - whether any templates or flows already exist
   - whether a public key already exists

## Success Criteria

Setup is successful when:
- Kelpi tools respond
- the user is authenticated
- workspace summary returns usable state

## Next Step

After success, suggest the smallest next action:
- if no sender exists, start sender setup
- if the workspace is empty, create the first template and flow
- if flows exist, ask whether to create a new flow or inspect an existing one
