from  tkinter import *
from tkinter import simpledialog

class Application(object):
    def __init__(self,master):
        self.master=master
        self.master.configure(background="#37474f")
        self.master.geometry("800x650+200+200")
        self.AddFormatting()
        self.AddButtons()

    def AddFormatting(self):
        self.TopFrame=Frame(self.master,bg="#7CBE5F",width=800,height=155)
        self.TopFrame.grid(column=0,row=1)

        self.title=Label(self.master,text="NetLock",bg="#7CBE5F",fg="#FFFFFF",font=("Georgia",40))
        self.title.place(x=25,y=100)

        #self.WhiteList=scrollTxtArea(self.master)
        
   
    def AddButtons(self):
        self.Register=Button(self.master,text="Start Class", width=20,height=4,bd=0,
            activeforeground="#fff",activebackground="#7CBE5F",command = self.StartCommand)
        self.Register.place(x=35,y=185)

        self.Request=Button(self.master,text="Stop Class", width=20,height=4,bd=0,
            activeforeground="#fff",activebackground="#7CBE5F",command=self.StopCommand)
        self.Request.place(x=35,y=305)

        self.Setup=Button(self.master,text="Setup", width=20,height=4,bd=0,
            activeforeground="#fff",activebackground="#7CBE5F",command=self.SetUpCommand)
        self.Setup.place(x=35,y=425)

    def StartCommand(self):
        self.ChooseClassCommand()

    def StopCommand(self):
        #calls function to stop mointering
        print("placeholder")
        #opens a table with names and minutes in class
        table=Tk()

    def SetUpCommand(self):
        classentry=Tk()
        self.TextArea=Text(master=classentry)
        Finish=Button(master=classentry,text="Finished",command=self.Test)
        self.TextArea.pack(expand=YES,fill=BOTH)
        Finish.pack()
        
    def Test(self):
        self.newclass=self.TextArea.get(1.0,END)
        print(self.newclass)
    def ChooseClassCommand(self):
        #child of main window
        child=Tk()
        classNum=3
        #list of the classes, if incremented by one then should start mointering class
        var=[]
        chooseclass=[]
        for i in range(classNum):
            var.append(IntVar())
            chooseclass.append(Checkbutton(child,text=i, variable=var[i]))
            chooseclass[i].grid(row=i,sticky=W)
        Enter=Button(child,text="Enter", command=child.destroy)
        Enter.grid(row=classNum,sticky=W)
    

#class scrollTxtArea:
    #def __init__(self,master):
        #self.master=master
        #self.frame=Frame(self.master)
    #def textArea(self,frame):
        #textArea=Frame(frame)
        #self.text=Text(textArea,height=90,width=50)

        #scroll=Scrollbar(textArea)
        #self.text.configure(yscrollcommand=scroll.set)

        
app=Tk()
Application=Application(app)
app.mainloop()
