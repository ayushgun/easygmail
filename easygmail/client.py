import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

from .validation import validate_gmail, validate_password


class Client:
    """
    A client for sending emails via Gmail.

    This class manages the connection to the Gmail SMTP server and provides
    a member function for sending email messages.

    Attributes:
        email_address (str): Email address of the client.
        password (str): App password on the client's email account.
        server (smtplib.SMTP): Instance of SMTP for email transmission.

    Args:
        env_file (str, optional): Path to the .env file containing EMAIL_ADDRESS
            and PASSWORD. If not provided, email_address and app password must be
            given directly.
        email_address (str, optional): The Gmail address from which emails will be sent.
        password (str, optional): An app password on the given Gmail account.

    Raises:
        ValueError: If the necessary credentials are not provided or invalid.
    """

    def __init__(
        self, email_address: str = None, password: str = None, env_file: str = None
    ) -> None:
        if env_file:
            load_dotenv(env_file)
            email_address = os.getenv("EMAIL_ADDRESS")
            password = os.getenv("PASSWORD")

            if not email_address or not password:
                raise ValueError(
                    "Environment variables 'EMAIL_ADDRESS' and 'PASSWORD' must be set in the .env file"
                )

        if not email_address or not password:
            raise ValueError("Email address and password must be provided")
        if not validate_gmail(email_address):
            raise ValueError("Email must be a Gmail address (ends with @gmail.com)")
        if not validate_password(password):
            raise ValueError("Password must be at least 8 characters long")

        self.email_address = email_address
        self.password = password
        self.__init_server()

    def __del__(self) -> None:
        if getattr(self, "server", None):
            self.server.quit()

    def __init_server(self) -> None:
        """
        Initializes the SMTP server for sending emails.

        This member function sets up the SMTP server with Gmail's settings and logs in
        using the provided credentials. It is called during the initialization
        of the Client object.
        """

        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.ehlo_or_helo_if_needed()
        self.server.starttls()
        self.server.ehlo_or_helo_if_needed()
        self.server.login(self.email_address, self.password)

    def send(self, email: EmailMessage) -> None:
        """
        Sends an email message.

        This member function sends an EmailMessage using the initialized SMTP server.
        If the 'From' field is not set in the email, it uses the client's email address.

        Args:
            email (EmailMessage): The email message to be sent.
        """

        if "From" not in email:
            email["From"] = self.email_address

        self.server.send_message(email)
