🔴 RedScan — Offensive Reconnaissance Framework
<p align="center"> <img src="https://img.shields.io/badge/Domain-Offensive%20Security-red?style=for-the-badge"> <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge"> <img src="https://img.shields.io/badge/Architecture-Modular-success?style=for-the-badge"> <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"> </p>
📌 Overview

RedScan is a modular offensive reconnaissance framework designed to automate initial information gathering during penetration testing, red team engagements, and security assessments.

The tool follows real-world reconnaissance methodology, clearly separating passive and active recon, while generating professional, human-readable and machine-readable reports.

RedScan is suitable for:

Penetration testers

Red teamers

Cybersecurity students

Internship & academic projects

Bug bounty reconnaissance

Open-source security tooling portfolios

🎯 Objectives

Automate domain & IP-based reconnaissance

Apply correct recon methodology (FQDN-aware DNS enumeration)

Provide a clean, modular, extensible architecture

Generate professional HTML & JSON reports

Serve as a foundation for advanced offensive tooling

✨ Features
🔍 Passive Reconnaissance

WHOIS enumeration (domain ownership & registration data)

DNS enumeration using authoritative FQDN:

A (IPv4) records

MX records (with mail server IP resolution)

NS records

Subdomain enumeration using Certificate Transparency (crt.sh)

Subdomain IP resolution (only valid & resolvable hosts)

⚡ Active Reconnaissance

Port scanning (Nmap-based)

Banner grabbing on identified open ports only

Web technology detection:

HTTP headers

TLS certificate Common Name (CN)

Reverse DNS (PTR) lookup for IP targets (contextual only)

📊 Reporting

HTML report

Dark mode

Non-technical friendly

Presentation-ready

JSON report

Structured

Automation-friendly

Timestamped scans

Target-wise report directories

No report overwrites

🧩 Architecture

Fully modular design

Independent recon modules

CLI-driven execution

Verbose logging support

Easy extensibility for new modules

🖥 Tool Banner
██████╗ ███████╗██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝█████╗  ██║  ██║███████╗██║     ███████║██╔██╗ ██║
██╔══██╗██╔══╝  ██║  ██║╚════██║██║     ██╔══██║██║╚██╗██║
██║  ██║███████╗██████╔╝███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
          MODULAR • RECONNAISSANCE • FRAMEWORK

📁 Project Structure
RedScan/
├── redscan.py
├── requirements.txt
├── README.md
├── modules/
│   ├── whois_mod.py
│   ├── dns_mod.py
│   ├── subdomain_mod.py
│   ├── portscan_mod.py
│   ├── banner_mod.py
│   └── techdetect_mod.py
├── utilities/
│   ├── logger.py
│   └── report.py
└── reports/

⚙️ Installation
Requirements

Python 3.8+

Nmap installed

Linux / Kali Linux recommended

Install Dependencies
pip3 install -r requirements.txt

🚀 Usage
Full Recon (Default)
python3 redscan.py -t example.com

Full Recon with Verbose Output
python3 redscan.py -t example.com -v

Selective Module Execution
python3 redscan.py -t example.com --dns --subdomains

IP Target Recon (with FQDN inference)
python3 redscan.py -t 142.250.202.238

⚙️ Command-Line Flags
Flag	Description
-t, --target	Target domain or IP address
-v	Enable verbose logging
--whois	WHOIS enumeration
--tech	Technology detection
--ports	Port scanning
--banners	Banner grabbing
--dns	DNS enumeration (via authoritative FQDN)
--subdomains	Subdomain enumeration
--all	Run all modules

Note:
If no module flags are provided, RedScan runs full reconnaissance by default.

📂 Output Structure
reports/
└── example.com/
    ├── recon_20260123_223015.html
    └── recon_latest.json


HTML → Human-readable, non-technical friendly

JSON → Automation & analysis friendly

🧠 Recon Methodology Highlights

DNS enumeration is always performed using an authoritative FQDN

PTR (reverse DNS) results are informational only

DNS records are never enumerated blindly on PTR hostnames

MX records include mail server IP resolution

Subdomains are filtered to resolvable, valid hosts only

🛡️ Legal Disclaimer

⚠️ RedScan is intended for educational and authorized security testing only.

You must have explicit permission before scanning any target.
The author(s) are not responsible for misuse of this tool.

👨‍💻 Author

TEAM DELTA

⭐ Support

If you find this project useful:

⭐ Star the repository

🍴 Fork it

🧠 Learn and improve it

🔴 RedScan — Scan Smart. Scan Red.
