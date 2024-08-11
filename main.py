import argparse
from tests import web_traffic, email_traffic
from utils.logger import log

def main():
    parser = argparse.ArgumentParser(description="NS Firewall Testing Script")
    parser.add_argument("--web", action="store_true", help="Run web traffic tests")
    parser.add_argument("--email", action="store_true", help="Run email traffic tests")
    parser.add_argument("--all", action="store_true", help="Run all tests")

    args = parser.parse_args()

    if args.all or args.web:
        web_traffic.run_tests()
    
    if args.all or args.email:
        email_traffic.run_tests()
    
    if not any(vars(args).values()):
        parser.print_help()

if __name__ == "__main__":
    main()
