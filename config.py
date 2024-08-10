import os
from dotenv import load_dotenv

load_dotenv()

# Test URLs
ALLOWED_WEBSITES = ["https://www.google.com"]
BLOCKED_WEBSITES = ["https://www.taobao.com"]

# Email settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = os.getenv("GMAIL_USERNAME")
SMTP_PASSWORD = os.getenv("GMAIL_PASSWORD")
SMTP_RECIPIENT = os.getenv("RECIPIENT_EMAIL")

# Remote access settings
SSH_PORT = 22
RDP_PORT = 3389

# VPN settings
VPN_SERVER = "vpn.example.com"
VPN_PORT = 1194
