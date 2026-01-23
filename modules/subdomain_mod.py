import requests
import dns.resolver
from utilities.logger import verbose

def resolve_ip(host):
    ips = []
    try:
        answers = dns.resolver.resolve(host, "A")
        for r in answers:
            ips.append(str(r))
    except:
        pass
    return ips

def run(domain):
    output = "<h2>Subdomain Enumeration</h2>"
    output += """
    <div class="section-note">
    This section lists discovered subdomains and their resolved IP addresses.
    Only valid and resolvable subdomains are included.
    </div>
    <table>
    <tr><th>Subdomain</th><th>Resolved IP Address(es)</th></tr>
    """

    results = []

    url = f"https://crt.sh/?q=%25.{domain}&output=json"

    try:
        verbose("Fetching certificate transparency data")
        data = requests.get(url, timeout=10).json()

        subs = set()
        for entry in data:
            names = entry.get("name_value", "").splitlines()
            for name in names:
                name = name.strip().lower()
                if name.startswith("*."):
                    name = name[2:]
                if name.endswith(domain):
                    subs.add(name)

        for sub in sorted(subs):
            ips = resolve_ip(sub)
            if ips:
                output += f"<tr><td>{sub}</td><td>{', '.join(ips)}</td></tr>"
                results.append({
                    "subdomain": sub,
                    "ips": ips
                })

        output += f"<tr><td colspan='2'><b>Total Resolvable Subdomains:</b> {len(results)}</td></tr>"

    except Exception as e:
        output += f"<tr><td colspan='2'>Subdomain enumeration failed: {e}</td></tr>"

    output += "</table>"
    return output, results
