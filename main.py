import argparse
import os
from tests import web_traffic, email_traffic
from utils.logger import log

def main():
    parser = argparse.ArgumentParser(description="NS Firewall Testing Script")
    parser.add_argument("--web", action="store_true", help="Run web traffic tests")
    parser.add_argument("--email", action="store_true", help="Run email traffic tests")
    parser.add_argument("--all", action="store_true", help="Run all tests")
    parser.add_argument("--profile", choices=["Sales", "HR", "IT"], help="Set the user profile")

    args = parser.parse_args()

    if not args.profile:
        log("error", "Please specify a profile using the --profile argument [Sales, HR, IT]")
        return

    if args.all or args.web:
        os.environ["OPENSSL_CONF"] = "./openssl.cnf"
        web_traffic.run_tests(args.profile)
    
    if args.all or args.email:
        email_traffic.run_tests()
    
    if not any(vars(args).values()):
        parser.print_help()

if __name__ == "__main__":
    main()
