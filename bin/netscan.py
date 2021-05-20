#/usr/bin/env python3

#imports
import scapy.all as scapy

#Functions
#Scan one ip
def scan(ip):
    scapy.arping(ip)

scan("10.10.10.28")
