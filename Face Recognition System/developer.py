from tkinter import *
from tkinter import ttk
from turtle import bgcolor, right, width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

    
        title_lbl = Label(self.root,text="DEVELOPERS [ACHEIVERS]",font=("times new roman",33,"bold"),bg="purple",fg="white")
        title_lbl.place(x=0,y=0,width=1550,height=45)


        #images Top
        imgTop1 = Image.open(r"Images\dev.jpg")
        imgTop1 = imgTop1.resize((1500,750),Image.ANTIALIAS)
        self.photoImgTop1 = ImageTk.PhotoImage(imgTop1)
        
        f_lbl = Label(self.root,image=self.photoImgTop1)
        f_lbl.place(x = 0,y = 45,width=1550,height=750)


        #frame
        mainFrame = Frame(f_lbl,bd = 2,bg="white")
        mainFrame.place(x = 1000, y = 15, width=500, height=650)

        #left frame
        leftFrame = Frame(f_lbl,bd = 2,bg="lightgreen")
        leftFrame.place(x = 40, y = 15, width=450, height=350)

        #mentor detail
        img = Image.open(r"DevImages\mp.jpg")
        img = img.resize((150,170),Image.ANTIALIAS)
        self.photoImg = ImageTk.PhotoImage(img)

        f_lbl = Label(leftFrame,image=self.photoImg)
        f_lbl.place(x = 130,y = 10,width=150,height=170)

        #detail 1
        photo_lbl = Label(leftFrame,text="Project Guide, Prof. Moujhuri Patra",font=("times new roman",18,"bold"),bg="Black",fg="white")
        photo_lbl.place(x=20,y=190,width=400,height=150)


        #image 1
        img1 = Image.open(r"DevImages\Vivek.jpg")
        img1 = img1.resize((120,150),Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(mainFrame,image=self.photoImg1)
        f_lbl.place(x = 10,y = 10,width=120,height=150)

        #detail 1
        title_lbl = Label(mainFrame,text="Hello, I am Vivek Kumar Gupta",font=("times new roman",18,"bold"),bg="Black",fg="white")
        title_lbl.place(x=140,y=10,width=350,height=150)

        img2 = Image.open(r"DevImages\Lukesh.jpeg")
        img2 = img2.resize((120,150),Image.ANTIALIAS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(mainFrame,image=self.photoImg2)
        f_lbl.place(x = 10,y = 170,width=120,height=150)

        #detail 2
        title_lbl = Label(mainFrame,text="Hello, I am Lukesh Kumar Nayak",font=("times new roman",18,"bold"),bg="Red",fg="white")
        title_lbl.place(x=140,y=170,width=350,height=150)

        img3 = Image.open(r"DevImages\gulab.jpeg")
        img3 = img3.resize((120,150),Image.ANTIALIAS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        
        f_lbl = Label(mainFrame,image=self.photoImg3)
        f_lbl.place(x = 10,y = 330,width=120,height=150)

        #detail 3
        title_lbl = Label(mainFrame,text="Hello, I am Gulab Chand Mahto",font=("times new roman",18,"bold"),bg="Blue",fg="white")
        title_lbl.place(x=140,y=330,width=350,height=150)

        img4 = Image.open(r"DevImages\ayush.jpeg")
        img4 = img4.resize((120,150),Image.ANTIALIAS)
        self.photoImg4 = ImageTk.PhotoImage(img4)
        
        f_lbl = Label(mainFrame,image=self.photoImg4)
        f_lbl.place(x = 10,y = 487,width=120,height=150)

        #Detail4
        title_lbl = Label(mainFrame,text="Hello, I am Ayush Ojha",font=("times new roman",18,"bold"),bg="gray",fg="white")
        title_lbl.place(x=140,y=487,width=350,height=150)

        


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()