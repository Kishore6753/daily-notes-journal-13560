# Contributing Guide

Thank you for your interest in contributing to Daily Notes Journal!

This repository is currently a scaffold with no implementation code. To prepare for incoming contributions, we define baseline expectations for code quality, linting, and static analysis. Please follow these guidelines when adding code.

## General Guidelines
- Keep changes small and focused.
- Include clear docstrings/comments for public functions, classes, and modules.
- Avoid hard-coding configuration values; use environment variables and document them in a `.env.example` file.

## Python Projects (if Python is chosen)
- Use `pyproject.toml` to configure tools.
- Recommended tools:
  - Formatter: `black`
  - Import sorter: `isort`
  - Linter: `ruff` (preferred) or `flake8`
  - Type checking: `mypy`
- Suggested commands:
  - Format: `black . && isort .`
  - Lint: `ruff check .` (or `flake8`)
  - Types: `mypy .`
- Suggested ruff rulesets: `E,F,I,UP,B,PT,RET,SIM,PL` (adjust as needed).
- Minimum structure:
  ```
  .
  ├─ src/
  │  └─ app/__init__.py
  ├─ tests/
  └─ pyproject.toml
  ```

## Node.js/TypeScript Projects (if Node is chosen)
- Use `package.json` to configure scripts and dev dependencies.
- Recommended tools:
  - Linter: `eslint` (with airbnb/base or standard config)
  - Formatter: `prettier`
  - Types: `typescript` + `tsc` (if TS)
- Suggested scripts:
  - `"lint": "eslint ."`
  - `"format": "prettier --write ."`
  - `"typecheck": "tsc --noEmit"`
- Minimum structure:
  ```
  .
  ├─ src/
  │  └─ index.ts (or index.js)
  ├─ tests/
  ├─ tsconfig.json (if TS)
  └─ .eslintrc.cjs
  ```

## Continuous Integration
- Set up CI to run on pushes and PRs:
  - Python: run black (check), ruff, mypy, and tests.
  - Node: run eslint, prettier (check), tsc (noEmit), and tests.
- Fail the build on lint or type errors.

## Commit Conventions
- Use meaningful commit messages.
- Consider Conventional Commits (feat:, fix:, docs:, chore:, refactor:, test:, build:, ci:).

## Documentation
- Keep `README.md` updated with:
  - Project overview and goals.
  - Setup steps.
  - How to run the project and tests.
- For public APIs, document endpoints, parameters, and responses.

## Environment Variables
- Do not commit `.env` files.
- Provide `.env.example` listing required variables with placeholder values.

## Security and Compliance
- Do not commit secrets or API keys.
- Run dependency audits (`pip-audit` or `npm audit`) periodically.
