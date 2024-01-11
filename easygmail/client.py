import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv
from .utility import validate_gmail, validate_password


class Client:
    def __init__(
        self, env_file: str = None, email_address: str = None, password: str = None
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

    def __init_server(self) -> None:
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.ehlo_or_helo_if_needed()
        self.server.starttls()
        self.server.ehlo_or_helo_if_needed()
        self.server.login(self.email_address, self.password)

    def __del__(self) -> None:
        self.server.quit()

    def send(self, email: EmailMessage) -> None:
        if "From" not in email:
            email["From"] = self.email_address

        self.server.send_message(email)
