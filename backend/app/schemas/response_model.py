from pydantic import BaseModel
from typing import List, Dict, Optional


class ValidationIssue(BaseModel):
    issue_type: str
    severity: str
    description: str


class ClaimAnalysis(BaseModel):
    claim_status: str
    submission_ready: bool
    confidence_score: float
    summary: str


class BillingAnalysis(BaseModel):
    billing_status: str
    total_claim_amount: float
    estimated_reimbursement: float
    revenue_leakage_risk: str
    summary: str


class ValidationAnalysis(BaseModel):
    validation_status: str
    compliance_status: str
    missing_fields: List[str]
    issues: List[ValidationIssue]


class AgentOutputs(BaseModel):
    claims_agent_output: str
    billing_agent_output: str
    validation_agent_output: str


class RevenueCycleResponse(BaseModel):
    success: bool

    claim_id: str
    patient_id: str

    claim_analysis: ClaimAnalysis

    billing_analysis: BillingAnalysis

    validation_analysis: ValidationAnalysis

    recommendations: List[str]

    overall_risk_level: str

    workflow_status: str

    processing_time_seconds: float

    agent_outputs: AgentOutputs

    metadata: Optional[Dict] = {}