from app.config.settings import settings
logger = settings.get_logger()

from app.implementation.revenue_cycle_impl import (
    RevenueCycleImplementation
)

from app.models.request_model import ClaimRequest

import mlflow
from datetime import datetime
from datetime import datetime
import time
from app.config.settings import (
    settings,
    usage_capture,
    INPUT_PRICE_PER_1M,
    OUTPUT_PRICE_PER_1M,
)

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
            start_time = datetime.now()
            start_ts = time.perf_counter()

            logger.info(
                f"Starting claim processing | "
                f"Claim ID={request.claim_id} | "
                f"Patient ID={request.patient_id}"
            )

            with mlflow.start_run(
                run_name=
                f"Revenue_Cycle_Management_Agent_Process_Claim_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            ):
                

                mlflow.log_param("start_time", start_time.isoformat())
                with usage_capture() as usage:
                    result = await self.impl.process_claim(
                        request
                    )

                execution_time = time.perf_counter() - start_ts
                usage_values = usage.as_dict()

                # Log configuration and actual usage separately.
                mlflow.log_param("llm_model", usage_values["model"])
                mlflow.log_param(
                    "input_price_per_1m_usd", INPUT_PRICE_PER_1M
                )
                mlflow.log_param(
                    "output_price_per_1m_usd", OUTPUT_PRICE_PER_1M
                )
                mlflow.log_param("input", request)
                mlflow.log_param("output", result)
                mlflow.log_param("execution_time", execution_time)

                metric_names = (
                    "input_tokens",
                    "output_tokens",
                    "total_tokens",
                    "input_cost_usd",
                    "output_cost_usd",
                    "total_cost_usd",
                    "llm_call_count",
                    "usage_reported_call_count",
                )
                for metric_name in metric_names:
                    mlflow.log_metric(
                        metric_name,
                        float(usage_values[metric_name])
                    )

                

                mlflow.set_tag("llm_usage_source", usage_values["source"])
                mlflow.log_param("end_time", datetime.now().isoformat())

                mlflow.log_param("execution_time", execution_time)

                

                mlflow.set_tag(
                    "source",
                    "FastAPI"
                )

                mlflow.set_tag(
                    "endpoint",
                    "revenue-cycle/process-claim"
                )
                logger.info(
                    "LLM usage captured: "
                    f"model={usage_values['model']}, "
                    f"input_tokens={usage_values['input_tokens']}, "
                    f"output_tokens={usage_values['output_tokens']}, "
                    f"total_tokens={usage_values['total_tokens']}, "
                    f"input_cost_usd={usage_values['input_cost_usd']:.15f}, "
                    f"output_cost_usd={usage_values['output_cost_usd']:.15f}, "
                    f"total_cost_usd={usage_values['total_cost_usd']:.15f}, "
                    f"llm_call_count={usage_values['llm_call_count']}, "
                    f"usage_reported_call_count="
                    f"{usage_values['usage_reported_call_count']}"
                )

                if usage_values["usage_reported_call_count"] == 0:
                    logger.warning(
                        "No token usage was reported by the AutoGen model "
                        "client. Check that MonitoringImplementation uses "
                        "settings.get_model_client() and that the provider "
                        "returns usage metadata."
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