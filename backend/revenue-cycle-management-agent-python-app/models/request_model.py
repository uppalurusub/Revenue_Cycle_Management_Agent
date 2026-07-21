from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date


class InsuranceInfo(BaseModel):
    provider_name: str
    policy_number: str
    group_number: Optional[str] = None
    member_id: str
    authorization_number: Optional[str] = None


class ProviderInfo(BaseModel):
    provider_id: str
    provider_name: str
    specialty: Optional[str] = None
    facility_name: Optional[str] = None


class DiagnosisCode(BaseModel):
    code: str
    description: Optional[str] = None


class ProcedureCode(BaseModel):
    code: str
    description: Optional[str] = None
    units: int = 1
    charge_amount: float


class ClaimRequest(BaseModel):
    claim_id: str = Field(
        ...,
        description="Unique claim identifier"
    )

    patient_id: str
    patient_name: str
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None

    service_date: date

    insurance: InsuranceInfo

    provider: ProviderInfo

    diagnosis_codes: List[DiagnosisCode]

    procedure_codes: List[ProcedureCode]

    total_claim_amount: float

    notes: Optional[str] = None