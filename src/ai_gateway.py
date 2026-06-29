def inspect_prompt(user: str, prompt: str) -> dict:
    """Fake Prompt Security inspection placeholder for demo purposes."""
    risky_terms = ["password", "secret", "api_key", "token"]
    lowered = prompt.lower()
    findings = [term for term in risky_terms if term in lowered]
    return {
        "status": "flagged" if findings else "allowed",
        "findings": findings,
        "user": user,
    }
