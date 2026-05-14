# IoT Security Test System

A modular security scanning framework based on the OWASP IoT Top 10.
Designed to identify common security vulnerabilities in IoT devices and embedded systems
by analyzing their network-accessible attack surface.

---

## Features

- Modular architecture — each OWASP item is an independent module
- Automatic module discovery — drop a module in, it runs automatically
- Multiple report formats — JSON and HTML output
- Configurable — targets, ports, timeout and modules via `config.yaml`
- CLI interface — simple and scriptable

---

## OWASP IoT Top 10 Coverage

| ID | Category | Status | 
|---|---|---|
| I1 | Weak/Guessable Passwords | 🔄 In Progress |
| I2 | Insecure Network Services | 🔄 In Progress |
| I3 | Insecure Ecosystem Interfaces | 🔄 In Progress |
| I5 | Use of Insecure/Outdated Components | 🔄 In Progress |
| I7 | Insecure Data Transfer & Storage | 🔄 In Progress |
| I9 | Insecure Default Settings | 🔄 In Progress |

---

## Architecture

```
iot-security-test-system/
│
├── core/
│   ├── finding.py          # Finding data structure
│   ├── target.py           # Target data structure  
│   ├── scanner.py          # Main scan orchestrator
│   └── module_loader.py    # Dynamic module loader
│
├── modules/
│   ├── i1_weak_passwords/
│   ├── i2_insecure_network_services/
│   ├── i3_insecure_ecosystem_interfaces/
│   ├── i5_outdated_components/
│   ├── i7_insecure_data_transfer_storage/
│   └── i9_insecure_default_settings/
│
├── reports/
│   ├── json_report.py
│   └── html_report.py
│
├── docs/
│   ├── architecture.md
│   ├── owasp_iot_mapping.md
│   └── team_workflow.md
│
├── main.py
├── config.yaml
└── requirements.txt
```
---

## Installation

```bash
# Clone the repository
git clone git@github.com:nuralmmdv/iot-security-test-system.git
cd iot-security-test-system

# Install dependencies
pip install -r requirements.txt

# Install nmap (required for network scanning)
sudo apt install nmap
```

---

## Usage

```bash
# Basic scan
python main.py -t 192.168.56.101

# Scan with custom ports
python main.py -t 192.168.56.101 -p 22 80 443

# Scan with custom timeout
python main.py -t 192.168.56.101 --timeout 10

# JSON report only
python main.py -t 192.168.56.101 --report json

# HTML report only
python main.py -t 192.168.56.101 --report html
```

---

## Project Structure

| Path | Description |
|---|---|
| `core/` | Framework core — scanner, loader, data structures |
| `modules/` | OWASP IoT Top 10 scanner modules |
| `reports/` | Report generators (JSON, HTML) |
| `docs/` | Project documentation |
| `main.py` | Entry point |
| `config.yaml` | Configuration file |
| `requirements.txt` | Python dependencies |
