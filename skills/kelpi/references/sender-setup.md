# Sender Setup

Handle sender readiness before flow creation.

## Preferred Tool

Use:

```text
kelpi_ensure_sender_identity
```

This is the best first-run tool because it can:
- reuse an existing sender
- create a sender on a verified custom domain
- present a quick-start versus branded-domain choice

## Smooth Decision Policy

If the tool returns a choice between quick start and branded sending:
- recommend quick start for evaluation and speed
- recommend branded setup for production use

Use plain language:
- quick start: sends sooner, uses Kelpi domain
- branded: takes longer, uses the user's domain

## Domain Workflow

If the user chooses branded sending and no verified custom domain exists:
1. use `kelpi_create_domain`
2. show the DNS records clearly
3. wait for the user to add them
4. use `kelpi_verify_domain`
5. return to `kelpi_ensure_sender_identity`

## Defaults

For a first sender:
- `email_local`: prefer `hello`, `founder`, or `support` based on context
- `from_name`: use the founder, company, or product name from context
- `purpose`: use `marketing` for onboarding emails unless the user says otherwise
