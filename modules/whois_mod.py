import whois
from utilities.logger import verbose

def clean(value):
    if isinstance(value, list):
        return ", ".join(str(v) for v in value)
    return str(value)

def run(domain):
    output = "<h2>Domain Ownership Information (WHOIS)</h2>"
    output += """
    <div class="section-note">
    WHOIS data provides information about domain ownership, registration dates,
    and authoritative name servers.
    </div>
    <table>
    """

    data = {}

    try:
        verbose("Querying WHOIS records")
        w = whois.whois(domain)

        fields = {
            "Domain Name": w.domain_name,
            "Registrar": w.registrar,
            "Creation Date": w.creation_date,
            "Expiration Date": w.expiration_date,
            "Name Servers": w.name_servers
        }

        for key, value in fields.items():
            clean_value = clean(value)
            output += f"<tr><td><b>{key}</b></td><td>{clean_value}</td></tr>"
            data[key] = clean_value

    except Exception as e:
        output += f"<tr><td>Error</td><td>{e}</td></tr>"

    output += "</table>"
    return output, data
