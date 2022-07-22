from tkinter import *
from tkinter import ttk
from turtle import bgcolor, right, width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os
from time import strftime
from datetime import datetime
import numpy as np

class faceDetector:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        # title Label
        title_lbl = Label(self.root,text="Face Detector",font=("times new roman",33,"bold"),bg="Green",fg="white")
        title_lbl.place(x=0,y=0,width=1550,height=45)

        #image 1
        imgLeftMain = Image.open(r"Images\faceDetector2.jpg")
        imgLeftMain = imgLeftMain.resize((768,690),Image.ANTIALIAS)
        self.photoImgLeftMain = ImageTk.PhotoImage(imgLeftMain)
        
        f_lbl = Label(self.root,image=self.photoImgLeftMain)
        f_lbl.place(x = 0,y = 45,width=768,height=770)

        #image 2
        imgRightMain = Image.open(r"Images\faceDetector1.jpg")
        imgRightMain = imgRightMain.resize((768,690),Image.ANTIALIAS)
        self.photoImgRightMain = ImageTk.PhotoImage(imgRightMain)
        
        f_lbl = Label(self.root,image=self.photoImgRightMain)
        f_lbl.place(x = 768,y = 45,width=768,height=770)

        #faceDectector Button
        detectBtn = Button(f_lbl,text="Detect face",command=self.faceRecog,font=("times new Roman",18, "bold"),bg="darkgreen",fg="white",cursor="hand2")
        detectBtn.place(x = 280,y = 645,width=200,height=40)

    # ----------Attendence Function-----------
    def markAttendence(self,n,r,d,s):
        with open("Attendence.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            nameList = []

            for line in myDataList :
                entry = line.split((","))
                nameList.append(entry[0])

            if( (s not in nameList) and (r not in nameList) and (d not in nameList) and (n not in nameList) ):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{r},{d},{s},{dtString},{d1},Present")




    # ----------face Recognition-------------

    def faceRecog(self):

        def drawBoundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(grayImage,scaleFactor,minNeighbors)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(grayImage[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost",username="root",password="vivek@123",database="face_recognizer")
                myCursor = conn.cursor()

                myCursor.execute("select Name from student where StudentId=" + str(id))
                n = myCursor.fetchone()
                n = "+".join(n)

                myCursor.execute("select Roll from student where StudentId=" + str(id))
                r = myCursor.fetchone()
                r = "+".join(r)

                myCursor.execute("select Department from student where StudentId=" + str(id))
                d = myCursor.fetchone()
                d = "+".join(d)

                myCursor.execute("select StudentId from student where StudentId=" + str(id))
                s = myCursor.fetchone()
                s = "+".join(s)
                

                
                if(confidence > 77):
                    cv2.putText(img,f"Accurecy:{confidence}",(x,y - 90),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    cv2.putText(img,f"ID:{s}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    self.markAttendence(n,r,d,s)


                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord = [x,y,w,h]

            return coord,img

        def recognize(img,clf,faceCascade):
            coord,img = drawBoundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

        while True :
            _, img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face recognizer (Press Enter Key to Quit/Mark Attendence)",img)

            if cv2.waitKey(1) & 0xFF == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
                    

if __name__ == "__main__":
    root = Tk()
    obj = faceDetector(root)
    root.mainloop()