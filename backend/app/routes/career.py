from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from app.services.gemini_client import generate_gemini_response
from app.prompts.templates import career_advice_template
import json

router = APIRouter(prefix="/ask", tags=["career"])

class PromptRequest(BaseModel):
    prompt: str

@router.post("/career")
def ask_gemini(request: PromptRequest):
    raw_response = generate_gemini_response(request.prompt, career_advice_template)
    try:
        parsed = json.loads(raw_response)
        print(parsed)
        return parsed
    except json.JSONDecodeError:
        return JSONResponse(content={"response": raw_response}, status_code=200)