import config
from utils.network_utils import test_connection

def run_tests():
    print("Running Web Traffic Tests")
    for url in config.ALLOWED_WEBSITES:
        test_connection(url, should_connect=True)
    for url in config.BLOCKED_WEBSITES:
        test_connection(url, should_connect=False)
