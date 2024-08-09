import requests
import socket
from .logger import log

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

def test_smtp_connection(server, port):
    try:
        with socket.create_connection((server, port), timeout=5):
            log("success", f"Successfully connected to SMTP server {server}:{port}")
    except (socket.timeout, ConnectionRefusedError):
        log("error", f"Failed to connect to SMTP server {server}:{port}")

def test_port_connection(host, port, service_name):
    try:
        with socket.create_connection((host, port), timeout=5):
            log("success", f"Successfully connected to {service_name} on {host}:{port}")
    except (socket.timeout, ConnectionRefusedError):
        log("error", f"Failed to connect to {service_name} on {host}:{port}")

def test_vpn_connection(server, port):
    log("info", f"Testing VPN connection to {server}:{port}")
