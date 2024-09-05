def get_email(email: str):
    if "@" not in email:
        raise ValueError("Invalid email")
    return email
