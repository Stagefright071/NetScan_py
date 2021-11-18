# NetScan_py
This is a network scanner that finds out:
1. IP address
2. MAC address
3. Vendor Manufacturer)

```
╭─compromyse@Aspire ~/Projects/NetScan_py ‹main› 
╰─$ sudo python3 netscan.py                                                                                                                               
[sudo] password for compromyse: 

███╗░░██╗███████╗████████╗░██████╗░█████╗░░█████╗░███╗░░██╗
████╗░██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔══██╗████╗░██║
██╔██╗██║█████╗░░░░░██║░░░╚█████╗░██║░░╚═╝███████║██╔██╗██║
██║╚████║██╔══╝░░░░░██║░░░░╚═══██╗██║░░██╗██╔══██║██║╚████║
██║░╚███║███████╗░░░██║░░░██████╔╝╚█████╔╝██║░░██║██║░╚███║
╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝


Would you like to:

1. Scan an IP address

2. Scan an IP range

3. Update vendor sources (Requires Wifi)

> 2

██╗██████╗░  ██████╗░░█████╗░███╗░░██╗░██████╗░███████╗
██║██╔══██╗  ██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔════╝
██║██████╔╝  ██████╔╝███████║██╔██╗██║██║░░██╗░█████╗░░
██║██╔═══╝░  ██╔══██╗██╔══██║██║╚████║██║░░╚██╗██╔══╝░░
██║██║░░░░░  ██║░░██║██║░░██║██║░╚███║╚██████╔╝███████╗
╚═╝╚═╝░░░░░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝

Enter an IP Range > 192.168.1.0/24

IP Range is valid, script can continue...

IP			MAC			Vendor
------------------------------------------------------------------
192.168.1.254		00:11:22:33:44:55	CIG SHANGHAI CO LTD
------------------------------------------------------------------
192.168.1.48		00:11:22:33:44:66	Intel Corporate
------------------------------------------------------------------
192.168.1.27		00:11:22:33:44:77	Zebra Technologies Inc.
------------------------------------------------------------------
192.168.1.12		00:11:22:33:44:88	Espressif Inc.
------------------------------------------------------------------
192.168.1.13		00:11:22:33:44:99	Espressif Inc.
------------------------------------------------------------------
192.168.1.28		00:11:22:33:44:00	Amazon Technologies Inc.

Press [ENTER] to exit

```

<!-- windows requires npcap -->

# Running

## Linux
> Install python and git
```
Debian / Ubuntu based: $ sudo apt install python3 python3-pip git

Arch based: $ sudo pacman -S python python-pip
```

> Clone git repository
```
git clone https://github.com/compromyse/NetScan_py
```

> Install script requirements
```
python3 -m pip install -r requirements.txt
```

> Run the script as **root**
```
sudo python3 netscan.py
```

## Windows

> Install python, git and npcap

Download and install python from https://python.org

Download and install git from https://git-scm.com

Download and install npcap from https://nmap.org/npcap

### **Do this in a command prompt running as administrator**

> Clone git repository
```
git clone https://github.com/compromyse/NetScan_py
```

> Install script requirements
```
python -m pip install -r requirements.txt
```

> Run the script as **administrator**
```
python netscan.py
```

# Thanks!
