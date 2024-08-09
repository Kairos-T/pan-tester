from colorama import Fore, Style, init

init(autoreset=True)

def log(level, message):
    if level == "info":
        print(f"[{Fore.BLUE}*{Style.RESET_ALL}] {message}")
    elif level == "success":
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] {message}")
    elif level == "error":
        print(f"[{Fore.RED}x{Style.RESET_ALL}] {message}")
    else:
        print(message)
