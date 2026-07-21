import type { RevenueCycleResponse } from "../../models/claim";
import {currency,percent} from "../../utils/formatters"; import SummaryCard from "./SummaryCard";
export default function ResponseView({data}:{data:RevenueCycleResponse}){
 return <div className="results">
  <section className="hero card"><div><span className="eyebrow">WORKFLOW RESULT</span><h2>{data.claim_id}</h2><p>Patient {data.patient_id} · {data.metadata.insurance_provider}</p></div><div className="hero-status"><span className="badge">{data.workflow_status}</span><strong>{data.overall_risk_level} Risk</strong></div></section>
  <div className="metrics"><div className="metric"><span>Claim Amount</span><strong>{currency(data.billing_analysis.total_claim_amount)}</strong></div><div className="metric"><span>Est. Reimbursement</span><strong>{currency(data.billing_analysis.estimated_reimbursement)}</strong></div><div className="metric"><span>Confidence</span><strong>{percent(data.claim_analysis.confidence_score)}</strong></div><div className="metric"><span>Processing Time</span><strong>{data.processing_time_seconds.toFixed(2)}s</strong></div></div>
  <SummaryCard title="Claims Agent Summary" status={data.claim_analysis.claim_status} summary={data.claim_analysis.summary}><div className="mini-row"><span>Submission Ready: <b>{data.claim_analysis.submission_ready?"Yes":"No"}</b></span></div></SummaryCard>
  <SummaryCard title="Billing Agent Summary" status={data.billing_analysis.billing_status} summary={data.billing_analysis.summary}><div className="mini-row"><span>Revenue Leakage Risk: <b>{data.billing_analysis.revenue_leakage_risk}</b></span></div></SummaryCard>
  <SummaryCard title="Validation Agent Summary" status={data.validation_analysis.validation_status} summary={data.agent_outputs.validation_agent_output}><div className="mini-row"><span>Compliance: <b>{data.validation_analysis.compliance_status}</b></span></div></SummaryCard>
  <section className="card"><h3>Final Recommendations</h3><ul>{data.recommendations.map((x,i)=><li key={i}>{x}</li>)}</ul></section>
 </div>
}