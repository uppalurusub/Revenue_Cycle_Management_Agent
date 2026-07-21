import { useState } from "react";
import { processClaim } from "../api/revenueCycleApi";
import ClaimForm from "../components/claim/ClaimForm";
import ResponseView from "../components/response/ResponseView";
import type { ClaimRequest, RevenueCycleResponse } from "../models/claim";

const initialClaim: ClaimRequest = {
  "claim_id": "CLM20260001",
  "patient_id": "PAT10001",
  "patient_name": "John Doe",
  "date_of_birth": "1985-05-15",
  "gender": "Male",
  "service_date": "2026-06-20",
  "insurance": {
    "provider_name": "Blue Cross Blue Shield",
    "policy_number": "POL987654321",
    "group_number": "GRP10001",
    "member_id": "MEM123456789",
    "authorization_number": "AUTH567890"
  },
  "provider": {
    "provider_id": "PRV10001",
    "provider_name": "Dr. Sarah Johnson",
    "specialty": "Cardiology",
    "facility_name": "City Heart Medical Center"
  },
  "diagnosis_codes": [
    {
      "code": "I10",
      "description": "Essential Hypertension"
    },
    {
      "code": "E11.9",
      "description": "Type 2 Diabetes Mellitus Without Complications"
    }
  ],
  "procedure_codes": [
    {
      "code": "99214",
      "description": "Office or Outpatient Visit",
      "units": 1,
      "charge_amount": 250.0
    },
    {
      "code": "93000",
      "description": "Electrocardiogram Complete",
      "units": 1,
      "charge_amount": 150.0
    },
    {
      "code": "80053",
      "description": "Comprehensive Metabolic Panel",
      "units": 1,
      "charge_amount": 100.0
    }
  ],
  "total_claim_amount": 500.0,
  "notes": "Follow-up visit for hypertension and diabetes management. ECG and laboratory tests performed."
};

export default function RevenueCyclePage(){
 const [claim,setClaim]=useState<ClaimRequest>(initialClaim);
 const [result,setResult]=useState<RevenueCycleResponse|null>(null);
 const [loading,setLoading]=useState(false);
 const [error,setError]=useState("");
 const submit=async()=>{setLoading(true);setError("");setResult(null);try{setResult(await processClaim(claim));}catch(e){setError(e instanceof Error?e.message:"Unable to process claim.");}finally{setLoading(false);}};
 return <main className="shell"><header className="topbar"><span className="eyebrow">HEALTHCARE AI OPERATIONS</span><h1>Revenue Cycle Management Agent</h1><p>Claims processing, billing review and validation workflow.</p></header>{error&&<div className="error">{error}</div>}<div className="layout"><ClaimForm value={claim} onChange={setClaim} onSubmit={submit} loading={loading}/><div>{result?<ResponseView data={result}/>:<section className="card"><h2>Agent Response</h2><p>Submit the claim to display claims, billing and validation agent summaries.</p></section>}</div></div></main>;
}