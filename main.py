#!/usr/bin/env python3
import requests
import json
from colorama import Fore
from colorama import Style
import colorama
import os
from phonenumbers import geocoder, carrier, timezone
import phonenumbers
import socket
from scapy.all import IP, TCP, sr1, send
import ipVerify

class titles:
    @staticmethod
    def option():
        print(Fore.GREEN + Style.BRIGHT + """

░██████╗░███████╗░█████╗░██████╗░██████╗░░█████╗░██████╗░███████╗
██╔════╝░██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██╗░█████╗░░██║░░██║██████╔╝██████╔╝██║░░██║██████╦╝█████╗░░
██║░░╚██╗██╔══╝░░██║░░██║██╔═══╝░██╔══██╗██║░░██║██╔══██╗██╔══╝░░
╚██████╔╝███████╗╚█████╔╝██║░░░░░██║░░██║╚█████╔╝██████╦╝███████╗
░╚═════╝░╚══════╝░╚════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝
                                                                                

        *    
       ***   
      *****  
     *******               
    *********  
   ***********              _|==|_  
  *************              ('')___/                             
       |||               >--(`^^')                                                     
       |||                 (`^'^'`)   
       |||                 `======'                                                      
-----------------------------------------                                         
        
[ 1 ]: IP Geo Tracker
[ 2 ]: Phonenumber Locate
[ 3 ]: Show your IP address
[ 4 ]: Port scanner
[ 5 ]: SSM Osint
[ 0 ]: Exit
            """)  
    
    @staticmethod
    def portScanOption():
        print(Fore.GREEN + Style.BRIGHT +  """
█▀█ █▀█ █▀█ ▀█▀   █▀ █▀▀ ▄▀█ █▄░█
█▀▀ █▄█ █▀▄ ░█░   ▄█ █▄▄ █▀█ █░▀█
        
[ 1 ]: Full Handshake
[ 2 ]: Half open Handshake
[ 0 ]: Exit to main menu        
            """)

    @staticmethod
    def accountOsint():
        print(Fore.GREEN + Style.BRIGHT + """
█▀ █▀ █▀▄▀█   █▀█ █▀ █ █▄░█ ▀█▀
▄█ ▄█ █░▀░█   █▄█ ▄█ █ █░▀█ ░█░

[ 1 ]: Enter username
[ 0 ]: Exit to main menu

        """)

class scanOptions:
    def __init__(self):
        self.common_ports = {
            20: "FTP Data Transfer",
            21: "FTP Control",
            22: "SSH (Secure Shell)",
            23: "Telnet",
            25: "SMTP (Simple Mail Transfer Protocol)",
            53: "DNS (Domain Name System)",
            80: "HTTP (HyperText Transfer Protocol)",
            110: "POP3 (Post Office Protocol v3)",
            119: "NNTP (Network News Transfer Protocol)",
            123: "NTP (Network Time Protocol)",
            143: "IMAP (Internet Message Access Protocol)",
            161: "SNMP (Simple Network Management Protocol)",
            194: "IRC (Internet Relay Chat)",
            443: "HTTPS (HTTP Secure)",
            465: "SMTPS (SMTP Secure)",
            514: "Syslog",
            587: "SMTP (Mail Submission)",
            636: "LDAPS (LDAP Secure)",
            993: "IMAPS (IMAP Secure)",
            995: "POP3S (POP3 Secure)",
            1433: "Microsoft SQL Server",
            1521: "Oracle Database",
            3306: "MySQL",
            3389: "Remote Desktop Protocol (RDP)",
            5432: "PostgreSQL",
            5900: "VNC (Virtual Network Computing)",
            8080: "HTTP Proxy / Alternative HTTP",
        }
    def fullScan(self, ip):
        ipVER = ipVerify.fullVerify(ip)
        #all_ports = input("All ports are common ports(RECOMMENDED)? (A/C)- > ")

        if not ipVER:
            print(Fore.RED + "IP" + Fore.WHITE + "address" + Fore.RED + "INVALID")
            print(Fore.RED + "ERROR: " + Fore.WHITE + "IP Address " + Fore.RED + ip + Fore.YELLOW + " is " + Fore.WHITE + "unreachable")
            print(Fore.WHITE + "Press " + Fore.RED + "ENTER " + Fore.WHITE + "to go back to the " + Fore.RED + "Menu")
            input("")
            os.system("clear")
            main()
        else:
            print(Fore.RED+"IP "+Fore.WHITE+"address "+Fore.GREEN+"VALID")
  

        #################################### PORT SCAN ####################################


        # Ask user for scanning preference
        all_ports = input("All ports or common ports (RECOMMENDED)? (A/C) -> ").strip().lower()

        # Full port range for "A" and common ports for "C"
        if all_ports == "a":
            port_range = range(1, 65536)  # Full range of ports
        elif all_ports == "c":
            port_range = self.common_ports.keys()  # Use dictionary keys for common ports
        else:
            print(Fore.RED + "ERROR: " + Fore.BLUE + Style.BRIGHT + "WRONG INPUT FIELD")
            print(Fore.WHITE + "Press " + Fore.RED + "ENTER " + Fore.WHITE + "to go back to the " + Fore.RED + "Menu")
            input("")
            os.system("clear")
            main()
            return  # Exit the function

        # Perform port scanning
        for port in port_range:
            try:
                serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                serv.settimeout(0.5)
                if serv.connect_ex((ip, port)) == 0:  # Port is open
                    port_name = self.common_ports.get(port, "Unknown")  # Get port name if available
                    print(Fore.GREEN + f"[OPEN] Port {port} is open || {port_name}")
                serv.close()  # Close connection
            except Exception as e:
                print(Fore.RED + f"Error scanning port {port}: {e}")

        print(Fore.WHITE + "Press " + Fore.RED + "ENTER " + Fore.WHITE + "to go back to the " + Fore.RED + "Menu")
        input("")
        os.system("clear")
        main()
        return


