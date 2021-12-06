from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from addBooks import *
from deleteBooks import *
from viewBooks import *
from issueBook import *
from returnBook import *

root=Tk()
root.title('Library')
root.geometry('1300x700') 	
img=ImageTk.PhotoImage(file="lib.jpg")
lbl=Label(root,image=img,width=1300,height=700)
lbl.place(x=0,y=0)
headFrame=Frame(root,bg="#FFBB00",bd=4)
headFrame.place(x=300,y=10,width=700,height=100)
l=Label(headFrame,text="Welcome to Library",bg='black',fg="White",font=('Courier',18))
l.place(x=20,y=15,width=650,height=60)
b1=Button(root,text="Add Book Details",bg='Orange',fg="White",font=('Courier',14),command=addBook)
b1.place(x=550,y=200,width=250,height=50)
b2=Button(root,text="Delete Book Details",bg='black',fg="White",font=('Courier',14),command=delete)
b2.place(x=550,y=250,width=250,height=50)
b3=Button(root,text="View Book Details",bg='black',fg="White",font=('Courier',14),command=View)
b3.place(x=550,y=300,width=250,height=50)
b4=Button(root,text="Issue Book to Student",bg='black',fg="White",font=('Courier',14),command=issueBook)
b4.place(x=550,y=350,width=250,height=50)
b5=Button(root,text="Return Book",bg='black',fg="White",font=('Courier',14),command=returnBook)
b5.place(x=550,y=400,width=250,height=50)
root.mainloop()
