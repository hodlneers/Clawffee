# Contributing to Clawffee

Thanks for contributing.

Clawffee is a local-first security inspection tool. Changes should prioritize clarity, reliability, and compatibility with the documented architecture.

## Branch Strategy

- `main`: stable branch. No direct pushes.
- `develop`: integration branch. No direct pushes.
- `feature/<issue>-<short-title>`: new feature work from `develop`.
- `fix/<issue>-<short-title>`: bug fixes from `develop`.
- `docs/<issue>-<short-title>`: documentation changes from `develop`.
- `chore/<issue>-<short-title>`: maintenance/tooling updates from `develop`.

## Required Workflow

1. Create your branch from `develop`.
2. Keep commits focused and logically grouped.
3. Rebase your branch on latest `develop` before opening/updating PR.
4. Open PR targeting `develop`.
5. After review and CI pass, merge using repository merge policy.

## Merge Policy

- Default: **Rebase and merge** to keep history linear and preserve meaningful commits.
- Selective: **Squash and merge** when a branch contains WIP/fixup micro-commits that do not stand alone.
- Avoid: merge commits for routine PRs.

## Commit Message Guidance

Use concise commit messages that describe intent clearly.

Examples:
- `feat: add dependency manifest detector scaffold`
- `fix: correct severity aggregation for empty indicator sets`
- `docs: clarify OpenClaw upstream validation policy`

## Quality Expectations

- Add or update tests for behavior changes.
- Keep docs in sync with implementation.
- Do not introduce claims of security guarantees or certifications.
- Prefer local-first defaults; avoid unnecessary external coupling.

## Pull Request Checklist

- [ ] Branch is up to date with `develop`
- [ ] Tests pass locally (or CI status is green)
- [ ] Docs updated if behavior/contracts changed
- [ ] No vendored external snapshot artifacts

## Governance Notes

Branch protection settings should enforce:
- PR requirement for `main` and `develop`
- approval requirement before merge
- disallow direct pushes

Maintainers should use:
- `docs/process/MAINTAINER_MERGE_CHECKLIST.md`



## Branch Naming Examples

- `feature/142-add-diff-mode`
- `fix/207-handle-empty-target`
- `docs/315-update-upstream-policy`
- `chore/418-ci-branch-name-check`
