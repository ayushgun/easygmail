from email.message import EmailMessage
from typing import Self

from .validation import validate_email


class EmailBuilder:
    """
    A builder class for creating EmailMessage objects.

    This class provides a fluent interface to build an EmailMessage with a receiver,
    subject, and body. It includes member functions for setting each of these components
    and for validating the email address of the receiver.

    Attributes:
        message (EmailMessage): The email message being built.

    Args:
        receiver (str, optional): The email address of the receiver.
        subject (str, optional): The subject of the email.
        body (str, optional): The body content of the email.

    Raises:
        ValueError: If the provided receiver email address is invalid.
    """

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
        """
        Sets the receiver of the email.

        Args:
            receiver (str): The email address of the receiver.

        Returns:
            Self: Returns a copy of itself for fluent chaining.

        Raises:
            ValueError: If the provided receiver email address is invalid.
        """

        if not validate_email(receiver):
            raise ValueError("Receiver must be a valid email address")

        new_email = self
        new_email.message["To"] = receiver
        return new_email

    def set_subject(self, subject: str) -> Self:
        """
        Sets the subject of the email.

        Args:
            subject (str): The subject text of the email.

        Returns:
            Self: Returns a copy of  itself for fluent chaining.
        """

        new_email = self
        new_email.message["Subject"] = subject
        return new_email

    def set_body(self, body: str) -> Self:
        """
        Sets the body of the email.

        Args:
            body (str): The body content of the email.

        Returns:
            Self: Returns a copy of itself for fluent chaining.
        """

        new_email = self
        new_email.message.set_content(body)
        return new_email

    def build(self) -> EmailMessage:
        """
        Finalizes and returns the EmailMessage object.

        Ensures that the receiver, subject, and body are all set before returning
        the email message. If any of these components are missing, a ValueError
        is raised.

        Returns:
            EmailMessage: The fully constructed email message.

        Raises:
            ValueError: If receiver, subject, or body is not set.
        """

        if not self.message["To"]:
            raise ValueError("Email receiver is not set.")
        if not self.message["Subject"]:
            raise ValueError("Email subject is not set.")
        if not self.message.get_payload(decode=True):
            raise ValueError("Email body is not set.")

        return self.message
