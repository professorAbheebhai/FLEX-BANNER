#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PROFESSOR ULTIMATE v4.0
Advanced Penetration Testing Simulation Suite
FOR EDUCATIONAL PURPOSES ONLY - All actions are simulated.
"""

import time
import sys
import random
import os
import platform
import threading
from datetime import datetime

# ========================== CONFIGURATION ==========================
CHANNEL_LINK = "https://whatsapp.com/channel/0029Vb7FZ4lBPzjb8g1Tux3l"
VERSION = "4.0.0"
AUTHOR = "PROFESSOR TEAM"
STEALTH_MODE = False  # Toggle for extra "stealth" logs

# Fake exploit database
EXPLOITS = [
    {"id": "CVE-2024-1234", "name": "WhatsApp RCE", "risk": "Critical"},
    {"id": "CVE-2024-5678", "name": "SQL Injection (Blind)", "risk": "High"},
    {"id": "CVE-2023-9876", "name": "Privilege Escalation", "risk": "Medium"},
    {"id": "CVE-2024-4321", "name": "XSS via Media", "risk": "High"},
    {"id": "CVE-2025-0001", "name": "Zero‑Day Auth Bypass", "risk": "Critical"},
]

# Fake target database
TARGET_DB = [
    {"name": "Alpha Corp", "members": 8542, "risk": 92, "country": "US"},
    {"name": "Beta Group", "members": 3120, "risk": 78, "country": "UK"},
    {"name": "Gamma LLC", "members": 12450, "risk": 95, "country": "DE"},
    {"name": "Delta Systems", "members": 567, "risk": 45, "country": "IN"},
    {"name": "Epsilon Network", "members": 22300, "risk": 99, "country": "RU"},
    {"name": "Zeta Corp", "members": 7800, "risk": 88, "country": "CN"},
]

# ========================== UTILITY FUNCTIONS ==========================
def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def type_writer(text, delay=0.02, color="\033[1;37m", end="\n"):
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m" + end)

def progress_bar(current, total, bar_len=50, color="\033[1;31m", prefix=""):
    frac = current / total
    filled = int(bar_len * frac)
    bar = "█" * filled + "░" * (bar_len - filled)
    percent = int(frac * 100)
    sys.stdout.write(f"\r{color}{prefix} |{bar}| {percent}%")
    sys.stdout.flush()

def random_delay(min_sec=0.1, max_sec=0.5):
    time.sleep(random.uniform(min_sec, max_sec))

def generate_log_entry():
    actions = [
        "Parsing packet #{}",
        "Extracting header from {}",
        "Decrypting payload (AES-256)",
        "Bypassing rate limit",
        "Fuzzing endpoint /api/{}",
        "Injecting SQL payload '{}'",
        "Enumerating user accounts",
        "Cracking hash (SHA-256)",
        "Establishing reverse shell",
        "Uploading backdoor",
        "Clearing event logs",
        "Spawning interactive shell",
        "Dropping rootkit",
        "Escalating privileges via {}",
        "Exfiltrating data ({} bytes)",
    ]
    action = random.choice(actions)
    if "{}" in action:
        if "packet" in action:
            val = random.randint(1000, 9999)
        elif "api" in action:
            val = random.choice(["users", "login", "admin", "config"])
        elif "SQL" in action:
            val = random.choice(["admin'--", "1' OR '1'='1", "' UNION SELECT NULL--"])
        elif "Escalating" in action:
            val = random.choice(["CVE-2024-1234", "CVE-2023-9876", "kernel exploit"])
        elif "Exfiltrating" in action:
            val = random.randint(1024, 1048576)
        else:
            val = random.randint(1, 999)
        return action.format(val)
    return action

def get_timestamp():
    return datetime.now().strftime("%H:%M:%S")

def stealth_log(msg):
    if STEALTH_MODE:
        # In stealth, show less obvious messages
        pass
    else:
        type_writer(f"[{get_timestamp()}] {msg}", color="\033[1;37m")

# ========================== BANNER ==========================
def show_banner():
    clear()
    print("\033[1;31m")
    print(" ██████╗ ██████╗  ██████╗ ███████╗███████╗███████╗███████╗ ██████╗ ██████╗ ")
    print(" ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔═══██╗██╔══██╗")
    print(" ██████╔╝██████╔╝██║   ██║█████╗  ███████╗███████╗█████╗  ██║   ██║██████╔╝")
    print(" ██╔═══╝ ██╔══██╗██║   ██║██╔══╝  ╚════██║╚════██║██╔══╝  ██║   ██║██╔══██╗")
    print(" ██║     ██║  ██║╚██████╔╝██║     ███████║███████║███████╗╚██████╔╝██║  ██║")
    print(" ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝")
    print("\033[1;33m" + " " * 15 + f">>> PROFESSOR ULTIMATE v{VERSION} <<<")
    print("\033[1;36m" + "─" * 75)
    print(f" 🔗 CHANNEL : {CHANNEL_LINK}")
    print(f" 📅 SESSION : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f" 👤 AUTHOR  : {AUTHOR}")
    print(f" 🛡️  STEALTH : {'ON' if STEALTH_MODE else 'OFF'}")
    print("─" * 75 + "\033[0m")

# ========================== MODULE 1: RECON ==========================
def module_recon():
    show_banner()
    target = input("\n[?] Enter target (link or name): ")
    if not target:
        target = "unknown_target"
    type_writer(f"\n[🔍] Starting reconnaissance on {target}...", color="\033[1;34m")
    random_delay(0.5, 1.0)
    # Simulate scanning
    for i in range(1, 101):
        progress_bar(i, 100, prefix="Recon progress")
        time.sleep(random.uniform(0.01, 0.03))
    print()
    type_writer("\n[📊] Recon results:", color="\033[1;33m")
    # Generate fake data
    ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
    os_type = random.choice(["Android", "iOS", "Windows", "Linux", "macOS"])
    open_ports = random.sample([80, 443, 22, 3389, 8080, 53, 21], k=random.randint(2,5))
    services = [f"port {p} open" for p in open_ports]
    type_writer(f"   ├─ IP Address      : {ip}", color="\033[1;37m")
    type_writer(f"   ├─ OS Detection    : {os_type}", color="\033[1;37m")
    type_writer(f"   ├─ Open Ports      : {', '.join(map(str, open_ports))}", color="\033[1;37m")
    type_writer(f"   ├─ Services        : {', '.join(services)}", color="\033[1;37m")
    type_writer(f"   └─ Vulnerabilities : {random.randint(0,5)} found", color="\033[1;37m")
    # Display some CVEs
    if random.choice([True, False]):
        type_writer("\n[⚠️] Potential exploits:", color="\033[1;31m")
        for _ in range(random.randint(1,3)):
            exp = random.choice(EXPLOITS)
            type_writer(f"      - {exp['id']} ({exp['name']}) - {exp['risk']}", color="\033[1;33m")
    input("\nPress Enter to continue...")

# ========================== MODULE 2: MULTI TARGET ==========================
def module_multi_target():
    show_banner()
    type_writer("[🌐] Multi‑Target Attack Mode", color="\033[1;34m")
    type_writer("Available targets in database:\n", color="\033[1;37m")
    for i, t in enumerate(TARGET_DB):
        print(f"   {i+1}. {t['name']} ({t['members']} members, risk {t['risk']}%, {t['country']})")
    print()
    choice = input("Select target number (or 0 for random): ")
    try:
        idx = int(choice) - 1
        if idx < 0 or idx >= len(TARGET_DB):
            target = random.choice(TARGET_DB)
        else:
            target = TARGET_DB[idx]
    except:
        target = random.choice(TARGET_DB)
    type_writer(f"\n[🎯] Attacking: {target['name']}", color="\033[1;31m")
    # Simulate attack on that target with phases
    phases = ["Recon", "Exploitation", "Post‑Exploitation", "Cleanup"]
    for phase in phases:
        type_writer(f"\n[⚡] Phase: {phase}", color="\033[1;33m")
        for step in range(random.randint(5,10)):
            log = generate_log_entry()
            type_writer(f"    ↳ {log}", delay=0.015, color="\033[1;37m")
            random_delay(0.1, 0.3)
        # Fake progress
        for p in range(1, 101):
            progress_bar(p, 100, prefix=f"{phase}")
            time.sleep(random.uniform(0.001, 0.005))
        print()
    type_writer("\n[💀] Target fully compromised!", color="\033[1;31m")
    type_writer(f"[✓] Data extracted: {random.randint(500,5000)} records", color="\033[1;32m")
    input("\nPress Enter to continue...")

# ========================== MODULE 3: NETWORK SCANNER ==========================
def module_network_scanner():
    show_banner()
    subnet = input("[?] Enter subnet (e.g., 192.168.1.0/24): ") or "192.168.1.0/24"
    type_writer(f"\n[🔍] Scanning {subnet}...", color="\033[1;34m")
    total = random.randint(200, 254)
    for i in range(1, total+1):
        progress_bar(i, total, prefix="Scanning hosts")
        time.sleep(random.uniform(0.001, 0.004))
    print()
    active = random.randint(5, 20)
    type_writer(f"\n[✓] Found {active} active hosts.", color="\033[1;32m")
    # List some fake hosts
    for _ in range(min(active, 5)):
        ip = f"192.168.1.{random.randint(1,254)}"
        hostname = f"host-{random.randint(100,999)}"
        type_writer(f"   ├─ {ip} ({hostname}) - OS: {random.choice(['Windows','Linux','Android'])}", color="\033[1;37m")
    if active > 5:
        type_writer(f"   └─ ... and {active-5} more", color="\033[1;37m")
    input("\nPress Enter to continue...")

# ========================== MODULE 4: CREDENTIAL CRACKER ==========================
def module_credential_cracker():
    show_banner()
    target_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"  # "password"
    type_writer(f"[🔑] Credential Cracker", color="\033[1;34m")
    type_writer(f"Target hash: {target_hash}", color="\033[1;37m")
    type_writer("Starting dictionary attack...", color="\033[1;37m")
    wordlist = ["admin", "123456", "password", "letmein", "qwerty", "abc123", "root", "toor", "welcome", "admin123"]
    random.shuffle(wordlist)
    found = False
    for i, w in enumerate(wordlist):
        progress_bar(i+1, len(wordlist), prefix="Cracking")
        time.sleep(random.uniform(0.2, 0.5))
        if random.random() < 0.2 and not found:  # simulate finding at some point
            type_writer(f"\n[✓] Password found: '{w}'", color="\033[1;32m")
            found = True
            break
    if not found:
        # fallback
        type_writer("\n[✓] Password found: 'password'", color="\033[1;32m")
    type_writer("Credentials: admin:password", color="\033[1;32m")
    input("\nPress Enter to continue...")

# ========================== MODULE 5: DDOS SIMULATION ==========================
def module_ddos():
    show_banner()
    target = input("[?] Enter target IP or domain: ") or "192.168.1.1"
    attack_type = input("[?] Attack type (layer7/layer4): ") or "layer7"
    type_writer(f"\n[💥] Starting DDoS attack on {target} ({attack_type})", color="\033[1;31m")
    type_writer("Saturating bandwidth...", color="\033[1;33m")
    for i in range(1, 101):
        progress_bar(i, 100, prefix="Attack progress")
        # Simulate packets
        if i % 10 == 0:
            type_writer(f"\n   ↳ Packet flood: {random.randint(10000, 99999)} pps", color="\033[1;37m", end="\r")
        time.sleep(random.uniform(0.01, 0.05))
    print()
    type_writer("\n[⚠️] Target is under heavy load!", color="\033[1;31m")
    type_writer("[✓] Attack completed (simulated)", color="\033[1;32m")
    input("\nPress Enter to continue...")

# ========================== MODULE 6: RANSOMWARE SIM ==========================
def module_ransomware():
    show_banner()
    target = input("[?] Enter target path (e.g., /data): ") or "/sdcard"
    type_writer(f"\n[💰] Ransomware Simulator", color="\033[1;34m")
    type_writer(f"Target directory: {target}", color="\033[1;37m")
    type_writer("Encrypting files (AES-256)...", color="\033[1;33m")
    files = random.randint(50, 200)
    for i in range(1, files+1):
        progress_bar(i, files, prefix="Encrypting")
        time.sleep(random.uniform(0.001, 0.01))
    print()
    type_writer(f"\n[✓] {files} files encrypted.", color="\033[1;32m")
    type_writer("[⚠️] Ransom note dropped: README.txt", color="\033[1;31m")
    type_writer("Ransom demand: 0.5 BTC", color="\033[1;33m")
    type_writer("[!] This is a simulation; no real encryption occurred.", color="\033[1;36m")
    input("\nPress Enter to continue...")

# ========================== MODULE 7: WIFI CRACKER ==========================
def module_wifi():
    show_banner()
    type_writer("[📶] Wi‑Fi Scanner & Cracker", color="\033[1;34m")
    type_writer("Scanning for nearby networks...", color="\033[1;37m")
    networks = []
    for i in range(random.randint(3,8)):
        ssid = f"WiFi-{random.randint(100,999)}"
        bssid = ":".join([f"{random.randint(0,255):02X}" for _ in range(6)])
        signal = random.randint(-80, -30)
        enc = random.choice(["WPA2", "WPA3", "WEP"])
        networks.append((ssid, bssid, signal, enc))
        type_writer(f"   ├─ {ssid} ({bssid}) - {enc} - {signal} dBm", color="\033[1;37m")
        random_delay(0.1, 0.3)
    # Select one to crack
    if networks:
        target_net = random.choice(networks)
        type_writer(f"\n[🎯] Attacking {target_net[0]} ({target_net[1]})", color="\033[1;31m")
        type_writer("Handshake captured. Starting brute‑force...", color="\033[1;33m")
        for i in range(1, 101):
            progress_bar(i, 100, prefix="Cracking")
            time.sleep(random.uniform(0.01, 0.03))
        print()
        type_writer(f"\n[✓] Password found: '{random.choice(['12345678','password','qwerty','letmein'])}'", color="\033[1;32m")
    input("\nPress Enter to continue...")

# ========================== MODULE 8: PAYLOAD GENERATOR ==========================
def module_payload():
    show_banner()
    type_writer("[💉] Payload Generator", color="\033[1;34m")
    payload_type = input("[?] Payload type (shell/reverse/bind): ") or "reverse"
    lhost = input("[?] LHOST: ") or "127.0.0.1"
    lport = input("[?] LPORT: ") or "4444"
    type_writer(f"\nGenerating {payload_type} payload...", color="\033[1;33m")
    time.sleep(1)
    # Generate fake hex code
    hex_code = "".join([f"{random.randint(0,255):02x}" for _ in range(64)])
    type_writer(f"Payload (hex): {hex_code}", color="\033[1;37m")
    type_writer(f"Encoded with Base64: {random.choice(['aW1wb3J0IG9zCg==', 'c3lzdGVtKCJpZA==', 'ZXhlYygiY2FsYyIp'])}", color="\033[1;37m")
    type_writer("[✓] Payload saved to payload.bin", color="\033[1;32m")
    input("\nPress Enter to continue...")

# ========================== MODULE 9: SYSTEM INFO ==========================
def module_sysinfo():
    show_banner()
    type_writer("[🖥️] System Information", color="\033[1;34m")
    type_writer(f"   OS           : {platform.system()} {platform.release()}", color="\033[1;37m")
    type_writer(f"   Architecture : {platform.architecture()[0]}", color="\033[1;37m")
    type_writer(f"   Processor    : {platform.processor() or 'Unknown'}", color="\033[1;37m")
    type_writer(f"   Python       : {sys.version.split()[0]}", color="\033[1;37m")
    type_writer(f"   Hostname     : {platform.node()}", color="\033[1;37m")
    type_writer("\n[!] This information is for simulation purposes.", color="\033[1;36m")
    input("\nPress Enter to continue...")

# ========================== MAIN MENU ==========================
def main():
    global STEALTH_MODE
    while True:
        show_banner()
        print("\n\033[1;36m[ MAIN MENU ]\033[0m")
        print("  \033[1;32m 1.\033[0m 🕵️  Target Reconnaissance")
        print("  \033[1;32m 2.\033[0m 🌐  Multi‑Target Attack")
        print("  \033[1;32m 3.\033[0m 🔍  Network Scanner")
        print("  \033[1;32m 4.\033[0m 🔑  Credential Cracker")
        print("  \033[1;32m 5.\033[0m 💥  DDoS Simulation")
        print("  \033[1;32m 6.\033[0m 💰  Ransomware Simulator")
        print("  \033[1;32m 7.\033[0m 📶  Wi‑Fi Cracker")
        print("  \033[1;32m 8.\033[0m 💉  Payload Generator")
        print("  \033[1;32m 9.\033[0m 🖥️  System Info")
        print("  \033[1;32m10.\033[0m 🌍  Open WhatsApp Channel")
        print("  \033[1;32m11.\033[0m 🛡️  Toggle Stealth Mode")
        print("  \033[1;32m 0.\033[0m ❌  Exit")
        print("\033[1;36m" + "─" * 75 + "\033[0m")
        
        choice = input("\033[1;33mSelect option: \033[0m")
        
        if choice == "1":
            module_recon()
        elif choice == "2":
            module_multi_target()
        elif choice == "3":
            module_network_scanner()
        elif choice == "4":
            module_credential_cracker()
        elif choice == "5":
            module_ddos()
        elif choice == "6":
            module_ransomware()
        elif choice == "7":
            module_wifi()
        elif choice == "8":
            module_payload()
        elif choice == "9":
            module_sysinfo()
        elif choice == "10":
            show_banner()
            type_writer("Opening WhatsApp channel...", color="\033[1;36m")
            if platform.system() == "Windows":
                os.system(f'start {CHANNEL_LINK}')
            elif platform.system() == "Darwin":
                os.system(f'open {CHANNEL_LINK}')
            else:
                os.system(f'termux-open-url "{CHANNEL_LINK}"')
            time.sleep(2)
        elif choice == "11":
            STEALTH_MODE = not STEALTH_MODE
            type_writer(f"\n[🛡️] Stealth mode {'ENABLED' if STEALTH_MODE else 'DISABLED'}", color="\033[1;33m")
            time.sleep(1)
        elif choice == "0":
            type_writer("\n[👋] Exiting PROFESSOR ULTIMATE. Stay safe!", color="\033[1;31m")
            break
        else:
            type_writer("\n[❌] Invalid option. Try again.", color="\033[1;31m")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Interrupted by user.\033[0m")
        sys.exit(0)
