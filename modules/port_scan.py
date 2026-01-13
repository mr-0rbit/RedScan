import nmap

def run(target):
    nm = nmap.PortScanner()
    nm.scan(target, "1-1000")
    results = {}

    for host in nm.all_hosts():
        results[host] = {}
        for port in nm[host].get("tcp", {}):
            results[host][port] = nm[host]["tcp"][port]["state"]

    return results
