from utils.logger import logger

from implementation.revenue_cycle_impl import (
    RevenueCycleImplementation
)

from models.request_model import ClaimRequest

import mlflow
from datetime import datetime

mlflow.set_tracking_uri(
    "http://localhost:5000"
)

mlflow.set_experiment(
    "Revenue_Cycle_Management_Agent_Interface"
)

class RevenueCycleService:

    def __init__(self):
        logger.info(
            "Initializing RevenueCycleService"
        )

        self.impl = RevenueCycleImplementation()

    async def process_claim(
        self,
        request: ClaimRequest
    ):
        """
        Process healthcare insurance claim
        """

        try:

            logger.info(
                f"Starting claim processing | "
                f"Claim ID={request.claim_id} | "
                f"Patient ID={request.patient_id}"
            )

            with mlflow.start_run(
                run_name=
                f"Revenue_Cycle_Management_Agent_Process_Claim_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            ):
                mlflow.log_param(
                    "input_text",
                    request
                )

                result = await self.impl.process_claim(
                    request
                )

                mlflow.log_param(
                    "response",
                    result
                )

                mlflow.set_tag(
                    "source",
                    "FastAPI"
                )

                mlflow.set_tag(
                    "endpoint",
                    "revenue-cycle/process-claim"
                )



            logger.success(
                f"Claim processing completed | "
                f"Claim ID={request.claim_id}"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"Claim processing failed | "
                f"Claim ID={request.claim_id} | "
                f"Error={str(ex)}"
            )

            raise ex

    async def validate_claim(
        self,
        request: ClaimRequest
    ):
        """
        Validate claim before submission
        """

        try:

            logger.info(
                f"Validating claim | "
                f"Claim ID={request.claim_id}"
            )

            result = await self.impl.validate_claim(
                request
            )

            logger.success(
                f"Claim validation completed | "
                f"Claim ID={request.claim_id}"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"Claim validation failed | "
                f"Claim ID={request.claim_id} | "
                f"Error={str(ex)}"
            )

            raise ex

    async def billing_review(
        self,
        request: ClaimRequest
    ):
        """
        Billing review workflow
        """

        try:

            logger.info(
                f"Billing review started | "
                f"Claim ID={request.claim_id}"
            )

            result = await self.impl.billing_review(
                request
            )

            logger.success(
                f"Billing review completed | "
                f"Claim ID={request.claim_id}"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"Billing review failed | "
                f"Claim ID={request.claim_id} | "
                f"Error={str(ex)}"
            )

            raise ex

    async def get_claim_status(
        self,
        claim_id: str
    ):
        """
        Retrieve claim status
        """

        try:

            logger.info(
                f"Fetching claim status | "
                f"Claim ID={claim_id}"
            )

            result = await self.impl.get_claim_status(
                claim_id
            )

            logger.success(
                f"Claim status retrieved | "
                f"Claim ID={claim_id}"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"Failed to retrieve claim status | "
                f"Claim ID={claim_id} | "
                f"Error={str(ex)}"
            )

            raise ex

    async def health_check(self):
        """
        Service health check
        """

        try:

            logger.info(
                "RevenueCycleService Health Check"
            )

            return {
                "status": "healthy",
                "service": "RevenueCycleService"
            }

        except Exception as ex:

            logger.exception(
                f"Health Check Failed: {str(ex)}"
            )

            return {
                "status": "unhealthy",
                "error": str(ex)
            }