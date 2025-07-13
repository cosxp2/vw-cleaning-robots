# VW Cleaning Robots

## Candidate Name: COSMIN PRICOP

## Overview

This project simulates a system for controlling autonomous cleaning robots deployed on a factory floor. Robots receive and execute movement commands to clean a rectangular grid-based workspace.  
The implementation follows the **Hexagonal Architecture** and applies **Tactical Domain-Driven Design patterns**, featuring a rich domain model where business logic is encapsulated within domain entities.

---

## Prerequisites

- Python 3.11+
- [Pipenv](https://pipenv.pypa.io/en/latest/)

---

## System Design

### Architectural Layers

- **Domain Layer**: defines pure business logic (e.g. `Robot`, `Position`, `Orientation`, `WorkspaceShape`)
- **Application Layer**: coordinates parsing and simulation logic, orchestrates domain objects
- **Adapters Layer**:
  - **CLI Adapter**: receives commands via standard input (could be extended to web/UI in the future)

### Design Highlights

- Domain model is rich and encapsulated: `Robot` owns its own state and operations
- Commands like `MOVE`, `LEFT`, and `RIGHT` are represented with an Enum
- Grid is abstracted as a `WorkspaceShape`, allowing future extension to non-rectangular shapes
- Logging and input validation are centralized for clean error handling and debugging
- Robots execute sequentially. The system prevents collisions by skipping moves into occupied positions

---

## How to Run

### 1. Install Dependencies

Execute the following commands from the project root.

```bash
pipenv install
```

### 2. Run via CLI

```bash
chmod +x scripts/run_cli.sh 
./scripts/run_cli.sh examples/<test_file.txt>
```

### 3. Run Tests

```bash
pipenv run pytest
```

### 4. Check Logs

```bash
tail -f simulation.log 
```

## Design Decisions

### Domain Model Benefits
The domain model encapsulates logic within cohesive objects:
- Position handles coordinate movement based on orientation
- Orientation defines valid directions and supports turning left/right
- Command maps input strings to robot actions in a type-safe way
- Robot maintains its own state and executes commands internally
- WorkspaceShape and RectangularGrid abstract spatial constraints

### Abstract Shape Class
To consider an extension of the architecture, the grid shape is defined via an abstract base class (`WorkspaceShape`). This allows support for other grid types (e.g., circular, L shaped) without changing the domain logic

### Grid Constraints
- Grid dimensions must be non-negative to ensure logical consistency (a negative-length space doesn t physically make sense)
- A valid grid must have at least one row or one column to ensure the existence of at least one valid cell

### Orientation Handling
`Orientation` defines a `_clockwise` sequence and uses modular arithmetic to support turning. This setup allows for easy extension to diagonal orientations (e.g., NE, SW) without rewriting the turning logic

### Position Validation
The `is_valid_position()` method encapsulates the logic to determine if a position lies within grid bounds. This abstraction ensures consistent boundary checking across the application

### Parser and Iterable Input
The parser is designed to operate on a generic iterable of strings, using `next()` to process input lines sequentially. This approach allows input to come from any source like such as files, standard input, or APIs. By decoupling input format from data source, the system supports multiple adapters (e.g., CLI, web, networked control) without needing to modify core logic

### Collision Avoidance
Even though the base spec didn’t require collision logic, a realistic robot system must account for physical space occupation. The runner prevents multiple robots from occupying the same cell, and skips conflicting moves

### Empty Command Handling
Blank command strings are accepted without raising errors. This accounts for possible human input mistakes, such as accidentally omitting a command. Rather than failing, the system assumes no commands are intended and continues gracefully, improving robustness