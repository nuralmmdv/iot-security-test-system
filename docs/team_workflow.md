# Team Workflow

## 1. Project Overview

IoT Security Test System is a modular security scanning framework based on the OWASP IoT Top 10.
The goal is to automatically detect common security vulnerabilities in IoT devices and embedded systems
by analyzing their network-accessible attack surface.

Each team member is responsible for developing independent scanner modules.
All modules share the same core framework and produce standardized findings.

**Module assignments:**

| Module | Category | Owner |
|---|---|---|
| I1 | Weak/Guessable Passwords | Member A |
| I2 | Insecure Network Services | Member A |
| I9 | Insecure Default Settings | Member A |
| I3 | Insecure Ecosystem Interfaces | Member B |
| I5 | Use of Insecure/Outdated Components | Member B |
| I7 | Insecure Data Transfer & Storage | Member B |

---

## 2. Getting Started

```bash
# Clone the repository
git clone git@github.com:nuralmmdv/iot-security-test-system.git
cd iot-security-test-system

# Switch to develop branch
git checkout develop

# Install python3-venv if not available
sudo apt install python3.12-venv

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install nmap
sudo apt install nmap
```

---

## 3. Branch Strategy
```
main
└── develop
├── feature/i1_weak_passwords
├── feature/i2_network_services
├── feature/i3_ecosystem_interfaces
├── feature/i5_outdated_components
├── feature/i7_data_transfer
└── feature/i9_default_settings
```

**Rules:**
- Never push directly to `develop` or `main`
- Always branch from `develop`
- Always merge back to `develop` via Pull Request
- Delete branch after merge

**Creating a new branch:**
```bash
git checkout develop
git pull origin develop
git checkout -b feature/i3_ecosystem_interfaces
```

---

## 4. Commit Message Format
```
feat(i1): short description of what was added
fix(i3): short description of what was fixed
docs(readme): short description of what was updated
refactor(i5): short description of what was restructured
test(i7): short description of what was tested
```
---

## 5. Module Development Guide

Each module lives in its own folder under `modules/` and must contain a `module.py` file.

**Module structure:**

```python
from typing import List
from core.target import Target
from core.finding import Finding


class Module:
    ID = "I1"
    NAME = "Weak/Guessable Passwords"

    def run(self, target: Target) -> List[Finding]:
        findings = []

        # your scanning logic here

        findings.append(Finding(
            module_id=self.ID,
            title="Example Finding Title",
            severity="high",
            description="What was found and why it is dangerous.",
            recommendation="How to fix it.",
            evidence="Optional proof — banner, version, response snippet."
        ))

        return findings
```

**Severity levels:** `critical` / `high` / `medium` / `low` / `info`

**Important:**
- Class name must be `Module`
- `run()` must return a `List[Finding]`
- If nothing is found, return an empty list `[]`
- Do not print inside modules — return findings only

---

## 6. Pull Request Rules

- One module per PR
- PR title must follow commit format: `feat(i3): ecosystem interfaces module`
- Base branch must be `develop`
- Make sure the module runs without errors before opening PR
- Delete branch after merge
