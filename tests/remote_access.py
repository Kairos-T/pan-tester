import config
from utils.network_utils import test_port_connection

def run_tests():
    print("Running Remote Access Tests")
    test_port_connection("localhost", config.SSH_PORT, "SSH")
    test_port_connection("localhost", config.RDP_PORT, "RDP")
