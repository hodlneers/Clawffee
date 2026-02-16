# Clawffee v1 — Security Inspector & Skill Vetting (MVP Spec)

## Product Goal
Provide a **local-first, informational security inspection** tool for OpenClaw skills that helps builders understand a skill’s **capabilities, risk surface, and changes over time** *before* enabling it.

Clawffee is a **visibility and decision aid**, not a certification body.

---

## Non-Goals (v1)
Clawffee v1 explicitly does **not**:
- certify skills as “safe/unsafe”
- claim malware detection or provide guarantees
- sandbox or block execution (advisory only)
- upload code to a cloud service by default
- collect or store prompts, user data, or secrets
- maintain public leaderboards, scores, or shaming lists

---

## Target Users
1. OpenClaw builders installing community skills
2. Teams running agents locally (Mac mini / workstation)
3. “I want to save my keys and my machine” power users

---

## Core User Stories
### US-1: “Before I enable a skill, tell me what it can do.”
Clear capability summary: filesystem, network, shell, env access.

### US-2: “Tell me what changed since last time.”
Diff across commits/tags to spot supply-chain risk.

### US-3: “Give me risk indicators without drama.”
Non-judgmental flags like “unbounded network” or “reads all env”.

### US-4: “Work offline and locally.”
Runs entirely on the user’s machine.

---

## Product Surface Area (MVP)
### CLI (Primary)
Commands:
- `clawffee inspect <path|repo-url>`
- `clawffee diff <path|repo-url>`
- `clawffee report <scan.json>`

Reports:
- JSON (default)
- Markdown (optional)

---

## Capability Detection (v1)
- Shell execution
- Network egress
- Filesystem access
- Secrets / env access
- Dynamic code & obfuscation
- Dependency & supply-chain signals

---

## Risk Indicators
Indicators are **informational**, not guarantees.

Severity: INFO, LOW, MEDIUM, HIGH

Examples:
- HIGH: Executes shell commands
- HIGH: Broad env access
- MEDIUM: Filesystem writes
- LOW: Bounded network calls

---

## Diff Report
Highlights:
- New HIGH indicators
- Network scope expansion
- Filesystem changes
- Dependency drift

---

## UX Principles
- “Here’s what we can see” language
- No moral framing
- Calm, factual tone

---

## Storage & Privacy
- Local-only by default
- No telemetry
- Optional local scan storage

---

## Acceptance Criteria
- Consistent reports
- Meaningful diffs
- Fully local execution
- No implied guarantees

---

## v1.1 Preview — Token Optimization
- Token usage per run
- Cost estimation
- Waste detection
- Advisory Clawffee moments
