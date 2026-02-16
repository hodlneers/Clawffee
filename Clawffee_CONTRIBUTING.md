# Contributing to Clawffee ☕🦀

Thanks for your interest in contributing to **Clawffee for Agents**.

Clawffee is a practical, local-first toolkit designed to make AI agent workflows:
- safer
- clearer
- more efficient

This guide explains how to contribute without overcomplicating things.

---

## Project Values (Plain, Not Philosophical)

We try to keep Clawffee:
- useful first
- calm by default
- non-authoritative
- easy to remove
- boring in a good way

If a contribution adds clarity, reduces risk, or saves resources, it probably fits.

If it introduces enforcement, scoring, or moral framing, it probably doesn’t.

---

## What We’re Happy to Accept

### Code Contributions
- new detectors for skill inspection
- improved static analysis accuracy
- performance improvements
- better diffing and reporting
- clearer CLI output
- bug fixes and tests

### Documentation
- clearer explanations
- usage examples
- edge cases
- security disclaimers written in plain language

### Issues & Discussions
- false positives or false negatives
- unclear output
- confusing UX
- real-world OpenClaw use cases

---

## What We Avoid (By Design)

Please avoid contributions that:
- enforce behavior or block execution
- certify skills as “safe” or “unsafe”
- assign moral or ethical scores
- add permanent background monitoring
- require cloud services by default
- collect or transmit user data
- anthropomorphize agents

Clawffee informs.  
It does not judge.

---

## How to Contribute Code

1. Fork the repository
2. Create a focused branch:
   - `feature/<short-description>`
   - `fix/<short-description>`
3. Keep changes scoped
4. Add or update tests if behavior changes
5. Explain what the change does, not why it’s “good”

---

## Code Style & Expectations

- Prefer clarity over cleverness
- Favor explicit over implicit
- Keep detectors modular and explainable
- Every risk indicator should:
  - point to evidence
  - explain what was detected
  - avoid guessing intent

If a human can’t understand the output in under two minutes, it’s probably too complex.

---

## Reporting Security Concerns

If you discover:
- a vulnerability in Clawffee itself
- a detector that leaks data
- behavior that could surprise users

Please do not open a public issue.

Instead, contact the maintainers privately (see README for details).

---

## Scope Boundaries

Clawffee is intentionally:
- advisory
- local-first
- non-blocking

Pull requests that expand scope into:
- runtime enforcement
- sandboxing
- certification
- surveillance

will likely be declined.

---

## Testing & Validation

Before submitting:
- run the CLI against real OpenClaw skills
- verify output is stable and readable
- confirm no secrets or prompts are logged
- ensure behavior works offline

---

## Licensing

By contributing, you agree that your work may be included under the project’s license.

If you have questions about licensing or attribution, open an issue before submitting a PR.

---

## Final Note

Clawffee exists to make agent systems feel:
- more predictable
- more transparent
- less chaotic

If your contribution moves things in that direction, it’s welcome.

Thanks for helping keep things calm. ☕
