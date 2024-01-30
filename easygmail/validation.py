import re


def validate_gmail(email: str) -> bool:
    """
    Validates whether an email address is a Gmail address.

    This function simply checks if the provided email address ends with '@gmail.com'.
    It is specific to Gmail addresses only.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is a Gmail address, False otherwise.
    """

    return email.endswith("@gmail.com")


def validate_email(email: str) -> bool:
    """
    Validates the format of an email address using a regular expression.

    This function uses a regular expression to check if the provided email
    address conforms to a standard email address format. It checks for a
    general email pattern, not specific to any email provider.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is in a valid format, False otherwise.
    """

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def validate_password(password: str) -> bool:
    """
    Validates the length of a password.

    This function checks if the provided password is at least 8 characters long.
    It validates only the length of the password, not its complexity or strength.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is at least 8 characters long, False otherwise.
    """

    return len(password) >= 8
