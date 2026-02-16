# Clawffee v1 --- Security Inspector & Skill Vetting (MVP Spec)

## Product Goal

Provide a **local-first, informational security inspection** tool for
OpenClaw skills that helps builders understand a skill's **capabilities,
risk surface, and changes over time** *before* enabling it.

Clawffee is a **visibility and decision aid**, not a certification body.

------------------------------------------------------------------------

## Non-Goals (v1)

Clawffee v1 explicitly does **not**: - certify skills as "safe/unsafe" -
claim malware detection or provide guarantees - sandbox or block
execution (advisory only) - upload code to a cloud service by default -
collect or store prompts, user data, or secrets - maintain public
leaderboards, scores, or shaming lists

------------------------------------------------------------------------

## Target Users

1)  OpenClaw builders installing community skills\
2)  Teams running agents locally (Mac mini / workstation)\
3)  Power users who want clarity before granting permissions

------------------------------------------------------------------------

## Core User Stories

### US-1: "Before I enable a skill, tell me what it can do."

Clear capability summary: filesystem, network, shell, env access, etc.

### US-2: "Tell me what changed since last time."

Diff report across commits/tags to detect supply-chain risk.

### US-3: "Give me risk indicators without drama."

Non-judgmental flags such as: - unbounded network access\
- broad environment variable reads\
- recursive file deletion

### US-4: "Work offline and locally."

Fully local operation by default.

------------------------------------------------------------------------

## Product Surface Area (MVP)

### CLI (Primary Interface)

Commands: - `clawffee inspect <path|repo-url>` -
`clawffee diff <path|repo-url> --against <ref>` -
`clawffee report <scan.json> --format md`

------------------------------------------------------------------------

## Capability Detection Areas (v1)

### Shell Execution

-   child_process, subprocess, os.system, exec
-   Download-and-execute patterns

### Network Egress

-   HTTP libraries
-   Hardcoded domains
-   Unbounded dynamic URLs

### Filesystem Access

-   Read/write operations
-   Recursive deletion
-   Writes outside project root

### Environment / Secrets

-   process.env / os.environ
-   Broad env access patterns
-   Common API key references

### Dynamic Code / Obfuscation

-   eval / exec
-   Dynamic imports
-   Base64 decoding patterns

### Dependencies

-   Postinstall scripts
-   Remote git dependencies
-   Lockfile drift

------------------------------------------------------------------------

## Risk Indicator Format

Each indicator includes: - id - severity (INFO \| LOW \| MEDIUM \|
HIGH) - title - detail - evidence (file + line) - confidence (LOW \|
MEDIUM \| HIGH)

No "safe/unsafe" language.

------------------------------------------------------------------------

## Diff Mode

Highlights: - New HIGH indicators - Expanded filesystem scope - New
network endpoints - New dynamic code patterns - Dependency changes

------------------------------------------------------------------------

## Privacy & Data Handling

Default behavior: - Fully local - No telemetry - No prompt storage -
Optional local scan history

------------------------------------------------------------------------

## Acceptance Criteria (v1)

Clawffee v1 is complete when: 1. Inspect generates consistent JSON
reports 2. Diff clearly highlights meaningful changes 3. Reports are
readable in under 2 minutes 4. Tool runs entirely offline 5. No
guarantee language exists in output

------------------------------------------------------------------------

## Future Companion: Token Optimization

Planned addition: - Token usage tracking - Cost estimation - Waste
pattern detection - Advisory optimization suggestions - Optional
"Clawffee Moment" pause suggestion

------------------------------------------------------------------------

End of MVP Spec
