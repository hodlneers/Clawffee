# Clawffee v1 --- Repo Skeleton + Interfaces

## Overview

This document defines the recommended repository structure, module
contracts, core interfaces, and report schema for Clawffee v1 (Security
Inspector + Diff Engine).

Clawffee is a **local-first static analysis tool** designed to inspect
OpenClaw skills.

------------------------------------------------------------------------

# Repository Structure

    clawffee/
    ├── package.json
    ├── README.md
    ├── tsconfig.json
    ├── src/
    │   ├── cli/
    │   │   ├── index.ts
    │   │   ├── commands/
    │   │   │   ├── inspect.ts
    │   │   │   ├── diff.ts
    │   │   │   └── report.ts
    │   │   └── args.ts
    │   │
    │   ├── core/
    │   │   ├── scanner.ts
    │   │   ├── diffEngine.ts
    │   │   ├── capabilityAggregator.ts
    │   │   └── severity.ts
    │   │
    │   ├── detectors/
    │   │   ├── base.ts
    │   │   ├── shell/
    │   │   │   └── shellDetector.ts
    │   │   ├── network/
    │   │   │   └── networkDetector.ts
    │   │   ├── filesystem/
    │   │   │   └── filesystemDetector.ts
    │   │   ├── secrets/
    │   │   │   └── envDetector.ts
    │   │   ├── dynamic/
    │   │   │   └── dynamicCodeDetector.ts
    │   │   └── dependencies/
    │   │       └── dependencyDetector.ts
    │   │
    │   ├── models/
    │   │   ├── report.ts
    │   │   ├── indicator.ts
    │   │   ├── capability.ts
    │   │   └── diff.ts
    │   │
    │   ├── utils/
    │   │   ├── fileWalker.ts
    │   │   ├── git.ts
    │   │   ├── logger.ts
    │   │   └── hash.ts
    │   │
    │   └── constants/
    │       ├── riskIndicators.ts
    │       └── patterns.ts
    │
    └── tests/
        ├── fixtures/
        ├── detectorTests/
        └── integration/

------------------------------------------------------------------------

# Core Interfaces

## Detector Interface

All detectors must implement:

``` ts
export interface Detector {
  id: string;
  description: string;

  scan(filePath: string, content: string): DetectionResult[];
}

export interface DetectionResult {
  indicatorId: string;
  file: string;
  line?: number;
  snippet?: string;
  confidence: "LOW" | "MEDIUM" | "HIGH";
}
```

Detectors should be: - Stateless - Pure (no side effects) -
Deterministic

------------------------------------------------------------------------

## Indicator Model

``` ts
export type Severity = "INFO" | "LOW" | "MEDIUM" | "HIGH";

export interface RiskIndicator {
  id: string;
  severity: Severity;
  title: string;
  description: string;
}
```

Indicators must not use moral or guarantee language.

------------------------------------------------------------------------

## Capability Model

``` ts
export interface CapabilityProfile {
  shell: {
    canExecute: boolean;
  };
  network: {
    canConnect: boolean;
    domains: string[];
    unbounded: boolean;
  };
  filesystem: {
    canRead: boolean;
    canWrite: boolean;
    recursiveDeleteDetected: boolean;
  };
  secrets: {
    envAccess: "NONE" | "NARROW" | "BROAD";
  };
  dynamicCode: {
    present: boolean;
  };
  dependencies: {
    count: number;
    postInstallScripts: boolean;
  };
}
```

------------------------------------------------------------------------

# Scan Report Format

``` ts
export interface ScanReport {
  tool: {
    name: "clawffee";
    version: string;
  };

  target: {
    type: "path" | "git";
    path?: string;
    repoUrl?: string;
    ref?: string;
  };

  summary: {
    filesScanned: number;
    overallProfile: "LOW" | "MEDIUM" | "HIGH";
  };

  capabilities: CapabilityProfile;

  indicators: {
    id: string;
    severity: Severity;
    file: string;
    line?: number;
    detail: string;
    confidence: "LOW" | "MEDIUM" | "HIGH";
  }[];

  disclaimer: string;
}
```

------------------------------------------------------------------------

# Diff Engine Interface

``` ts
export interface DiffResult {
  newIndicators: string[];
  removedIndicators: string[];
  changedSeverity: string[];

  networkChanges: {
    addedDomains: string[];
    removedDomains: string[];
  };

  dependencyChanges: {
    added: string[];
    removed: string[];
  };
}
```

------------------------------------------------------------------------

# Severity Calculation Strategy

Severity should be computed by: - Highest indicator present - Aggregated
risk signals - Never claim "safe"

Example logic:

-   If HIGH indicators present → overallProfile = "HIGH"
-   If only MEDIUM → overallProfile = "MEDIUM"
-   Else → "LOW"

------------------------------------------------------------------------

# CLI Command Interfaces

## inspect

``` ts
inspect(target: string, options: InspectOptions): ScanReport
```

## diff

``` ts
diff(base: string, head: string): DiffResult
```

------------------------------------------------------------------------

# Design Constraints

-   Local-first execution
-   No network calls unless explicitly scanning remote repo
-   No telemetry
-   Deterministic output
-   Human-readable Markdown conversion layer

------------------------------------------------------------------------

# Future Extensions

-   Token usage module
-   Cost estimation engine
-   Policy enforcement layer (opt-in)
-   Optional UI dashboard

------------------------------------------------------------------------

End of Repo Skeleton + Interfaces Spec
