from email import message
from tkinter import *
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector as c
from main import Face_Recognition

def main():
    new_window=Tk()
    app=Login_window(new_window)
    new_window.mainloop()


class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.title("Login")        

        # ----Background----
        self.bg=ImageTk.PhotoImage(file=r"icon\RE4wB6Z.jfif")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        

        img1 = Image.open(r"Images\LOGO.png")
        img1 = img1.resize((500,400),Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(lbl_bg,image=self.photoImg1)
        f_lbl.place(x = 109,y = 190,width=500,height=400)


        #main Frame
        
        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)

        #--------Head Icon------

        img1=Image.open(r"icon\useri.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        #--------Label Top ------
        get_str= Label(frame,text="Login Info.",font=("Adobe Fan Heiti Std B",20,"bold"),fg="black",bg="white")
        get_str.place(x=105,y=100)

        #label Username
        username=lbl=Label(frame,text="Email Id",font=("Adobe Fan Heiti Std B",15,"bold"),fg="black",bg="white")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("Adobe Fan Heiti Std B",15))
        self.txtuser.place(x=40,y=180,width=270)

        #label Password

        password=lbl=Label(frame,text="Password",font=("Adobe Fan Heiti Std B",15,"bold"),fg="black",bg="white")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("Adobe Fan Heiti Std B",15))
        self.txtpass.place(x=40,y=250,width=270)

        #---------------Icons-----------
        #-----usrnm Icon----

        img2=Image.open(r"icon\atr.png")
        img2=img2.resize((27,27),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="white",borderwidth=0)
        lblimg2.place(x=650,y=323,width=27,height=27)

        #------pwd Icon-----
        img3=Image.open(r"icon\key.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg2=Label(image=self.photoimage3,bg="white",borderwidth=0)
        lblimg2.place(x=650,y=392,width=25,height=25)

        #------------Login Button------
        loginbtn=Button(frame,command=self.login,text="Submit",font=("Lucida Sans",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="green")
        loginbtn.place(x=110,y=320,width=120,height=35)

        #---------Register button----
        regbtn=Button(frame,text="Register New User",command=self.register_win,font=("Lucida Sans",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="white",activebackground="brown")
        regbtn.place(x=20,y=360,width=160)


        #---------Forgot Pwd button----
        forgotbtn=Button(frame,text="Forgot Password !",font=("Lucida Sans",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="white",activebackground="orange")

        forgotbtn=Button(frame,command=self.forgot_pass_win,text="Forgot Password !",font=("Lucida Sans",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="white",activebackground="orange")

        forgotbtn.place(x=20,y=380,width=160)

        #-----Register Function------

    def register_win(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
        #------Login function--------- 

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showwarning("Blank Field","All fields are required fill.")
        elif self.txtuser.get()=="user1" and  self.txtpass.get()=="okuser":
            messagebox.showinfo("Login Success","Welcome User !")
        else:
            conn = c.connect(host= "localhost",username = "root",password = "vivek@123" , database = "face_recognizer")

            myCursor = conn.cursor()
            myCursor.execute("select * from register where email = %s and pass = %s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))

            row = myCursor.fetchone()

            if row == None:
                messagebox.showerror("Error","Invalid Username And Password")
            else:
                open_main = messagebox.askyesno("YesNo","Access Only Admin")

                if open_main >0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition(self.new_window)

                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


#>>>>   sq2             #sql 2.8.20

    
    #---------REST PASSWORD-----------
    def reset_pass(self):
        if self.combo_security_q.get()=="Select":
            messagebox.showerror("Selection Error","Choose the Security Q")
        elif self.txt_security.get()=="":
            messagebox.showwarning("Blank Error","Fill the Answer")
        elif self.txt_newpwd.get()=="":
            messagebox.showerror("Error","Enter your New Password. Try again.")
        else:
            conn = c.connect(host= "localhost",username = "root",password = "vivek@123" , database = "face_recognizer")
            myCursor = conn.cursor() 
            query = ("select * from register where email = %s and securityQues = %s and securityAns = %s")
            value = (self.txtuser.get(),self.combo_security_q.get(),self.txt_security.get(),) 
            myCursor.execute(query,value)
            row = myCursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Please enter correct Answer")
            else:
                query = "update register set pass = %s where email = %s"
                value = (self.txt_newpwd.get(),self.txtuser.get())
                myCursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been reset now proceed to login page")


#>>>> sq4           #sql 2.40.37

    #---------forgot funtion--------
    def forgot_pass_win(self):
        if self.txtuser.get()=="":
            messagebox.showwarning("Null !","Enter your 'Email Id' for reset Password ")
        else:
            conn = c.connect(host= "localhost",username = "root",password = "vivek@123" , database = "face_recognizer")
            myCursor = conn.cursor()
            query = "select * from register where email = %s"
            value = (self.txtuser.get(),)
            myCursor.execute(query,value)
            row = myCursor.fetchone()
 
#>>>>     sq3          #sql 2.21.56 - 2.25.30

        if row==None:
           messagebox.showerror("ID Error","Enter Valid username.")
        else:
            conn.close()
            self.root2=Toplevel()
            self.root2.title("Reset Password !")
            self.root2.geometry("340x450+610+170")


            l=Label(self.root2,text="Reset Password !",font=("Adobe Fan Heiti Std B",15,"bold"),fg="black",bg="white")
            l.place(x=0,y=0,relwidth=1)

            security_q=Label(self.root2,text="Select Seurity Question",font=("Lucida Sans",15,"bold"),bg="white",fg="black")
            security_q.place(x=50,y=800)

            self.combo_security_q=ttk.Combobox(self.root2,font=("Rockwell",15,"bold"),state="readonly")
            self.combo_security_q["values"]=("Select Question","Your First College","Your Nickname","Your Pet Name")
            self.combo_security_q.place(x=50,y=110,width=250)
            self.combo_security_q.current(0)

            security_a=Label(self.root2,text="Security Answer",font=("Lucida Sans",15,"bold"),bg="white",fg="black")
            security_a.place(x=50,y=145)

            self.txt_security=ttk.Entry(self.root2,font=("century",15))
            self.txt_security.place(x=50,y=180,width=250)

            new_pass=Label(self.root2,text="New Password",font=("Lucida Sans",15,"bold"),bg="white",fg="black")
            new_pass.place(x=50,y=220)

            self.txt_newpwd=ttk.Entry(self.root2,font=("century",15))
            self.txt_newpwd.place(x=50,y=250,width=250)

            btn6=Button(self.root2,command=self.reset_pass,text="Reset",font=("Lucida Sans",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="green")
            btn6.place(x=100,y=290)


            #>>>> 2.37.21

       #-------- Register Class-----
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

# ------------------variables----------------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_cnfpass=StringVar()

#----background Image-------
        self.bg=ImageTk.PhotoImage(file=r"icon\unsplash.jpg")

        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
   
    #-------Left label image------
        self.bg4=ImageTk.PhotoImage(file=r"icon\Dfmp.png")

        left_lbl=Label(self.root,image=self.bg4)
        left_lbl.place(x=50,y=100,width=370,height=550)
   
    #-----------Register MAIN frame------   
        frame=Frame(self.root,bg="white")
        frame.place(x=420,y=100,width=900,height=550)

        register_lbl=Label(frame,text="REGISTER HERE (Fill the Details)",font=("Lucida Sans",25,"bold","underline"),fg="darkblue",bg="white")
        register_lbl.place(x=20,y=20)

    #------------label and entry-------------
        
        #~~~~~~~~~~ row 1 ~~~~~~~~~
        fname=Label(frame,text="First Name",font=("Lucida Sans",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("century",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("Lucida Sans",15,"bold"),bg="white")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("century",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        #~~~~~~~~~ row 2 ~~~~~~~~~~~~~~~
        contact=Label(frame,text="Contact No.",font=("Lucida Sans",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("century",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email Id.",font=("Lucida Sans",15,"bold"),bg="white",fg="black")
        email.place(x=295,y=170,width=250)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("century",15))
        self.txt_email.place(x=370,y=200,width=250)

        #~~~~~~~~~~ row 3 ~~~~~~~~~~~~~
        security_q=Label(frame,text="Select Seurity Question",font=("Lucida Sans",15,"bold"),bg="white",fg="black")
        security_q.place(x=50,y=240)

        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("Rockwell",15,"bold"),state="readonly")
        self.combo_security_q["values"]=("Select Question","Your First College","Your Nickname","Your Pet Name")
        self.combo_security_q.place(x=50,y=270,width=250)
        self.combo_security_q.current(0)

        security_a=Label(frame,text="Security Answer",font=("Lucida Sans",15,"bold"),bg="white",fg="black")
        security_a.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("century",15))
        self.txt_security.place(x=370,y=270,width=250)

        #~~~~~~~~~ row  4 ~~~~~~~~~~~~~~

        pswd=Label(frame,text="Password",font=("Lucida Sans",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("century",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        cnfpswd=Label(frame,text="Confirm Password",font=("Lucida Sans",15,"bold"),bg="white",fg="black")
        cnfpswd.place(x=370,y=310)

        self.txt_cnfpswd=ttk.Entry(frame,textvariable=self.var_cnfpass,font=("century",15))
        self.txt_cnfpswd.place(x=370,y=340,width=250)

        #---------Checkmark-------
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the Terms & Conditions",font=("Lucida Sans",15,"underline"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        #---------button Register---------
        img=Image.open(r"icon\register.jpg")
        img=img.resize((248,100),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=50,y=420,width=250)

        #---------button Login---------
        img1=Image.open(r"icon\login.jpg")
        img1=img1.resize((198,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b2.place(x=450,y=420,width=200)


#--------------Function Decleartion----------

    def register_data(self):
        if self.var_fname.get() == "" or self.var_securityQ.get()=="Select":
            messagebox.showwarning("Missing Detail","All fields are required fill.")
        elif self.var_pass.get() != self.var_cnfpass.get():
            messagebox.showerror("Error Field","The Confirm password does not match ")
        elif self.var_check.get() == 0:
            messagebox.showwarning("Require","Please accept the Terms & Conditions")
        else:
            conn = c.connect(host= "localhost",username = "root",password = "vivek@123" , database = "face_recognizer")

            myCursor = conn.cursor()
            query = "select * from register where email = %s"
            value = (self.var_email.get(),)
            myCursor.execute(query,value)
            row = myCursor.fetchone()

            if row != None:
                messagebox.showerror("Error","User Already Exist!!,Please Try Another email")
            else:
                myCursor.execute("insert into register values (%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registration Successull")

#>>>>  sq1            #sql 1.49.12 

    #--------LOGIN FUNCTION IN REGISTER PAGE-------
    
    def return_login(self):
        self.root.destroy()




if __name__ == "__main__":
    main()
   
   # root=Tk()
   # obj = Login_window(root)
   # root.mainloop()
