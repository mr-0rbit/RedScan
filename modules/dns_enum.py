import dns.resolver

def run(domain):
    records = {}
    for rtype in ["A", "MX", "TXT", "NS"]:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            records[rtype] = [str(r) for r in answers]
        except:
            records[rtype] = []
    return records
