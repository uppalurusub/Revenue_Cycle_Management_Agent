import sys
import time

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from utils.logger import logger

from routers.revenue_cycle_router import (
    router as revenue_cycle_router
)



# --------------------------------------------------
# Configure Loguru
# --------------------------------------------------

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:"
        "<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    )
)

logger.add(
    "logs/revenue_cycle_management.log",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    level="INFO",
    enqueue=True
)

# --------------------------------------------------
# FastAPI App
# --------------------------------------------------

app = FastAPI(
    title="Revenue Cycle Management Agent",
    description="Healthcare Revenue Cycle Management using AutoGen 0.7.5",
    version="1.0.0"
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --------------------------------------------------
# Middleware
# --------------------------------------------------

@app.middleware("http")
async def log_requests(
    request: Request,
    call_next
):
    start_time = time.time()

    logger.info(
        f"Incoming Request | "
        f"{request.method} "
        f"{request.url.path}"
    )

    response = await call_next(request)

    process_time = round(
        time.time() - start_time,
        3
    )

    logger.info(
        f"Completed Request | "
        f"Status={response.status_code} | "
        f"Duration={process_time}s"
    )

    return response




# --------------------------------------------------
# Global Exception Handler
# --------------------------------------------------

@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):

    logger.exception(
        f"Unhandled Exception: {str(exc)}"
    )

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": str(exc)
        }
    )


# --------------------------------------------------
# Root Endpoint
# --------------------------------------------------

@app.get("/")
async def root():

    logger.info(
        "Root Endpoint Accessed"
    )

    return {
        "application":
            "Revenue Cycle Management Agent",
        "version":
            "1.0.0",
        "framework":
            "FastAPI",
        "autogen_version":
            "0.7.5",
        "status":
            "running"
    }


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/health")
async def health_check():

    logger.info(
        "Health Check Requested"
    )

    return {
        "status": "healthy"
    }


# --------------------------------------------------
# Register Routers
# --------------------------------------------------

app.include_router(
    revenue_cycle_router
)

logger.info(
    "Revenue Cycle Router Registered"
)