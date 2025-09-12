import { apiClient } from "./client";

export async function askCareer(prompt) {
  const response = await apiClient.post("/ask/career", { prompt });
  return response.data;
}
