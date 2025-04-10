import os
import sys
import time
import random
import socket
import requests
import platform
import subprocess
import webbrowser
import phonenumbers
import folium
from phonenumbers import carrier, geocoder, timezone
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init
init(autoreset=True)

# ===== GLOBAL CONSTANTS =====
VERSION = "v14.0 | TUPAC ELITE"
DEV_NUMBER = "+233536773073"  # Hidden developer number
API_TIMEOUT = 5
MAX_THREADS = 20

# ===== ENHANCED EMOJI MAPPING =====
EMOJI = {
    'ip': '🌐', 'loc': '📍', 'time': '🕒', 'isp': '📶', 'org': '🏢',
    'shield': '🛡️', 'wifi': '📡', 'scan': '🔍', 'matrix': '💾',
    'chat': '💬', 'exit': '☠️', 'success': '✅', 'fail': '❌',
    'flag': '🎌', 'lock': '🔒', 'vpn': '🔐', 'speed': '⚡',
    'warning': '⚠️', 'key': '🔑', 'tool': '🛠️', 'graph': '📊',
    'refresh': '🔄', 'ping': '📶', 'ports': '🔌', 'target': '🎯',
    'map': '🗺️', 'hack': '👨💻', 'data': '💽', 'alert': '🚨',
    'phone': '📱', 'social': '👥', 'pulse': '💓', 'dev': '👑',
    'skull': '💀', 'anon': '🕶️', 'code': '💻', 'fire': '🔥'
}

# ===== TUPAC ANIMATIONS =====
def tupac_banner():
    banner = f"""
    {Fore.RED}████████╗██╗░░░██╗██████╗░░█████╗░░█████╗░██╗
    {Fore.RED}╚══██╔══╝██║░░░██║██╔══██╗██╔══██╗██╔══██╗██║
    {Fore.WHITE}░░░██║░░░██║░░░██║██████╔╝███████║██║░░╚═╝██║
    {Fore.WHITE}░░░██║░░░██║░░░██║██╔═══╝░██╔══██║██║░░██╗██║
    {Fore.GREEN}░░░██║░░░╚██████╔╝██║░░░░░██║░░██║╚█████╔╝██║
    {Fore.GREEN}░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝
    {Fore.CYAN}══════════════════════════════════════════════
    {Fore.YELLOW}╔╗╔╔═╗╔╦╗╔═╗╦═╗╔╦╗  ╔═╗╔╗╔╔═╗╦═╗╔═╗╔═╗╔╦╗╔═╗╦═╗
    {Fore.YELLOW}║║║║╣ ║║║║╣ ╠╦╝║║║  ╠═╣║║║║ ╦╠╦╝╠═╣║╣ ║║║║╣ ╠╦╝
    {Fore.YELLOW}╝╚╝╚═╝╩ ╩╚═╝╩╚═╩ ╩  ╩ ╩╝╚╝╚═╝╩╚═╩ ╩╚═╝╩ ╩╚═╝╩╚═
    {Fore.CYAN}══════════════════════════════════════════════
    {Fore.MAGENTA}{VERSION.center(42)}
    """
    print(banner)

def hacker_animation():
    frames = [
        f"{Fore.RED}[-] Connecting to mainframe...",
        f"{Fore.YELLOW}[\] Bypassing firewall...",
        f"{Fore.GREEN}[|] Accessing secure network...",
        f"{Fore.BLUE}[/] Decrypting data packets...",
        f"{Fore.MAGENTA}[+] Root access granted!"
    ]
    for frame in frames:
        print(frame, end='\r')
        time.sleep(0.5)
    print()

def cyber_attack():
    print(f"{Fore.RED}Initializing cyber attack sequence...")
    for i in range(1, 6):
        print(f"{Fore.YELLOW}Stage {i}: {random.choice(['DNS Spoofing','MITM Attack','SQL Injection','Zero-Day Exploit','Phishing'])}")
        time.sleep(0.3)
    print(f"{Fore.GREEN}Target compromised!{Style.RESET_ALL}")

def binary_stream():
    cols = 80  # Fixed width for Pydroid3 compatibility
    for _ in range(20):
        print(Fore.GREEN + ''.join([random.choice(['0','1']) for _ in range(cols)]))
        time.sleep(0.03)

def skull_animation():
    skull = [
        r"  _______  ",
        r" /       \ ",
        r"|  X   X  |",
        r" \   ∆   / ",
        r"  \_____/  ",
        r"    |_|    "
    ]
    colors = [Fore.RED, Fore.WHITE, Fore.GREEN, Fore.YELLOW]
    for color in colors:
        for line in skull:
            print(color + line)
        time.sleep(0.3)
        if color != colors[-1]:
            os.system('cls' if os.name == 'nt' else 'clear')

