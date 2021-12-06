from tkinter import *
from tkinter import messagebox
import mysql.connector

def returnn():
    con=mysql.connector.connect(host="localhost",user="root",passwd="iics",database="project")
    cur=con.cursor(dictionary=True)
    allBid=[]

    bid=bookInfo1.get()
    try:
        cur.execute("select * from books_issued")
        for i in cur:
            allBid.append(i['bid'])
        if bid in allBid:
            cur.execute("select * from books where bid= '"+bid+"'")
            for i in cur:
                check=i['status']
            if check=='Issued':
                status=True
            else:
                status=False
        else:
            messagebox.showinfo("Error ","Books ID not available")
    except:
        messagebox.showinfo("Error","Cannot fetch Book IDs")
    try:
        if bid in allBid and status==True:
            cur.execute("delete from books_issued where bid = '"+bid+"'")
            con.commit()
            cur.execute("update books set status='Avail' where bid = '"+bid+"'")
            con.commit()
            messagebox.showinfo("Success","Book Returned Successfully")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo("Message","Please check the Book ID")
            root.destroy()
    except:
        messagebox.showinfo("Search Error","The value enteredis wrong, Try Again")
    allBid.clear()
def returnBook():
    global bookInfo1,root
    root=Tk()
    root.geometry("1300x700")
    root.title("Library")
    c=Canvas(root)
    c.config(bg="#006B38")
    c.pack(expand=True,fill=BOTH)

    headFrame=Frame(root,bg="#FFBB00",bd=4)
    headFrame.place(x=300,y=10,width=700,height=100)
    l=Label(headFrame,text="Return Book",bg="black",fg="white",font=('Courier',18))
    l.place(x=20,y=15,width=650,height=60)

    lFrame=Frame(root,bg="black")
    lFrame.place(x=200,y=200,width=900,height=300)

    lb1=Label(lFrame,text="Book ID",bg="black",fg="white",font=('Courier',14))
    lb1.place(x=50,y=100,height=30,width=300)

    bookInfo1=Entry(lFrame,font=('Courier',14))
    bookInfo1.place(x=350,y=100,width=300,height=30)

    submitBtn=Button(root,text="RETURN",bg="#d1ccc0",fg="black",command=returnn)
    submitBtn.place(x=500,y=550,width=80,height=40)

    quitBtn=Button(root,text="QUIT",bg="#f7f1e3",fg="black",command=root.destroy)
    quitBtn.place(x=750,y=550,width=80,height=40)
    
    root.mainloop()
