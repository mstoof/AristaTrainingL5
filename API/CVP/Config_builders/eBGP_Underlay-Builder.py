"""
This module generates interfaces code, this is just a templating agent.
You would still need to run these commands on the devices specified below.

The code is generated for the use of CVP on Arista platforms

V1 just generates code for 1 device,
V2 will generate interfaces information for both devices. 
"""


import yaml
config = """
leaf1-DC1:
  interfaces:
    loopback0:
        ipv4: 192.168.101.11
        mask: 32
    loopback1:
        ipv4: 192.168.102.11
        mask: 32
    Ethernet3:
        ipv4: 192.168.103.0
        mask: 31
    Ethernet4:
        ipv4: 192.168.103.2
        mask: 31
    Ethernet5:
        ipv4: 192.168.103.4
        mask: 31
leaf2-DC1:
  interfaces:
    loopback0: 
        ipv4: 192.168.101.12
        mask: 32
    loopback1: 
        ipv4: 192.168.102.11
        mask: 32
    Ethernet3:
        ipv4: 192.168.103.6
        mask: 31
    Ethernet4: 
        ipv4: 192.168.103.8
        mask: 31
    Ethernet5: 
        ipv4: 192.168.103.10
        mask: 31
"""
switches = yaml.load(config)

# Version 1.0
"""
for iface in switches['leaf1-DC1']['interfaces']:
#Iterate through all interfaces using iface variable as the incrementing index
    print("interface %s") % iface
#Pull variables into easier to use variables
    ip = switches['leaf1-DC1']['interfaces'][iface]['ipv4']
    mask = switches['leaf1-DC1']['interfaces'][iface]['mask']
    print(" ip address %s/%s") % (ip, mask)
"""

# Version 2.0 
"""    
#Iterate through all switches in the switches dictionary
for switch in switches:
    for iface in switches[switch]['interfaces']:
#Iterate through all interfaces using iface variable as the incrementing index
    print("interface %s") % iface
#Pull variables into easier to use variables
    ip = switches[switch]['interfaces'][iface]['ipv4']
    mask = switches[switch]['interfaces'][iface]['mask']
    print(" ip address %s/%s") % (ip, mask)
    if "Ethernet" in iface:
        print " no switchport"
"""
