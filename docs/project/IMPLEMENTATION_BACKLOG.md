# Implementation Backlog

This backlog converts the current docs into actionable implementation slices.

## Milestone 1: Core Scanner (Current)
- [x] Bootstrap package layout
- [x] Add base models and report renderers
- [x] Implement initial pattern-based `SecurityInspector`
- [x] Add OpenClaw adapter serialization layer
- [x] Add unit tests
- [x] Add CI workflow

## Milestone 2: Detection Quality
- [ ] Add configurable rule packs and severities
- [ ] Add duplicate-indicator collapsing
- [ ] Add dependency manifest inspection (`package.json`, `requirements.txt`)
- [ ] Add diff mode between scans

## Milestone 3: OpenClaw Integration
- [ ] Add plugin metadata and registration stubs
- [ ] Add OpenClaw invocation entrypoint
- [ ] Add compatibility tests against real OpenClaw fixture skills

## Milestone 4: Token Optimizer (v1.1)
- [ ] Define token usage model and telemetry boundaries
- [ ] Add token waste heuristics
- [ ] Add advisory recommendations and report sections
