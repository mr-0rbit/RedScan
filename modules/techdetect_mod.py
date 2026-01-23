import requests
from utilities.logger import verbose

def run(domain):
    output = "<h2>Technology Detection</h2><table>"
    data = {}

    try:
        verbose("Sending HTTP request for header analysis")
        r = requests.get(f"http://{domain}", timeout=5)
        headers = r.headers

        if "Server" in headers:
            output += f"<tr><td><b>Web Server</b></td><td>{headers['Server']}</td></tr>"
            data["server"] = headers["Server"]

        if "X-Powered-By" in headers:
            output += f"<tr><td><b>Backend</b></td><td>{headers['X-Powered-By']}</td></tr>"
            data["backend"] = headers["X-Powered-By"]

    except:
        output += "<tr><td>Technology detection failed</td></tr>"

    output += "</table>"
    return output, data
