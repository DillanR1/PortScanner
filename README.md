# Python Port Scanner v2

A simple Python-based TCP port scanner that detects open ports on a host and grabs service banners.
This project serves as a baseline for learning networking, Python scripting, and structured data output.

---

## Features
- Scan specific ports on a target host (IP or hostname)
- Grab banners from open ports (service information)
- Output results in JSON and CSV formats
- Designed for learning networking and Python fundamentals

---

## How to Use

1. Run the script by typing:
python port_scanner.py

2. Enter target host. Safe options for testing:
- 127.0.0.1 or localhost (your own machine)
- VM lab IPs (e.g., 192.168.56.101)
⚠️ Do not scan external machines without permission

3. Enter ports to scan, comma-separated (e.g., 22,80,443)

4. View results:
- Open ports and banners are printed to the console
- JSON and CSV results are saved automatically in scans/ with timestamped filenames, for example:
scan_results_20250826_144501.json
scan_results_20250826_144501.csv

---

## What is Banner Grabbing?

Banner grabbing is the process of connecting to an open network port and retrieving a small piece of information about the service running there.

Examples:
- Port 22 might respond with SSH-2.0-OpenSSH_8.2
- Port 80 might respond with Apache/2.4.41 (Ubuntu)

This helps identify which services are active, which is useful for monitoring, auditing, or learning about networked systems.

---

## Why This Tool is Useful

**For technical users:**
- Quickly identify open network ports on a server or device
- Check which services are running (e.g., SSH, HTTP)
- Generate structured reports for monitoring or auditing

**For non-technical users:**
Think of your computer or network as a building, and each port as a door.
- Open doors allow communication with other computers
- Unknown open doors can be risky

This tool helps visualize which “doors” are open, making it easier to see potential risks and track network activity safely.

---

## Notes

- Only scan devices you own or have permission to scan
- The scans/ folder keeps your project organized and portfolio-ready
- Each scan produces a unique timestamped file to prevent overwriting previous results

---

## Portfolio Screenshot Tip

To safely show results:
- Scan `127.0.0.1` or a VM lab to avoid exposing real network info
- Open the CSV or JSON in a spreadsheet or text editor
- Highlight the open ports and banners, but **mask sensitive IPs** if needed
- Take a clean screenshot for GitHub or your portfolio

## Safe Demo Targets

When creating screenshots or demos for your portfolio:

- Always use devices you own or have permission to scan  
- Recommended safe targets:
  - `127.0.0.1` or `localhost` (your own machine)
  - Virtual machines in your lab environment (e.g., 192.168.56.x)
- Do **not** scan external networks or servers without explicit authorization
