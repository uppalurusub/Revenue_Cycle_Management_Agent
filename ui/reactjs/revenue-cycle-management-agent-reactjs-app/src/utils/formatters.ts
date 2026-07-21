export const currency = (value:number) => new Intl.NumberFormat("en-US",{style:"currency",currency:"USD"}).format(value);
export const percent = (value:number) => `${Math.round(value * 100)}%`;
export const label = (value:string) => value.replaceAll("_"," ").replace(/\b\w/g,c=>c.toUpperCase());