import os
from datetime import datetime
from time import strftime
from tkinter import *
from tkinter import ttk
import tkinter
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
from student import Student
from train import Train
from faceRecognizor import faceDetector
from Attendence import Attendence
from developer import Developer
from chatbot import ChatBot

class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        # img1
        img = Image.open(r"Images\face1.png")
        img = img.resize((500,135),Image.ANTIALIAS)
        self.photoImg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root,image=self.photoImg)
        f_lbl.place(x = 0,y = 0,width=500,height=135)

        # img2
        img1 = Image.open(r"Images\face2.jpg")
        img1 = img1.resize((500,135),Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoImg1)
        f_lbl.place(x = 500,y = 0,width=500,height=135)

        # img3
        img2 = Image.open(r"Images\face3.jpg")
        img2 = img2.resize((540,135),Image.ANTIALIAS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root,image=self.photoImg2)
        f_lbl.place(x = 1000,y = 0,width=540,height=135)

        # bg - img
        img3 = Image.open(r"Images\bgImg.jpg")
        img3 = img3.resize((1550,790),Image.ANTIALIAS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root,image=self.photoImg3)
        bg_img.place(x = 0,y = 135,width=1550,height=670)

        #title Label
        title_lbl = Label(bg_img,text="Face Recognition Attendence System Software",font=("times new roman",33,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1550,height=45)

        #time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl = Label(title_lbl,font=("time new roman",14,"bold"),background = "white",foreground="blue")
        lbl.place(x = 5,y = 0,width=110,height=50)
        time()

        # 1. Student Button 
        studentImg = Image.open(r"Images\student.png")
        studentImg = studentImg.resize((300,225),Image.ANTIALIAS)
        self.photoImg4 = ImageTk.PhotoImage(studentImg)
        
        b1 = Button(bg_img,command = self.Student_details,image=self.photoImg4,cursor="hand2")
        b1.place(x = 200,y = 100,width = 220,height = 225)

        b1_1 = Button(bg_img,command = self.Student_details,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x = 200,y = 290,width = 220,height = 40) 

        # 2. Detect Face
        detectFace = Image.open(r"Images\faceDetector.jpg")
        detectFace = detectFace.resize((300,225),Image.ANTIALIAS)
        self.photoImg5 = ImageTk.PhotoImage(detectFace)
        
        b1 = Button(bg_img,image=self.photoImg5,cursor="hand2",command=self.faceDetector)
        b1.place(x = 500, y = 100,width = 220,height = 225)

        b1_1 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.faceDetector,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x = 500,y = 290,width = 220,height = 40) 


        # 3. Attendence Manager
        attendence = Image.open(r"Images\attendence.jpg")
        attendence = attendence.resize((220,225),Image.ANTIALIAS)
        self.photoImg6 = ImageTk.PhotoImage(attendence)
        
        b1 = Button(bg_img,image=self.photoImg6,command=self.Attendence,cursor="hand2")
        b1.place(x = 800, y = 100,width = 220,height = 225)

        b1_1 = Button(bg_img,text="Attendence Manager",command=self.Attendence,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x = 800,y = 290,width = 220,height = 40) 


        # 4. HelpDesk
        help = Image.open(r"chat.jpg")
        help = help.resize((300,225),Image.ANTIALIAS)
        self.photoImg7 = ImageTk.PhotoImage(help)
        
        b1 = Button(bg_img,image=self.photoImg7,cursor="hand2",command=self.chatbot)
        b1.place(x = 1100, y = 100,width = 220,height = 225)

        b1_1 = Button(bg_img,text="Talk To Our ChatBot",cursor="hand2",command=self.chatbot,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x = 1100,y = 290,width = 220,height = 40) 

        #  5. Train DataSet
        trainData = Image.open(r"Images\trainData.jpg")
        trainData = trainData.resize((300,300),Image.ANTIALIAS)
        self.photoImg8 = ImageTk.PhotoImage(trainData)
        
        b1 = Button(bg_img,image=self.photoImg8,cursor="hand2",command=self.trainData)
        b1.place(x = 200, y = 350,width = 220,height = 225)

        b1_1 = Button(bg_img,text="Train DataSet",cursor="hand2",command=self.trainData,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x = 200,y = 540,width = 220,height = 40) 

        # 6. Photos 
        photos = Image.open(r"Images\photos.jpg")
        photos = photos.resize((300,225),Image.ANTIALIAS)
        self.photoImg9 = ImageTk.PhotoImage(photos)
        
        b1 = Button(bg_img,image=self.photoImg9,command=self.openPhotos,cursor="hand2")
        b1.place(x = 500, y = 350,width = 220,height = 225)

        b1_1 = Button(bg_img,text="Photos",command=self.openPhotos,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x = 500,y = 540,width = 220,height = 40)

        # 7. Developer
        dev = Image.open(r"Images\developer.jpg")
        dev = dev.resize((220,225),Image.ANTIALIAS)
        self.photoImg10 = ImageTk.PhotoImage(dev)
        
        b1 = Button(bg_img,image=self.photoImg10,cursor="hand2",command=self.Developer)
        b1.place(x = 800, y = 350,width = 220,height = 225)

        b1_1 = Button(bg_img,text="Developer",cursor="hand2",command=self.Developer,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x = 800,y = 540,width = 220,height = 40) 

        # 8. Exit

        exit = Image.open(r"Images\exit.jpg")
        exit = exit.resize((180,200),Image.ANTIALIAS)
        self.photoImg11 = ImageTk.PhotoImage(exit)
        
        b1 = Button(bg_img,image=self.photoImg11,cursor="hand2",command=self.Exit)
        b1.place(x = 1100, y = 350,width = 220,height = 225)

        b1_1 = Button(bg_img,text="Exit",cursor="hand2",command=self.Exit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x = 1100,y = 540,width = 220,height = 40)

    

    # Student Details Function Declaration
    def Student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window) 

    #Photos Button Function Declaration
    def openPhotos(self):
        os.startfile("Data")

    #Train Data Function
    def trainData(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    #faceDetector
    def faceDetector(self):
        self.new_window = Toplevel(self.root)
        self.app = faceDetector(self.new_window)

    #Attendence Function
    def Attendence(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendence(self.new_window)

    #Developer Function
    def Developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    #Help
    def chatbot(self):
        self.new_window = Toplevel(self.root)
        self.app = ChatBot(self.new_window)

    def Exit(self):
        self.Exit = tkinter.messagebox.askyesno("Face Recognition","Are You Sure",parent = self.root)
        if self.Exit > 0:
            self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()


