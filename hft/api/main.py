"""FastAPI application entry point."""

import os
import socket

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from hft.api.dependencies import lifespan
from hft.api.history import router as history_router
from hft.api.metrics import router as metrics_router
from hft.api.symbols import router as symbols_router
from hft.api.websocket import router as ws_router

VITE_DEV_URL = "http://localhost:5173"
VITE_PORT = 5173


def is_vite_running() -> bool:
    """Check if Vite dev server is running on port 5173."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.1)
            s.connect(("localhost", VITE_PORT))
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

app = FastAPI(
    title="HFT Platform",
    description="High-Frequency Trading Platform - Binance Market Data & Visualization",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS middleware for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files for frontend
# In production, serve from frontend/dist (Vite build output)
# Falls back to frontend/ for backwards compatibility
frontend_dist = "frontend/dist"
frontend_root = "frontend"

try:
    if os.path.isdir(frontend_dist):
        app.mount("/static", StaticFiles(directory=frontend_dist, html=True), name="static")
    elif os.path.isdir(frontend_root):
        app.mount("/static", StaticFiles(directory=frontend_root), name="static")
except Exception:
    # Frontend directory might not exist yet
    pass

# Include routers
app.include_router(history_router, prefix="/api", tags=["history"])
app.include_router(metrics_router, prefix="/api", tags=["metrics"])
app.include_router(symbols_router, tags=["symbols"])
app.include_router(ws_router, tags=["websocket"])


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "ok"}


@app.get("/")
async def root():
    """Redirect to frontend - Vite dev server if running, otherwise static build."""
    if is_vite_running():
        return RedirectResponse(url=VITE_DEV_URL)
    return RedirectResponse(url="/static/index.html")
