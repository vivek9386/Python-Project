from calendar import c
from tkinter import *
from tkinter import ttk,filedialog
from turtle import bgcolor, right, width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os,csv,cv2
from time import strftime
from datetime import datetime
import numpy as np

myData = []

class Attendence:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #text variables
        self.varAttId = StringVar()        
        self.varAttRoll = StringVar()        
        self.varAttName = StringVar()        
        self.varAttDep = StringVar()        
        self.varAttTime = StringVar()        
        self.varAttDate = StringVar()        
        self.varAttAttendence = StringVar()        

        #image 1
        imgLeftMain = Image.open(r"Images\attendence1.jpg")
        imgLeftMain = imgLeftMain.resize((768,250),Image.ANTIALIAS)
        self.photoImgLeftMain = ImageTk.PhotoImage(imgLeftMain)
        
        f_lbl = Label(self.root,image=self.photoImgLeftMain)
        f_lbl.place(x = 0,y = 0,width=768,height=250)

        #image 2
        imgRightMain = Image.open(r"Images\attendence2.jpg")
        imgRightMain = imgRightMain.resize((768,200),Image.ANTIALIAS)
        self.photoImgRightMain = ImageTk.PhotoImage(imgRightMain)
        
        f_lbl = Label(self.root,image=self.photoImgRightMain)
        f_lbl.place(x = 768,y = 0,width=768,height=200)

        #Title
        title_lbl = Label(self.root,text="ATTENDENCE MANAGEMENT SYSTEM",font=("times new roman",33,"bold"),bg="Green",fg="white")
        title_lbl.place(x=0,y=200,width=1550,height=45)

        #mainFrame
        mainFrame = Frame(self.root,bd = 2,bg="white")
        mainFrame.place(x = 15, y = 245, width=1500, height=550)

        #LEFT FRAME
        leftFrame = LabelFrame(mainFrame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new Roman",12,"bold"))
        leftFrame.place(x = 10,y = 10, width=740,height=530)

        #imageLeft
        imgLeft = Image.open(r"Images\studentDash.jpg")
        imgLeft = imgLeft.resize((720,135),Image.ANTIALIAS)
        self.photoImgLeft = ImageTk.PhotoImage(imgLeft)
        
        f_lbl = Label(leftFrame,image=self.photoImgLeft)
        f_lbl.place(x = 5,y = 0,width=720,height=135)

        #leftInsideFrame
        leftInsideFrame = LabelFrame(leftFrame,bd=2,bg="white",relief=RIDGE)
        leftInsideFrame.place(x = 5,y = 180, width=720,height=250)

        #EntryFills
        attendenceId = Label(leftInsideFrame,text="Attendence Id:",font=("times new Roman",14, "bold"),bg="white")
        attendenceId.grid(row = 0,column = 0,padx=5,pady=10)

        attendenceIdEntry = ttk.Entry(leftInsideFrame,width=20,textvariable=self.varAttId,font=("times new roman",11,"bold"))
        attendenceIdEntry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #rollNumber
        roll = Label(leftInsideFrame,text="Roll Number:",font=("times new Roman",14, "bold"),bg="white")
        roll.grid(row = 0,column = 2,padx=5,pady=10)

        rollEntry = ttk.Entry(leftInsideFrame,width=20,textvariable=self.varAttRoll,font=("times new roman",11,"bold"))
        rollEntry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #Name
        name = Label(leftInsideFrame,text="Name:",font=("times new Roman",14, "bold"),bg="white")
        name.grid(row = 1,column = 0,padx=5,pady=10)

        nameEntry = ttk.Entry(leftInsideFrame,width=20,textvariable=self.varAttName,font=("times new roman",11,"bold"))
        nameEntry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #Date
        date = Label(leftInsideFrame,text="Date:",font=("times new Roman",14, "bold"),bg="white")
        date.grid(row = 1,column = 2,padx=5,pady=10)

        dateEntry = ttk.Entry(leftInsideFrame,width=20,textvariable=self.varAttDate,font=("times new roman",11,"bold"))
        dateEntry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        #Department
        department = Label(leftInsideFrame,text="Department:",font=("times new Roman",14, "bold"),bg="white")
        department.grid(row = 2,column = 0,padx=5,pady=10)

        departmentEntry = ttk.Entry(leftInsideFrame,width=20,textvariable=self.varAttDep,font=("times new roman",11,"bold"))
        departmentEntry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #Time
        time = Label(leftInsideFrame,text="Time:",font=("times new Roman",14, "bold"),bg="white")
        time.grid(row = 2,column = 2,padx=5,pady=10)

        timeEntry = ttk.Entry(leftInsideFrame,width=20,textvariable=self.varAttTime,font=("times new roman",11,"bold"))
        timeEntry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #Attendence Status
        attStatus = Label(leftInsideFrame,text="Attendence Status:",font=("times new Roman",14, "bold"),bg="white")
        attStatus.grid(row = 3,column = 0,padx=5,pady=10)

        self.attStatusCombo = ttk.Combobox(leftInsideFrame,width=18,textvariable=self.varAttAttendence,font=("times new roman",11,"bold"),state="readonly")
        self.attStatusCombo["values"] = ("Status","Present","Absent")
        self.attStatusCombo.current(0)
        self.attStatusCombo.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        #buttons Frame------------
        btnFrame = LabelFrame(leftInsideFrame,bd=2,bg="white",relief=RIDGE)
        btnFrame.place(x=2,y=210,width=710,height=32)

        importBtn = Button(btnFrame,text="Import CSV",command=self.importCsv,font=("times new Roman",12, "bold"),bg="blue",fg="white",width=25)
        importBtn.grid(row = 0,column=0)

        exportBtn = Button(btnFrame,text="Export CSV",command=self.exportCsv,font=("times new Roman",12, "bold"),bg="blue",fg="white",width=25)
        exportBtn.grid(row = 0,column=1)
        
        resetBtn = Button(btnFrame,text="Reset",command=self.resetData,font=("times new Roman",12, "bold"),bg="blue",fg="white",width=26)
        resetBtn.grid(row = 0,column=2)


        #----------------------Right frame-----------------
        rightFrame = LabelFrame(mainFrame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new Roman",12,"bold"))
        rightFrame.place(x = 760,y = 10, width=720,height=530)

        tableFrame = LabelFrame(rightFrame,bd=2,bg="white",relief=RIDGE)
        tableFrame.place(x=2,y=0,width=710,height=445)

        #scroll bar table

        scrollX = ttk.Scrollbar(tableFrame,orient=HORIZONTAL)
        scrollY = ttk.Scrollbar(tableFrame,orient=VERTICAL)

        self.AttendenceReportTable = ttk.Treeview(tableFrame,columns= ("id","roll","name","department","time","date","attendence"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)

        scrollX.pack(side=BOTTOM,fill=X) 
        scrollY.pack(side=RIGHT,fill=Y)

        scrollX.config(command=self.AttendenceReportTable.xview)
        scrollY.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="Attendence Id")
        self.AttendenceReportTable.heading("roll",text="Roll")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence")

        self.AttendenceReportTable["show"] = "headings"

        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)

        self.AttendenceReportTable.pack(fill=BOTH,expand=1)

        self.AttendenceReportTable.bind("<ButtonRelease>",self.getCursor)

    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)

    #import CSV
    def importCsv(self):
        global myData
        myData.clear()
        fln = filedialog.askopenfilename(initialdir = os.getcwd(),title="Open CSV",filetypes= (("CSV File","*.csv"),("All File","*.*")),parent=self.root)

        with open(fln) as myFile:
            csvread = csv.reader(myFile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)

    #Export CSV

    def exportCsv(self):
        try:
            if len(myData) < 1:
                messagebox.showerror("No Data","No Data Found to export",parent = self.root)
                return False
            
            fln = filedialog.asksaveasfilename(initialdir = os.getcwd(),title="Open CSV",filetypes= (("CSV File","*.csv"),("All File","*.*")),parent=self.root)

            with open(fln,mode="w",newline = "") as myFile:
                expWrite = csv.writer(myFile,delimiter=",")
                for i in myData:
                    expWrite.writerow(i)
                messagebox.showinfo("Data Export","Your Data is Exported to " + os.path.basename(fln)+ " successfully")

        except Exception as es:
            messagebox.showerror("Error",f"Due to : {str(es)}",parent = self.root)

    #Show in Entry Fields
    def getCursor(self,event = ""):
        cursorRow = self.AttendenceReportTable.focus()
        content = self.AttendenceReportTable.item(cursorRow)
        rows = content['values']
        self.varAttId.set(rows[0])
        self.varAttRoll.set(rows[1])
        self.varAttName.set(rows[2])
        self.varAttDep.set(rows[3])
        self.varAttTime.set(rows[4])
        self.varAttDate.set(rows[5])
        self.varAttAttendence.set(rows[6])

    #Reset Data

    def resetData(self):
        self.varAttId.set("")
        self.varAttRoll.set("")
        self.varAttName.set("")
        self.varAttDep.set("")
        self.varAttTime.set("")
        self.varAttDate.set("")
        self.varAttAttendence.set("Status")


if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()