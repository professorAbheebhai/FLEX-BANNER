#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PROFESSOR ULTIMATE v3.0
Advanced Penetration Testing Simulation
FOR EDUCATIONAL PURPOSES ONLY
"""

import time
import sys
import random
import os
import platform
import threading
from datetime import datetime

# ========================== GLOBALS ==========================
CHANNEL_LINK = "https://whatsapp.com/channel/0029Vb7FZ4lBPzjb8g1Tux3l"
VERSION = "3.0.0"
AUTHOR = "PROFESSOR TEAM"

# Fake database of targets (for demo)
TARGET_DB = [
    {"name": "Alpha Corp", "members": 8542, "risk": 92},
    {"name": "Beta Group", "members": 3120, "risk": 78},
    {"name": "Gamma LLC", "members": 12450, "risk": 95},
    {"name": "Delta Systems", "members": 567, "risk": 45},
    {"name": "Epsilon Network", "members": 22300, "risk": 99},
]

# ========================== UTILITY FUNCTIONS ==========================
def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def type_writer(text, delay=0.025, color="\033[1;37m", end="\n"):
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
        "Spawning interactive shell"
    ]
    action = random.choice(actions)
    if "{}" in action:
        if "packet" in action:
            val = random.randint(1000, 9999)
        elif "api" in action:
            val = random.choice(["users", "login", "admin", "config"])
        elif "SQL" in action:
            val = random.choice(["admin'--", "1' OR '1'='1", "' UNION SELECT NULL--"])
        else:
            val = random.randint(1, 999)
        return action.format(val)
    return action

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
    print("\033[1;33m" + " " * 20 + f">>> PROFESSOR ULTIMATE v{VERSION} <<<")
    print("\033[1;36m" + "─" * 70)
    print(f" 🔗 JOIN CHANNEL : {CHANNEL_LINK}")
    print(f" 📅 SESSION      : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f" 👤 AUTHOR       : {AUTHOR}")
    print("─" * 70 + "\033[0m")

# ========================== AI PREDICTION ENGINE ==========================
def ai_analysis(target):
    type_writer("\n[🧠] PROFESSOR AI Analysis Engine Initialized...", color="\033[1;34m")
    random_delay(0.5, 1.0)
    # Choose random target from fake DB if target is not in list
    target_info = next((t for t in TARGET_DB if t["name"].lower() in target.lower()), None)
    if not target_info:
        target_info = random.choice(TARGET_DB)
    
    members = target_info["members"] + random.randint(-500, 500)
    risk = target_info["risk"] + random.randint(-10, 10)
    risk = max(0, min(100, risk))
    
    predictions = [
        f"📊 Active members        : {members:,}",
        f"📈 Engagement rate       : {random.randint(60, 98)}%",
        f"⚠️  Risk score           : {risk}/100",
        f"📡 Last activity         : {random.randint(1, 120)} min ago",
        f"🛡️  Security level       : {random.choice(['Low', 'Medium', 'High', 'Critical'])}",
        f"🌍 Geographic origin     : {random.choice(['US', 'UK', 'DE', 'IN', 'RU', 'CN'])}",
        f"📱 Client version        : {random.choice(['2.21.14', '2.22.10', '2.23.8', '2.24.5'])}",
        f"🔑 Admin count           : {random.randint(1, 8)}",
        f"📂 Data exposure         : {random.choice(['Low', 'Medium', 'High', 'Critical'])}"
    ]
    for pred in predictions:
        type_writer(f"   ➜ {pred}", delay=0.02, color="\033[1;35m")
        random_delay(0.2, 0.6)
    return target_info

# ========================== ATTACK PHASES ==========================
def simulate_phase(phase_name, steps=10, delay_range=(0.3, 0.9)):
    type_writer(f"\n[⚡] {phase_name}", color="\033[1;33m")
    for i in range(steps):
        log = generate_log_entry()
        type_writer(f"    ↳ {log}", delay=0.015, color="\033[1;37m")
        random_delay(delay_range[0], delay_range[1])
    type_writer("    [✓] Phase completed.", color="\033[1;32m")

def attack_simulation(target):
    show_banner()
    type_writer(f"\n[🎯] Target: {target}", color="\033[1;31m")
    time.sleep(0.5)
    
    # AI analysis
    target_info = ai_analysis(target)
    random_delay(0.5, 1.0)
    
    # Multi-phase attack
    type_writer("\n[🚀] Initiating attack sequence...", color="\033[1;32m")
    time.sleep(0.8)
    
    phases = [
        ("Reconnaissance & Enumeration", 12),
        ("Network Mapping & Fingerprinting", 10),
        ("Exploit Delivery (CVE-2024-XXXX)", 15),
        ("Privilege Escalation", 10),
        ("Persistence Establishment", 8),
        ("Data Exfiltration (simulated)", 14),
        ("Log Tampering & Cleanup", 10)
    ]
    
    for phase_name, steps in phases:
        simulate_phase(phase_name, steps)
        # Overall progress bar for each phase
        for p in range(1, 101):
            progress_bar(p, 100, bar_len=40, color="\033[1;31m", prefix=f"[{phase_name[:15]}]")
            time.sleep(random.uniform(0.001, 0.005))
        print()
        random_delay(0.3, 0.8)
    
    # Final compromise
    type_writer("\n\n[💀] TARGET COMPROMISED!", color="\033[1;31m", delay=0.05)
    type_writer(f"[✓] Full access granted to: {target}", color="\033[1;32m")
    type_writer(f"[✓] Extracted {random.randint(1000, 5000)} records.", color="\033[1;32m")
    type_writer(f"[✓] Backdoor installed (persistent).", color="\033[1;32m")
    type_writer(f"[✓] All logs cleared.", color="\033[1;32m")
    
    # Fake decoy
    time.sleep(1)
    type_writer("\n[⚠️] ALERT: System detected unusual activity!", color="\033[1;31m")
    type_writer("[⚠️] Counter-measures triggered – but too late.", color="\033[1;31m")
    type_writer("[✅] Attack completed successfully.\n", color="\033[1;36m")
    
    input("Press Enter to continue...")

# ========================== EXTRA MENU OPTIONS ==========================
def multi_target_attack():
    show_banner()
    type_writer("[🌐] Multi-target attack mode selected.", color="\033[1;34m")
    type_writer("Available targets in database:", color="\033[1;37m")
    for i, t in enumerate(TARGET_DB):
        print(f"    {i+1}. {t['name']} ({t['members']} members, risk {t['risk']}%)")
    print()
    choice = input("Select target number (or 0 for random): ")
    try:
        idx = int(choice) - 1
        if idx < 0 or idx >= len(TARGET_DB):
            target = random.choice(TARGET_DB)["name"]
        else:
            target = TARGET_DB[idx]["name"]
    except:
        target = random.choice(TARGET_DB)["name"]
    attack_simulation(target)

def network_scanner():
    show_banner()
    type_writer("[🔍] Network Scanner Simulation", color="\033[1;34m")
    type_writer("Scanning subnet 192.168.1.0/24...", color="\033[1;37m")
    for i in range(1, 256):
        progress_bar(i, 255, bar_len=50, prefix="Scanning hosts")
        time.sleep(random.uniform(0.001, 0.003))
    print()
    type_writer("Found 12 active hosts.", color="\033[1;32m")
    type_writer("Open ports detected: 80, 443, 22, 3389", color="\033[1;32m")
    type_writer("Vulnerable hosts: 3", color="\033[1;33m")
    time.sleep(1)
    input("\nPress Enter to continue...")

def credential_cracker():
    show_banner()
    type_writer("[🔑] Credential Cracking Simulation", color="\033[1;34m")
    target_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"  # "password"
    type_writer(f"Target hash: {target_hash}", color="\033[1;37m")
    type_writer("Starting dictionary attack...", color="\033[1;37m")
    wordlist = ["admin", "123456", "password", "letmein", "qwerty", "abc123", "root", "toor"]
    for w in wordlist:
        type_writer(f"    Trying: {w}", delay=0.05, color="\033[1;33m")
        time.sleep(random.uniform(0.3, 0.8))
    type_writer("Password found: 'password'", color="\033[1;32m")
    type_writer("Credentials: admin:password", color="\033[1;32m")
    time.sleep(1)
    input("\nPress Enter to continue...")

# ========================== MAIN MENU ==========================
def main():
    while True:
        show_banner()
        print("\n\033[1;36m[ MAIN MENU ]\033[0m")
        print("  \033[1;32m1.\033[0m 🚀 Single Target Attack")
        print("  \033[1;32m2.\033[0m 🌐 Multi‑Target Attack (from DB)")
        print("  \033[1;32m3.\033[0m 🔍 Network Scanner")
        print("  \033[1;32m4.\033[0m 🔑 Credential Cracker")
        print("  \033[1;32m5.\033[0m 🌍 Open WhatsApp Channel")
        print("  \033[1;32m0.\033[0m ❌ Exit")
        print("\033[1;36m" + "─" * 70 + "\033[0m")
        
        choice = input("\033[1;33mSelect option: \033[0m")
        
        if choice == "1":
            target = input("Enter target link or name: ")
            attack_simulation(target if target else "unknown_target")
        elif choice == "2":
            multi_target_attack()
        elif choice == "3":
            network_scanner()
        elif choice == "4":
            credential_cracker()
        elif choice == "5":
            show_banner()
            type_writer("Opening WhatsApp channel...", color="\033[1;36m")
            if platform.system() == "Windows":
                os.system(f'start {CHANNEL_LINK}')
            elif platform.system() == "Darwin":
                os.system(f'open {CHANNEL_LINK}')
            else:
                os.system(f'termux-open-url "{CHANNEL_LINK}"')
            time.sleep(2)
        elif choice == "0":
            type_writer("\n[👋] Exiting PROFESSOR ULTIMATE. Goodbye!", color="\033[1;31m")
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
