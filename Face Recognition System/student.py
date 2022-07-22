from tkinter import *
from tkinter import ttk
from datetime import datetime
from time import strftime
from turtle import bgcolor, right, width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #Variables creation

        self.varDep = StringVar()
        self.varCourse = StringVar()
        self.varYear = StringVar()
        self.varSemester = StringVar()
        self.varStdId = StringVar()
        self.varStdName = StringVar()
        self.varDiv = StringVar()
        self.varRoll = StringVar()
        self.varGender = StringVar()
        self.varDob = StringVar()
        self.varEmail = StringVar()
        self.varPhone = StringVar()
        self.varAddress = StringVar()
        self.varTeacher = StringVar()

        # img1
        img = Image.open(r"Images\student1.webp")
        img = img.resize((500,135),Image.ANTIALIAS)
        self.photoImg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root,image=self.photoImg)
        f_lbl.place(x = 0,y = 0,width=500,height=135)

        # img2
        img1 = Image.open(r"Images\student2.jpg")
        img1 = img1.resize((500,135),Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoImg1)
        f_lbl.place(x = 500,y = 0,width=500,height=135)

        # img3
        img2 = Image.open(r"Images\student3.jpg")
        img2 = img2.resize((540,135),Image.ANTIALIAS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root,image=self.photoImg2)
        f_lbl.place(x = 1000,y = 0,width=540,height=135)

        # -------------------------------------

        # bg - img
        img3 = Image.open(r"Images\bgImg.jpg")
        img3 = img3.resize((1550,790),Image.ANTIALIAS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root,image=self.photoImg3)
        bg_img.place(x = 0,y = 135,width=1550,height=670)

        # ----------------------------
        # Title Label
        title_lbl = Label(bg_img,text="Student Management System",font=("times new roman",33,"bold"),bg="purple",fg="white")
        title_lbl.place(x=0,y=0,width=1550,height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl = Label(title_lbl,font=("time new roman",14,"bold"),background = "Purple",foreground="white")
        lbl.place(x = 5,y = 0,width=110,height=50)
        time()

        # -----------------------------------------

        #MainFrame
        mainFrame = Frame(bg_img,bd = 2,bg="white")
        mainFrame.place(x = 15, y = 55, width=1500, height=600)

        # All these Frames Are nested inside each other

        #left Label Frame
        leftFrame = LabelFrame(mainFrame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new Roman",12,"bold"))
        leftFrame.place(x = 10,y = 10, width=740,height=580)

        imgLeft = Image.open(r"Images\studentDash.jpg")
        imgLeft = imgLeft.resize((720,135),Image.ANTIALIAS)
        self.photoImgLeft = ImageTk.PhotoImage(imgLeft)
        
        f_lbl = Label(leftFrame,image=self.photoImgLeft)
        f_lbl.place(x = 5,y = 0,width=720,height=135)

        #current Course
        currentCourse = LabelFrame(leftFrame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("times new Roman",12,"bold"))
        currentCourse.place(x = 5,y = 130, width=720,height=100)

        #Department
        deptlbl = Label(currentCourse,text="Department:",font=("times new Roman",12, "bold"),bg="white")
        deptlbl.grid(row = 0,column = 0,padx=10)

        deptCombo = ttk.Combobox(currentCourse,textvariable=self.varDep,font=("times new Roman",12,"bold"),width=17,state="readonly",)
        deptCombo["values"] = ("Select Department","CSE","IT","CIVIL","BCA","MCA","B.Sc","ECE","Others")
        deptCombo.current(0)
        deptCombo.grid(row=0,column=1,padx=2,pady=5)

        #Chosen Course
        chosenCourse = Label(currentCourse,text="Course:",font=("times new Roman",12, "bold"),bg="white")
        chosenCourse.grid(row = 0,column = 2,padx=10)

        courseCombo = ttk.Combobox(currentCourse,textvariable=self.varCourse,font=("times new Roman",12,"bold"),width=17,state="readonly",)
        courseCombo["values"] = ("Select Course","4 Year Course","3 Year Course","2 Year Course","1 Year Course")
        courseCombo.current(0)
        courseCombo.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        # Course year
        year = Label(currentCourse,text="Year:",font=("times new Roman",12, "bold"),bg="white")
        year.grid(row = 1,column = 0,padx=10,pady=10,sticky=W)

        yearCombo = ttk.Combobox(currentCourse,textvariable=self.varYear,font=("times new Roman",12,"bold"),width=17,state="readonly")
        yearCombo["values"] = ("Select Year","1st Year","2nd Year","3rd Year","4th Year")
        yearCombo.current(0)
        yearCombo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        #Semester
        semester = Label(currentCourse,text="Semester:",font=("times new Roman",12, "bold"),bg="white")
        semester.grid(row = 1,column = 2,padx=10)

        semCombo = ttk.Combobox(currentCourse,textvariable=self.varSemester,font=("times new Roman",12,"bold"),width=17,state="readonly")
        semCombo["values"] = ("Select Semester","1st Sem","2nd Sem","3rd Sem","4th Sem","5th Sem","6th Sem","7th Sem","8th Sem")
        semCombo.current(0)
        semCombo.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        
        # Class Student Information
        classStudentFrame = LabelFrame(leftFrame,bd=2,bg="white",relief=RIDGE,text="Class Course Information",font=("times new Roman",12,"bold"))
        classStudentFrame.place(x = 5,y = 230, width=720,height=325)

        #studentId
        studentId = Label(classStudentFrame,text="Student Id:",font=("times new Roman",12, "bold"),bg="white")
        studentId.grid(row = 0,column = 0,padx=5)

        studentIdEntry = ttk.Entry(classStudentFrame,textvariable=self.varStdId,width=20,font=("times new roman",11,"bold"))
        studentIdEntry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #studentName
        studentName = Label(classStudentFrame,text="Student Name:",font=("times new Roman",12, "bold"),bg="white")
        studentName.grid(row = 0,column = 2,padx=5)

        studentNameEntry = ttk.Entry(classStudentFrame,textvariable=self.varStdName,width=20,font=("times new roman",11,"bold"))
        studentNameEntry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #class Division
        classDiv = Label(classStudentFrame,text="Class Division",font=("times new Roman",12, "bold"),bg="white")
        classDiv.grid(row = 1,column = 0,padx=5)

        divCombo = ttk.Combobox(classStudentFrame,textvariable=self.varDiv,width=18,font=("times new roman",11,"bold"),state="readonly")
        divCombo["values"] = ("Select Division","A","B","C")
        divCombo.current(0)
        divCombo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #Roll No.
        rollNo = Label(classStudentFrame,text="Roll No:",font=("times new Roman",12, "bold"),bg="white")
        rollNo.grid(row = 1,column = 2,padx=5)

        rollNoEntry = ttk.Entry(classStudentFrame,textvariable=self.varRoll,width=20,font=("times new roman",11,"bold"))
        rollNoEntry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        #Gender.
        gender = Label(classStudentFrame,text="Gender:",font=("times new Roman",12, "bold"),bg="white")
        gender.grid(row = 2,column = 0,padx=5)

        genderCombo = ttk.Combobox(classStudentFrame,textvariable=self.varGender,width=18,font=("times new roman",11,"bold"),state="readonly")
        genderCombo["values"] = ("Select Gender","Male","Female","Others")
        genderCombo.current(0)
        genderCombo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #DOB.
        DOB = Label(classStudentFrame,text="Date Of Birth:",font=("times new Roman",12, "bold"),bg="white")
        DOB.grid(row = 2,column = 2,padx=5)

        DOBEntry = ttk.Entry(classStudentFrame,textvariable=self.varDob,width=20,font=("times new roman",11,"bold"))
        DOBEntry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #E-MAIL.
        e_mail = Label(classStudentFrame,text="E-Mail:",font=("times new Roman",12, "bold"),bg="white")
        e_mail.grid(row = 3,column = 0,padx=5)

        e_mailEntry = ttk.Entry(classStudentFrame,textvariable=self.varEmail,width=20,font=("times new roman",11,"bold"))
        e_mailEntry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        #Phone No.
        PhoneNo = Label(classStudentFrame,text="Phone No:",font=("times new Roman",12, "bold"),bg="white")
        PhoneNo.grid(row = 3,column = 2,padx=5)

        PhoneNoEntry = ttk.Entry(classStudentFrame,textvariable=self.varPhone,width=20,font=("times new roman",11,"bold"))
        PhoneNoEntry.grid(row=3,column=3,padx=10,pady=10,sticky=W)

        #Address.
        address = Label(classStudentFrame,text="Address:",font=("times new Roman",12, "bold"),bg="white")
        address.grid(row = 4,column = 0,padx=5)

        addressEntry = ttk.Entry(classStudentFrame,textvariable=self.varAddress,width=20,font=("times new roman",11,"bold"))
        addressEntry.grid(row=4,column=1,padx=10,pady=10,sticky=W)

        #Teachers Name.
        teacherName = Label(classStudentFrame,text="Tearcher's Name",font=("times new Roman",12, "bold"),bg="white")
        teacherName.grid(row = 4,column = 2,padx=5)

        teacherEntry = ttk.Entry(classStudentFrame,textvariable=self.varTeacher,width=20,font=("times new roman",11,"bold"))
        teacherEntry.grid(row=4,column=3,padx=10,pady=10,sticky=W)

        #radio Buttons
        self.varRadio1 = StringVar()
        radioBtn1 = ttk.Radiobutton(classStudentFrame,variable=self.varRadio1,text="Take Photo Sample",value="YES")
        radioBtn1.grid(row=5,column=0)

        radioBtn2 = ttk.Radiobutton(classStudentFrame,variable=self.varRadio1,text="No Photo Sample",value="No")
        radioBtn2.grid(row=5,column=1)

        #buttons Frame
        btnFrame = LabelFrame(classStudentFrame,bd=2,bg="white",relief=RIDGE)
        btnFrame.place(x=2,y=237,width=710,height=32)

        saveBtn = Button(btnFrame,text="Save",command=self.addData,font=("times new Roman",12, "bold"),bg="blue",fg="white",width=19)
        saveBtn.grid(row = 0,column=0)

        updateBtn = Button(btnFrame,text="Update",command=self.updateData,font=("times new Roman",12, "bold"),bg="blue",fg="white",width=19)
        updateBtn.grid(row = 0,column=1)
        
        deleteBtn = Button(btnFrame,text="Delete",command=self.deleteData,font=("times new Roman",12, "bold"),bg="blue",fg="white",width=19)
        deleteBtn.grid(row = 0,column=2)
        
        resetBtn = Button(btnFrame,text="Reset",command=self.resetData,font=("times new Roman",12, "bold"),bg="blue",fg="white",width=19)
        resetBtn.grid(row = 0,column=3)

        btnFrame1 = LabelFrame(classStudentFrame,bd=2,bg="white",relief=RIDGE)
        btnFrame1.place(x=2,y=269,width=710,height=32)

        takePhotoBtn = Button(btnFrame1,command=self.generateDataSet,text="Take Photo Sample",font=("times new Roman",12, "bold"),bg="blue",fg="white",width=38)
        takePhotoBtn.grid(row = 0,column=0)
        
        noPhotoBtn = Button(btnFrame1,text="No Photo Sample",font=("times new Roman",12, "bold"),bg="blue",fg="white",width=39)
        noPhotoBtn.grid(row = 0,column=1)

        # ------------------
        #Right Label Frame
        rightFrame = LabelFrame(mainFrame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new Roman",12,"bold"))
        rightFrame.place(x = 760,y = 10, width=720,height=580)

        #img Image
        imgRight = Image.open(r"Images\nature.jpg")
        imgRight = imgRight.resize((710,135),Image.ANTIALIAS)
        self.photoImgRight = ImageTk.PhotoImage(imgRight)
        
        f_lbl = Label(rightFrame,image=self.photoImgRight)
        f_lbl.place(x = 5,y = 0,width=710,height=130)

        #table Frame
        tableFrame = Frame(rightFrame,bd=2,bg="white",relief=RIDGE)
        tableFrame.place(x = 5,y = 110, width=710,height=450)

        #scroll Bar
        scrollX = ttk.Scrollbar(tableFrame,orient=HORIZONTAL)
        scrollY = ttk.Scrollbar(tableFrame,orient=VERTICAL)

        self.studentTable = ttk.Treeview(tableFrame,columns=("Department","Course","Year","Sem","Id","Name","Div","Roll","Gender","DOB","E_mail","Phone","Address","Teacher","Photo"),xscrollcommand=scrollX.set,yscrollcommand = scrollY.set)
        
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack (side=RIGHT,fill=Y)
        scrollX.config(command=self.studentTable.xview)
        scrollY.config(command=self.studentTable.yview)

        self.studentTable.heading("Department",text="Department")
        self.studentTable.heading("Course",text="Course")
        self.studentTable.heading("Year",text="Year")
        self.studentTable.heading("Sem",text="Semester")
        self.studentTable.heading("Id",text="Id")
        self.studentTable.heading("Name",text="Name")
        self.studentTable.heading("Div",text="Division")
        self.studentTable.heading("Roll",text="Roll")
        self.studentTable.heading("Gender",text="Gender")
        self.studentTable.heading("DOB",text="Date of Birth")
        self.studentTable.heading("E_mail",text="E-Mail")
        self.studentTable.heading("Phone",text="Phone")
        self.studentTable.heading("Address",text="Address")
        self.studentTable.heading("Teacher",text="Teacher")
        self.studentTable.heading("Photo",text="PhotoSampleStatus")
        self.studentTable["show"] = "headings"

        self.studentTable.column("Department",width=100)
        self.studentTable.column("Course",width=100)
        self.studentTable.column("Year",width=100)
        self.studentTable.column("Sem",width=100)
        self.studentTable.column("Id",width=100)
        self.studentTable.column("Name",width=100)
        self.studentTable.column("Div",width=100)
        self.studentTable.column("Roll",width=100)
        self.studentTable.column("Gender",width=100)
        self.studentTable.column("DOB",width=100)
        self.studentTable.column("E_mail",width=100)
        self.studentTable.column("Phone",width=100)
        self.studentTable.column("Address",width=100)
        self.studentTable.column("Teacher",width=100)
        self.studentTable.column("Photo",width=150)

        self.studentTable.pack(fill=BOTH,expand=1)
        self.studentTable.bind("<ButtonRelease>",self.getCursor)
        self.fetchData()
        

    # Function Declaration

    #Add Data Funtion
    def addData(self):
        if self.varDep.get() == "Select Department" or self.varStdName.get() == "" or self.varStdId.get == "" or self.varSemester.get() == "Select Semester" or self.varStdId.get == "" or self.varGender.get() == "Select Gender" or self.varDiv.get() == "Select Division" or self.varDob.get() == "":
            messagebox.showerror("Error","All fields are Required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="vivek@123",database="face_recognizer")
                myCursor = conn.cursor()
                myCursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.varDep.get(),
                    self.varCourse.get(),
                    self.varYear.get(),
                    self.varSemester.get(),
                    self.varStdId.get(),
                    self.varStdName.get(),
                    self.varDiv.get(),
                    self.varRoll.get(),
                    self.varGender.get(),
                    self.varDob.get(),
                    self.varEmail.get(),
                    self.varPhone.get(),
                    self.varAddress.get(),
                    self.varTeacher.get(),
                    self.varRadio1.get(),
                ))
                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo("Success","Student Details Has Been Added",parent= self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #Fetch Data
    def fetchData(self):
        self.conn = mysql.connector.connect(host="localhost",username="root",password="vivek@123",database="face_recognizer")
        myCursor = self.conn.cursor()
        myCursor.execute("select * from student")
        data=myCursor.fetchall()

        if len(data) != 0:
            self.studentTable.delete(*self.studentTable.get_children())
            for i in data:
                self.studentTable.insert("",END,values=i)
            self.conn.commit()
        self.conn.close()


    # Get Cursor
    def getCursor(self,event=""):
        cursorFocus = self.studentTable.focus()
        content = self.studentTable.item(cursorFocus)
        data = content["values"]

        self.varDep.set(data[0]) 
        self.varCourse.set(data[1]) 
        self.varYear.set(data[2]) 
        self.varSemester.set(data[3]) 
        self.varStdId.set(data[4]) 
        self.varStdName.set(data[5]) 
        self.varDiv.set(data[6]) 
        self.varRoll.set(data[7]) 
        self.varGender.set(data[8]) 
        self.varDob.set(data[9]) 
        self.varEmail.set(data[10]) 
        self.varPhone.set(data[11]) 
        self.varAddress.set(data[12]) 
        self.varTeacher.set(data[13]) 
        self.varRadio1.set(data[14]) 

    #Update Function
    def updateData(self):
        if self.varDep.get() == "Select Department" or self.varStdName.get() == "" or self.varStdId.get == "" or self.varSemester.get() == "Select Semester" or self.varStdId.get == "" or self.varGender.get() == "Select Gender" or self.varDiv.get() == "Select Division" or self.varDob.get() == "":
            messagebox.showerror("Error","All fields are Required",parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Do You Want To update this Student Details",parent = self.root)
                if(Update >0):
                    conn = mysql.connector.connect(host="localhost",username="root",password="vivek@123",database="face_recognizer")
                    myCursor = conn.cursor()
                    myCursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where StudentId=%s",(
                        self.varDep.get(),
                        self.varCourse.get(),
                        self.varYear.get(),
                        self.varSemester.get(),
                        self.varStdName.get(),
                        self.varDiv.get(),
                        self.varRoll.get(),
                        self.varGender.get(),
                        self.varDob.get(),
                        self.varEmail.get(),
                        self.varPhone.get(),
                        self.varAddress.get(),
                        self.varTeacher.get(),
                        self.varRadio1.get(),
                        self.varStdId.get(),
                    ))
                else:
                    if(not Update):
                        return
                messagebox.showinfo("Success","Student Details Successfully updated",parent=self.root)
                conn.commit()
                self.fetchData()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    #delete Function

    def deleteData(self):
        if(self.varStdId.get() == ""):
            messagebox.showerror("Error","Student is Required To perform This Action",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do You Want to delete this Student",parent= self.root)
                if(delete > 0 ):
                    conn = mysql.connector.connect(host="localhost",username="root",password="vivek@123",database="face_recognizer")
                    myCursor = conn.cursor()
                    sql="delete from student where StudentId=%s"
                    val=(self.varStdId.get(),)
                    myCursor.execute(sql,val)
                else:
                    if(not delete):
                        return
                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted Student Details",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    #Reset Function

    def resetData(self):
        self.varDep.set("Select Department")
        self.varCourse.set("Select Course")
        self.varYear.set("Select Year")
        self.varSemester.set("Select Semester")
        self.varStdId.set("")
        self.varStdName.set("")
        self.varDiv.set("Select Division")
        self.varRoll.set("")
        self.varGender.set("Select Gender")
        self.varDob.set("")
        self.varEmail.set("")
        self.varPhone.set("")
        self.varAddress.set("")
        self.varTeacher.set("")
        self.varRadio1.set("")

    #generate Data Set or take Photo Samples

    def generateDataSet(self):
        if self.varDep.get() == "Select Department" or self.varStdName.get() == "" or self.varSemester.get() == "Select Semester" or self.varStdId.get == "" or self.varGender.get() == "Select Gender" or self.varDiv.get() == "Select Division" or self.varDob.get() == "":
            messagebox.showerror("Error","All fields are Required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="vivek@123",database="face_recognizer")
                myCursor = conn.cursor()
                myCursor.execute("select * from student")
                myResult = myCursor.fetchall()
                id = 0
                for x in myResult:
                    id += 1
                    myCursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where StudentId=%s",(
                        self.varDep.get(),
                        self.varCourse.get(),
                        self.varYear.get(),
                        self.varSemester.get(),
                        self.varStdName.get(),
                        self.varDiv.get(),
                        self.varRoll.get(),
                        self.varGender.get(),
                        self.varDob.get(),
                        self.varEmail.get(),
                        self.varPhone.get(),
                        self.varAddress.get(),
                        self.varTeacher.get(),
                        self.varRadio1.get(),
                        self.varStdId.get() == id+1
                    ))
                conn.commit()
                self.fetchData()
                self.resetData()
                conn.close()

                #Load Predefined Frontal Face From OpenCV

                faceClasifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def faceCropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

                    #detect Faces
                    faces = faceClasifier.detectMultiScale(gray,1.3,5)

                    #scaling factor = 1.3
                    # Minimum neighbor = 5
                    
                    #draw
                    for(x,y,w,h) in faces:
                        faceCropped = img[y:y+h,x:x+w]
                        return faceCropped
                    
                cap = cv2.VideoCapture(0)
                imageId = 0
                while(True):
                    _,myFrame = cap.read()
                    if (faceCropped(myFrame) is not None):
                        imageId += 1
                        face = cv2.resize( faceCropped(myFrame) , (450,450) ) 
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        fileNamePath = "Data/user." + str(id) + "." + str(imageId) + ".jpg"
                        cv2.imwrite(fileNamePath,face)
                        cv2.putText(face,str(imageId) , (50,50) , cv2.FONT_HERSHEY_COMPLEX , 2 , (0,255,0) , 2)
                        cv2.imshow("Cropped Face",face)

                    if(cv2.waitKey(1) == 13 or int(imageId) == 100):
                        break

                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating Data Set Completed!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent = self.root)






if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()