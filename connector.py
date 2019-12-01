import time
import os
import re
import io
import sniffer


class connect:
    def __init__(self):
        self.dict = {}
        self.studentDict={}


    #The present students are added to a dictionnary with the time they were present from
    #as the value and the name as the key
    def present_students(self, name_mac_addresses):
        presentStudents = {}
        students = name_mac_addresses.keys()
        for student in students:
            if(len(student)>1):
                name, mac=student.split()
            if(name_mac_addresses[student]==True):
                presentStudents.update({name:"55min"})
        return presentStudents

    #Method to compare mac_addresses obtained to set name_mac_addresses
    #if the mac_address is contained in name_mac_addresses the student is marked present else absent
    def populate(self, mac_addresses, name_mac_addresses):
        students = name_mac_addresses.keys()
        
        notPresent = []
        for student in students:
            if(len(student)>1):
                name, mac=student.split()
            if(mac in mac_addresses):
                name_mac_addresses[student]=True
            else:
                name_mac_addresses[student]=False
                notPresent.append(name)

        #dict with name of student and how long present/absent
        self.studentDict = self.present_students(name_mac_addresses)

        for absent in notPresent:
            self.studentDict.update({absent:"0min"})

        


    def get_sniffed_addresses(self,addresses):
        sniffed_addresses = addresses
        self.create_student_dict(sniffed_addresses)

    def start(self): 
        self.get_sniffed_addresses(sniff.scan())

    def stop(self):
        return self.studentDict
    
    def get_students(self, studentMac):
        studentMac = studentMac
        #studentMac = "achour.3 94:f6:d6:d6:c3:18\nD'Avanzo.1 80:e6:50:0d:ca:a0\ndiago.2 fc:33:42:12:60:20\npetzev.2 fc:33:42:12:60:20"
        count = studentMac.count('\n')
        i = 0
        buf = io.StringIO(studentMac)
        #name_mac_add = {}
        while (i < count+1):
            list = []
            line = buf.readline()
            self.dict.update({line.strip('\n'):False})
            #name_mac_add.update({line.strip('\n'):False})
            i = i+1

    #Retrieves the string with the students and MACs from the GUI and creates a dictionnary with the name
    #and MAC address as key and the value as prensent or absent (initialized to False for absent)
    def create_student_dict(self, addresses):
        self.get_students("")
        self.populate(addresses, self.dict)

sniff = sniffer.scanner()
