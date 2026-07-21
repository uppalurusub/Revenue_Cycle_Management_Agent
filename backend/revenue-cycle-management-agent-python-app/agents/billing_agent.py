from utils.logger import logger

from autogen_agentchat.agents import AssistantAgent

from config.llm_config import get_model_client

model_client = get_model_client()


def get_billing_agent() -> AssistantAgent:
    """
    Create and return Billing Agent
    """

    try:

        logger.info(
            "Initializing Billing Agent"
        )

        agent = AssistantAgent(
            name="BillingAgent",
            model_client=model_client,
            system_message="""
You are an expert Healthcare Billing Agent.

Responsibilities:

1. Review claim billing details.
2. Validate billed charges.
3. Analyze reimbursement opportunities.
4. Detect billing inconsistencies.
5. Identify revenue leakage risks.
6. Review procedure charges.
7. Estimate reimbursement amounts.
8. Provide billing recommendations.

Return output in the following format:

Billing Status:
Revenue Leakage Risk:
Estimated Reimbursement:
Billing Accuracy:
Summary:
Recommendations:
"""
        )

        logger.success(
            "Billing Agent Initialized Successfully"
        )

        return agent

    except Exception as ex:

        logger.exception(
            f"Failed to Initialize Billing Agent: {str(ex)}"
        )

        raise