# ================================== HALF OPEN SCAN ==================================
    def syn_scan(self, ip):
        ipVER = ipVerify.fullVerify(ip)

        #all_ports = input("All ports are common ports(RECOMMENDED)? (A/C)- > ")

        if not ipVER:
            print(Fore.RED + "IP" + Fore.WHITE + "address" + Fore.RED + "INVALID")
            print(Fore.RED + "ERROR: " + Fore.WHITE + "IP Address " + Fore.RED + ip + Fore.YELLOW + " is " + Fore.WHITE + "unreachable")
            print(Fore.WHITE + "Press " + Fore.RED + "ENTER " + Fore.WHITE + "to go back to the " + Fore.RED + "Menu")
            input("")
            os.system("clear")
            main()
        else:
            print(Fore.RED+"IP "+Fore.WHITE+"address "+Fore.GREEN+"VALID")
  
        # Ask user for scanning preference
        all_ports = input("All ports or common ports (RECOMMENDED)? (A/C) -> ").strip().lower()

        # Full port range for "A" and common ports for "C"
        if all_ports == "a":
            port_range = range(1, 65536)  # Full range of ports
        elif all_ports == "c":
            port_range = self.common_ports.keys()  # Use dictionary keys for common ports
        else:
            print(Fore.RED + "ERROR: " + Fore.BLUE + Style.BRIGHT + "WRONG INPUT FIELD")
            print(Fore.WHITE + "Press " + Fore.RED + "ENTER " + Fore.WHITE + "to go back to the " + Fore.RED + "Menu")
            input("")
            os.system("clear")
            main()
            return  # Exit the function
        
        for port in port_range:
            try:
                # Create a SYN packet
                syn_packet = IP(dst=ip)/TCP(dport=port, flags="S")
                # Send the packet and receive the response
                response = sr1(syn_packet, timeout=2, verbose=0)

                if response is not None: 
                    if response.haslayer(TCP):
                        if response[TCP].flags == 0x12:  # SYN-ACK flag
                            port_name = self.common_ports.get(port, "Unknown")  # Get port name if available
                            print(Fore.GREEN + f"[OPEN] Port {port} is open || {port_name}")
                            # Send a RST packet to close the connection
                            rst_packet = IP(dst=ip)/TCP(dport=port, flags="R")
                            send(rst_packet, verbose=0)
            except Exception as ex:
                print(Fore.RED + "ERROR: " + Fore.BLUE + Style.BRIGHT + f"SCANNING PORT {port}: {ex}")
                print(Fore.RED + "RUN AS " + Fore.BLUE + Style.BRIGHT + f"ADMIN")
                break

        print(Fore.WHITE + "Press " + Fore.RED + "ENTER " + Fore.WHITE + "to go back to the " + Fore.RED + "Menu")
        input("")
        os.system("clear")
        main()
        return



