import socket
from utilities.logger import verbose

def parse_http_headers(raw):
    info = {}
    lines = raw.split("\r\n")

    for line in lines:
        if line.startswith("HTTP/"):
            info["status"] = line
        elif line.lower().startswith("location:"):
            info["location"] = line.split(":", 1)[1].strip()
        elif line.lower().startswith("server:"):
            info["server"] = line.split(":", 1)[1].strip()

    return info

def run(target, open_ports):
    output = "<h2>Service Identification (Banner Grabbing)</h2>"
    output += """
    <div class="section-note">
    This section identifies software and services running on exposed network ports
    using non-intrusive response analysis.
    </div>
    <table>
    <tr><th>Port</th><th>Identified Service Information</th></tr>
    """

    results = []

    for entry in open_ports:
        port = entry["port"]

        try:
            verbose(f"Attempting banner grab on port {port}")
            s = socket.socket()
            s.settimeout(3)
            s.connect((target, port))

            if port in [80, 443]:
                request = f"HEAD / HTTP/1.1\r\nHost: {target}\r\nConnection: close\r\n\r\n"
                s.sendall(request.encode())

            response = s.recv(4096).decode(errors="ignore")
            s.close()

            if not response:
                continue

            if port in [80, 443]:
                parsed = parse_http_headers(response)

                summary = []
                if "status" in parsed:
                    summary.append(parsed["status"])
                if "location" in parsed:
                    summary.append(f"Redirects to {parsed['location']}")
                if "server" in parsed:
                    summary.append(f"Server: {parsed['server']}")

                summary_text = " | ".join(summary)

                output += f"<tr><td>{port}</td><td>{summary_text}</td></tr>"
                results.append({
                    "port": port,
                    "summary": summary_text
                })

        except:
            verbose(f"No banner received on port {port}")

    output += "</table>"
    return output, results
