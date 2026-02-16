# Clawffee Roadmap — v1.0 to v1.1

This document outlines a **practical, adoption-first roadmap** for Clawffee, sequencing features to maximize trust, utility, and monetization while keeping liability low.

---

## Guiding Principles
- **Utility first, philosophy later**
- **Local-first by default**
- **Informational, not authoritative**
- **Opt-in, reversible, composable**
- **Save users money or protect their systems**

---

## v1.0 — Security Inspector & Skill Vetting (FOUNDATION)

### Goal
Establish Clawffee as a **trusted visibility tool** for OpenClaw skills by making risk legible *before* execution.

This version earns the right to exist.

### Target Outcome
Users say:
> “I won’t install a skill without running Clawffee first.”

### Core Features
- Local CLI (`inspect`, `diff`)
- Static analysis (no runtime guarantees)
- Capability mapping:
  - Shell execution
  - Network egress
  - Filesystem access
  - Env / secrets access
  - Dynamic code & obfuscation
  - Dependency & supply-chain signals
- Risk indicators (INFO / LOW / MEDIUM / HIGH)
- Evidence-backed findings (file + line)
- Diffing across commits / versions
- JSON + Markdown reports

### Explicit Non-Features
- No certification / approval
- No sandboxing or blocking
- No cloud upload by default
- No scores, leaderboards, or public shaming

### Adoption Channels
- CLI-first (copy/paste friendly)
- OpenClaw skill wrapper (thin integration)
- GitHub README examples
- YouTube demos (“before you install any skill…”)

### Monetization (v1.0)
- **Free**: Local scans, single-run analysis
- **Pro** (early):
  - Stored scan history
  - Advanced diffing
  - Policy presets (e.g., “paranoid mode”)
- **Team**:
  - Shared scan artifacts
  - Review workflows
  - Local-only enterprise mode

---

## v1.05 — Hardening & Trust (POLISH)

### Goal
Reduce friction and increase confidence without expanding scope.

### Features
- Faster scanners (AST caching)
- False-positive tuning
- Better dependency graph visualization
- More precise domain extraction
- Ignore lists / allowlists
- Clearer disclaimers & scope docs

### Outcome
Lower noise, higher signal, better retention.

---

## v1.1 — Token Optimization Companion (EXPANSION)

### Goal
Turn Clawffee from “protector” into **everyday utility** by saving users money.

This version scales adoption.

### Target Outcome
Users say:
> “Clawffee paid for itself this month.”

### Core Features
- Token usage tracking (per run / per agent)
- Model-based cost estimation
- Waste pattern detection:
  - Runaway verbosity
  - Rephrasing loops
  - Speculative continuation
- Suggestions (advisory only):
  - Summarize context
  - Tighten system prompts
  - Add stop conditions
  - Insert intent restatement checkpoints

### The Clawffee Moment (Soft Introduction)
- Optional pause suggestion
- Framed as **efficiency optimization**, not care
- No enforcement, no scoring

### Monetization (v1.1)
- **Free**:
  - Basic token counts
  - Single-session estimates
- **Pro**:
  - Historical cost charts
  - Savings deltas (before/after)
  - Optimization recommendations
- **Team**:
  - Budget alerts
  - Cost policies
  - Aggregated reporting

---

## v1.2 — Convergence (OPTIONAL)

### Goal
Unify security + efficiency into a single, coherent workflow.

### Features
- “Before you run” checklist:
  - Skill risk profile
  - Expected token cost
- Combined reports:
  - Risk surface + cost surface
- Optional CI hooks (fail only on user-defined rules)

---

## What Comes Much Later (INTENTIONALLY DEFERRED)
- Runtime enforcement
- Sandboxing
- Automatic blocking
- Public trust scores
- Skill marketplaces
- Any moral or behavioral judgment

These are **deliberately avoided** to prevent strange loops and liability creep.

---

## Strategic Summary
- **v1.0** earns trust (security & clarity)
- **v1.1** earns adoption (money saved)
- **Clawffee Moments** emerge naturally as optimization, not philosophy

> Lead with protection.  
> Scale with efficiency.  
> Let care arrive quietly.

---

## End
