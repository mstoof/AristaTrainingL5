import yaml
from cvplibrary import CVPGlobalVariables, GlobalVariableNames
hostname = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SERIAL)

config = """
DC1:
    subnets:
    - 192.168.101.0/24
    - 192.168.102.0/24
    - 192.168.103.0/24
    - 192.168.254.0/24
    devices: 
        Spine1-DC1:
            ASN: 65100
            interfaces: 
                loopback0:
                    ipv4: 192.168.101.101
                    mask: 32
                Ethernet2:
                    ipv4: 192.168.103.1
                    mask: 31
                Ethernet3:
                    ipv4: 192.168.103.7
                    mask: 31
                Ethernet4:
                    ipv4: 192.168.103.13
                    mask: 31
                Ethernet5: 
                    ipv4: 192.168.103.19
                    mask: 31
                Ethernet6: 
                    ipv4: 192.168.103.25
                    mask: 31
                Ethernet7: 
                    ipv4: 192.168.103.31
                    mask: 31
        Spine2-DC1:
            ASN: 65100  
            interfaces:
                loopback0:
                    ipv4: 192.168.101.102
                    mask: 32
                ethernet2: 
                    ipv4: 192.168.103.3
                    mask: 31
                ethernet3: 
                    ipv4: 192.168.103.9
                    mask: 31
                ethernet4:
                    ipv4: 192.168.103.15
                    mask: 31
                ethernet5: 
                    ipv4: 192.168.103.21
                    mask: 31
                ethernet6:
                    ipv4: 192.168.103.27
                    mask: 31
                ethernet7:
                    ipv4: 192.168.103.33
                    mask: 31
        Spine3-DC1:
            ASN: 65100
            interfaces:
                loopback0:
                    ipv4: 192.168.101.103
                    mask: 32
                ethernet2: 
                    ipv4: 192.168.103.5
                    mask: 31
                ethernet3: 
                    ipv4: 192.168.103.11
                    mask: 31
                ethernet4:
                    ipv4: 192.168.103.17
                    mask: 31
                ethernet5: 
                    ipv4: 192.168.103.23
                    mask: 31
                ethernet6:
                    ipv4: 192.168.103.29
                    mask: 31
                ethernet7:
                    ipv4: 192.168.103.35
                    mask: 31   
        Leaf1-DC1:
            ASN: 65101
            interfaces:
                loopback0:
                    ipv4: 192.168.101.11
                    mask: 32
                loopback1:
                    ipv4: 192.168.102.11
                    mask: 32
                ethernet3: 
                    ipv4: 192.168.103.0
                    mask: 31
                ethernet4:
                    ipv4: 192.168.103.2
                    mask: 31
                ethernet5: 
                    ipv4: 192.168.103.4
                    mask: 31
            spine_peers:
                - 192.168.103.1
                - 192.168.103.3
                - 192.168.103.5
        Leaf2-DC1:
            ASN: 65101
            interfaces:
                loopback0:
                    ipv4: 192.168.101.12
                    mask: 32
                loopback1:
                    ipv4: 192.168.102.11
                ethernet3: 
                    ipv4: 192.168.103.6
                    mask: 31
                ethernet4:
                    ipv4: 192.168.103.8
                    mask: 31
                ethernet5: 
                    ipv4: 192.168.103.10
                    mask: 31
            spine_peers:
                - 192.168.103.7
                - 192.168.103.9
                - 192.168.103.11 
        Leaf3-DC1:
            ASN: 65102
            interfaces:
                loopback0:
                    ipv4: 192.168.101.13
                    mask: 32
                loopback1:
                    ipv4: 192.168.102.13
                    mask: 32
                ethernet3: 
                    ipv4: 192.168.103.12
                    mask: 31
                ethernet4:
                    ipv4: 192.168.103.14
                    mask: 31
                ethernet5: 
                    ipv4: 192.168.103.16
                    mask: 31
            spine_peers:
                - 192.168.103.13
                - 192.168.103.15
                - 192.168.103.17
        Leaf4-DC1:
            ASN: 65102
            interfaces:
                loopback0:
                    ipv4: 192.168.101.14
                    mask: 32
                loopback1:
                    ipv4: 192.168.102.13
                    mask: 32
                ethernet3: 
                    ipv4: 192.168.103.18
                    mask: 31
                ethernet4:
                    ipv4: 192.168.103.20
                    mask: 31
                ethernet5: 
                    ipv4: 192.168.103.22
                    mask: 31
            spine_peers:
                - 192.168.103.19
                - 192.168.103.21
                - 192.168.103.23
        BorderLeaf1-DC1:
            ASN: 65103
            interfaces:
                loopback0:
                    ipv4: 192.168.101.21
                    mask: 32
                loopback1:
                    ipv4: 192.168.102.21
                    mask: 32
                ethernet3: 
                    ipv4: 192.168.103.24
                    mask: 31
                ethernet4:
                    ipv4: 192.168.103.26
                    mask: 31
                ethernet5: 
                    ipv4: 192.168.103.28
                    mask: 31
                ethernet12:
                    ipv4: 192.168.254.0
                    mask: 31
            spine_peers:
                - 192.168.103.25
                - 192.168.103.27
                - 192.168.103.29
        BorderLeaf2-DC1: 
            ASN: 65103
            interfaces:
                loopback0:
                    ipv4: 192.168.102.22
                    mask: 32
                loopback1:
                    ipv4: 192.168.102.21
                    mask: 32
                ethernet3: 
                    ipv4: 192.168.103.30
                    mask: 31
                ethernet4:
                    ipv4: 192.168.103.32
                    mask: 31
                ethernet5: 
                    ipv4: 192.168.103.34
                    mask: 31
                ethernet12:
                    ipv4: 192.168.254.2
                    mask: 31
            spine_peers:
                - 192.168.103.31
                - 192.168.103.33
                - 192.168.103.35
DC2:
    subnets:
    - 192.168.201.0/24
    - 192.168.202.0/24
    - 192.168.203.0/24
    - 192.168.254.0/24
    devices:
        Spine1-DC2:
            ASN: 65200
            interfaces: 
                loopback0:
                    ipv4: 192.168.201.101
                    mask: 32
                Ethernet2:
                    ipv4: 192.168.203.1
                    mask: 31
                Ethernet3:
                    ipv4: 192.168.203.7
                    mask: 31
                Ethernet4:
                    ipv4: 192.168.203.13
                    mask: 31
                Ethernet5: 
                    ipv4: 192.168.203.19
                    mask: 31
                Ethernet6: 
                    ipv4: 192.168.203.25
                    mask: 31
                Ethernet7: 
                    ipv4: 192.168.203.31
                    mask: 31
        Spine2-DC2:
            ASN: 65200
            interfaces:
                loopback0:
                    ipv4: 192.168.201.102
                    mask: 32
                ethernet2: 
                    ipv4: 192.168.203.3
                    mask: 31
                ethernet3: 
                    ipv4: 192.168.203.9
                    mask: 31
                ethernet4:
                    ipv4: 192.168.203.15
                    mask: 31
                ethernet5: 
                    ipv4: 192.168.203.21
                    mask: 31
                ethernet6:
                    ipv4: 192.168.203.27
                    mask: 31
                ethernet7:
                    ipv4: 192.168.203.33
                    mask: 31
        Spine3-DC2:
            ASN: 65200
            interfaces:
                loopback0:
                    ipv4: 192.168.201.103
                    mask: 32
                ethernet2: 
                    ipv4: 192.168.203.5
                    mask: 31
                ethernet3: 
                    ipv4: 192.168.203.11
                    mask: 31
                ethernet4:
                    ipv4: 192.168.203.17
                    mask: 31
                ethernet5: 
                    ipv4: 192.168.203.23
                    mask: 31
                ethernet6:
                    ipv4: 192.168.203.29
                    mask: 31
                ethernet7:
                    ipv4: 192.168.203.35
                    mask: 31   
        Leaf1-DC2:
            ASN: 65201
            interfaces:
                loopback0:
                    ipv4: 192.168.201.11
                    mask: 32
                loopback1:
                    ipv4: 192.168.202.11
                    mask: 32
                ethernet3: 
                    ipv4: 192.168.203.0
                    mask: 31
                ethernet4:
                    ipv4: 192.168.203.2
                    mask: 31
                ethernet5: 
                    ipv4: 192.168.203.4
                    mask: 31
            spine_peers:
                - 192.168.203.1
                - 192.168.203.3
                - 192.168.203.5
        Leaf2-DC2:
            ASN: 65201
            interfaces:
                loopback0:
                    ipv4: 192.168.201.12
                    mask: 32
                loopback1:
                    ipv4: 192.168.202.11
                ethernet3: 
                    ipv4: 192.168.203.6
                    mask: 31
                ethernet4:
                    ipv4: 192.168.203.8
                    mask: 31
                ethernet5: 
                    ipv4: 192.168.203.10
                    mask: 31
            spine_peers:
                - 192.168.203.7
                - 192.168.203.9
                - 192.168.203.11 
        Leaf3-DC2:
            ASN: 65202
            interfaces:
                loopback0:
                    ipv4: 192.168.201.13
                    mask: 32
                loopback1:
                    ipv4: 192.168.202.13
                    mask: 32
                ethernet3: 
                    ipv4: 192.168.203.12
                    mask: 31
                ethernet4:
                    ipv4: 192.168.203.14
                    mask: 31
                ethernet5: 
                    ipv4: 192.168.203.16
                    mask: 31
            spine_peers:
                - 192.168.203.13
                - 192.168.203.15
                - 192.168.203.17
        Leaf4-DC2:
            ASN: 65202
            interfaces:
                loopback0:
                    ipv4: 192.168.201.14
                    mask: 32
                loopback1:
                    ipv4: 192.168.202.13
                    mask: 32
                ethernet3: 
                    ipv4: 192.168.203.18
                    mask: 31
                ethernet4:
                    ipv4: 192.168.203.20
                    mask: 31
                ethernet5: 
                    ipv4: 192.168.203.22
                    mask: 31
            spine_peers:
                - 192.168.203.10
                - 192.168.203.21
                - 192.168.203.23
        BorderLeaf1-DC2:
            ASN: 65203 
            interfaces:
                loopback0:
                    ipv4: 192.168.201.21
                    mask: 32
                loopback1:
                    ipv4: 192.168.202.21
                    mask: 32
                ethernet3: 
                    ipv4: 192.168.203.24
                    mask: 31
                ethernet4:
                    ipv4: 192.168.203.26
                    mask: 31
                ethernet5: 
                    ipv4: 192.168.203.2
                    mask: 31
                ethernet12:
                    ipv4: 192.168.254.4
                    mask: 31
            spine_peers:
                - 192.168.203.2
                - 192.168.203.2
                - 192.168.203.2
        BorderLeaf2-DC2: 
            ASN: 65200
            interfaces:
                loopback0:
                    ipv4: 192.168.202.2
                    mask: 32
                loopback1:
                    ipv4: 192.168.202.2
                    mask: 32
                ethernet3: 
                    ipv4: 192.168.203.3
                    mask: 31
                ethernet4:
                    ipv4: 192.168.203.3
                    mask: 31
                ethernet5: 
                    ipv4: 192.168.203.3
                    mask: 31
                ethernet12:
                    ipv4: 192.168.254.6
                    mask: 31
            spine_peers:
                - 192.168.203.3
                - 192.168.203.3
                - 192.168.203.35    
"""

