import ReactMarkdown from "react-markdown"; import remarkGfm from "remark-gfm";
interface Props { title:string; status:string; children?:React.ReactNode; summary:string; }
export default function SummaryCard({title,status,children,summary}:Props){
 return <article className="card analysis"><div className="card-head"><h3>{title}</h3><span className="badge">{status}</span></div>{children}<div className="markdown"><ReactMarkdown remarkPlugins={[remarkGfm]}>{summary}</ReactMarkdown></div></article>
}