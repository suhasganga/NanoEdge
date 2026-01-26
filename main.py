"""HFT Platform - Start the server."""

import uvicorn


def main():
    """Start the FastAPI server."""
    uvicorn.run(
        "hft.api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()
