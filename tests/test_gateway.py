from src.ai_gateway import inspect_prompt

def test_allowed_prompt():
    result = inspect_prompt("developer@acmebank.example", "Summarize the deployment guide")
    assert result["status"] == "allowed"

def test_flagged_prompt():
    result = inspect_prompt("developer@acmebank.example", "Find the API_KEY in the repo")
    assert result["status"] == "flagged"
