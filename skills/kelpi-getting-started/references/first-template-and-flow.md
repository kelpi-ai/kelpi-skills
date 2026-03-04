# First Template And Flow

Optimize for one fast, reviewable first automation.

## If The User Has No Flow In Mind

Recommend this path first:
- welcome flow
- event trigger
- one welcome email
- optional short delay before a second email

Keep v1 intentionally small.

## Tool Order

1. `kelpi_ensure_sender_identity` if sender readiness is unresolved
2. `kelpi_create_template` for each approved email
3. `kelpi_create_flow` with `from_template`
4. optional targeted edits with flow-step tools

## Approval Model

Follow the checkpoint flow already encoded in the Kelpi MCP prompts:
1. gather the business goal
2. show the flow structure
3. wait for approval
4. show email copy
5. wait for approval
6. show final summary
7. wait for explicit create approval
8. create resources
9. ask explicitly before activation

Do not combine design output and creation in the same response.

## Template Guidance

- Always include variable defaults.
- Keep the first email simple and personalized.
- Prefer one primary CTA.
- Use `from_template` in flow email steps.

## Editor Usage

Use `kelpi_open_editor` and `kelpi_listen_editor_chat` when the user wants live visual editing or copy iteration after templates exist.

Do not force the editor loop for every first-run flow.
