# netscanx/scanner.py

import scapy.all as scapy
from scapy.all import get_if_list, conf
from rich.console import Console
from rich.table import Table
import time

console = Console()

def get_ip_range():
    default = "192.168.1.1/24"
    user_ip = input(f"Enter IP range (default {default}): ").strip()
    return user_ip if user_ip else default

def choose_interface():
    interfaces = get_if_list()
    console.print("[bold cyan]Available Interfaces:[/]")
    for i, iface in enumerate(interfaces):
        console.print(f"[green]{i}[/]: {iface}")
    try:
        idx = int(input("Select interface number (Enter to auto-select): "))
        conf.iface = interfaces[idx]
    except:
        conf.iface = scapy.get_working_if()
    console.print(f"[bold yellow]Using interface:[/] {conf.iface}")

def scan(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    console.print(f"🔍 Scanning network {ip_range}...")
    answered = scapy.srp(packet, timeout=3, verbose=False)[0]

    results = []
    for _, recv in answered:
        results.append({"ip": recv.psrc, "mac": recv.hwsrc})
    return results

def display_results(devices):
    if not devices:
        console.print("[red]No devices found.[/]")
        return

    table = Table(title="📡 Devices Found")
    table.add_column("S.No", justify="right")
    table.add_column("IP Address", style="cyan")
    table.add_column("MAC Address", style="magenta")

    for i, d in enumerate(devices, 1):
        table.add_row(str(i), d["ip"], d["mac"])
    console.print(table)

def save_to_file(devices, filename="netscanx_results.txt"):
    with open(filename, "w") as f:
        for d in devices:
            f.write(f"{d['ip']} - {d['mac']}\n")
    console.print(f"💾 Results saved to: [green]{filename}[/]")

def run():
    console.print("[bold blue]NetScanX - Smart Network Scanner[/]\n")
    ip_range = get_ip_range()
    choose_interface()

    start = time.time()
    results = scan(ip_range)
    end = time.time()

    display_results(results)
    save_to_file(results)
    console.print(f"\n⏱️ Scan finished in {round(end - start, 2)} seconds.")
