import config
from utils.network_utils import test_vpn_connection

def run_tests():
    print("Running VPN Connectivity Tests")
    test_vpn_connection(config.VPN_SERVER, config.VPN_PORT)
