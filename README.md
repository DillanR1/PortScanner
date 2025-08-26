# Python Port Scanner (Baseline Project)

A simple Python-based TCP port scanner that detects open ports on a host and optionally grabs service banners.  
This project serves as a baseline for learning networking, Python scripting, and structured data output.

---

## Features
- Scan specific ports on a target host (IP or hostname)
- Grab banners from open ports (optional)
- Output results in JSON and CSV formats
- Designed for learning networking and Python fundamentals

---

## How to Use

1. **Run the script**
```bash
python port_scanner.py

```

2. Enter target host (IP or hostname): 192.168.1.1

3. Enter ports to scan (comma-separated, e.g., 22,80,443): 22,80,443

4. View results

Open ports will be printed in the console with any banner info

JSON and CSV files are saved automatically with timestamps, e.g.,

scan_results_20250825_143012.json
scan_results_20250825_143012.csv

Why This Tool is Useful -

For technical users:

-Quickly identify open network ports on a server or device
-Check which services are running (e.g., SSH, HTTP)
-Generate structured reports for monitoring or auditing

For non-technical users:

Think of it as checking which “doors” on a computer or network are open. Open doors can let computers communicate, but some might be risky if unknown.

This tool helps visualize and track those “doors” safely, making it easier to secure a system or network.
