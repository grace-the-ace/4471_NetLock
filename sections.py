from datetime import date

#this class allows class section objects to be created. The class section object will contain all the information about the class section being modified during runtime.
#THere will be functions that can be called as methods on the object to print the current class section and attendance to a file. 

class classSection:

    def __init__(self, section, number):
        self.dictionary = section
        self.section = number
        self.fileName = open(f"section{number}", 'w+')

    def output(self):
        self.fileName.write(f"Student Attendance for {date.today()} \n")

        for student in self.dictionary:
            if self.dictionary[student]:
                presence = "Present"
            else:
                presence = "Absent"
            self.fileName.write(f'{student.split()[0]}      {presence} \n')
        



