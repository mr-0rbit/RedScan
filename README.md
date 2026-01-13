# 🔴 RedScan — Offensive Reconnaissance Framework

<p align="center">
  <img src="https://img.shields.io/badge/Domain-Offensive%20Security-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Architecture-Modular-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge">
</p>

---

## 📌 Overview

**RedScan** is a **lightweight, modular offensive reconnaissance framework** designed to automate **initial information gathering** during penetration testing and red team engagements.

It is built with **real-world offensive security practices** in mind and is suitable for:

- Penetration testers
- Red teamers
- Cybersecurity students
- Internship & academic projects
- Bug bounty reconnaissance
- Open-source security tooling portfolios

RedScan emphasizes **clean code, extensibility, CLI-driven execution, and professional reporting**.

---

## 🎯 Objectives

- Automate **passive and active reconnaissance**
- Provide a **modular & extensible architecture**
- Generate **professional reports** for documentation and automation
- Serve as a **foundation for advanced offensive security tooling**

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
- Clean separation of recon modules

### 📊 Reporting
- **HTML report** (human-readable, presentation-ready)
- **JSON report** (machine-readable, automation-friendly)
- Timestamped scans
- Target-wise organized output

### 🧩 Architecture
- Modular design
- Independent recon modules
- CLI flags for feature control
- Verbose logging support

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
