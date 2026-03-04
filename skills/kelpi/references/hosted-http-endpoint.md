# Hosted HTTP Endpoint

Kelpi's official MCP endpoint is:

`https://app.kelpi.ai/api/mcp`

## Default Setup Path

Optimize for the shortest successful setup.

For Claude Code, use:

```bash
claude mcp add --transport http kelpi "https://app.kelpi.ai/api/mcp"
```

Then run:

```text
kelpi_login
```

Use this path by default for new users unless they explicitly ask for a different client or installation method.

## Guidance

- Prefer one recommended path, not a matrix of options.
- Give the exact endpoint string with no substitutions.
- Assume new users want the fastest way to first success.
- After setup, verify immediately with `kelpi_status`.
