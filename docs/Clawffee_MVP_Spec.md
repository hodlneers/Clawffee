# Clawffee MVP Specification

## 1. Objective

The Minimum Viable Product (MVP) for Clawffee aims to deliver a proof-of-concept robotic barista capable of preparing a basic espresso beverage autonomously while demonstrating the core principles of safety, modularity, and extensibility set out in the Preliminary Design Report. The MVP should be sufficiently functional to showcase the feasibility of the system, collect user feedback, and lay the groundwork for subsequent iterations.

## 2. Scope of the MVP

The MVP will implement only the essential features required to brew a single espresso and serve it to the user. Optional or secondary features (milk steaming, multiple drink types, advanced UI) are deferred to later releases.

### 2.1 Functional Requirements

- Drink Request Submission: Provide a simple interface (command line or minimal web UI) for users to request an espresso.
- Hardware Initialization: Warm up the espresso machine, check water level, and calibrate sensors.
- Recipe Execution: Execute the espresso recipe via an automated sequence of skills:
  - Grind and dose beans
  - Tamp the puck
  - Attach portafilter
  - Brew shot using preset parameters
  - Detach portafilter and perform a quick clean
- Status Reporting: Show real-time status updates during preparation (heating, grinding, brewing, complete) and final result. Provide error messages if a fault is detected.
- Safety Confirmation: Require user confirmation before commencing brew if any sensor reading is abnormal (for example machine overheating or door open).
- Logging: Record brew parameters (grind size, time, yield) and any deviations for later analysis.

### 2.2 Non-Functional Requirements

- Safety and Compliance: Conform to the security inspector guidelines described in the PDR. Avoid actions that might cause harm and always fall back to a safe state on error.
- Reliability: Operate for at least 10 consecutive brew cycles without unhandled exceptions.
- Ease of Setup: Developer docs should enable a new contributor to set up and run the MVP using simulated hardware in under 30 minutes.
- Extensibility: Interfaces should support adding new drinks or hardware without significant refactoring.
- Documentation: Provide clear README and API docs; include recipe extension and calibration guidance.

## 3. System Components for MVP

- Hardware Simulation: Initially run against simulated modules (dummy implementations of ArmController, Grinder, BrewUnit). Real hardware adapters should conform to the same interfaces.
- Core Skills:
  - `grind_beans`
  - `dose_portafilter`
  - `tamp_puck`
  - `attach_portafilter`
  - `start_brew`
  - `detach_portafilter`
  - `quick_clean`
- Simple Planner: An `espresso` planner that sequences core skills with fixed parameters.
- Agent: OpenClaw agent with memory, planning, and security inspector enabled; initially load only espresso planner and core skills.
- User Interface:
  - CLI flow: user executes a brew command, or
  - Minimal endpoint: `POST /make-espresso` with JSON status updates.
- Logging Facility: Write action and sensor logs to `logs/brew_log.json` with timestamped events.

## 4. Implementation Approach

- Repository Structure: Follow `docs/Clawffee_Repo_Structure_and_Interfaces.md`.
- Dependencies: Python 3.10+; FastAPI or Flask for optional web interface; simulation-first hardware abstraction.
- Testing: Use `pytest` for unit tests and integration tests, including abnormal conditions.
- CI: Use GitHub Actions for test and static checks (`flake8`, `mypy`).
- Documentation: README setup path, simulation runbook, and documented skills/planners.

## 5. MVP Deliverables

- Executable Code: installable/runable Python package with skills, planner, and agent wiring.
- Simulation Environment: scripts/instructions to run against simulated hardware.
- Documentation:
  - `README.md`
  - `docs/Clawffee_MVP_Spec.md`
  - API docs for REST mode (if enabled)
- Test Suite: unit + integration tests with run instructions.
- Logging Data: sample brew logs demonstrating expected behavior.

## 6. Timeline

| Milestone | Description | Timeframe |
| --- | --- | --- |
| Requirements Finalization | Confirm functional and non-functional requirements | Week 1 |
| Hardware Abstraction | Implement simulated hardware modules | Week 2 |
| Skill Implementation | Build and test core skills | Weeks 3-4 |
| Planner and Agent Setup | Compose skills into planner and integrate OpenClaw agent | Week 5 |
| UI/API Development | Implement CLI or minimal web interface | Week 6 |
| Testing and Debugging | Integration tests and defect fixes | Week 7 |
| Documentation | README, MVP spec, developer notes | Week 7 |
| MVP Release | Tag MVP and collect feedback | Week 8 |

## 7. Out of Scope for MVP

- Multi-drink recipes (for example cappuccino, latte) and milk steaming support.
- Adaptive brewing based on dynamic sensor feedback.
- Advanced web UI with drink customization and user accounts.
- Remote monitoring and cloud analytics.
- Automatic maintenance routines (descaling, deep cleaning).

## 8. Conclusion

This MVP establishes a practical baseline for Clawffee by delivering a working espresso automation flow grounded in safety, modularity, and extensibility. Completion validates the architecture direction, enables stakeholder feedback, and provides the basis for expanded drink workflows.
