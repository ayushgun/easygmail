import pytest
from unittest.mock import patch, MagicMock
from easygmail import Client
from email.message import EmailMessage


def test_invalid_credentials():
    with pytest.raises(ValueError):
        Client(email_address="notgmail.com", password="short")

    with pytest.raises(ValueError):
        Client(email_address="test@gmail.com", password="short")


@pytest.mark.parametrize(
    "email_address,password",
    [(None, "validpassword"), ("test@gmail.com", None), (None, None)],
)
def test_missing_credentials(email_address, password):
    with pytest.raises(ValueError):
        Client(email_address=email_address, password=password)


@patch("smtplib.SMTP")
def test_smtp_server_initialization(mock_smtp):
    with patch("easygmail.validate_gmail", return_value=True), patch(
        "easygmail.validate_password", return_value=True
    ):
        Client(email_address="test@gmail.com", password="validpassword")
        mock_smtp.assert_called_with("smtp.gmail.com", 587)


@patch("smtplib.SMTP")
def test_send_email(mock_smtp):
    smtp_instance = MagicMock()
    mock_smtp.return_value = smtp_instance

    with patch("easygmail.validate_gmail", return_value=True), patch(
        "easygmail.validate_password", return_value=True
    ):
        client = Client(email_address="test@gmail.com", password="validpassword")
        email = EmailMessage()
        client.send(email)

        smtp_instance.send_message.assert_called_with(email)


@patch("smtplib.SMTP")
def test_destructor(mock_smtp):
    smtp_instance = MagicMock()
    mock_smtp.return_value = smtp_instance

    with patch("easygmail.validate_gmail", return_value=True), patch(
        "easygmail.validate_password", return_value=True
    ):
        client = Client(email_address="test@gmail.com", password="validpassword")
        del client

        smtp_instance.quit.assert_called_once()
