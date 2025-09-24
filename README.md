# Daily Notes Journal - Backend

This repository contains a minimal FastAPI backend scaffold to enable dependency installation and preview startup.

## Quick Start

Prerequisites:
- Python 3.9+ recommended

Setup:
1. Create and activate a virtual environment (recommended).
2. Install dependencies:
   - Option A (pip): `pip install -e .[dev]`
   - Option B (uv or pip-tools also possible if preferred by your environment)

3. Copy environment configuration:
   - `cp .env.example .env` (optional; defaults are sane for local preview)

Run:
- Development: `python run.py` (uses HOST and PORT from environment; default 0.0.0.0:8000)
- Alternatively: `python -m uvicorn app.main:app --host 0.0.0.0 --port 8000`

Endpoints:
- Health: GET `/health`
- OpenAPI docs: `/docs` and `/openapi.json`

## Project Structure

```
.
├─ src/
│  └─ app/
│     ├─ __init__.py
│     └─ main.py
├─ run.py
├─ pyproject.toml
└─ .env.example
```

## Notes

- Configuration is via environment variables; do not commit real `.env` files. Provide only `.env.example`.
- Follow CONTRIBUTING.md for code style (black, ruff, mypy suggested).
- This is a starting point; extend with actual journaling endpoints under `/api`.