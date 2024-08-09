import config
from utils.network_utils import test_smtp_connection

def run_tests():
    print("Running Email Traffic Tests")
    test_smtp_connection(config.SMTP_SERVER, config.SMTP_PORT, config.SMTP_USERNAME, config.SMTP_PASSWORD, config.SMTP_RECIPEINT)
