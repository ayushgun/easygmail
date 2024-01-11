import re


def validate_gmail(email: str) -> bool:
    return email.endswith("@gmail.com")


def validate_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def validate_password(password: str) -> bool:
    return len(password) >= 8
