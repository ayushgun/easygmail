import pytest
from easygmail import EmailBuilder


def test_initialization_with_valid_inputs():
    email = EmailBuilder("test@example.com", "Test Subject", "Test Body")
    assert email.message["To"] == "test@example.com"
    assert email.message["Subject"] == "Test Subject"
    assert email.message.get_content() == "Test Body\n"


def test_initialization_with_invalid_email():
    with pytest.raises(ValueError):
        EmailBuilder("invalid-email", "Test Subject", "Test Body")


def test_set_receiver():
    email = EmailBuilder().set_receiver("test@example.com")
    assert email.message["To"] == "test@example.com"

    with pytest.raises(ValueError):
        email.set_receiver("invalid-email")


def test_set_subject():
    email = EmailBuilder().set_subject("Test Subject")
    assert email.message["Subject"] == "Test Subject"


def test_set_body():
    email = EmailBuilder().set_body("Test Body")
    assert email.message.get_content() == "Test Body\n"


def test_build_email_with_missing_parts():
    email = EmailBuilder()
    with pytest.raises(ValueError):
        email.build()

    email.set_receiver("test@example.com")
    with pytest.raises(ValueError):
        email.build()

    email.set_subject("Test Subject")
    with pytest.raises(ValueError):
        email.build()


def test_successful_build():
    email = (
        EmailBuilder()
        .set_receiver("test@example.com")
        .set_subject("Test Subject")
        .set_body("Test Body")
    )
    built_email = email.build()
    assert built_email["To"] == "test@example.com"
    assert built_email["Subject"] == "Test Subject"
    assert built_email.get_content() == "Test Body\n"
