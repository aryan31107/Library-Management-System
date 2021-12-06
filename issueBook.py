from tkinter import *
from tkinter import messagebox
import mysql.connector
def issue():
    allBid=[]
    con=mysql.connector.connect(host="localhost",user="root",passwd="iics",database="project")
    cur=con.cursor(dictionary=True)
    bid=bookInfo1.get()
    issueto=bookInfo2.get()
    try:
        cur.execute("select * from books")
        for i in cur:
            allBid.append(i['bid'])
        if bid in allBid:
            cur.execute("select * from books where bid='"+bid+"'")
            for i in cur:
                check=i['status']
            if check=='Avail':
                status=True
            else:
                status=False
        else:
            messagebox.showinfo("Error"," Book ID is not available")
    except:
        messagebox.showinfo("Error","cannot fetch Book IDs")
    try:
        cur.execute("insert into books_issued values('"+bid+"','"+issueto+"')")
        con.commit()
        cur.execute("update books set status='Issued' where bid='"+bid+"'")
        con.commit()
        messagebox.showinfo("Success","Book Issued Successfully")
        root.destroy()
    except:
        messagebox.showinfo("Message","Book Already Issued")
    allBid.clear()

def issueBook():
    global bookInfo1,bookInfo2,root
    root=Tk()
    root.title("Library")
    root.geometry('1300x700')
   
    c=Canvas(root)
    c.config(bg="#00ddaa")
    c.pack(expand=True,fill=BOTH)
    headFrame1=Frame(root,bg="#FFBB00",bd=4)
    headFrame1.place(x=300,y=10,width=700,height=100)
    l=Label(headFrame1,text="Issue Books",bg="black",fg="white",font=('Courier',18))
    l.place(x=20,y=15,width=650,height=60)

    IFrame=Frame(root,bg="black")
    IFrame.place(x=200,y=200,width=900,height=300)

    lb1=Label(IFrame,text="Book ID ",bg="black",fg="white",font=('Courier',14))
    lb1.place(x=50,y=100,width=300,height=30)
    bookInfo1=Entry(IFrame,font=('Courier',14))
    bookInfo1.place(x=350,y=100,width=300,height=30)
    
    lb2=Label(IFrame,text="Issued to  ",bg="black",fg="white",font=('Courier',14))
    lb2.place(x=50,y=150,width=300,height=30)
    bookInfo2=Entry(IFrame,font=('Courier',14))
    bookInfo2.place(x=350,y=150,width=300,height=30)


    b1=Button(root,text="ISSUE",bg="#d1ccc0",fg="black",command=issue)
    b1.place(x=500,y=580,width=80,height=40)

    b2=Button(root,text="QUIT",bg="#f7f1e3",fg="black",command=root.destroy)
    b2.place(x=750,y=580,width=80,height=40)
    root.mainloop()
