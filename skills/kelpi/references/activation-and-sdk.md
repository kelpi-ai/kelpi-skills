# Activation And SDK

Activation is not the end of onboarding.

## Activation Rule

Only call `kelpi_activate_flow` after explicit user approval.

Say plainly that activation means:
- the flow starts listening for real triggers
- real contacts can enter the flow
- real emails can be sent

## Immediate Follow-Through

After activation, move directly into SDK integration.

## SDK Path

Use:

```text
kelpi_get_sdk_snippet
```

Choose the framework that matches the user's stack:
- `nextjs`
- `react`
- `node`
- `express`
- `vanilla`

## Smooth New-User Experience

After retrieving the snippet:
- explain which env var is needed
- explain which file should hold the client initialization
- give one concrete next action for tracking the first event

If you have access to the user's codebase and they want hands-on help, write the snippet into the project. Otherwise, provide the exact file and env placement instructions.
