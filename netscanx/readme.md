# 🛰️ NetScanX

**NetScanX** is a terminal-based network scanner written in Python using Scapy. It scans your local network, lists all live hosts, and displays their IP and MAC addresses in a readable format.

## ✨ Features

- Terminal-based ARP scanning
- Interface selection
- Saves results to file
- Rich CLI output

## 🔧 Installation

<pre>
git clone https://github.com/PULSAR-002/netscanx.git
cd netscanx
pip install . </pre>

⚠️ You may need to run the terminal with administrator/root privileges to use netscanx, as it sends ARP packets.
## Usage:
<pre>
  netscanx
  Enter the target IP range (e.g., 192.168.0.1/24) or press Enter for default.
  Select a network interface when prompted, or press Enter for auto-detection.
  Scan starts — all active devices will be listed with their IP and MAC.
  Scan results are saved to a file named netscanx_results.txt.
</pre>
