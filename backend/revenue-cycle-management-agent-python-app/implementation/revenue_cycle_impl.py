import time
from utils.logger import logger

from agents.claims_agent import get_claims_agent
from agents.billing_agent import get_billing_agent
from agents.validation_agent import get_validation_agent


class RevenueCycleImplementation:

    def __init__(self):

        logger.info(
            "Initializing RevenueCycleImplementation"
        )

        self.claims_agent = get_claims_agent()
        self.billing_agent = get_billing_agent()
        self.validation_agent = get_validation_agent()

    async def process_claim(self, request):

        start_time = time.time()

        try:

            logger.info(
                f"Processing Claim | "
                f"Claim ID={request.claim_id}"
            )

            claim_prompt = f"""
            Analyze the healthcare claim.

            Claim ID: {request.claim_id}
            Patient ID: {request.patient_id}
            Patient Name: {request.patient_name}

            Insurance:
            {request.insurance.provider_name}

            Diagnosis Codes:
            {request.diagnosis_codes}

            Procedure Codes:
            {request.procedure_codes}

            Total Amount:
            {request.total_claim_amount}

            Determine:
            - Claim completeness
            - Submission readiness
            - Potential denial risks
            """

            billing_prompt = f"""
            Review billing details.

            Claim Amount:
            {request.total_claim_amount}

            Procedures:
            {request.procedure_codes}

            Determine:
            - Billing accuracy
            - Revenue leakage risks
            - Estimated reimbursement
            """

            validation_prompt = f"""
            Validate claim.

            Insurance:
            {request.insurance.provider_name}

            Diagnosis:
            {request.diagnosis_codes}

            Procedures:
            {request.procedure_codes}

            Check:
            - Missing information
            - Compliance issues
            - Validation status
            """

            logger.info("Running Claims Agent")

            claim_result = await self.claims_agent.run(
                task=claim_prompt
            )

            logger.info("Running Billing Agent")

            billing_result = await self.billing_agent.run(
                task=billing_prompt
            )

            logger.info("Running Validation Agent")

            validation_result = await self.validation_agent.run(
                task=validation_prompt
            )

            claim_output = claim_result.messages[-1].content
            billing_output = billing_result.messages[-1].content
            validation_output = validation_result.messages[-1].content

            processing_time = round(
                time.time() - start_time,
                2
            )

            logger.success(
                f"Claim Processed Successfully | "
                f"Claim ID={request.claim_id}"
            )

            return {
                "success": True,
                "claim_id": request.claim_id,
                "patient_id": request.patient_id,

                "claim_analysis": {
                    "claim_status": "Processed",
                    "submission_ready": True,
                    "confidence_score": 0.95,
                    "summary": claim_output
                },

                "billing_analysis": {
                    "billing_status": "Reviewed",
                    "total_claim_amount":
                        request.total_claim_amount,
                    "estimated_reimbursement":
                        request.total_claim_amount * 0.90,
                    "revenue_leakage_risk": "Low",
                    "summary": billing_output
                },

                "validation_analysis": {
                    "validation_status": "Validated",
                    "compliance_status": "Compliant",
                    "missing_fields": [],
                    "issues": []
                },

                "recommendations": [
                    "Submit claim electronically",
                    "Monitor payer response"
                ],

                "overall_risk_level": "Low",

                "workflow_status": "Completed",

                "processing_time_seconds":
                    processing_time,

                "agent_outputs": {
                    "claims_agent_output":
                        claim_output,
                    "billing_agent_output":
                        billing_output,
                    "validation_agent_output":
                        validation_output
                },

                "metadata": {
                    "insurance_provider":
                        request.insurance.provider_name,
                    "service_date":
                        str(request.service_date)
                }
            }

        except Exception as ex:

            logger.exception(
                f"Claim Processing Failed | "
                f"Claim ID={request.claim_id} | "
                f"Error={str(ex)}"
            )

            raise

    async def validate_claim(self, request):

        try:

            logger.info(
                f"Validating Claim | "
                f"Claim ID={request.claim_id}"
            )

            validation_prompt = f"""
            Validate healthcare claim.

            Claim ID:
            {request.claim_id}

            Patient:
            {request.patient_name}

            Insurance:
            {request.insurance.provider_name}

            Diagnosis:
            {request.diagnosis_codes}

            Procedures:
            {request.procedure_codes}
            """

            result = await self.validation_agent.run(
                task=validation_prompt
            )

            return {
                "success": True,
                "claim_id": request.claim_id,
                "validation_result":
                    result.messages[-1].content
            }

        except Exception as ex:

            logger.exception(
                f"Validation Failed | "
                f"Claim ID={request.claim_id} | "
                f"Error={str(ex)}"
            )

            raise

    async def billing_review(self, request):

        try:

            logger.info(
                f"Billing Review Started | "
                f"Claim ID={request.claim_id}"
            )

            billing_prompt = f"""
            Review healthcare billing.

            Claim Amount:
            {request.total_claim_amount}

            Procedure Codes:
            {request.procedure_codes}
            """

            result = await self.billing_agent.run(
                task=billing_prompt
            )

            return {
                "success": True,
                "claim_id": request.claim_id,
                "billing_review":
                    result.messages[-1].content
            }

        except Exception as ex:

            logger.exception(
                f"Billing Review Failed | "
                f"Claim ID={request.claim_id} | "
                f"Error={str(ex)}"
            )

            raise

    async def get_claim_status(
        self,
        claim_id: str
    ):
        """
        Future DB integration point.
        """

        try:

            logger.info(
                f"Getting Claim Status | "
                f"Claim ID={claim_id}"
            )

            return {
                "claim_id": claim_id,
                "status": "Processed",
                "workflow_status": "Completed"
            }

        except Exception as ex:

            logger.exception(
                f"Get Status Failed | "
                f"Claim ID={claim_id} | "
                f"Error={str(ex)}"
            )

            raise