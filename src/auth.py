def validate_user(email: str) -> bool:
    """Demo-only identity check."""
    return email.endswith("@acmebank.example")
