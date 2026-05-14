# Architecture Documentation

## Core Components

---

### `core/finding.py`

Represents a single security finding produced by a module.

**Fields:**
- `module_id` — which module found it (e.g. "I1", "I2")
- `title` — name of the finding (e.g. "SSH Default Password")
- `severity` — criticality level: `critical`, `high`, `medium`, `low`, `info`
- `description` — what was found and why it is dangerous
- `recommendation` — how to fix it
- `evidence` — optional proof (banner, version info, etc.)

**Methods:**
- `to_dict()` — converts finding to dictionary for JSON/HTML reporting

---

### `core/target.py`

Represents the target system to be scanned.

**Fields:**
- `host` — target IP or hostname (e.g. "192.168.56.101")
- `ports` — list of ports to scan (default: 21, 22, 23, 80, 443, 8080, 8443)
- `timeout` — connection timeout in seconds (default: 5)

**Default ports and why:**
- 21 → FTP
- 22 → SSH
- 23 → Telnet
- 80 → HTTP
- 443 → HTTPS
- 8080 → alternative HTTP
- 8443 → alternative HTTPS

**Methods:**
- `to_dict()` — converts target to dictionary for reporting

**Validation (`__post_init__`):**
- Host cannot be empty
- Timeout must be at least 1 second

---

### `core/module_loader.py`

Dynamically loads all available scanner modules from the `modules/` directory.

**How it works:**
1. Iterates over folders inside `modules/`
2. Looks for a `module.py` file inside each folder
3. Imports it dynamically using `importlib`
4. Instantiates the `Module` class inside it
5. If a module fails to load, it is skipped and an error is printed

**Why dynamic loading:**
New modules can be added by simply creating a new folder — no changes needed in core code.

---

### `core/scanner.py`

Central component that orchestrates all modules and collects findings.

**Fields:**
- `target` — the Target object to scan
- `findings` — accumulated list of all Finding objects
- `loader` — ModuleLoader instance

**Methods:**

`run()` — main execution flow:
1. Loads all modules via ModuleLoader
2. Calls `run(target)` on each module
3. Extends findings list with results
4. Skips failed modules without stopping the scan

`summary()` — counts findings by severity level, used for report overview.

---

### `main.py`

Entry point of the application. Parses CLI arguments, initializes the scan, and saves the report.

**CLI Arguments:**
- `-t / --target` — target IP or hostname (required)
- `-p / --ports` — ports to scan (optional, overrides default)
- `--timeout` — connection timeout in seconds (optional, default: 5)
- `--report` — report format: `json`, `html`, or `both` (default: both)

**Usage examples:**
```bash
python main.py -t 192.168.56.101
python main.py -t 192.168.56.101 -p 22 80 443
python main.py -t 192.168.56.101 --timeout 10 --report json
```

**Execution flow:**
1. Parse CLI arguments
2. Create `Target` object
3. Initialize `Scanner` and run all modules
4. Print summary table to terminal
5. Save report in selected format

**`if __name__ == "__main__"` pattern:**
Ensures `main()` is only called when the file is run directly, not when imported.

---

### `requirements.txt`

Project dependencies with pinned versions to ensure reproducibility.

| Package | Version | Purpose |
|---|---|---|
| python-nmap | 0.7.1 | Nmap wrapper for port and service scanning (I2, I9) |
| paramiko | 3.4.0 | SSH connections for credential testing (I1) |
| requests | 2.31.0 | HTTP/HTTPS requests for web interface testing (I3) |
| pyyaml | 6.0.1 | Parsing config.yaml |
| jinja2 | 3.1.3 | HTML report rendering |

Install with:
```bash
pip install -r requirements.txt
```

---

### `config.yaml`

Central configuration file for the scanner. Controls module behavior, default ports, and reporting options.

**Sections:**

`scanner` — global scan settings:
- `timeout` — connection timeout in seconds
- `max_threads` — maximum parallel threads

`target.default_ports` — ports scanned when no `-p` argument is provided

`modules` — per-module settings:
- `enabled` — set to `false` to skip a module during scan
- `wordlist` — path to wordlist file (only for I1)

`reporting` — output directory and report formats

**Important:** When adding a new module, a corresponding entry must be added here with at least `enabled: true`.
