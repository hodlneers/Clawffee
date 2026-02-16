# Clawffee Preliminary Design Report (PDR)

## 1. Purpose

This PDR defines the initial architecture and delivery plan for Clawffee's MVP robotic barista flow, with OpenClaw-aligned modular skills and planner orchestration.

## 2. Architecture Overview

System layers:
1. Interface Layer: CLI or minimal HTTP endpoint for brew request intake.
2. Agent/Planner Layer: OpenClaw planner that sequences espresso workflow steps.
3. Skill Layer: isolated skills for grind, dose, tamp, attach, brew, detach, clean.
4. Hardware Abstraction Layer: simulated adapters first, real device adapters later.
5. Safety and Logging Layer: guard checks, confirmation gate, and structured logs.

## 3. Core Modules

- `clawffee/interface/`: request intake and status reporting.
- `clawffee/planners/espresso_planner.py`: fixed-sequence planner.
- `clawffee/skills/`: skill implementations.
- `clawffee/hardware/`: simulation and device adapters.
- `clawffee/safety/`: thresholds and abnormal-state checks.
- `clawffee/logging/`: JSON event logging.

## 4. Safety Considerations

- Preflight checks before skill execution.
- Human confirmation gate when safety thresholds are crossed.
- Immediate fail-safe transition on critical errors.
- No silent retries on potentially unsafe actions.

## 5. Testing Strategy

- Unit tests per skill.
- Planner tests for sequence correctness.
- Integration tests for end-to-end simulated brew.
- Fault-injection tests for abnormal sensor scenarios.

## 6. Delivery Plan

- Week 1: finalize requirements and constraints.
- Week 2: hardware simulation adapters.
- Weeks 3-4: core skills + tests.
- Week 5: planner and OpenClaw integration.
- Week 6: interface implementation.
- Week 7: hardening, integration tests, docs.
- Week 8: MVP tag and feedback collection.

## 7. Risks and Mitigation

- Hardware interface drift: enforce stable adapter interfaces.
- Unsafe state transitions: centralize safety checks.
- Integration complexity: simulation-first with deterministic tests.
- Scope creep: keep single-drink MVP boundaries.

## 8. Exit Criteria

The PDR phase is complete when architecture, safety model, and delivery milestones are agreed and traceable to requirements and MVP spec docs.
