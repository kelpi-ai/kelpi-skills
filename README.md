# Kelpi Skills

Kelpi onboarding skills for AI coding agents.

These skills are designed around Kelpi's official hosted MCP endpoint:

```text
https://app.kelpi.ai/api/mcp
```

## Install

Once this repo is published, install it with:

```bash
npx skills add kelpi-ai/kelpi-skills
```

Choose:
- `Claude Code` as the target agent if you want these in Claude Code
- `Project` scope for repo-local installation or `Global` for machine-wide installation
- `Symlink` unless you specifically want copied files

## After Install

Add the Kelpi MCP server:

```bash
claude mcp add --transport http kelpi "https://app.kelpi.ai/api/mcp"
```

Restart Claude Code, then use the skills directly:

```text
/kelpi help me set up Kelpi and onboard my first flow
```

Or run the setup skill explicitly:

```text
/kelpi-mcp-setup connect Kelpi MCP, authenticate me, and verify my workspace
```

Then continue into onboarding:

```text
/kelpi-getting-started inspect my workspace and help me launch a simple welcome flow
```

## Included Skills

- `kelpi`
  - Routes broad Kelpi setup and onboarding requests
- `kelpi-mcp-setup`
  - Connects the hosted MCP endpoint, authenticates, and verifies workspace access
- `kelpi-getting-started`
  - Guides a new user from workspace inspection to sender setup, first flow, activation, and SDK follow-through

## Repo Layout

```text
skills/
  kelpi/
  kelpi-mcp-setup/
  kelpi-getting-started/
```

The `skills/` directory is the source of truth for distribution. Do not add `.claude/skills` or `.agents/skills` to this repo; those are installation targets in consuming projects.

## Validate

Run the local validator before publishing changes:

```bash
python3 scripts/validate_skills.py
```
