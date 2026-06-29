from fastapi import FastAPI
from pydantic import BaseModel
from .ai_gateway import inspect_prompt

app = FastAPI(title="ACME Finance AI Platform", version="0.1.0")

class PromptRequest(BaseModel):
    user: str
    prompt: str

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "acme-finance-ai-platform"}

@app.post("/ask-ai")
def ask_ai(request: PromptRequest):
    inspection = inspect_prompt(user=request.user, prompt=request.prompt)
    return {
        "user": request.user,
        "inspection_status": inspection["status"],
        "response": "This is a fake AI response for Prompt Security Agentic AI demo validation."
    }
