import tkinter as tk
from tkinter import *
from add_student_data import DatabaseManage

class AddStudent(tk.Frame):

    def __init__(self, parent):
        global db
        db = DatabaseManage()
        global rootWindow
        global e1, e2
        rootWindow = parent
        tk.Frame.__init__(self, parent)
        self.parent = parent
        l=Label(parent,bg="white",text="Student Management System",font=("Helvetica 17 bold"))
        l.grid(row=0,column=0,columnspan=3,padx=15,pady=15)

        lbl2 = Label(parent, text="Student Name : ").grid(row=1, sticky=E, pady=5)
        lbl3 = Label(parent, text="Class : ").grid(row=2, sticky=E)

        e1 = Entry(parent)
        e2 = Entry(parent)

        e1.grid(row=1, column=1, pady=5)
        e2.grid(row=2, column=1)

        b1=Button(parent, text="Save", width=10,bg="#ffcccc", fg="black",command= lambda: save_data())
        b1.grid(row=3, columnspan=3, pady=10)

        b=Button(parent,text="Close",bg="red", fg="white",command= lambda: deleteWindow())
        b.grid(row=3,column=2,columnspan=3,sticky=W,padx=15,pady=5)

def deleteWindow():
	rootWindow.destroy()

def save_data():
	name = e1.get()
	classname = e2.get()
	e1.delete(0, END)
	e2.delete(0, END)
	db.insertData(name, classname)
    