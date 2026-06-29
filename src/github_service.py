def create_security_issue(repo: str, title: str, body: str) -> dict:
    """Fake GitHub issue creation placeholder."""
    return {
        "repo": repo,
        "title": title,
        "body": body,
        "status": "demo-only-not-created"
    }
