# 🛰️ NetScanX

**NetScanX** is a terminal-based network scanner written in Python using [Scapy](https://scapy.net/) and [Rich](https://github.com/Textualize/rich). It allows you to quickly scan your local network and identify active devices using ARP requests. Designed for ethical hackers, cybersecurity students, network administrators, and anyone curious about what's on their LAN.

---

## 📌 Features

- ⚡ **Fast ARP-based network scanning**
- 🖥️ **Displays IP and MAC addresses** of live hosts
- 🌐 **Auto-detect or manually select** active network interface
- 🎨 **Rich, colorful terminal output** using `rich`
- 💾 **Save scan results** to a file (`netscanx_results.txt`)
- ✅ Lightweight, clean CLI with no unnecessary dependencies

---

##  Demo

<pre>
$ netscanx

📡 NetScanX - Smart Network Scanner

Enter IP range (default 192.168.1.1/24): 
Available Interfaces:
[0] eth0
[1] wlan0
Select interface number (Enter to auto-select): 0

⏳ Scanning 192.168.1.1/24...
📡 Devices Found:

┌─────┬───────────────┬──────────────────────┐
│ S.No│ IP Address    │ MAC Address          │
├─────┼───────────────┼──────────────────────┤
│ 1   │ 192.168.1.1   │ fc:40:09:f8:29:5b     │
│ 2   │ 192.168.1.100 │ 08:00:27:15:3a:9e     │
└─────┴───────────────┴──────────────────────┘

✅ Results saved to: netscanx_results.txt </pre>

Clone and Installation
<pre>
  git clone https://github.com/PULSAR-002/netscanx.git
  cd netscanx
  pip install .

</pre>
## Install the requirements in virtual environment (recommended)
<pre>
  pip install -r requirements.txt

</pre>
⚠️ Make sure you're using Python 3 (recommended: 3.8 or above)

## Basic Usage
<pre>
  sudo netscanx
</pre>
