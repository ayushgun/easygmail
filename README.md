# EasyGmail

## Overview

EasyGmail is a lightweight, minimalistic, and synchronous Python API designed for quick email sending via Gmail.

## Getting Started

### Installation

```
pip install git+https://github.com/ayushgun/easygmail
```

### Prerequisites

Before using EasyGmail, ensure you have an [app password](https://support.google.com/mail/answer/185833?hl=en#app-passwords) for Gmail. Do **not** use your regular account password.

### Quick Start Example

```python
from easygmail import Client, EmailBuilder

client = Client("<address>@gmail.com", "<app password>")

msg = EmailBuilder(
    receiver="<recipient>@domain.com", subject="<subject text>", body="<body text>"
).build()

client.send(msg)
```

### Client Initialization

You can instantiate a `Client` object in two ways:

1. **Direct Credentials**:
   Provide email address and app password directly as arguments.

```python
from easygmail import Client

client = Client("<address>@gmail.com", "<app password>")
```

2. **Environment File**:
   Use a `.env` file to store credentials.

```python
from easygmail import Client

client = Client(env_file=".env")
```

Your `.env` file should contain:

```bash
EMAIL_ADDRESS="<address>@gmail.com"
PASSWORD="<app password>"
```

### Creating Email Messages

Create `EmailMessage` objects using one of the following methods:

1. **EmailBuilder Constructor**:

```python
from easygmail import EmailBuilder

msg = EmailBuilder(
    receiver="<recipient>@domain.com", subject="<subject text>", body="<body text>"
).build()
```

2. **EmailBuilder Factory Interface**:

```python
from easygmail import EmailBuilder

msg = (
    EmailBuilder()
    .set_receiver("<recipient>@domain.com")
    .set_subject("<subject text>")
    .set_body("<body text>")
).build()
```

3. **Directly Using `EmailMessage`**:

```python
from email.message import EmailMessage

msg = EmailMessage()
msg["To"] = "<recipient>@domain.com"
msg["Subject"] = "<subject text>"
msg.set_content("<body text>")
```
