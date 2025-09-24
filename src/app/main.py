import os
from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel, Field

# PUBLIC_INTERFACE
def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance.

    Returns:
        FastAPI: Configured FastAPI app with routes and OpenAPI metadata.
    """
    app = FastAPI(
        title="Daily Notes Journal API",
        description=(
            "Minimal backend scaffold to enable dependency installation and preview startup.\n\n"
            "This API currently exposes a health endpoint and project metadata. "
            "Future endpoints for notes and journaling can be added under /api."
        ),
        version=os.getenv("APP_VERSION", "0.1.0"),
        openapi_tags=[
            {"name": "system", "description": "System and health endpoints"},
        ],
    )

    class HealthResponse(BaseModel):
        status: str = Field(..., description="Overall health status")
        version: str = Field(..., description="Application version")
        environment: str = Field(..., description="Deployment environment name")

    @app.get(
        "/health",
        response_model=HealthResponse,
        summary="Health check",
        description="Returns the health status and basic metadata for the service.",
        tags=["system"],
        responses={
            200: {
                "description": "Service is healthy",
            }
        },
    )
    # PUBLIC_INTERFACE
    def health() -> Dict[str, str]:
        """Health check endpoint.

        Returns:
            dict: A dictionary with health status, version, and environment name.
        """
        return {
            "status": "ok",
            "version": os.getenv("APP_VERSION", "0.1.0"),
            "environment": os.getenv("APP_ENV", "development"),
        }

    return app


app = create_app()

# PUBLIC_INTERFACE
def get_app() -> FastAPI:
    """Return the FastAPI app instance for ASGI servers (e.g., uvicorn, gunicorn)."""
    return app
