import time
import os
import re
import io


class connect:
    def __init__(self):
        pass

    #The present students are added to a dictionnary with the time they were present from
    #as the value and the name as the key
    def present_students(self, name_mac_addresses):
        presentStudents = {}
        students = name_mac_addresses.keys()
        for student in students:
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
            name, mac=student.split()
            if(mac in mac_addresses):
                name_mac_addresses[student]=True
            else:
                name_mac_addresses[student]=False
                notPresent.append(name)

        studentDict = self.present_students(name_mac_addresses)

        for absent in notPresent:
            studentDict.update({absent:"0min"})

        print(studentDict)

    
    #Retrieves the string with the students and MACs from the GUI and creates a dictionnary with the name
    #and MAC address as key and the value as prensent or absent (initialized to False for absent)
    def create_student_dict(self, addresses):
        studentNameMac = get_students(test)
        self.populate(addresses, name_mac_add)

    def get_sniffed_addresses(self, addresses){
        sniffed_addresses = addresses
        self.create_student_dict(sniffed_addresses)
    }

    def get_students(self, studentMac){
        studentMac = "achour.3 fc:33:42:10:90:30\nD'Avanzo.1 fc:33:42:12:60:20\ndiago.2 fc:33:42:12:60:20\npetzev.2 fc:33:42:12:60:20"
        count = test.count('\n')
        i = 0
        buf = io.StringIO(test)
        name_mac_add = {}
        while (i < count+1):
            list = []
            line = buf.readline()
            name_mac_add.update({line.strip('\n'):False})
            i = i+1

        return name_mac_add
    }
