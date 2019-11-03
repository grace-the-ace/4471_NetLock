#This class takes dictionaries of class sections and stores them in persistent files. These files are read into dictionaries at runtime to restore the class list without user intervention. 
#before termination, update the list with any class sections that have been changed. 
#call appropriate class method to retreive dictionary and set appropriate classSections index equal to that dictionary.
class dictionaries:
    def _init_(self, dictionary, section):
        self.dictionary = dictionary
        self.dictFile = "classList" + section + ".txt"
        self.classSections = []

    


    #list of dictionaries, each dictionary contains every student in a class section and their MAC address




    #after the dictionary is updated, update THAT dictionary file and that dictionary file only with the current dictionary.
    #each dictionary file must contain: 
    #           Student Name        Presence
    #for each student in the class section, where presence is determined by the most recent class section
    #potential enhancement area would be to add n dates of presense I.E
    #   Student Name       11/2/19      11/4/19     11/6/19
    #   diago.3            Present      Absent      Present
