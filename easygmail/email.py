from email.message import EmailMessage


class EmailBuilder:
    def __init__(
        self, receiver: str = None, subject: str = None, body: str = None
    ) -> None:
        self.message = EmailMessage()

        if receiver:
            self.message["To"] = receiver
        if subject:
            self.message["Subject"] = subject
        if body:
            self.message.set_content(body)

    def set_receiver(self, receiver: str) -> "EmailBuilder":
        self.message["To"] = receiver
        return self

    def set_subject(self, subject: str) -> "EmailBuilder":
        self.message["Subject"] = subject
        return self

    def set_body(self, body: str) -> "EmailBuilder":
        self.message.set_content(body)
        return self

    def build(self) -> EmailMessage:
        if not self.message["To"]:
            raise ValueError("Email receiver is not set.")
        if not self.message["Subject"]:
            raise ValueError("Email subject is not set.")
        if not self.message.get_content():
            raise ValueError("Email body is not set.")

        return self.message
