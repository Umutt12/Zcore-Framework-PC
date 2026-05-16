import socket
import threading
import requests
import os
import subprocess
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

SERVICE_MAP = {
    21: "FTP", 22: "SSH", 23: "Telnet (RISK)", 53: "DNS",
    80: "HTTP", 139: "NetBIOS", 443: "HTTPS", 445: "SMB (CRITICAL)",
    1900: "UPnP", 3306: "MySQL", 3389: "RDP", 5431: "UPnP Router",
    8080: "Proxy", 44401: "Router Backdoor", 50805: "Game Stream"
}

def log_to_file(data):
    try:
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        filepath = os.path.join(desktop, 'zcore_report.txt')
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(f"[{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}] {data}\n")
    except:
        pass

def clear_screen(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def show_logo():
    print(Fore.RED + Style.BRIGHT + """
  ███████╗ ██████╗ ██████╗ ██████╗ ███████╗  ██████╗ ██╗      ██████╗ ██████╗  █████╗ ██╗     
  ╚══███╔╝██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝ ██║     ██╔═══██╗██╔══██╗██╔══██╗██║     
    ███╔╝ ██║     ██║   ██║██████╔╝█████╗   ██║  ███╗██║     ██║   ██║██████╔╝███████║██║     
   ███╔╝  ██║     ██║   ██║██╔══██╗██╔══╝   ██║   ██║██║     ██║   ██║██╔══██╗██╔══██║██║     
  ███████╗╚██████╗╚██████╔╝██║  ██║███████╗ ╚██████╔╝███████╗╚██████╔╝██████╔╝██║  ██║███████╗
  ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
    """)
    print(Fore.CYAN + Style.BRIGHT + "   ===[ SCAMHUNTER GLOBAL INTEL COMMAND MATRIX | 25 ACTIVE OPTIONS ]===")
    print(Fore.YELLOW + "   ===                   Developer: Umut Zcore [GLOBAL]             ===\n")

# CORE ENGINES
def get_clean_target(target):
    if "http" in target:
        target = target.split("//")[-1].split("/")[0].split("?")[0]
    return target

def resolve_target(target):
    target = get_clean_target(target)
    try:
        return socket.gethostbyname(target)
    except:
        return None

def fetch_api_data(ip):
    try:
        return requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
    except:
        return None

def port_worker(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        if s.connect_ex((str(ip), port)) == 0:
            srv = SERVICE_MAP.get(port, "Unknown Service")
            if port in [23, 445, 44401]:
                print(Fore.RED + Style.BRIGHT + f" [!!!] ALERT -> {ip}:{port} OPEN | {srv}")
            else:
                print(Fore.GREEN + f" [+] {ip}:{port} OPEN | {srv}")
        s.close()
    except:
        pass

def ping_worker(ip):
    try:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        output = subprocess.Popen(f"ping -n 1 -w 150 {ip}", stdout=subprocess.PIPE, startupinfo=startupinfo).communicate()[0]
        if "reply from" in output.decode('latin-1').lower() or "ttl=" in output.decode('latin-1').lower():
            print(Fore.GREEN + Style.BRIGHT + f"[+] HOST ALIVE -> {ip}")
            for p in [80, 443, 445]:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.05)
                if s.connect_ex((str(ip), p)) == 0:
                    print(Fore.YELLOW + f"    └─> Port {p} OPEN")
                s.close()
    except:
        pass

# MAIN COMPONENT
def main():
    while True:
        try:
            clear_screen()
            show_logo()
            
            # 25 OPTION INTERFACE MATRIX
            print(Fore.WHITE + "--- OSINT & TARGET RECON ---             --- LAN RADAR & INFRASTRUCTURE ---")
            print(Fore.WHITE + "1] My Public External IP                 11] Live Host Ping Sweep")
            print(Fore.WHITE + "2] Domain to IP Resolver                 12] LAN Service Discovery Scanner")
            print(Fore.WHITE + "3] IP to Nameserver (Reverse DNS)        13] Gateway Protocol Finder (Router IP)")
            print(Fore.WHITE + "4] WHOIS Registrar Core Lookup           14] MAC Vendor System Identifier")
            print(Fore.WHITE + "5] Geo-Location Radar Mapping            15] Subnet Mask Host Calculator")
            print(Fore.WHITE + "\n--- PORT AUDITING ENGINES ---            --- SCAMHUNTER ANTI-FRAUD ---")
            print(Fore.WHITE + "6] Stealth Port Scan (Top 5 Essential)   16] Phishing URL Engine Cleaner")
            print(Fore.WHITE + "7] System Services Scan (1-1024)         17] Cloudflare WAF Proxy Detector")
            print(Fore.WHITE + "8] Gaming & Backdoor Port Audit          18] Hosting Reputation Check")
            print(Fore.WHITE + "9] Custom Target Port Scanner            19] SSL Certificate Validity Test")
            print(Fore.WHITE + "10] Banner Grabbing Core Tester          20] Bulk Link Threat Analyzer Loop")
            print(Fore.WHITE + "\n--- ENDPOINT SYSTEM DEFENSE & SYSTEM MANAGEMENT ---")
            print(Fore.WHITE + "21] SMB Share Integrity Auditor         23] DNS Connection Trace Cache Extractor")
            print(Fore.WHITE + "22] Active Interface Adapter Lister     24] Wipe Session Intelligence Data Report")
            print(Fore.WHITE + "25] Secure Core Framework Logout\n")
            
            choice = input(Fore.CYAN + "Zcore-Matrix > ").strip()
            
            if choice == "25":
                print(Fore.CYAN + "\nShutting down Command Matrix. Session secured.")
                break
                
            elif choice == "1":
                my_ip = requests.get('https://api.ipify.org', timeout=5).text
                print(Fore.GREEN + f"\n[+] Your Public IP Address: {my_ip}")
                log_to_file(f"Self IP query executed: {my_ip}")
                
            elif choice == "2":
                dom = input("\nEnter Domain Target: ").strip()
                res = resolve_target(dom)
                print(Fore.GREEN + f"[+] Resolved: {res}" if res else Fore.RED + "[-] Lookup Failed")
                
            elif choice == "3":
                ip = input("\nEnter Target IP: ").strip()
                try:
                    print(Fore.GREEN + f"[+] PTR Record: {socket.gethostbyaddr(ip)[0]}")
                except: print(Fore.RED + "[-] No PTR Record Found")
                
            elif choice == "4":
                dom = get_clean_target(input("\nEnter Domain: ").strip())
                print(Fore.YELLOW + f"[*] Fetching registrar data for {dom} via API proxy...")
                try:
                    r = requests.get(f"https://rdap.org/domain/{dom}", timeout=5).json()
                    print(Fore.GREEN + f"[+] Entity: {r['entities'][0]['vcardArray'][1][1][3]}")
                except: print(Fore.RED + "[-] RDAP data unavailable.")
                
            elif choice == "5":
                ip = resolve_target(input("\nEnter Target IP/Domain: ").strip())
                data = fetch_api_data(ip)
                if data and data['status'] == 'success':
                    print(Fore.GREEN + f"[+] Coordinates: {data['lat']}, {data['lon']} | {data['city']}, {data['country']}")
                else: print(Fore.RED + "[-] Localization failed.")
                
            elif choice == "6":
                ip = resolve_target(input("\nEnter Target IP/Domain: ").strip())
                if ip:
                    print(Fore.YELLOW + f"[*] Auditing critical ports on {ip}...")
                    for p in [21, 22, 80, 443, 445]: port_worker(ip, p)
                    
            elif choice == "7":
                ip = resolve_target(input("\nEnter Target IP/Domain: ").strip())
                if ip:
                    print(Fore.YELLOW + f"[*] Scanning system ports 1-1024... Multithreading active...")
                    threads = [threading.Thread(target=port_worker, args=(ip, p)) for p in range(1, 1025)]
                    for t in threads: t.start()
                    for t in threads: t.join()
                    
            elif choice == "8":
                ip = resolve_target(input("\nEnter Target IP/Domain: ").strip())
                if ip:
                    print(Fore.YELLOW + "[*] Checking special backdoors & network game lines...")
                    for p in [3389, 5431, 44401, 50805]: port_worker(ip, p)
                    
            elif choice == "9":
                ip = resolve_target(input("\nEnter Target IP/Domain: ").strip())
                p = int(input("Enter Custom Port Number: ").strip())
                if ip: port_worker(ip, p)
                
            elif choice == "10":
                ip = resolve_target(input("\nEnter Target IP: ").strip())
                p = int(input("Port (e.g. 80, 21): ").strip())
                try:
                    s = socket.socket()
                    s.settimeout(1.0)
                    s.connect((ip, p))
                    s.send(b"HEAD / HTTP/1.1\r\n\r\n")
                    print(Fore.GREEN + f"[+] Banner Output:\n {s.recv(1024).decode('latin-1')}")
                    s.close()
                except: print(Fore.RED + "[-] Banner Grab Timed Out")
                
            elif choice == "11":
                base = input("\nEnter Subnet Base (Default: 192.168.1): ").strip()
                if not base: base = "192.168.1"
                threads = [threading.Thread(target=ping_worker, args=(f"{base}.{i}",)) for i in range(1, 255)]
                for t in threads: t.start()
                for t in threads: t.join()
                
            elif choice == "12":
                print(Fore.YELLOW + "[*] Scanning local environment for open services...")
                # Automatically loops across default base
                threads = [threading.Thread(target=ping_worker, args=(f"192.168.1.{i}",)) for i in range(1, 255)]
                for t in threads: t.start()
                for t in threads: t.join()
                
            elif choice == "13":
                print(Fore.GREEN + "[+] Scanning local route gateway configuration maps...")
                os.system("netstat -r | findstr /i \"default\"")
                
            elif choice == "14":
                mac = input("\nEnter target MAC Address to identify: ").strip()
                try:
                    r = requests.get(f"https://api.macvendors.com/{mac}", timeout=4).text
                    print(Fore.GREEN + f"[+] Hardware Manufacturer: {r}")
                except: print(Fore.RED + "[-] Identification database unreachable.")
                
            elif choice == "15":
                cidr = input("\nEnter Mask Bits (e.g. 24, 16): ").strip()
                if cidr == "24": print(Fore.GREEN + "[+] Subnet Limit: 254 Usable Hosts (Class C Local Network)")
                elif cidr == "16": print(Fore.GREEN + "[+] Subnet Limit: 65,534 Usable Hosts (Class B Production)")
                else: print(Fore.YELLOW + "[*] Non-standard masking profile.")
                
            elif choice == "16":
                url = input("\nEnter Dirty Scam Link: ").strip()
                print(Fore.GREEN + f"[+] Extracted Clean Domain Profile: {get_clean_target(url)}")
                
            elif choice == "17":
                ip = resolve_target(input("\nEnter Domain Name: ").strip())
                data = fetch_api_data(ip)
                if data and ("cloudflare" in data.get('isp','').lower() or "cloudflare" in data.get('org','').lower()):
                    print(Fore.RED + "[!] TARGET HIDDEN: Active Cloudflare Proxy Intercept Found.")
                else: print(Fore.GREEN + "[+] Clean Host: Server is sitting on bare allocation profile.")
                
            elif choice == "18":
                ip = resolve_target(input("\nEnter Target domain: ").strip())
                data = fetch_api_data(ip)
                if data: print(Fore.WHITE + f"[+] Host ISP: {data.get('isp')} | Org: {data.get('org')}")
                
            elif choice == "19":
                dom = get_clean_target(input("\nEnter Domain: ").strip())
                try:
                    ctx = socket.create_default_context()
                    with ctx.wrap_socket(socket.socket(), server_hostname=dom) as s:
                        s.settimeout(2.0)
                        s.connect((dom, 443))
                        cert = s.getpeercert()
                        print(Fore.GREEN + f"[+] SSL Registered to: {cert['subject'][3][0][1]}")
                except Exception as e: print(Fore.RED + f"[-] Invalid SSL Layer Profile: {e}")
                
            elif choice == "20":
                links = input("\nEnter target addresses separated by commas: ").strip().split(',')
                for l in links:
                    ip = resolve_target(l.strip())
                    print(Fore.YELLOW + f"[*] Bulk Thread Processing -> {l.strip()} IP: {ip}")
                    
            elif choice == "21":
                print(Fore.CYAN + "[*] Checking local endpoint visibility vector shares...")
                os.system("net share")
                
            elif choice == "22":
                print(Fore.CYAN + "[*] Printing current local active hardware adapters...")
                os.system("ipconfig | findstr /i \"IPv4 Subnet Gateway\"")
                
            elif choice == "23":
                print(Fore.CYAN + "[*] Compiling core temporary system connection footprints...")
                try:
                    cmd = subprocess.Popen("ipconfig /displaydns", stdout=subprocess.PIPE, shell=True)
                    out, _ = cmd.communicate()
                    lines = out.decode('latin-1').split('\n')
                    count = 0
                    for line in lines:
                        if "Record Name" in line:
                            print(Fore.WHITE + line.strip())
                            count += 1
                            if count >= 15: break
                except: print(Fore.RED + "[-] Could not access trace arrays.")
                
            elif choice == "24":
                try:
                    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
                    filepath = os.path.join(desktop, 'zcore_report.txt')
                    if os.path.exists(filepath):
                        os.remove(filepath)
                        print(Fore.GREEN + "[+] Target intelligence logs deleted.")
                    else: print(Fore.YELLOW + "[-] Report log already clean.")
                except: print(Fore.RED + "[-] Permission fault.")
                
            input("\nPress Enter to return to Matrix Panel...")
        except KeyboardInterrupt:
            input("\n[-] Process Interrupted. Press Enter...")
        except Exception as e:
            print(Fore.RED + f"\n[!] Matrix Error: {e}")
            input("\nPress Enter...")

if __name__ == "__main__":
    main()
