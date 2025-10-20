# Tutorial: Mastering the Port Scanner with Banner Grabbing and CVE Hints

Welcome to this hands-on tutorial for the Port Scanner with Banner Grabbing and CVE Hints! This Python tool is designed for educational exploration, scanning target hosts, capturing service banners, and suggesting CVEs (like CVE-2023-44487 for HTTP/2 Rapid Reset). With threaded speed and colorful output, it’s perfect for learning networking and coding skills. Let’s get started—safely and legally!

## Demo
Here's the port scanner in action!:

<image-card alt="Port Scanner Demo" src="https://raw.githubusercontent.com/DillanR1/PortScanner/main/assets/Portscanner-Action.gif" ></image-card>

## What You’ll Learn
- How to set up your environment for the port scanner.
- How to install and configure the tool for use.
- How to run scans with different options and interpret results.
- How to explore suggested ports and targets for practice.

## Step 1: Getting to Know the Port Scanner
This is a threaded Python script that scans multiple ports concurrently, grabs banners from open ports (e.g., HTTP/HTTPS, SSH), and hints at CVEs. It saves results to timestamped JSON and CSV files in a `scans/` folder, with green for open ports, red for closed, and yellow for CVE alerts. Use it only on authorized targets to stay out of trouble.

## Step 2: Preparing Your Environment
Let’s ensure everything is ready before diving in.

### Prerequisites
- **Python 3.x**: Check your version with
    ```python3 --version``` or ```python3 -v```
- **Dependencies**: Install these packages using
    ```pip3 install requests termcolor```
- **Operating System**: Compatible with Linux (tested in WSL Ubuntu), Windows, or macOS.
- **Permissions**: Ensure network access (no root needed for public targets).

## Step 3: Setting Up the Project
Get the code and dependencies in place.

### Clone the Repository
Start by cloning the project to your machine:
    ```git clone https://github.com/yourusername/PortScanner.git```
    cd PortScanner

### Install Dependencies
Set up the required libraries:
    ```pip3 install -r requirements.txt```
(Note: Create a `requirements.txt` file with `requests` and `termcolor` if it’s missing.)

## Step 4: Running the Port Scanner
Learn to execute the tool with various configurations.

### Running from Any Directory
**Direct Execution**:
Navigate to the script or use the full path:
    ```python3 /path/to/port_scanner.py --target scanme.nmap.org --ports 22,80,443```
(Replace the path, e.g., ~/projects/PortScanner/.)

**Configure as an Alias** (for easier access):
Add this line to your shell config file (e.g., ~/.zshrc or ~/.bashrc):
    ```alias portscanner="python3 /home/youruser/projects/PortScanner/port_scanner.py"```
Reload your shell:
    ```source ~/.zshrc  # or source ~/.bashrc```

### Command Syntax
Use this structure to run the scanner:
    ```portscanner --target <hostname_or_ip> --ports <port1,port2,...> [--retries <n>] [--timeout <sec>]```
- **Required Arguments**:
  - `--target`: The host to scan (e.g., scanme.nmap.org, 127.0.0.1).
  - `--ports`: A comma-separated list of ports (e.g., 22,80,443—no ranges).
- **Optional Arguments**:
  - `--retries`: Number of retry attempts per port (default: 2).
  - `--timeout`: Timeout in seconds per port (default: 1.0).

### Example Commands
Try these to see it in action:
- Basic scan of common ports:
    ```portscanner --target scanme.nmap.org --ports 22,80,443``` - This is the default behavior of ```portscanner``` with no arguments
- Wide scan with unique ports and settings:
    ```portscanner --target scanme.nmap.org --ports 21,22,23,25,37,42,53,69,80,110,143,443,666,1024,1337,1984,2600,31337,4444,9929,12345 --retries 3 --timeout 2```

## Step 5: Exploring Suggested Ports
Practice with these ports, each with a story or significance:

| Port  | Service/Tie-In                       |
|-------|--------------------------------------|
| 21    | FTP (old-school hack target)         |
| 22    | SSH (modern secure shell)            |
| 23    | Telnet (vintage vuln magnet)         |
| 25    | SMTP (email relay, spam vector)      |
| 37    | Time protocol (syncing easter egg)   |
| 42    | WINS (Hitchhiker’s “Answer to Life”) |
| 53    | DNS (spoofing playground)            |
| 69    | TFTP (meme “nice” number)            |
| 80    | HTTP (web exploit central)           |
| 110   | POP3 (email retrieval)               |
| 143   | IMAP (email access)                  |
| 443   | HTTPS (secure web, MitM target)      |
| 666   | DOOM/trojans (devilish vibe)         |
| 1024  | Reserved (often dynamic)             |
| 1337  | Leet speak (hacker elite)            |
| 1984  | Big Brother reference                |
| 2600  | Phreaking magazine port              |
| 31337 | Back Orifice (leet easter egg)       |
| 4444  | Metasploit default (four deaths)     |
| 9929  | Nping echo (Nmap test port)          |
| 12345 | NetBus trojan (backdoor classic)     |

### Suggested Targets
- **scanme.nmap.org**: Nmap’s test host (ports 22, 80, 9929, 31337 active as of Oct 2025).
- **localhost (127.0.0.1)**: Test your own services.
- **testmyports.org**: A legal target with open ports.

## Step 6: Analyzing the Output
Understand what the scanner shows you.

- **Console Output**: See real-time results with colors.
  Example:
    ```Port 80: open -> Server: Apache/2.4.7 (Ubuntu) (Check for CVE-2021-41773)
    Port 443: closed -> Closed```
- **File Output**: Results are saved in `scans/` with timestamps (e.g., scan_results_20251019_2140XX.json, scan_results_20251019_2140XX.csv).
  - JSON includes host, port details, banners, and CVE hints.
  - CSV mirrors the JSON for spreadsheet use.

## Step 7: Safety and Legal Notes
> **Disclaimer:** This tool is for educational fun only. Scanning unauthorized networks (e.g., work servers or neighbors’ routers) can lead to legal trouble. Stick to suggested targets to avoid issues.

## Step 8: Enhancing and Contributing
- Fork the repo, add features like more CVE checks, or optimize threading, then submit a pull request.
- Consider adding a GUI or improving banner grabbing.
- Share your progress and learnings!

## License
MIT—free to use, modify, and share, but no warranty. Scan at your own risk!