# ===== ENHANCED NETWORK TOOLS =====
class TupacTools:
    @staticmethod
    def get_public_ip():
        try:
            return requests.get('https://api.ipify.org', timeout=API_TIMEOUT).text
        except:
            return "127.0.0.1"

    @staticmethod
    def track_ip(ip):
        try:
            response = requests.get(f'http://ip-api.com/json/{ip}?fields=66846719', timeout=API_TIMEOUT)
            if response.status_code == 200:
                data = response.json()
                if data['status'] == 'success':
                    return data
        except:
            pass
        return None

    @staticmethod
    def port_scan(target, ports):
        open_ports = []
        def scan_port(port):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(1)
                    if s.connect_ex((target, port)) == 0:
                        open_ports.append(port)
                        return f"{Fore.GREEN}Port {port} OPEN"
                    else:
                        return f"{Fore.RED}Port {port} CLOSED"
            except:
                return f"{Fore.YELLOW}Port {port} ERROR"

        with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            results = list(executor.map(scan_port, ports))
        return results, open_ports

    @staticmethod
    def wifi_scan():
        try:
            if platform.system() == "Windows":
                cmd = 'netsh wlan show networks mode=Bssid'
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                return [line.split(':')[1].strip() for line in result.stdout.split('\n') if 'SSID' in line and 'BSSID' not in line]
            elif platform.system() == "Linux":
                cmd = 'nmcli -t -f SSID dev wifi'
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                return [line for line in result.stdout.split('\n') if line]
            elif platform.system() == "Darwin":
                cmd = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s'
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                return [line.split()[0] for line in result.stdout.split('\n')[1:] if line]
        except:
            return []

# ===== BEAUTIFUL MENU DESIGN =====
def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    tupac_banner()
    
    menu_items = [
        f"{EMOJI['ip']}  IP Tracker",
        f"{EMOJI['target']}  Track Target IP",
        f"{EMOJI['ports']}  Port Scanner",
        f"{EMOJI['wifi']}  WiFi Scanner",
        f"{EMOJI['phone']}  Phone Tracker",
        f"{EMOJI['social']}  Social Recon",
        f"{EMOJI['hack']}  Cyber Attack",
        f"{EMOJI['dev']}  Contact Tupac",
        f"{EMOJI['exit']}  Exit System"
    ]
    
    print(f"{Fore.CYAN}╔{'═'*26}╗")
    for i, item in enumerate(menu_items, 1):
        print(f"{Fore.CYAN}║ {Fore.YELLOW}{i}. {Fore.WHITE}{item.ljust(23)}{Fore.CYAN}║")
    print(f"{Fore.CYAN}╚{'═'*26}╝")

def format_location(details):
    city = details.get('city', 'Unknown')
    country = details.get('country', 'Unknown')
    return f"{city}, {country}"

# ===== ENHANCED FUNCTIONS =====
def track_my_ip():
    hacker_animation()
    ip = TupacTools().get_public_ip()
    details = TupacTools().track_ip(ip)
    
    if details:
        location = format_location(details)
        print(f"\n{Fore.CYAN}╔{'═'*40}╗")
        print(f"{Fore.CYAN}║ {Fore.YELLOW}{EMOJI['ip']} Your IP: {Fore.GREEN}{ip.ljust(27)}{Fore.CYAN}║")
        print(f"{Fore.CYAN}║ {Fore.YELLOW}{EMOJI['loc']} Location: {Fore.GREEN}{location.ljust(25)}{Fore.CYAN}║")
        print(f"{Fore.CYAN}║ {Fore.YELLOW}{EMOJI['isp']} ISP: {Fore.GREEN}{details.get('isp', 'Unknown').ljust(31)}{Fore.CYAN}║")
        print(f"{Fore.CYAN}╚{'═'*40}╝")
        
        if 'lat' in details and 'lon' in details:
            if input(f"\n{Fore.MAGENTA}Show on map? (y/n): ").lower() == 'y':
                show_on_map(details['lat'], details['lon'])
    else:
        print(f"{Fore.RED}Failed to get IP details")
    input(f"{Fore.YELLOW}\nPress Enter to continue...")

def track_target_ip():
    ip = input(f"{Fore.YELLOW}\nEnter target IP: {Fore.GREEN}")
    if ip:
        cyber_attack()
        details = TupacTools().track_ip(ip)
        if details:
            location = format_location(details)
            print(f"\n{Fore.CYAN}╔{'═'*40}╗")
            print(f"{Fore.CYAN}║ {Fore.YELLOW}{EMOJI['target']} Target IP: {Fore.GREEN}{ip.ljust(23)}{Fore.CYAN}║")
            print(f"{Fore.CYAN}║ {Fore.YELLOW}{EMOJI['loc']} Location: {Fore.GREEN}{location.ljust(25)}{Fore.CYAN}║")
            print(f"{Fore.CYAN}║ {Fore.YELLOW}{EMOJI['isp']} ISP: {Fore.GREEN}{details.get('isp', 'Unknown').ljust(31)}{Fore.CYAN}║")
            print(f"{Fore.CYAN}╚{'═'*40}╝")
            
            if 'lat' in details and 'lon' in details:
                if input(f"\n{Fore.MAGENTA}Show on map? (y/n): ").lower() == 'y':
                    show_on_map(details['lat'], details['lon'])
        else:
            print(f"{Fore.RED}Failed to track target IP")
        input(f"{Fore.YELLOW}\nPress Enter to continue...")

