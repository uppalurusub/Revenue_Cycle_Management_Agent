import axios from "axios";
import type { ClaimRequest, RevenueCycleResponse } from "../models/claim";

const API_URL = "http://127.0.0.1:8000/revenue-cycle/process-claim";

export async function processClaim(payload: ClaimRequest): Promise<RevenueCycleResponse> {
  try {
    const { data } = await axios.post<RevenueCycleResponse>(API_URL, payload, {
      headers: { "Content-Type": "application/json" }
    });
    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      const detail = error.response?.data?.detail;
      throw new Error(detail || `Unable to connect to ${API_URL}. Verify the FastAPI service and CORS configuration.`);
    }
    throw error;
  }
}