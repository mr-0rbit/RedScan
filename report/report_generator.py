import json
from datetime import datetime
from utils.helpers import create_output_dir

def table(headers, rows):
    html = "<table>"
    html += "<tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>"
    for row in rows:
        html += "<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>"
    html += "</table>"
    return html

def generate_report(target, data):
    out_dir = create_output_dir(target)

    # ---------------- JSON REPORT ----------------
    json_path = f"{out_dir}/report.json"
    with open(json_path, "w") as jf:
        json.dump(data, jf, indent=4)

    # ---------------- HTML REPORT ----------------
    html = f"""
<html>
<head>
<title>RedScan Report - {target}</title>
<style>
body {{
    font-family: Arial, sans-serif;
    background-color: #0f172a;
    color: #e5e7eb;
    padding: 30px;
}}

h1 {{ color: #38bdf8; }}
h2 {{ color: #22d3ee; margin-top: 40px; }}

table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
}}

th, td {{
    border: 1px solid #334155;
    padding: 10px;
}}

th {{
    background-color: #020617;
    color: #38bdf8;
}}

tr:nth-child(even) {{
    background-color: #020617;
}}

footer {{
    margin-top: 50px;
    font-size: 12px;
    color: #94a3b8;
}}
</style>
</head>
<body>

<h1>RedScan Reconnaissance Report</h1>
<p><b>Target:</b> {target}</p>
<p><b>Generated:</b> {datetime.now()}</p>
"""

    # -------- TARGET INFO --------
    html += "<h2>Target Information</h2>"
    html += table(
        ["Field", "Value"],
        [
            ["Domain", data.get("target", "")],
            ["IP Address", data.get("ip", "")]
        ]
    )

    # -------- WHOIS --------
    if "whois" in data:
        html += "<h2>WHOIS Information</h2>"
        rows = []
        for k, v in data["whois"].items():
            if isinstance(v, list):
                for item in v:
                    rows.append([k, item])
            else:
                rows.append([k, v])
        html += table(["Field", "Value"], rows)

    # -------- DNS --------
    if "dns" in data:
        html += "<h2>DNS Records</h2>"
        rows = []
        for rtype, values in data["dns"].items():
            for val in values:
                rows.append([rtype, val])
        html += table(["Record Type", "Value"], rows)

    # -------- SUBDOMAINS --------
    if "subdomains" in data:
        html += "<h2>Discovered Subdomains</h2>"
        rows = [[i + 1, sub] for i, sub in enumerate(data["subdomains"])]
        html += table(["#", "Subdomain"], rows)

    # -------- PORTS --------
    if "ports" in data:
        html += "<h2>Open Ports</h2>"
        rows = []
        for host, ports in data["ports"].items():
            for port, state in ports.items():
                rows.append([host, port, state])
        html += table(["Host", "Port", "State"], rows)

    html += """
<footer>
<hr>
RedScan — Offensive Reconnaissance Framework
</footer>
</body>
</html>
"""

    with open(f"{out_dir}/report.html", "w") as hf:
        hf.write(html)

    # ---------------- TERMINAL JSON OUTPUT ----------------
    print("\n========== JSON OUTPUT ==========")
    print(json.dumps(data, indent=4))
    print("=================================\n")

    print(f"[+] HTML report saved: {out_dir}/report.html")
    print(f"[+] JSON report saved: {json_path}")
