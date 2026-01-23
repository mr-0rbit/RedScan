from datetime import datetime
from colorama import Fore, init

init(autoreset=True)

VERBOSE = False

def set_verbose(value: bool):
    global VERBOSE
    VERBOSE = value

def banner():
    print(Fore.RED + r"""
██████╗ ███████╗██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝█████╗  ██║  ██║███████╗██║     ███████║██╔██╗ ██║
██╔══██╗██╔══╝  ██║  ██║╚════██║██║     ██╔══██║██║╚██╗██║
██║  ██║███████╗██████╔╝███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
          MODULAR • RECONNAISSANCE • FRAMEWORK
""")

def log(msg):
    print(Fore.CYAN + f"[*] {msg}")

def success(msg):
    print(Fore.GREEN + f"[+] {msg}")

def error(msg):
    print(Fore.RED + f"[-] {msg}")

def verbose(msg):
    if VERBOSE:
        print(Fore.YELLOW + f"    └─ {msg}")
