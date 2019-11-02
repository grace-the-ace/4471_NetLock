import os
import re
# Be connected to your home network
# Run command line arp -a
os.system("arp -a > MACaddress.txt")
# Parse all the MAC addresses into a list
file = open('MACaddress.txt')
whitelist = open("Whitelist.txt", "r+")

#list of all the MAC addresses of all the devices on the network
list_mac_addresses=set({})
#regex to extract mac addresses from the file
mac_reg = re.compile("([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})")

#iterates over entire arp -a results
for line in file:
    macAddress = re.search(mac_reg, line)
    if macAddress:
        macAddress = macAddress.group()
        list_mac_addresses.add(macAddress)
#prints list of mac addresses
print(list_mac_addresses)


for line in whitelist:
    for mac in list_mac_addresses:
        # Notify admin of unauthorized device.
        if mac != line:
            whitelist.write(mac)

    file.close()
    whitelist.close()
    break
