from utils.logger import logger

from autogen_agentchat.agents import AssistantAgent

from config.llm_config import get_model_client

model_client = get_model_client()


def get_validation_agent() -> AssistantAgent:
    """
    Create and return Validation Agent
    """

    try:

        logger.info(
            "Initializing Validation Agent"
        )

        agent = AssistantAgent(
            name="ValidationAgent",
            model_client=model_client,
            system_message="""
You are an expert Healthcare Claim Validation Agent.

Your responsibilities include:

1. Validate claim completeness.
2. Verify required patient information.
3. Verify insurance details.
4. Review diagnosis codes.
5. Review procedure codes.
6. Detect missing information.
7. Identify compliance issues.
8. Assess denial risks.
9. Determine claim submission readiness.

Provide output in the following format:

Validation Status:
Compliance Status:
Missing Fields:
Denial Risk:
Submission Ready:
Summary:
Recommendations:
"""
        )

        logger.success(
            "Validation Agent Initialized Successfully"
        )

        return agent

    except Exception as ex:

        logger.exception(
            f"Failed to Initialize Validation Agent: {str(ex)}"
        )

        raise