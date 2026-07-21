import type { ClaimRequest } from "../../models/claim";
interface Props { value:ClaimRequest; onChange:(value:ClaimRequest)=>void; onSubmit:()=>void; loading:boolean; }
export default function ClaimForm({value,onChange,onSubmit,loading}:Props){
 const set=(key:keyof ClaimRequest,v:unknown)=>onChange({...value,[key]:v});
 return <section className="card">
   <div className="section-title"><div><span className="eyebrow">CLAIM INTAKE</span><h2>Process Healthcare Insurance Claim</h2></div><span className="endpoint">POST /revenue-cycle/process-claim</span></div>
   <div className="grid">
    <label>Claim ID<input value={value.claim_id} onChange={e=>set("claim_id",e.target.value)}/></label>
    <label>Patient ID<input value={value.patient_id} onChange={e=>set("patient_id",e.target.value)}/></label>
    <label>Patient Name<input value={value.patient_name} onChange={e=>set("patient_name",e.target.value)}/></label>
    <label>Date of Birth<input type="date" value={value.date_of_birth} onChange={e=>set("date_of_birth",e.target.value)}/></label>
    <label>Gender<input value={value.gender} onChange={e=>set("gender",e.target.value)}/></label>
    <label>Service Date<input type="date" value={value.service_date} onChange={e=>set("service_date",e.target.value)}/></label>
    <label>Total Claim Amount<input type="number" value={value.total_claim_amount} onChange={e=>set("total_claim_amount",Number(e.target.value))}/></label>
   </div>
   <label>Notes<textarea rows={3} value={value.notes} onChange={e=>set("notes",e.target.value)}/></label>
   <details><summary>Request JSON</summary><textarea className="json" rows={18} value={JSON.stringify(value,null,2)} onChange={e=>{try{onChange(JSON.parse(e.target.value))}catch{}}}/></details>
   <button onClick={onSubmit} disabled={loading}>{loading ? "Processing Claim..." : "Process Claim"}</button>
 </section>
}