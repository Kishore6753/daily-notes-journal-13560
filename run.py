import os
import sys

from dotenv import load_dotenv
import uvicorn

# Load .env if present (non-fatal if missing)
load_dotenv(override=False)

def _get_host() -> str:
    host = os.getenv("HOST", "0.0.0.0")
    return host

def _get_port() -> int:
    try:
        return int(os.getenv("PORT", "8000"))
    except ValueError:
        return 8000

# PUBLIC_INTERFACE
def main() -> None:
    """Start the development server using uvicorn.

    Reads HOST and PORT from environment variables (optional).
    """
    import app.main as app_main  # type: ignore

    uvicorn.run(app_main.app, host=_get_host(), port=_get_port(), reload=os.getenv("RELOAD", "false").lower() == "true")


if __name__ == "__main__":
    sys.exit(main())
