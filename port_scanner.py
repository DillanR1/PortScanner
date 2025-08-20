# Step 1 - Import Libraries
import socket
import json


# Step 2 - Define Port Scanner
def scan_ports(host, ports):
    open_ports = []  # list to store ports that are open

    # Loop through each port we want to check
    for port in ports:
        try:
            # Create a socket (doorway) using IPv4 and TCP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Set a timeout so we don't wait too long on closed/unreachable ports
            s.settimeout(0.5)

            # Try connecting to the host on this port
            result = s.connect_ex((host, port))

            # If result is 0, the connection succeeded (port is open)
            if result == 0:
                open_ports.append(port)

            # Close the socket to free resources
            s.close()

        except Exception as e:
            # If anything goes wrong, print the error but keep scanning
            print(f"Error scanning port {port}: {e}")

    # Return the list of open ports
    return open_ports


# Step 3 - Interactive User Input
if __name__ == "__main__":
    # Ask the user for a host (could be "localhost", "google.com", or an IP like "192.168.1.1")
    target_host = input("Enter target host (IP or hostname): ")

    # Ask the user for ports to scan, typed as comma-separated values (e.g., 22,80,443)
    target_ports = input("Enter ports to scan (comma-separated, e.g., 20,22,80): ")

    # Convert that string into a list of integers
    # "22,80,443" → ["22","80","443"] → [22,80,443]
    port_list = [int(p.strip()) for p in target_ports.split(",")]

    # Tell the user scanning has started
    print(f"\nScanning {target_host}...")

    # Run the port scanner we built in Step 2
    open_ports = scan_ports(target_host, port_list)

    # Print the results to the console
    print(f"Open ports: {open_ports}")

    # Easter Egg for "→"
    # Press Ctrl+Shift+P → “Insert Unicode” → type 2192


# Step 4 - Output results to JSON
    # Create a Python dictionary to hold the results
    # Keys: "host" (string), "open_ports" (list of ints)

result_data = {
    "host": target_host,
    "open_ports": open_ports
}

# Open (or create) a file named "scan_results.json" in write mode
# "with" ensures the file closes automatically after writing

with open("scan_results.json", "w") as f:
   
    # Write the result_data dictionary into the file as JSON
    # indent=4 makes it pretty and easy for humans to read
   
    json.dump(result_data, f, indent=4)

# Let the user know where the results were saved

print("\nResults saved to scan_results.json (React-ready!)")

###DELETE ME LATER