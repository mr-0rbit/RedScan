# 🔴 RedScan — Offensive Reconnaissance Tool

## 📌 Overview

**RedScan** is a lightweight, modular **offensive reconnaissance tool** developed in Python to automate **initial information gathering** during penetration testing and red team engagements.

The tool is designed for:
- Cybersecurity internships
- Academic & Final Year Projects (FYP)
- Bug bounty reconnaissance
- Red team initial access phase
- Learning offensive security tooling

RedScan follows real-world offensive security practices with a clean CLI interface and professional reporting.

---

## ✨ Features

### 🔍 Passive Reconnaissance
- WHOIS lookup
- DNS enumeration:
  - A records
  - MX records
  - TXT records
  - NS records
- Subdomain enumeration using **crt.sh**

### ⚡ Active Reconnaissance
- Port scanning (Nmap wrapper)
- IP address resolution
- Modular design for future expansion

### 📊 Reporting
- **HTML report** (human-readable)
- **JSON report** (machine-readable)
- Timestamped scan results
- Target-based output directories

---

## 🖥️ Tool Banner

```text
██████╗ ███████╗██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝█████╗  ██║  ██║███████╗██║     ███████║██╔██╗ ██║
██╔══██╗██╔══╝  ██║  ██║╚════██║██║     ██╔══██║██║╚██╗██║
██║  ██║███████╗██████╔╝███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
        Offensive Reconnaissance Framework
```

---

## 📁 Project Structure

```bash
RedScan/
├── redscan.py
├── requirements.txt
├── README.md
├── modules/
│   ├── whois_lookup.py
│   ├── dns_enum.py
│   ├── subdomain_enum.py
│   └── port_scan.py
├── utils/
│   ├── logger.py
│   └── helpers.py
├── report/
│   └── report_generator.py
└── output/
```

---

## ⚙️ Installation

### Requirements
- Python 3.8+
- Nmap installed
- Linux / Kali Linux recommended

### Install Dependencies
```bash
pip3 install -r requirements.txt
```

---

## 🚀 Usage

### Basic Run
```bash
python3 redscan.py example.com
```

### Full Recon with Report
```bash
python3 redscan.py example.com \
  --whois \
  --dns \
  --subdomains \
  --ports \
  --report \
  -v
```

### Command-Line Options

| Option | Description |
|------|------------|
| `--whois` | WHOIS lookup |
| `--dns` | DNS enumeration |
| `--subdomains` | Subdomain enumeration |
| `--ports` | Port scanning |
| `--report` | Generate HTML & JSON reports |
| `-v` | Verbose logging |

---

## 📂 Output

```bash
output/
└── example.com/
    ├── report.html
    └── report.json
```

- `report.html` → For documentation & presentation
- `report.json` → For automation & further analysis

---

## 🛡️ Legal Disclaimer

⚠️ **RedScan is intended for educational and authorized security testing only.**

You must have **explicit permission** before scanning any target.  
The author is **not responsible for misuse** of this tool.

---

## 👨‍💻 Author

**Muhammad Hamza Zahid**  
Cybersecurity | Offensive Security  

---

## ⭐ Support

If you find this project useful:
- ⭐ Star the repository
- 🍴 Fork it
- 🧠 Learn and improve it

---

### 🔴 RedScan — Scan Smart. Scan Red.
