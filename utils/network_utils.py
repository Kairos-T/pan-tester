import requests
import socket
from .logger import log
import smtplib
from email.mime.text import MIMEText
import ssl

def test_connection(url, should_connect=True):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200 and should_connect:
            log("success", f"Successfully connected to {url}")
        elif response.status_code != 200 and not should_connect:
            log("success", f"Successfully blocked connection to {url}")
        else:
            log("error", f"Unexpected result for {url}")
    except requests.exceptions.RequestException:
        if should_connect:
            log("error", f"Failed to connect to {url}")
        else:
            log("success", f"Successfully blocked connection to {url}")

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

def test_port_connection(host, port, service_name):
    try:
        with socket.create_connection((host, port), timeout=5):
            log("success", f"Successfully connected to {service_name} on {host}:{port}")
    except (socket.timeout, ConnectionRefusedError):
        log("error", f"Failed to connect to {service_name} on {host}:{port}")

def test_vpn_connection(server, port):
    log("info", f"Testing VPN connection to {server}:{port}")
