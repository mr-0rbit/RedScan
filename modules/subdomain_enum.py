import requests

def run(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    subdomains = set()

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            for entry in response.json():
                names = entry.get("name_value", "")
                for sub in names.split("\n"):
                    subdomains.add(sub.strip())
    except:
        pass

    return list(subdomains)
