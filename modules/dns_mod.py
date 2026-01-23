import dns.resolver
from utilities.logger import verbose

def resolve_ips(host):
    ips = []
    try:
        answers = dns.resolver.resolve(host, "A")
        for r in answers:
            ips.append(str(r))
    except:
        pass
    return ips

def run(fqdn):
    output = "<h2>DNS Enumeration</h2>"
    output += f"""
    <div class="section-note">
    DNS enumeration performed using the Fully Qualified Domain Name (FQDN):
    <b>{fqdn}</b>
    </div>
    <table>
    <tr><th>Record Type</th><th>Details</th></tr>
    """

    data = {
        "fqdn_used": fqdn
    }

    # A Records
    try:
        verbose("Resolving A records")
        answers = dns.resolver.resolve(fqdn, "A")
        data["A"] = []
        for r in answers:
            output += f"<tr><td>A (Website IP)</td><td>{r}</td></tr>"
            data["A"].append(str(r))
    except:
        verbose("No A records found")

    # MX Records
    try:
        verbose("Resolving MX records")
        answers = dns.resolver.resolve(fqdn, "MX")
        data["MX"] = []

        for r in answers:
            mx_host = str(r.exchange).rstrip(".")
            priority = r.preference
            ips = resolve_ips(mx_host)

            detail = f"{mx_host} (Priority {priority}) → {', '.join(ips) if ips else 'IP not resolved'}"
            output += f"<tr><td>MX (Email Server)</td><td>{detail}</td></tr>"

            data["MX"].append({
                "server": mx_host,
                "priority": priority,
                "ips": ips
            })
    except:
        verbose("No MX records found")

    # NS Records
    try:
        verbose("Resolving NS records")
        answers = dns.resolver.resolve(fqdn, "NS")
        data["NS"] = []
        for r in answers:
            output += f"<tr><td>NS (Name Server)</td><td>{r}</td></tr>"
            data["NS"].append(str(r))
    except:
        verbose("No NS records found")

    output += "</table>"
    return output, data
