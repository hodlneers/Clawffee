# Clawffee Requirements Document

This document captures functional and non-functional requirements for the Clawffee MVP described in `docs/Clawffee_MVP_Spec.md`.

## Functional Requirements

### FR-1: Drink Request Intake
The system SHALL accept an espresso request through a CLI command or minimal HTTP endpoint.

### FR-2: Hardware Readiness
The system SHALL initialize simulated/real hardware, confirm readiness, and fail safely if readiness checks fail.

### FR-3: Espresso Workflow Execution
The system SHALL execute the espresso sequence in order:
1. Grind beans
2. Dose portafilter
3. Tamp puck
4. Attach portafilter
5. Start brew
6. Detach portafilter
7. Quick clean

### FR-4: Safety Confirmation Gate
The system SHALL require explicit user confirmation before brew start if abnormal sensor conditions are detected.

### FR-5: Runtime Status and Error Reporting
The system SHALL expose progress states and actionable error messages during execution.

### FR-6: Logging
The system SHALL persist timestamped logs including key brew parameters and safety-related events.

## Non-Functional Requirements

### NFR-1: Safety Behavior
On any unrecoverable fault, the system SHALL transition to a safe state and halt execution.

### NFR-2: Reliability
The MVP SHOULD complete at least 10 consecutive simulated brew cycles without unhandled exceptions.

### NFR-3: Setup Time
A new contributor SHOULD be able to run the simulated MVP in under 30 minutes using project docs.

### NFR-4: Extensibility
Skill/planner interfaces SHOULD allow additional drink recipes and hardware adapters with minimal refactor.

### NFR-5: Testability
Core skills and planner flow SHALL be covered by unit and integration tests runnable in CI.

### NFR-6: Documentation Quality
README and docs SHALL include setup, execution, troubleshooting, and extension guidance.

## Acceptance Criteria
- Espresso flow runs end-to-end in simulation mode.
- Safety gate triggers on abnormal sensor input.
- Logs are written with expected fields and timestamps.
- Test suite passes in CI.
