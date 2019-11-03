import time
import os
import re
import pyshark
import io
from datetime import datetime

start_of_class=0
time_to_be_present=5;

def populate(mac_addresses,name_mac_addresses):
	now = datetime.now()
	timestamp = datetime.timestamp(now)
	students = name_mac_addresses.keys()
	for student in students:
		name, mac=student.split()
		if(mac in mac_addresses):
			name_mac_addresses[student]=True
		else:
			name_mac_addresses[student]=False
	
	present_students(name_mac_addresses)

def present_students(name_mac_addresses):
	presentStudents = set({})
	students = name_mac_addresses.keys()
	for student in students:
		if(name_mac_addresses[student]==True):
			presentStudents.add(student)
	
	return presentStudents
			
	

def scan(addresses):
	capture = pyshark.LiveCapture(interface='en0')
	mac_reg = re.compile("(Source: )([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})")
	mac_reg2 = re.compile("([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})")
	for packet in capture.sniff_continuously(packet_count=100):
		packet=str(packet)
		macAddress = re.search(mac_reg, packet).group()
		macAddress2 = re.search(mac_reg2, macAddress).group()
		if(macAddress2):
			addresses.add(macAddress2)
		
def end_class(name_mac_addresses):
	now = datetime.now()
	end= datetime.timestamp(now)
	students = name_mac_addresses.keys()
	for student in students:
		name, mac=student.split()
		if(name_mac_addresses[student]!=-1):
			time_present=end-name_mac_addresses[student]
			if(time_present>=time_to_be_present):
				name_mac_addresses[student]=end-name_mac_addresses[student]
			else:
				name_mac_addresses[student]=-1

def begin_class():
	now = datetime.now()
	start_of_class= datetime.timestamp(now)





addresses=set()

test = "achour.3 fc:33:42:10:90:30\nD'Avanzo.1 fc:33:42:12:60:20\ndiago.2 fc:33:42:12:60:20\npetzev.2 fc:33:42:12:60:20"
count = test.count('\n')
i = 0
buf = io.StringIO(test)
name_mac_add = {}
while (i < count+1):
	list = []
	line = buf.readline()
	name_mac_add.update({line.strip('\n'):False})
	i = i+1

#print(name_mac_add)
	

scan(addresses)
print(addresses)

populate(addresses,name_mac_add)
time.sleep(4)
end_class(name_mac_add)
#print(name_mac_add)

