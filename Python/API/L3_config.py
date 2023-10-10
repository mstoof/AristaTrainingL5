import pyeapi

connect = pyeapi.connect_to("leaf1-DC1")

# Create will make the port automatically layer 3 (no switchport)
connect.api("ipinterfaces").create('Ethernet4') 


# Set the Ethernet4 for the IP address of 4.4.4.4 and put the result into a variable 

result = connect.api("ipinterfaces").set_address('Ethernet4', '4.4.4.4/24')

# Basic error handling 

if result == True:
    print("Completed")
if result == False:
    print(" Error! ")

