# 🔴 RedScan — Offensive Reconnaissance Framework

<p align="center">
  <img src="https://img.shields.io/badge/Domain-Offensive%20Security-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Architecture-Modular-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge">
</p>

---

## 📌 Overview

**RedScan** is a **modular offensive reconnaissance framework** designed to automate **initial information gathering** during penetration testing, red team engagements, and security assessments.

The tool follows **real-world reconnaissance methodology**, clearly separating **passive and active recon**, while generating **professional, human-readable and machine-readable reports**.

RedScan is suitable for:

- Penetration testers  
- Red teamers  
- Cybersecurity students  
- Internship & academic projects  
- Bug bounty reconnaissance  
- Open-source security tooling portfolios  

---

## 🎯 Objectives

- Automate **domain & IP-based reconnaissance**
- Apply **correct recon methodology** (FQDN-aware DNS enumeration)
- Provide a **clean, modular, extensible architecture**
- Generate **professional HTML & JSON reports**
- Serve as a **foundation for advanced offensive tooling**

---

## ✨ Features

### 🔍 Passive Reconnaissance
- WHOIS enumeration
- DNS enumeration (A, MX, NS records)
- Subdomain enumeration using Certificate Transparency
- Subdomain IP resolution

### ⚡ Active Reconnaissance
- Port scanning (Nmap-based)
- Banner grabbing
- Technology detection (HTTP headers & TLS)

### 📊 Reporting
- HTML & JSON reports
- Timestamped scans
- Target-wise directories

---

## 🚀 Usage

```bash
python3 redscan.py -t example.com -v
```

---

## 🛡️ Legal Disclaimer

Use only on authorized targets.
