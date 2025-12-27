import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

mcp=FastMCP()

MAIL_ACCOUNT = os.getenv('MAIL_ACCOUNT')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
SMTP_USE_STARTTLS = os.getenv('SMTP_USE_STARTTLS') == 'True'
SMTP_USE_SSL = os.getenv('SMTP_USE_SSL') == 'False'


@mcp.tool()
def send_email(to:str, subject:str, body:str) -> str:
    msg = EmailMessage()
    msg['From'] = MAIL_ACCOUNT
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(body)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(MAIL_ACCOUNT, os.getenv('MAIL_PASSWORD'))
        server.send_message(msg)
    return "Email sent successfully."