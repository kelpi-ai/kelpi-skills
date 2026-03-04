# Kelpi Skills

Kelpi onboarding skills for AI agents, optimized for the official hosted Kelpi MCP endpoint:

```text
https://app.kelpi.ai/api/mcp
```

These skills are designed to make a new Kelpi user successful quickly:
- connect Kelpi MCP
- authenticate and verify workspace access
- inspect workspace readiness
- set up a sender
- launch a first flow
- continue into SDK setup

## Quick Start

1. Install the skills:

   ```bash
   npx skills add kelpi-ai/kelpi-skills
   ```

2. In the installer, choose:
   - `Claude Code` if you want these in Claude Code
   - `Project` for repo-local install or `Global` for machine-wide install
   - `Symlink` unless you specifically want copied files

3. Add Kelpi MCP to Claude Code:

   ```bash
   claude mcp add --transport http kelpi "https://app.kelpi.ai/api/mcp"
   ```

4. Restart Claude Code.

5. Start with:

   ```text
   /kelpi help me set up Kelpi and onboard my first flow
   ```

## Recommended First Prompts

Broad setup plus onboarding:

```text
/kelpi help me set up Kelpi and onboard my first flow
```

Connection and auth only:

```text
/kelpi connect Kelpi MCP, authenticate me, and verify my workspace
```

First workflow after setup:

```text
/kelpi inspect my workspace and help me launch a simple welcome flow
```

## Included Skill

### `kelpi`

Connects the hosted MCP endpoint, guides authentication, verifies workspace access, inspects workspace readiness, sets up a sender, creates a first flow, activates it safely, and continues into SDK follow-through.

## Intended Experience

This repo is intentionally onboarding-first.

It does not try to expose every possible Kelpi workflow up front. The default path is:
1. connect
2. verify
3. inspect
4. launch one small flow

That keeps the first-run experience short and concrete instead of overwhelming the user with tool lists.

## Claude Code Setup Notes

These skills assume:
- Kelpi's official MCP endpoint is `https://app.kelpi.ai/api/mcp`
- the user will authenticate through the MCP flow when prompted
- onboarding continues after connection instead of stopping at "MCP is installed"

## Repository Layout

```text
skills/
  kelpi/
```

The `skills/` directory is the source of truth for distribution. Do not add `.claude/skills` or `.agents/skills` to this repo; those are install targets in consuming projects.

## Validation

Run the local validator before publishing changes:

```bash
python3 scripts/validate_skills.py
```
