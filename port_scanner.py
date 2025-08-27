# Python Port Scanner v2
import socket
import json
import csv
import os
from datetime import datetime

# -----------------------------
# Function: Scan ports and grab banners
# -----------------------------
def scan_ports_with_banners(host, ports):
    """
    Scan a list of ports on a given host.
    For each open port, attempt to grab a banner (service info).
    Returns a list of dictionaries: [{"port": 22, "banner": "SSH-2.0-OpenSSH_8.2"}, ...]
    """
    results = []  # Store each port's result here

    for port in ports:
        try:
            # Create socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((host, port))

            # If connection succeeds
            if result == 0:
                try:
                    # Sending a newline can sometimes trigger a banner
                    s.sendall(b"\n")
                    banner = s.recv(1024).decode().strip()
                    if not banner:
                        banner = "No banner"
                except:
                    banner = "No banner"

                results.append({"port": port, "banner": banner})

            s.close()

        except Exception as e:
            print(f"Error scanning port {port}: {e}")

    return results

# -----------------------------
# Main program
# -----------------------------
if __name__ == "__main__":
    target_host = input("Enter target host (IP or hostname): ")
    target_ports = input("Enter ports to scan (comma-separated, e.g., 22,80,443): ")
    port_list = [int(p.strip()) for p in target_ports.split(",")]

    print(f"\nScanning {target_host}...")
    scan_results = scan_ports_with_banners(target_host, port_list)

    # Print results to console
    if scan_results:
        for r in scan_results:
            print(f"Port {r['port']} open -> {r['banner']}")
    else:
        print("No open ports found.")

    # -----------------------------
    # Prepare scans folder
    # -----------------------------
    scans_folder = os.path.join(os.path.dirname(__file__), "scans")
    os.makedirs(scans_folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # -----------------------------
    # Save JSON
    # -----------------------------
    json_file = os.path.join(scans_folder, f"scan_results_{timestamp}.json")
    with open(json_file, "w") as f:
        json.dump({"host": target_host, "results": scan_results}, f, indent=4)

    # -----------------------------
    # Save CSV
    # -----------------------------
    csv_file = os.path.join(scans_folder, f"scan_results_{timestamp}.csv")
    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["port", "banner"])
        writer.writeheader()
        writer.writerows(scan_results)

    print(f"\nResults saved as:\nJSON → {json_file}\nCSV  → {csv_file}")
