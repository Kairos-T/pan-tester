import requests
import socket
from .logger import log
import smtplib
from email.mime.text import MIMEText
import ssl

def test_connection(url, should_connect=True):
    requests.packages.urllib3.disable_warnings()
    try:
        response = requests.get(url, timeout=5, verify=False)
        if response.status_code != 503 and should_connect:
            log("success", f"Successfully connected to {url}")
        elif response.status_code == 503 and not should_connect:
            log("success", f"Successfully blocked connection to {url}")
        else:
            log("error", f"Unexpected result for {url}")
    except requests.exceptions.RequestException:
        if should_connect:
            log("error", f"Failed to connect to {url}")
        else:
            log("success", f"Successfully blocked connection to {url}")

# def test_facebook_message(email, password, thread_id, session_cookies):
#     try:
#         client = Client(email, password, session_cookies=session_cookies)
#         client.send(Message(text="This is a test message"), thread_id=thread_id, thread_type=ThreadType.USER)
#         log("error", "Application facebook-chat can be accessed")
#     except:
#         log("success", "Application facebook-chat cannot be accessed")

def test_smtp_connection(server, port, username, password, recipient):
    try:
        msg = MIMEText("This email confirms that SMTP traffic is allowed, and this email is well received.")
        msg['From'] = username
        msg['To'] = recipient
        msg['Subject'] = "Success: NS SMTP Test"
        
        context = ssl._create_unverified_context()
        context.options |= ssl.OP_LEGACY_SERVER_CONNECT

        with smtplib.SMTP(server, port) as smtp_server:
            smtp_server.starttls(context=context)
            smtp_server.login(username, password)
            smtp_server.sendmail(username, recipient, msg.as_string())
        log("success", f"Successfully connected to SMTP server {server}:{port}")
    except (socket.timeout, ConnectionRefusedError) as e:
        log("error", f"Failed to connect to SMTP server {server}:{port}. Error: {str(e)}")
    except ssl.SSLError as e:
        log("error", f"SSL error while connecting to SMTP server {server}:{port}. Error: {str(e)}")
