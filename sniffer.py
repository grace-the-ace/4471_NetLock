import time
import os
import re
import pyshark
import io
import connector
from datetime import datetime


class scanner:
	def __init__(self):
		n=0

	def populate(self, mac_addresses,name_mac_addresses):
		now = datetime.now()
		timestamp = datetime.timestamp(now)
		students = name_mac_addresses.keys()
		notPresent = []
		for student in students:
			name, mac=student.split()
			if(mac in mac_addresses):
				name_mac_addresses[student]=True
			else:
				name_mac_addresses[student]=False
				notPresent.append(name)
				
		studentDict = present_students(name_mac_addresses)
					
		for absent in notPresent:
			studentDict.update({absent:"0min"})
		print(studentDict)



	def present_students(self, name_mac_addresses):
		presentStudents = {}
		students = name_mac_addresses.keys()
		for student in students:
			name, mac=student.split()
			if(name_mac_addresses[student]==True):
				presentStudents.update({name:"55min"})
		return presentStudents
				
		

	def scan(self):
		addresses = set()
		capture = pyshark.LiveCapture(interface='en0')
		mac_reg = re.compile("(Source: )([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})")
		mac_reg2 = re.compile("([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})")
		for packet in capture.sniff_continuously(packet_count=10):
			packet=str(packet)
			macAddress = re.search(mac_reg, packet).group()
			macAddress2 = re.search(mac_reg2, macAddress).group()
			if(macAddress2):
				addresses.add(macAddress2)
		
		return addresses


	con = connector.connect()
	addresses = scan()
	con.create_student_dict(addresses)
	# def end_class(name_mac_addresses):
	# 	now = datetime.now()
	# 	end= datetime.timestamp(now)
	# 	time_to_be_present=5
	# 	students = name_mac_addresses.keys()
	# 	for student in students:
	# 		name, mac=student.split()
	# 		if(name_mac_addresses[student]!=-1):
	# 			time_present=end-name_mac_addresses[student]
	# 			if(time_present>=time_to_be_present):
	# 				name_mac_addresses[student]=end-name_mac_addresses[student]
	# 			else:
	# 				name_mac_addresses[student]=-1

	# def begin_class():
	# 	start_of_class=0
	# 	now = datetime.now()
	# 	start_of_class= datetime.timestamp(now)





	# test = "achour.3 fc:33:42:10:90:30\nD'Avanzo.1 fc:33:42:12:60:20\ndiago.2 fc:33:42:12:60:20\npetzev.2 fc:33:42:12:60:20"
	# count = test.count('\n')
	# i = 0
	# buf = io.StringIO(test)
	# name_mac_add = {}
	# while (i < count+1):
	# 	list = []
	# 	line = buf.readline()
	# 	name_mac_add.update({line.strip('\n'):False})
	# 	i = i+1

	#print(name_mac_add)
		
	# addresses=set()
	# scan(addresses)
	# print(addresses)

	# populate(addresses,name_mac_add)
	#end_class(name_mac_add)
	#print(name_mac_add)
