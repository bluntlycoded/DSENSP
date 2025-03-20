# DSENSP Design Specification

## Overview
Our dynamic self-evolving network security protocol integrates three key modules:
- Cryptography Module: Manages dynamic encryption and key changes.
- Routing Module: Provides adaptive routing strategies.
- Deception Module: Implements decoy and honeypot mechanisms.

A genetic algorithm evolves a flat set of parameters that are decoded and applied to these modules. A simulation engine evaluates overall fitness based on security, efficiency, and deception performance.

## Modules and Interfaces

- Protocol Manager:
  - Coordinates protocol evolution and simulation.
  - Decodes GA chromosomes into module-specific parameters.

- GA Engine (src/main/ga/):
  - Contains the core genetic algorithm, plus separate files for selection, mutation, and crossover.

- Network Simulation (src/main/network_simulation/):
  - Simulates network conditions and integrates module evaluations.
  - Provides basic node and topology models.

- Logging (src/main/logging/):
  - Offers centralized logging and immutable audit trails.

## Data Flow Diagram
Refer to architecture_diagram.png for a high-level overview.
