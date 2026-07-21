from utils.logger import logger

from autogen_agentchat.agents import AssistantAgent

from config.llm_config import get_model_client

model_client = get_model_client()


def get_claims_agent() -> AssistantAgent:
    """
    Create and return Claims Agent
    """

    try:

        logger.info(
            "Initializing Claims Agent"
        )

        agent = AssistantAgent(
            name="ClaimsAgent",
            model_client=model_client,
            system_message="""
You are an expert Healthcare Claims Processing Agent.

Your responsibilities include:

1. Review healthcare insurance claims.
2. Verify diagnosis (ICD-10) codes.
3. Verify procedure (CPT/HCPCS) codes.
4. Identify missing claim information.
5. Assess claim completeness.
6. Detect potential claim denial risks.
7. Verify payer submission readiness.
8. Generate claim processing recommendations.

Provide output in the following format:

Claim Status:
Submission Ready:
Denial Risk:
Confidence Score:
Summary:
Recommendations:
"""
        )

        logger.success(
            "Claims Agent Initialized Successfully"
        )

        return agent

    except Exception as ex:

        logger.exception(
            f"Failed to Initialize Claims Agent: {str(ex)}"
        )

        raise