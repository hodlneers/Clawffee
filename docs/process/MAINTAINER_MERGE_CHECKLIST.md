# Maintainer Merge Checklist

Use this checklist before merging any PR.

## 1) Scope And Traceability
- [ ] PR links to an issue (`Closes #...` or equivalent)
- [ ] Branch name follows policy (`feature|fix|docs|chore/<issue>-<short-title>`)
- [ ] Change scope is clear and appropriately sized

## 2) Quality Gates
- [ ] Required checks are green (`CI`, `validate-branch-name`, others as configured)
- [ ] Branch is up to date with target branch
- [ ] Conversations are resolved
- [ ] Required approvals are present

## 3) Risk Review
- [ ] Risk level identified (low/medium/high)
- [ ] Backward-compatibility impact reviewed
- [ ] Rollback path is clear for risky changes

## 4) Docs And Policy
- [ ] Docs updated if behavior/contracts changed
- [ ] No vendored snapshot artifacts added
- [ ] Security language remains informational (no guarantee/certification claims)

## 5) Merge Method (Policy)
- [ ] Default to **Rebase and merge**
- [ ] Use **Squash and merge** only for noisy WIP/fixup commit chains
- [ ] Do not use merge commits

## 6) Post-Merge
- [ ] Confirm branch auto-deleted (or delete manually if needed)
- [ ] Confirm target branch remains green after merge
- [ ] If needed, sync `develop`/`main` according to release flow
