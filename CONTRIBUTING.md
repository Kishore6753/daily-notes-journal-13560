# Contributing Guide

Thank you for your interest in contributing to Daily Notes Journal!

This repository now contains a minimal Python FastAPI scaffold to enable dependency installation and preview startup. Please follow these guidelines when adding code.

## General Guidelines
- Keep changes small and focused.
- Include clear docstrings/comments for public functions, classes, and modules.
- Avoid hard-coding configuration values; use environment variables and document them in a `.env.example` file.

## Python Project Tooling
- Using `pyproject.toml` for configuration.
- Recommended tools:
  - Formatter: `black`
  - Linter: `ruff` (preferred)
  - Type checking: `mypy`
- Suggested commands:
  - Format: `black .`
  - Lint: `ruff check .`
  - Types: `mypy .`
- Suggested ruff rulesets: `E,F,I,UP,B,PT,RET,SIM,PL` (adjust as needed).
- Structure:
  ```
  .
  ├─ src/
  │  └─ app/
  │     ├─ __init__.py
  │     └─ main.py
  ├─ run.py
  ├─ tests/
  └─ pyproject.toml
  ```

## Running Locally
- Install dependencies: `pip install -e .[dev]`
- Copy env: `cp .env.example .env` (optional)
- Start server: `python run.py` (defaults to 0.0.0.0:8000)

## Continuous Integration
- On pushes and PRs, run:
  - `black --check .`
  - `ruff check .`
  - `mypy .`
  - tests (`pytest`) when available

## Commit Conventions
- Use meaningful commit messages.
- Consider Conventional Commits (feat:, fix:, docs:, chore:, refactor:, test:, build:, ci:).

## Documentation
- Keep `README.md` updated with setup and run instructions.
- For public APIs, document endpoints, parameters, and responses.

## Environment Variables
- Do not commit `.env` files.
- Provide `.env.example` listing required variables with placeholder values.

## Security and Compliance
- Do not commit secrets or API keys.
- Run dependency audits (`pip-audit`) periodically.
