# Workspace Readiness

Start every onboarding session here.

## First Call

Call:

```text
kelpi_workspace_summary
```

## Summarize Only What Matters

Report:
- workspace name
- sender default present or missing
- verified domains present or missing
- recent templates and flows
- whether a public key already exists

## Branching

### Empty workspace

If the workspace is mostly empty:
- set up sender readiness first
- then create a simple welcome flow

### Partially configured workspace

If sender or templates already exist:
- reuse what is already there when it makes onboarding faster
- avoid recreating duplicate resources

### Existing active flows

If active flows already exist:
- ask whether the user wants a new flow or to inspect the existing setup

## Recommended First Use Case

If the user has no defined use case, recommend:
- a welcome flow triggered by signup or account creation

Alternatives:
- trial reminder flow
- re-engagement flow
