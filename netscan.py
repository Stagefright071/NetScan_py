#!/usr/bin/env python3

#Imports
import scapy.all as scapy
import re
from mac_vendor_lookup import MacLookup
from scapy.data import PPI_CAPTURE_INFO

#Function to scan ip addresses
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    clients_list = []
    for element in answered_list:
        clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list

mac = MacLookup()

print('''
███╗░░██╗███████╗████████╗░██████╗░█████╗░░█████╗░███╗░░██╗
████╗░██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔══██╗████╗░██║
██╔██╗██║█████╗░░░░░██║░░░╚█████╗░██║░░╚═╝███████║██╔██╗██║
██║╚████║██╔══╝░░░░░██║░░░░╚═══██╗██║░░██╗██╔══██║██║╚████║
██║░╚███║███████╗░░░██║░░░██████╔╝╚█████╔╝██║░░██║██║░╚███║
╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝''')

print("\n")

#Main
choice = input("Would you like to:\n\n1. Scan an IP address\n\n2. Scan an IP range\n\n3. Update vendor sources (Requires Wifi)\n\n> ")

#Pattern to check if IP range is valid
range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

#Pattern to check if IP is valid
ip_pattern = re.compile("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$")

if choice == "1":
    print('''
██╗██████╗░  ░█████╗░██████╗░██████╗░██████╗░███████╗░██████╗░██████╗
██║██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
██║██████╔╝  ███████║██║░░██║██║░░██║██████╔╝█████╗░░╚█████╗░╚█████╗░
██║██╔═══╝░  ██╔══██║██║░░██║██║░░██║██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██║██║░░░░░  ██║░░██║██████╔╝██████╔╝██║░░██║███████╗██████╔╝██████╔╝
╚═╝╚═╝░░░░░  ╚═╝░░╚═╝╚═════╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░''')
    ip_address_chosen = input("\nEnter an IP address > ")
    if ip_pattern.search(ip_address_chosen):
        print("\nIP is valid, script can continue...\n")
    else:
        print("IP is not valid! Script will exit now...")
        exit(0)
    scan_result = scan(ip_address_chosen)
    print("IP" + "\t\t\t" + "MAC" + "\t\t\t" +"Vendor")
    for client in scan_result:
        print("------------------------------------------------------------------")
        print(client["ip"] + "\t\t" + client["mac"] + "\t" + MacLookup().lookup(client["mac"]))
elif choice == "2":
    print('''
██╗██████╗░  ██████╗░░█████╗░███╗░░██╗░██████╗░███████╗
██║██╔══██╗  ██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔════╝
██║██████╔╝  ██████╔╝███████║██╔██╗██║██║░░██╗░█████╗░░
██║██╔═══╝░  ██╔══██╗██╔══██║██║╚████║██║░░╚██╗██╔══╝░░
██║██║░░░░░  ██║░░██║██║░░██║██║░╚███║╚██████╔╝███████╗
╚═╝╚═╝░░░░░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝''')
    range_chosen = input("\nEnter an IP Range > ")
    if range_pattern.search(range_chosen):
        print("\nIP Range is valid, script can continue...\n")
    else:
        print("IP Range is not valid! Script will exit now...")
        exit(0)
    scan_result = scan(range_chosen)
    print("IP" + "\t\t\t" + "MAC" + "\t\t\t" + "Vendor")
    for client in scan_result:
        print("------------------------------------------------------------------")
        print(client["ip"] + "\t\t" + client["mac"] + "\t" + MacLookup().lookup(client["mac"]))
elif choice == "3":
    print("\nUpdating sources... This can take a few seconds...\n")
    mac = MacLookup()
    mac.update_vendors()
    print("Done!")

    def find_mac(mac_address):
        print(mac.lookup(mac_address))
else:
    print("Thats not a valid input, Please chose either 1 or 2!")

input("Press [ENTER] to exit")