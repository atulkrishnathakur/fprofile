from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
mailconf = ConnectionConfig(
    MAIL_USERNAME="softtestinfo@gmail.com",
    MAIL_PASSWORD="kmbonzewdsmorthm",
    MAIL_FROM="atul77.cs@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS = True    
)