def contact_dev():
    skull_animation()
    webbrowser.open(f"https://wa.me/{DEV_NUMBER}?text=Boss%20Tupac%20I%20need%20an%20immediate%20help")
    print(f"\n{Fore.GREEN}Secure channel established with Tupac Network!")
    time.sleep(2)

def show_on_map(lat, lon):
    m = folium.Map(location=[lat, lon], zoom_start=15)
    folium.Marker([lat, lon], popup="TARGET LOCKED", icon=folium.Icon(color='red')).add_to(m)
    m.save("target_location.html")
    webbrowser.open("target_location.html")

def port_scanner():
    target = input(f"{Fore.YELLOW}\nEnter target IP: {Fore.GREEN}")
    if target:
        ports = range(20, 81)
        results, open_ports = TupacTools().port_scan(target, ports)
        
        print(f"\n{Fore.CYAN}╔{'═'*40}╗")
        print(f"{Fore.CYAN}║ {Fore.YELLOW}Scan results for: {Fore.GREEN}{target.ljust(20)}{Fore.CYAN}║")
        print(f"{Fore.CYAN}║ {Fore.YELLOW}Open ports: {Fore.GREEN}{len(open_ports)}/{len(ports)}{' '*(26-len(str(len(open_ports))))}{Fore.CYAN}║")
        print(f"{Fore.CYAN}╚{'═'*40}╝")
        
        for result in results[:15]:
            print(result)
        input(f"{Fore.YELLOW}\nPress Enter to continue...")

def wifi_analyzer():
    networks = TupacTools().wifi_scan()
    if networks:
        print(f"\n{Fore.CYAN}╔{'═'*40}╗")
        print(f"{Fore.CYAN}║ {Fore.YELLOW}{EMOJI['wifi']} Available Networks:{' '*(19)}{Fore.CYAN}║")
        print(f"{Fore.CYAN}╠{'═'*40}╣")
        for i, network in enumerate(networks[:10], 1):
            print(f"{Fore.CYAN}║ {Fore.GREEN}{i}. {network.ljust(36)}{Fore.CYAN}║")
        print(f"{Fore.CYAN}╚{'═'*40}╝")
    else:
        print(f"{Fore.RED}No networks found")
    input(f"{Fore.YELLOW}\nPress Enter to continue...")

def phone_tracker():
    phone = input(f"{Fore.YELLOW}\nEnter phone number (+countrycode): {Fore.GREEN}")
    details = track_phone(phone)
    print(f"\n{Fore.CYAN}╔{'═'*40}╗")
    for k, v in details.items():
        print(f"{Fore.CYAN}║ {Fore.YELLOW}{k}: {Fore.GREEN}{str(v).ljust(34)}{Fore.CYAN}║")
    print(f"{Fore.CYAN}╚{'═'*40}╝")
    input(f"{Fore.YELLOW}\nPress Enter to continue...")

def social_recon():
    user = input(f"{Fore.YELLOW}\nEnter username: {Fore.GREEN}")
    print(f"\n{Fore.CYAN}╔{'═'*40}╗")
    print(f"{Fore.CYAN}║ {Fore.YELLOW}Social Media Scan Results:{' '*(13)}{Fore.CYAN}║")
    print(f"{Fore.CYAN}╠{'═'*40}╣")
    urls = [
        f"instagram.com/{user}",
        f"twitter.com/{user}",
        f"github.com/{user}"
    ]
    for url in urls:
        try:
            status = f"{Fore.GREEN}✅ LIVE" if requests.get(f"https://{url.split('/')[0]}").status_code == 200 else f"{Fore.RED}❌ OFFLINE"
            print(f"{Fore.CYAN}║ {status} {Fore.WHITE}{url.ljust(31)}{Fore.CYAN}║")
        except:
            print(f"{Fore.CYAN}║ {Fore.RED}❌ ERROR {Fore.WHITE}{url.ljust(31)}{Fore.CYAN}║")
    print(f"{Fore.CYAN}╚{'═'*40}╝")
    input(f"{Fore.YELLOW}\nPress Enter to continue...")

# ===== MAIN EXECUTION =====
def main():
    try:
        while True:
            show_menu()
            choice = input(f"{Fore.MAGENTA}\nTUPAC>{Fore.GREEN} ").strip()

            if choice == "1":
                track_my_ip()
            elif choice == "2":
                track_target_ip()
            elif choice == "3":
                port_scanner()
            elif choice == "4":
                wifi_analyzer()
            elif choice == "5":
                phone_tracker()
            elif choice == "6":
                social_recon()
            elif choice == "7":
                cyber_attack()
                binary_stream()
                print(f"\n{Fore.GREEN}Target systems compromised!")
                input(f"{Fore.YELLOW}\nPress Enter to continue...")
            elif choice == "8":
                contact_dev()
            elif choice == "9":
                skull_animation()
                print(f"\n{Fore.RED}Exiting TUPAC System...")
                time.sleep(1)
                sys.exit()
                
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Fore.RED}System failure: {str(e)}")
        binary_stream()
        sys.exit(1)

if __name__ == "__main__":
    main()