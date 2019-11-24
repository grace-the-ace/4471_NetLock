from  tkinter import *
from tkinter import simpledialog
import tkinter.ttk as ttk
import connector
#import sniffer

class Application(object):
    def __init__(self,master):
        self.master=master
        self.master.title("NetLock")
        self.master.configure(background="#37474f")
        self.master.geometry("800x650+200+200")
        self.AddFormatting()
        self.AddButtons()

    def AddFormatting(self):
        self.SideFrame=Frame(self.master,bg="#54705b",width=230,height=800)
        self.SideFrame.place(x=0,y=0)

        self.SideLine=Frame(self.master,bg="#e3e3e3",width=4,height=800)
        self.SideLine.place(x=230,y=0)

        self.TopFrame=Frame(self.master,bg="#65994e",width=800,height=120)
        self.TopFrame.grid(column=0,row=1)

        self.TopLine=Frame(self.master,bg="#e3e3e3",width=800,height=4)
        self.TopLine.place(x=0,y=120)

        self.title=Label(self.master,text="NetLock",bg="#65994e",fg="#e3e3e3",font=("Georgia",55))
        self.title.place(x=37,y=42)
        #TODO 
        #after Start pressed begin updating object classList
        self.scrollBar=Scrollbar(self.master)

        self.classList=Text(self.master,yscrollcommand=self.scrollBar.set)
        self.classList.configure(state=DISABLED,height=22,width=40)
        self.classList.place(x=400,y=235)
        
        self.listTitle=Label(self.master,text="Currently In Class", font=("Georgia",17),bg="#37474f",fg="#7CBE5F")
        self.listTitle.place(x=397,y=206)
    def AddButtons(self):
        #creates and places the Start, Stop, and SetUp Buttons
        #Start begins the mointering of the selected class
        self.Start=Button(self.master,text="Start Class", font="Georgia",width=20,height=4,bd=0,
            activeforeground="#fff",activebackground="#7CBE5F",command = self.StartCommand)
        self.Start.place(x=35,y=220)
        #Stop stops any classes being currently mointered and prints the results
        self.Stop=Button(self.master,text="Stop Class", width=20,height=4,bd=0,font="Georgia",
            activeforeground="#fff",activebackground="#7CBE5F",command=self.StopCommand)
        self.Stop.place(x=35,y=350)
        #Setup allows you to add another class the application can mointer
        self.Setup=Button(self.master,text="Setup", width=20,height=4,bd=0,font="Georgia",
            activeforeground="#fff",activebackground="#7CBE5F",command=self.SetUpCommand)
        self.Setup.place(x=35,y=480)
    #Command executes when Start button pressed
    def StartCommand(self):
        #opens a new window
        child=Tk()
        child.geometry("130x200+350+300")
        child.configure(background="#37474f")
        #number of class variables created in setup
        #placeholder
        classNum=3
        #list of vars for each class
        #if incremented then mointering needs to begin
        var=[]
        #frame to make it look purty
        
        #list of checkbuttons
        chooseclass=[]
        #creates lists
        for i in range(classNum):
            var.append(IntVar())
            chooseclass.append(Checkbutton(child,text=("Class "+str(i)), variable=var[i],font="Georgia",fg="#7CBE5F",bg="#37474f"))
            chooseclass[i].pack(side=TOP)
        #creates button to enter which class will begin mointering
        #exits the window
        Enter=Button(child,text="Enter", command=child.destroy,font="Georgia",fg="#7CBE5F",bg="#37474f")
        Enter.pack()
        
        con.start()
        #TODO
        #take the list of var[] and use this to begin mointering of the appropriate classes
        #TODO
        #update list display
    
    #Command called when stop button is pressed
    def StopCommand(self):
        #TODO
        #calls function to stop mointering
        print("placeholder")
        #TODO
        #opens a table with names and minutes in class
        table=Tk()
    #Command called when setup button is pressed
    def SetUpCommand(self):
        #opens a new window
        classentry=Tk()
        classentry.configure(background="#37474f")
        #creates text entry area
        TextArea=Text(master=classentry,width=80,height=35)
        #instructions for data entry
        TextArea.insert(END,"Please enter the data in the following format: name.number MACaddress.\nPress enter after each entry and Finish once it is complete.\n")
        #creates button to be pressed after all data is entered
        Finish=Button(master=classentry,text="Finished",command=lambda: self.CreateNewClass(classentry, TextArea)
            ,bg="#37474f",fg="#7CBE5F",width=6,height=2,font=("Georgia",17))
        Finish.pack(side=BOTTOM)
        #creates frames around textbox
        topFrame=Frame(master=classentry,bg="#37474f",width=500,height=10)
        topFrame.pack(side=TOP)
        leftFrame=Frame(master=classentry,bg="#37474f",width=10,height=500)
        leftFrame.pack(side=LEFT)
        rightFrame=Frame(master=classentry,bg="#37474f",width=10,height=500)
        rightFrame.pack(side=RIGHT)
        TextArea.pack(expand=YES,fill=NONE,side=TOP)
        
        #TODO
        #Format finish button better
    #creates a new class from the entered data
    def CreateNewClass(self,window, text):
        #this is the string!!!

        newclass=text.get(3.0,END)

        


        con.get_students(newclass)
        #sniff=sniffer.scanner()
        
        #add new class to data structure of classes
        #can assume set up will be each line as a name a space and then the MAC address
        #TODO
        print(newclass)
        window.destroy()



con = connector.connect()        
app=Tk()
Application=Application(app)
app.mainloop()
