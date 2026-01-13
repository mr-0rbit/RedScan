import whois

def run(domain):
    try:
        w = whois.whois(domain)
        return {
            "registrar": w.registrar,
            "creation_date": str(w.creation_date),
            "expiration_date": str(w.expiration_date),
            "name_servers": w.name_servers
        }
    except Exception as e:
        return {"error": str(e)}
