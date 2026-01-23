import nmap
from utilities.logger import verbose

def run(target):
    output = "<h2>Open Ports & Services</h2><table>"
    data = []

    scanner = nmap.PortScanner()
    verbose("Starting Nmap SYN scan")
    scanner.scan(target, arguments="-sS -T4")

    for host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            for port in scanner[host][proto]:
                service = scanner[host][proto][port]['name']
                output += f"<tr><td>{port}/{proto}</td><td>{service}</td></tr>"
                data.append({
                    "port": port,
                    "protocol": proto,
                    "service": service
                })

    output += "</table>"
    return output, data
