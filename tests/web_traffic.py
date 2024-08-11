import config
from utils.network_utils import test_connection

def run_tests():
    print("Running Web Traffic Tests")
    for url in config.ALLOWED_WEBSITES:
        test_connection(url, should_connect=True)
    for url in config.BLOCKED_WEBSITES:
        test_connection(url, should_connect=False)

    # print()

    # print("Running App-ID Tests")
    # test_connection("https://www.facebook.com", should_connect=True)

    # session_cookies = json.loads(base64.b64decode(config.FACEBOOK_COOKIES))
    # test_facebook_message(config.FACEBOOK_CLIENT_EMAIL, config.FACEBOOK_CLIENT_PASSWORD, config.FACEBOOK_THREAD_ID, session_cookies)
