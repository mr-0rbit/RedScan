import argparse
from modules import (
    whois_lookup,
    dns_enum,
    subdomain_enum,
    port_scan
)
from report.report_generator import generate_report
from utils.logger import setup_logger
from utils.helpers import resolve_ip

def banner():
    print(r"""
██████╗ ███████╗██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝█████╗  ██║  ██║███████╗██║     ███████║██╔██╗ ██║
██╔══██╗██╔══╝  ██║  ██║╚════██║██║     ██╔══██║██║╚██╗██║
██║  ██║███████╗██████╔╝███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
        Offensive Reconnaissance Framework
""")

banner()

parser = argparse.ArgumentParser(
    description="RedScan - Offensive Recon Tool"
)

parser.add_argument("target", help="Target domain or IP")
parser.add_argument("--whois", action="store_true")
parser.add_argument("--dns", action="store_true")
parser.add_argument("--subdomains", action="store_true")
parser.add_argument("--ports", action="store_true")
parser.add_argument("--report", action="store_true")
parser.add_argument("-v", "--verbose", action="store_true")

args = parser.parse_args()
logger = setup_logger(args.verbose)

logger.info("RedScan started")

ip = resolve_ip(args.target)
logger.info(f"Resolved IP: {ip}")

results = {
    "target": args.target,
    "ip": ip
}

if args.whois:
    results["whois"] = whois_lookup.run(args.target)

if args.dns:
    results["dns"] = dns_enum.run(args.target)

if args.subdomains:
    results["subdomains"] = subdomain_enum.run(args.target)

if args.ports:
    results["ports"] = port_scan.run(args.target)

if args.report:
    generate_report(args.target, results)

logger.info("RedScan finished")
