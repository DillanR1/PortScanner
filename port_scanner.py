#!/usr/bin/env python3

# Python Port Scanner v3

import socket
import json
import csv
import os
from datetime import datetime
import requests
from termcolor import colored
import time
from concurrent.futures import ThreadPoolExecutor
import argparse

# -----------------------------
# Function: Scan a single port
# -----------------------------

def scan_single_port(host, port, timeout, retries):
    for attempt in range(retries):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            banner = "No banner"
            vuln_hint = ""
            if result == 0:
                if port in [80, 443]:
                    try:
                        proto = "https" if port == 443 else "http"
                        url = f"{proto}://{host}"
                        response = requests.get(url, timeout=timeout)
                        server = response.headers.get("Server", "Unknown")
                        powered_by = response.headers.get("X-Powered-By", "")
                        banner = f"Server: {server}"
                        if powered_by:
                            banner += f" | X-Powered-By: {powered_by}"
                        if "Apache" in server:
                            vuln_hint = "Check for CVE-2021-41773 (Apache 2.4.x)"
                        elif "nginx" in server:
                            vuln_hint = "Check for CVE-2023-44487 (HTTP/2 Rapid Reset)"
                    except requests.RequestException:
                        banner = "HTTP/HTTPS - No response"
                else:
                    try:
                        time.sleep(0.1)
                        banner = s.recv(1024).decode().strip()
                        if not banner:
                            banner = "No banner"
                        if "SSH" in banner:
                            vuln_hint = "Check for CVE-2023-38408 (OpenSSH < 9.3)"
                    except:
                        banner = "No banner"
                s.close()
                return {"port": port, "banner": banner, "vulnerability_hint": vuln_hint}
            else:
                s.close()
                return {"port": port, "banner": "Closed", "vulnerability_hint": ""}
        except Exception as e:
            if attempt == retries - 1:
                print(colored(f"Error scanning port {port} after {retries} attempts: {e}", "red"))
            s.close()
            time.sleep(0.2)
        finally:
            s.close()
    return {"port": port, "banner": "Error", "vulnerability_hint": ""}

# -----------------------------
# Function: Scan ports with threading
# -----------------------------

def scan_ports_with_banners(host, ports, retries=2, timeout=1.0):
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_port = {executor.submit(scan_single_port, host, port, timeout, retries) :port for port in ports}
        for future in future_to_port:
            results.append(future.result())
    return sorted(results, key=lambda x: x["port"])


# -----------------------------
# Main program
# -----------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port scanner with banner grabbing")
    parser.add_argument("--target", default="localhost", help="Target host (IP or hostname)")
    parser.add_argument("--ports", default="22,80,443", help="Comma-separated ports (e.g., 22,80,443)")
    parser.add_argument("--retries", type=int, default=2, help="Number of retries per port")
    parser.add_argument("--timeout", type=float, default=1.0, help="Timeout per port in seconds")
    args = parser.parse_args()

    target_host = args.target
    port_list = [int(p.strip()) for p in args.ports.split(",")]

    print(f"\nScanning {target_host}...")
    scan_results = scan_ports_with_banners(target_host, port_list, args.retries, args.timeout)

# -----------------------------
# Save results
# -----------------------------

scans_folder = os.path.join(os.path.dirname(__file__), "scans")
os.makedirs(scans_folder, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
json_file = os.path.join(scans_folder, f"scan_results_{timestamp}.json")
csv_file = os.path.join(scans_folder, f"scan_results_{timestamp}.csv")
try:
    with open(json_file, "w") as f:
        json.dump({"host": target_host, "results": scan_results}, f, indent=4)
    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["port", "banner", "vulnerability_hint"])
        writer.writeheader()
        writer.writerows(scan_results)
    print(f"\nResults saved as:\nJSON → {os.path.basename(json_file)}\nCSV  → {os.path.basename(csv_file)}")
except Exception as e:
    print(f"Error saving results: {e}")

# -----------------------------
# Print results
# -----------------------------


if scan_results:
    for r in scan_results:
        status = "open" if "Closed" not in r["banner"] else "closed"
        color = "green" if status == "open" else "red"
        output = f"Port {r['port']}: {status} -> {r['banner']}"
        print(colored(output, color, force_color=True), end="")
        if r["vulnerability_hint"]:
            print(colored(f" ({r['vulnerability_hint']})", "yellow", force_color=True), end="")
        print() 
else:
    print(colored("No open ports found.", "cyan", force_color=True))