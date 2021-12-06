from tkinter import *
from tkinter import messagebox
import mysql.connector
def bookRegister():
        bid=bookInfo1.get()
        title=bookInfo2.get()
        author=bookInfo3.get()
        status=bookInfo4.get()
        con=mysql.connector.connect(host="localhost",user="root",passwd="iics",database="project")
        cur=con.cursor()
        try:
            cur.execute("insert into books(bid,title,author,status)values('"+bid+"','"+title+"','"+author+"','"+status+"')")
            con.commit()
            messagebox.showinfo("Success","Book added successfully")
        except:
            messagebox.showinfo("Error","Cannot add data into database")
        root.destroy()
def addBook():
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,root
    root=Tk()
    root.title("Library")
    root.geometry('1300x700')

    c=Canvas(root)
    c.config(bg="blue")
    c.pack(expand=True,fill=BOTH)
    headFrame1=Frame(root,bg="#FFBB00",bd=4)
    headFrame1.place(x=300,y=10,width=700,height=100)
    l=Label(headFrame1,text="Add Books",bg="black",fg="white",font=('Courier',18))
    l.place(x=20,y=20,width=650,height=60)

    IFrame=Frame(root,bg="black")
    IFrame.place(x=200,y=200,width=900,height=300)

    lb1=Label(IFrame,text="Book ID ",bg="black",fg="white",font=('Courier',14))
    lb1.place(x=50,y=25,width=300,height=30)
    bookInfo1=Entry(IFrame,font=('Courier',14))
    bookInfo1.place(x=350,y=25,width=300,height=30)

    lb2=Label(IFrame,text="Title ",bg="black",fg="white",font=('Courier',14))
    lb2.place(x=50,y=85,width=300,height=30)
    bookInfo2=Entry(IFrame,font=('Courier',14))
    bookInfo2.place(x=350,y=85,width=300,height=30)

    lb3=Label(IFrame,text="Author ",bg="black",fg="white",font=('Courier',14))
    lb3.place(x=50,y=140,width=300,height=30)
    bookInfo3=Entry(IFrame,font=('Courier',14))
    bookInfo3.place(x=350,y=140,width=300,height=30)

    lb4=Label(IFrame,text="Student (Avail/Issued) ",bg="black",fg="white",font=('Courier',14))
    lb4.place(x=50,y=190,width=300,height=30)
    bookInfo4=Entry(IFrame,font=('Courier',14))
    bookInfo4.place(x=350,y=190,width=300,height=30)

    b1=Button(root,text="SUBMIT",bg="#d1ccc0",fg="black",command=bookRegister)
    b1.place(x=500,y=600,width=80,height=40)

    b2=Button(root,text="QUIT",bg="#f7f1e3",fg="black",command=root.destroy)
    b2.place(x=750,y=600,width=80,height=40)
    root.mainloop()