class Tracker:
    @staticmethod
    def phonTrack():
        PNUM = input("Phone number -> ")
        
        try:
            parsed_num = phonenumbers.parse(PNUM)
            
            # Get location (country/region)
            location = geocoder.description_for_number(parsed_num, "en")
            
            # Get carrier (if available)
            sim_carrier = carrier.name_for_number(parsed_num, "en")
            
            # Get time zone
            time_zones = timezone.time_zones_for_number(parsed_num)
            
            print("\nTracking Information:")
            print(f"Location: {location}")
            print(f"Carrier: {sim_carrier if sim_carrier else 'Unknown'}")
            print(f"Time Zone(s): {', '.join(time_zones)}")
    
            print(Fore.WHITE + "Press " + Fore.RED + "ENTER " + Fore.WHITE + "to go back to the " + Fore.RED + "Menu")
            input("")
            os.system("clear")
            main()
            return
        
        except phonenumbers.NumberParseException:
            print("Invalid phone number format. Please include the country code.")
            print(Fore.WHITE + "Press " + Fore.RED + "ENTER " + Fore.WHITE + "to go back to the " + Fore.RED + "Menu")
            input("")
            os.system("clear")
            main()
            return
        
    @staticmethod
    def req_IPADDR():
        IP = input("Enter Ip addr -> ")
        
        API = "http://ip-api.com/json/"
        
        OUT = requests.get(API + IP) # GET THE WEBSITE
        
        OUT_JSON = OUT.json() # PRINT OUT THE JSON TO PARSE
        
        if OUT.status_code == 200:
            print(Fore.RED + json.dumps(OUT_JSON, indent=4))
            print(Fore.WHITE + "Press " + Fore.RED + "ENTER " + Fore.WHITE + "to go back to the " + Fore.RED + "Menu")
            input("")
            os.system("clear")
            main()
            return
            
        else:
            print("ERROR")
    
    @staticmethod
    def showIpADDR():
        os.system("curl https://icanhazip.com")
        print(Fore.WHITE + "Press " + Fore.RED + "ENTER " + Fore.WHITE + "to go back to the " + Fore.RED + "Menu")
        input("")
        os.system("clear")
        main()
        
    @staticmethod
    def PORTSCAN():
        t = titles()
        scanner = scanOptions()
        t.portScanOption()
        op = input("- > ")

        if op == "1":
            ip = input("Enter IP Address -> ")
            scanner.fullScan(ip)

        if op == "2":
            ip = input("Enter Ip Address -> ")
            scanner.syn_scan(ip)

class osint:
    def __init__(self):
        self.websiteList = [
            "https://www.facebook.com",
            "https://www.instagram.com",
            "https://www.twitter.com",
            "https://www.tiktok.com",
            "https://www.snapchat.com",
            "https://www.linkedin.com",
            "https://www.youtube.com",
            "https://www.reddit.com",
            "https://www.pinterest.com",
            "https://www.whatsapp.com",
            "https://www.telegram.org",
            "https://www.discord.com",
            "https://www.twitch.tv",
            "https://www.threads.net",
            "https://www.wechat.com",
            "https://www.imqq.com",
            "https://www.tumblr.com",
            "https://www.joinmastodon.org",
            "https://www.vk.com",
            "https://www.clubhouse.com",
            "https://www.bereal.com",
            "https://www.byte.co",
            "https://www.triller.co",
            "https://www.rumble.com",
            "https://www.gab.com",
            "https://www.mewe.com"
        ]
    
    def search(self):
        l = titles()
        l.accountOsint()

        ans = input("- > ")

        if ans == "1":
            username = input("Username - > ")
        elif ans == "0":
            os.system("clear")
            main()
        else:
            print(Fore.RED + "ERROR: " + Fore.BLUE + Style.BRIGHT + "WRONG INPUT FIELD")

        for w in self.websiteList:
            try:
                url = f"{w}/{username}"
                connection = requests.get(url)
                if connection.status_code == 200:
                    f = Fore.BLUE + Style.BRIGHT + f"{url} || " + Fore.GREEN + Style.BRIGHT + "TRUE"
                    print(f)
                else:
                    f = Fore.BLUE + Style.BRIGHT +  f"{w} || " + Fore.RED + Style.BRIGHT + "FALSE"
                    print(f)
            except requests.ConnectionError as ex:
                pass

        print(Fore.WHITE + "Press " + Fore.RED + "ENTER " + Fore.WHITE + "to go back to the " + Fore.RED + "Menu")
        input("")
        os.system("clear")
        main()


def main():
    if os.geteuid() != 0:
        print(Fore.RED + "ERROR: " + Fore.BLUE + Style.BRIGHT + "RUN AS ADMIN")
        exit()
    else:
        pass

    l = titles()
    track = Tracker()
    o = osint()
    colorama.init()
    
    l.option()

    
    ans = input("- > ")
    
    if ans == "1": # track ip address
        os.system("clear")
        track.req_IPADDR()

    elif ans == "2": # phone number track
        os.system("clear")
        track.phonTrack()

    elif ans == "3": # show the users ip addr
        os.system("clear")
        track.showIpADDR()

    elif ans == "4": # Port scan
        os.system("clear")
        track.PORTSCAN()
    elif ans == "5": # SSM Osint
        os.system("clear")
        o.search()

    elif ans == "0":
        os.system("clear")
        exit()
        
    else:
        print(Fore.RED + "ERROR: " + Fore.BLUE + Style.BRIGHT + "WRONG INPUT FIELD")
        print(Fore.WHITE + "Press " + Fore.RED + "ENTER " + Fore.WHITE + "to go back to the " + Fore.RED + "Menu")
        input("")
        os.system("clear")
        main()

if __name__ == "__main__":
    main()
