import config
from utils.network_utils import test_connection

def run_tests(profile):
    allowed_websites = config.BASE_ALLOWED_WEBSITES
    blocked_websites = config.BASE_BLOCKED_WEBSITES

    if profile == "Sales":
        allowed_websites.extend(config.SALES_ALLOWED_WEBSITES)
        blocked_websites.extend(config.SALES_BLOCKED_WEBSITES)
    elif profile == "HR":
        allowed_websites.extend(config.HR_ALLOWED_WEBSITES)
        blocked_websites.extend(config.HR_BLOCKED_WEBSITES)
    elif profile == "IT":
        allowed_websites.extend(config.IT_ALLOWED_WEBSITES)
        blocked_websites.extend(config.IT_BLOCKED_WEBSITES)

    print("Running Allowed Web Traffic Tests")
    for url in allowed_websites:
        test_connection(url, should_connect=True)

    print()
    print("Running Blocked Web Traffic Tests")
    for url in blocked_websites:
        test_connection(url, should_connect=False)

    # print()

    # print("Running App-ID Tests")
    # test_connection("https://www.facebook.com", should_connect=True)

    # session_cookies = json.loads(base64.b64decode(config.FACEBOOK_COOKIES))
    # test_facebook_message(config.FACEBOOK_CLIENT_EMAIL, config.FACEBOOK_CLIENT_PASSWORD, config.FACEBOOK_THREAD_ID, session_cookies)
