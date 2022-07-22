from importlib.resources import path
from tkinter import *
from tkinter import ttk
from turtle import bgcolor, right, width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #title Label
        title_lbl = Label(self.root,text="Train Data Set",font=("times new roman",33,"bold"),bg="purple",fg="white")
        title_lbl.place(x=0,y=0,width=1550,height=45)


        #images Top
        imgTop1 = Image.open(r"Images\trainData1.jpg")
        imgTop1 = imgTop1.resize((768,320),Image.ANTIALIAS)
        self.photoImgTop1 = ImageTk.PhotoImage(imgTop1)
        
        f_lbl = Label(self.root,image=self.photoImgTop1)
        f_lbl.place(x = 0,y = 45,width=768,height=320)

        imgTop2 = Image.open(r"Images\trainData2.jpg")
        imgTop2 = imgTop2.resize((768,320),Image.ANTIALIAS)
        self.photoImgTop2 = ImageTk.PhotoImage(imgTop2)
        
        f_lbl = Label(self.root,image=self.photoImgTop2)
        f_lbl.place(x = 768,y = 45,width=768,height=320)

        #train data Button
        trainBtn = Button(self.root,text="Train Data",command=self.trainClasifier,font=("times new Roman",40, "bold"),bg="Red",fg="white",cursor="hand2")
        trainBtn.place(x = 0,y = 370,width=1540,height=65)


        #Images Bottom
        imgBottom1 = Image.open(r"Images\trainData3.jpg")
        imgBottom1 = imgBottom1.resize((1535,350),Image.ANTIALIAS)
        self.photoImgBottom1 = ImageTk.PhotoImage(imgBottom1)
        
        f_lbl = Label(self.root,image=self.photoImgBottom1)
        f_lbl.place(x = 0,y = 440,width=1535,height=350)


    #LBPH Algorithm Function
    def trainClasifier(self):
        data_dir = "Data"
        path= [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces = []
        ids = []
        for image in path :
            img = Image.open(image).convert("L")  #Converting to grayScale Image
            imageNp = np.array(img,"uint8")
            id = int(os.path.split(image)[1].split(".")[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training Data Set",imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)
        
        #train Classifier and Save
 
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces,ids)
        recognizer.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","training Data Set Completed")
        

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()