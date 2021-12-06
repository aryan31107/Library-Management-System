from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import mysql.connector
import os
import sys
w=Tk()
w.geometry('400x400')
user=StringVar()
pass1=StringVar()
def logcheck():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="iics",database="project")
    c=mydb.cursor(dictionary=True)
    c.execute("select username,password from login")
    for row in c:
        v1=row['username']
        v2=row['password']
    if v1==user.get() and v2==pass1.get():
        messagebox.showinfo("Login","Login Successful")
        os.system('python Homepage.py')
    else:
        messagebox.showinfo("Login","Login Denied")
def cancel():
    messagebox.askyesno("Cancel","Are you Sure???")
    sys.exit()
f1=Font(family="Cooper",size=18,weight="bold")
l1=Label(w,text="LOGIN PORTAL",font=f1).place(x=100,y=50)
l2=Label(w,text="Username").place(x=70,y=100)
l3=Label(w,text="Password").place(x=70,y=150)
e1=Entry(w,textvariable=user).place(x=150,y=100)
e2=Entry(w,show="*",textvariable=pass1).place(x=150,y=150)
b1=Button(w,text="Login",command=logcheck).place(x=80,y=210)
b2=Button(w,text="Cancel",command=cancel).place(x=180,y=210)
w.mainloop()
