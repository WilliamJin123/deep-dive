---
name: calculator
description: A deterministic calculator for mathematical expressions.
license: Apache-2.0
metadata:
  version: "1.0.0"
  author: agno-user
  tags: ["math", "calculator", "deterministic"]
---

# Calculator Skill

Use this skill to perform accurate mathematical calculations.

## When to Use

- The user asks for a math calculation (e.g., "What is 2 + 2?").
- Complex arithmetic is required.
- You need a deterministic answer, avoiding LLM hallucination on math.

## Capabilities

- Basic arithmetic (+, -, *, /)
- Power (** or ^)
- Math functions (sin, cos, tan, log, sqrt, etc. via python's math module)

## Usage

The agent can run the `calculate.py` script with a mathematical expression string.
