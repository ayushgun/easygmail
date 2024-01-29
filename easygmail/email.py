from email.message import EmailMessage
from typing import Self

from .utility import validate_email


class EmailBuilder:
    def __init__(
        self, receiver: str = None, subject: str = None, body: str = None
    ) -> None:
        self.message = EmailMessage()

        if receiver:
            if not validate_email(receiver):
                raise ValueError("Receiver must be a valid email address")

            self.message["To"] = receiver

        if subject:
            self.message["Subject"] = subject

        if body:
            self.message.set_content(body)

    def set_receiver(self, receiver: str) -> Self:
        if not validate_email(receiver):
            raise ValueError("Receiver must be a valid email address")

        new_email = self
        new_email.message["To"] = receiver
        return new_email

    def set_subject(self, subject: str) -> Self:
        new_email = self
        new_email.message["Subject"] = subject
        return new_email

    def set_body(self, body: str) -> Self:
        new_email = self
        new_email.message.set_content(body)
        return new_email

    def build(self) -> EmailMessage:
        if not self.message["To"]:
            raise ValueError("Email receiver is not set.")
        if not self.message["Subject"]:
            raise ValueError("Email subject is not set.")
        if not self.message.get_content():
            raise ValueError("Email body is not set.")

        return self.message
