from tkinter import *
from tkinter import messagebox
import mysql.connector
def View():
    root=Tk()
    root.title("Library")
    root.geometry("1300x700")

    canvas1=Canvas(root)
    canvas1.config(bg="#12a4d9")
    canvas1.pack(expand=True,fill=BOTH)

    headFrame=Frame(root,bg="#FFBB00",bd=4)
    headFrame.place(x=300,y=10,width=700,height=100)

    l=Label(headFrame,text="View Books",bg="black",fg="white",font=('Courier',18))
    l.place(x=20,y=15,width=650,height=60)

    lFrame=Frame(root,bg="black")
    lFrame.place(x=200,y=200,width=900,height=300)
    e1=Label(lFrame,width=35,text="Book ID",borderwidth=2,relief='groove',anchor="w",bg="gray",fg="white")
    e1.grid(row=0,column=0)
    e2=Label(lFrame,width=35,text="Title",borderwidth=2,relief='groove',anchor="w",bg="gray",fg="white")
    e2.grid(row=0,column=1)
    e3=Label(lFrame,width=35,text="Author",borderwidth=2,relief='groove',anchor="w",bg="gray",fg="white")
    e3.grid(row=0,column=2)
    e4=Label(lFrame,width=35,text="Status",borderwidth=2,relief='groove',anchor="w",bg="gray",fg="white")
    e4.grid(row=0,column=3)
    con=mysql.connector.connect(host="localhost",user="root",passwd="iics",database="project")
    cur=con.cursor(dictionary=True)
    try:
        cur.execute("select * from books")
        k=1
        for i in cur:
            m=0
            for j in i.keys():
                e=Label(lFrame,width=35,text=i.get(j),borderwidth=2,relief='ridge',anchor="w")
                e.grid(row=k,column=m)
                m=m+1
            k=k+1  
    except:
        messagebox.showinfo("Error","Error in fetching records")

    quitBtn=Button(root,text="QUIT",bg="#f7f1e3",fg="black",command=root.destroy)
    quitBtn.place(x=650,y=550,width=80,height=40)
    root.mainloop()
