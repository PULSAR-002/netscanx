from setuptools import setup, find_packages

setup(
    name="netscanx",
    version="0.1",
    description="A terminal-based ARP scanner by PULSAR",
    author="PULSAR",
    packages=find_packages(),
    install_requires=["scapy", "rich"],
    entry_points={
        "console_scripts": [
            "netscanx=netscanx.scanner:run"
        ]
    }
)
