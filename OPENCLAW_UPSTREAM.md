# OpenClaw Upstream Reference (Clawffee)

Clawffee is a companion tool designed to support operators working inside the OpenClaw ecosystem.

We do **not** vendor OpenClaw code in this repository.

## Why this exists

Early in Clawffee’s development we kept an OpenClaw snapshot locally to stay aligned with upstream patterns while planning.
That snapshot was for research only — not a dependency.

Keeping frozen copies in-tree creates two problems:
- It drifts from upstream quietly.
- It adds weight and noise to this repo.

So we track OpenClaw explicitly and fetch it on demand.

## Upstream

- Upstream repository: https://github.com/openclaw/openclaw

Clawffee is **independent** and **not affiliated** with OpenClaw.
We aim for compatibility, not coupling.

## “Validated against” policy

Clawffee is validated against a specific OpenClaw commit or release tag.

- Validated OpenClaw ref: **TBD**
  - Set this to a commit SHA or tag after running the validation flow.
  - Example formats:
    - Tag: v0.8.2
    - Commit: 1a2b3c4d5e6f...

Until a ref is recorded above, treat compatibility as best-effort.

## Fetch OpenClaw locally (on demand)

We fetch OpenClaw into a gitignored directory so it never becomes a vendored dependency.

From repo root:

```bash
./scripts/fetch-openclaw.sh
```

To fetch a specific commit or tag:

```bash
OPENCLAW_REF=v0.8.2 ./scripts/fetch-openclaw.sh
# or
OPENCLAW_REF=1a2b3c4d5e6f ./scripts/fetch-openclaw.sh
```

This will clone (or update) OpenClaw into:

external/openclaw/

That path is intentionally ignored by git.
