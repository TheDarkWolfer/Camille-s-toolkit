#!/usr/bin/python

import socket, threading, requests, os, platform, ctypes
from scapy.all import IP, TCP, send, sniff

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'
INVERT = '\033[7m'
HIDE = '\033[8m'
STRIKETHROUGH = '\033[9m'
DEFAULT_FONT = '\033[10m'
FONT1 = '\033[11m'
FONT2 = '\033[12m'
FONT3 = '\033[13m'
FONT4 = '\033[14m'
FONT5 = '\033[15m'

def isAdmin():
    if platform.system() == 'Windows':
        try:
            return os.getuid() == 0
        except:
            return ctypes.windll.shell32.IsUserAnAdmin()
    elif platform.system() == 'Linux':
        return os.getuid() == 0
    elif platform.system() == 'Darwin':
        return os.getuid() == 0
    else:
        #print("Error : what the fuck is your OS ?!")
        return False
    
if not isAdmin():
    print(f"[{CYAN}🔍{RESET}] {BOLD}{RED}x_x{RESET} Error : you must be root to use this tool ! {BOLD}{RED}x_x{RESET}")
    exit()

def output(inputString,log=False):
    if log:
        with open('log.txt', 'a') as f:
            f.write(inputString)
    print(inputString)

def public_ip():
    response = requests.get('https://ipinfo.io/ip')
    ip = response.text.strip()
    return ip

def packet_handler(packet):
    if IP in packet and packet[IP].dst == public_ip():

        packet[IP].dst = public_ip()

        
        send(packet)

def start_packet_interception():
    sniff(filter='ip', prn=packet_handler)

interception_thread = threading.Thread(target=start_packet_interception)
interception_thread.start()
    
#=================================#
#=         PORT SCANNING         =#
#=================================#

def port_sweep(target_host, startPort:int, endPort:int,doLog=False):
    try:

        output(f"[{CYAN}🔍{RESET}] Scanning {GREEN}{target_host}{RESET} from port {GREEN}{startPort}{RESET} to {GREEN}{endPort}{RESET}...",log=doLog)

        for port in range(startPort,endPort):
            packet = IP(dst=target_host, src="192.168.0.123") / TCP(dport=port, flags="S")

            response = send(packet, verbose=False)
            
            output(f"[{CYAN}🔍{RESET}] Port {port} is {('open' if response[TCP].flags == 'SA' else 'closed')} \t\t\t [{port}:{(f'{GREEN}+{RESET}' if response[TCP].flags == 'SA' else f'{RED}-{RESET}')}]",log=doLog)

    except socket.error:
        output(f"[{CYAN}🔍{RESET}] {RED}x_x{RESET} socket error {RED}x_x{RESET}",log=doLog)

def single_scan(target_host, port, doLog=False):
    try:
        
        packet = IP(dst=target_host, src="192.168.0.123") / TCP(dport=port, flags="S")
        
        
        response = send(packet, verbose=False)

        
        if response and response.haslayer(TCP):
            if response[TCP].flags == "SA":
                output(f"[{CYAN}🔍{RESET}] Port {port} is open \t\t\t [{port}:{f'{GREEN}+{RESET}'}]", log=doLog)
            else:
                output(f"[{CYAN}🔍{RESET}] Port {port} is closed \t\t\t [{port}:{f'{RED}-{RESET}'}]", log=doLog)
        else:
            output(f"[{CYAN}🔍{RESET}] {RED}x_x{RESET} No response or unexpected response {RED}x_x{RESET}", log=doLog)
    except Exception as e:
        output(f"[{CYAN}🔍{RESET}] {RED}x_x{RESET} Error: {str(e)} {RED}x_x{RESET}", log=doLog)


def banner_grab(target_host, port, doLog=False):
    try:
        
        packet = IP(dst=target_host, src="192.168.0.123") / TCP(dport=port, flags="S")

        
        response = send(packet, verbose=False)

        
        if response and response.haslayer(TCP):
            if response[TCP].flags == "SA":
                output(f"[{CYAN}🔍{RESET}] Port {port} is open \t\t\t [{port}:{f'{GREEN}+{RESET}'}]", log=doLog)
                output(f"[{CYAN}🔍{RESET}] {GREEN}{response.summary()}{RESET}", log=doLog)
            else:
                output(f"[{CYAN}🔍{RESET}] Port {port} is closed \t\t\t [{port}:{f'{RED}-{RESET}'}]", log=doLog)
        else:
            output(f"[{CYAN}🔍{RESET}] {RED}x_x{RESET} No response or unexpected response {RED}x_x{RESET}", log=doLog)
    except Exception as e:
        output(f"[{CYAN}🔍{RESET}] {RED}x_x{RESET} Error: {str(e)} {RED}x_x{RESET}", log=doLog)




def main():

    command = input(f"[{CYAN}🔍{RESET}] Different options : \n\t1. Scan a single port\n\t2. Scan a range of ports\n\t3. Grab banner\n\t4. Exit\n[{CYAN}🔍{RESET}] Enter your choice : ")

    if command == "1":
        target_host = input(f"[{CYAN}🔍{RESET}] Enter the target host : ")
        port = int(input(f"[{CYAN}🔍{RESET}] Enter the port to scan : "))
        single_scan(target_host, port, doLog=True)
    elif command == "2":
        target_host = input(f"[{CYAN}🔍{RESET}] Enter the target host : ")
        startPort = int(input(f"[{CYAN}🔍{RESET}] Enter the start port : "))
        endPort = int(input(f"[{CYAN}🔍{RESET}] Enter the end port : "))
        port_sweep(target_host, startPort, endPort, doLog=True)
    elif command == "3":
        target_host = input(f"[{CYAN}🔍{RESET}] Enter the target host : ")
        port = int(input(f"[{CYAN}🔍{RESET}] Enter the port to scan : "))
        banner_grab(target_host, port, doLog=True)
    elif command == "4":
        exit()
    else:
        output(f"[{CYAN}🔍{RESET}] {RED}x_x{RESET} Invalid command {RED}x_x{RESET}")

if __name__ == "__main__":
    while True:
        main()