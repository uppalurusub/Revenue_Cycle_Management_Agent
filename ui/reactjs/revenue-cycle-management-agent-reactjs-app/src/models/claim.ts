export interface Insurance { provider_name:string; policy_number:string; group_number:string; member_id:string; authorization_number:string; }
export interface Provider { provider_id:string; provider_name:string; specialty:string; facility_name:string; }
export interface DiagnosisCode { code:string; description:string; }
export interface ProcedureCode { code:string; description:string; units:number; charge_amount:number; }
export interface ClaimRequest { claim_id:string; patient_id:string; patient_name:string; date_of_birth:string; gender:string; service_date:string; insurance:Insurance; provider:Provider; diagnosis_codes:DiagnosisCode[]; procedure_codes:ProcedureCode[]; total_claim_amount:number; notes:string; }

export interface ClaimAnalysis { claim_status:string; submission_ready:boolean; confidence_score:number; summary:string; }
export interface BillingAnalysis { billing_status:string; total_claim_amount:number; estimated_reimbursement:number; revenue_leakage_risk:string; summary:string; }
export interface ValidationAnalysis { validation_status:string; compliance_status:string; missing_fields:string[]; issues:string[]; }
export interface AgentOutputs { claims_agent_output:string; billing_agent_output:string; validation_agent_output:string; }
export interface RevenueCycleResponse {
 success:boolean; claim_id:string; patient_id:string; claim_analysis:ClaimAnalysis;
 billing_analysis:BillingAnalysis; validation_analysis:ValidationAnalysis; recommendations:string[];
 overall_risk_level:string; workflow_status:string; processing_time_seconds:number;
 agent_outputs:AgentOutputs; metadata:{insurance_provider:string;service_date:string};
}