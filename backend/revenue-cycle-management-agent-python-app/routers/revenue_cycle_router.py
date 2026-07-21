from fastapi import APIRouter, HTTPException
from utils.logger import logger

from services.revenue_cycle_service import RevenueCycleService
from models.request_model import ClaimRequest
from models.response_model import RevenueCycleResponse

router = APIRouter(
    prefix="/revenue-cycle",
    tags=["Revenue Cycle Management Agent"]
)

service = RevenueCycleService()


@router.post(
    "/process-claim",
    response_model=RevenueCycleResponse
)
async def process_claim(
    request: ClaimRequest
):
    """
    Process Healthcare Insurance Claim
    """

    try:
        logger.info(
            f"Received claim request | "
            f"Claim ID={request.claim_id} | "
            f"Patient ID={request.patient_id}"
        )

        response = await service.process_claim(
            request
        )

        logger.success(
            f"Claim processed successfully | "
            f"Claim ID={request.claim_id}"
        )

        return response

    except Exception as ex:

        logger.exception(
            f"Error processing claim "
            f"Claim ID={request.claim_id} | "
            f"Error={str(ex)}"
        )

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


@router.get("/health")
async def health_check():
    """
    Health Check Endpoint
    """

    try:

        logger.info(
            "Revenue Cycle Management Agent Health Check"
        )

        return {
            "status": "healthy",
            "service": "Revenue Cycle Management Agent"
        }

    except Exception as ex:

        logger.exception(
            f"Health check failed: {str(ex)}"
        )

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


@router.get("/info")
async def application_info():
    """
    Application Information
    """

    try:

        logger.info(
            "Revenue Cycle Management Agent Info Requested"
        )

        return {
            "application": "Revenue Cycle Management Agent",
            "version": "1.0.0",
            "framework": "FastAPI",
            "autogen_version": "0.7.5",
            "agents": [
                "Claims Agent",
                "Billing Agent",
                "Validation Agent"
            ],
            "capabilities": [
                "Claims Processing",
                "Billing Review",
                "Claim Validation",
                "Workflow Automation"
            ]
        }

    except Exception as ex:

        logger.exception(
            f"Info endpoint error: {str(ex)}"
        )

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )