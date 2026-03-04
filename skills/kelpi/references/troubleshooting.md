# Troubleshooting

Keep troubleshooting short and specific.

## Common Problems

### Auth failure

Symptoms:
- `kelpi_status` fails
- the client says auth is required

Actions:
1. Re-run `kelpi_login` if the client supports it.
2. Confirm the MCP server URL is exactly `https://app.kelpi.ai/api/mcp`.
3. Retry `kelpi_status`.

### Connected but workspace unavailable

Symptoms:
- auth succeeds
- workspace access is denied or incomplete

Actions:
1. Tell the user auth worked but the workspace is not ready yet.
2. Ask them to finish any required account or workspace setup.
3. Retry `kelpi_workspace_summary`.

### Session issues or flaky first run

Symptoms:
- the server was added but tools do not respond consistently
- the client loses the session after reconnecting

Actions:
1. Retry once.
2. Reconnect the MCP server entry if needed.
3. Re-run auth.
4. Re-verify with `kelpi_status`.

## Tone

- Do not overwhelm the user with protocol details.
- Always end with the next exact action to take.
