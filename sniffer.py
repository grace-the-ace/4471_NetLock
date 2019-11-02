import time
import os
import re
import pyshark
import io


capture = pyshark.LiveCapture(interface='en0')
mac_reg = re.compile("(Source: )([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})");
mac_reg2 = re.compile("([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})");
addresses = set({})
for packet in capture.sniff_continuously(packet_count=100):
	packet=str(packet);
	macAddress = re.search(mac_reg, packet).group()
	macAddress2 = re.search(mac_reg2, macAddress).group()
	if(macAddress2):
		addresses.add(macAddress2)
		

print(addresses)