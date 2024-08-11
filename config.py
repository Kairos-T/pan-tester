import os
from dotenv import load_dotenv

load_dotenv()

# Test URLs
ALLOWED_WEBSITES = ["https://www.google.com"]
BLOCKED_WEBSITES = ["https://www.taobao.com", "https://www.minecraft.net"]

# Email settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = os.getenv("GMAIL_USERNAME")
SMTP_PASSWORD = os.getenv("GMAIL_PASSWORD")
SMTP_RECIPIENT = os.getenv("RECIPIENT_EMAIL")

# Facebook settings
# FACEBOOK_CLIENT_EMAIL = os.getenv("FACEBOOK_CLIENT_EMAIL")
# FACEBOOK_CLIENT_PASSWORD = os.getenv("FACEBOOK_CLIENT_PASSWORD")
# FACEBOOK_THREAD_ID = os.getenv("FACEBOOK_THREAD_ID")
# FACEBOOK_COOKIES = os.getenv("FACEBOOK_COOKIES")
