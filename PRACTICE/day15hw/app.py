from tkinter import *
from tkinter import messagebox
from db import Formdata

db=Formdata("StudentData.db")

def datainlistbox():
    data_list.delete(0,END)
    for row in db.fetch():
        data_list.insert(END,row)


def submit_btn():
    if Student_Name.get()=="" or Class.get()=="" or Section.get()=="" or Roll_No.get()=="" or Gurdian_Contact.get()=="" or Form_Fee.get()=="":
        messagebox.showerror("Missing Data","Please fill all data in given Fields")
        return
    db.insert(Student_Name.get(),Class.get(),Section.get(),Roll_No.get(),Gurdian_Contact.get(),Form_Fee.get())
    data_list.delete(0,END)
    data_list.insert(END,Student_Name.get(),Class.get(),Section.get(),Roll_No.get(),Gurdian_Contact.get(),Form_Fee.get())
    clear_btn()
    datainlistbox()

def select_data(event):
    global selected_data
    index=data_list.curselection()[0]
    selected_data=data_list.get(index)
    Student_entry.delete(0,END)
    Student_entry.insert(END,selected_data[1])
    Class_entry.delete(0,END)
    Class_entry.insert(END,selected_data[2])
    Section_entry.delete(0,END)
    Section_entry.insert(END,selected_data[3])
    Roll_entry.delete(0,END)
    Roll_entry.insert(END,selected_data[4])
    Gurdian_entry.delete(0,END)
    Gurdian_entry.insert(END,selected_data[5])
    Form_entry.delete(0,END)
    Form_entry.insert(END,selected_data[6])

def clear_btn():
    Student_entry.delete(0,END)
    Class_entry.delete(0,END)
    Section_entry.delete(0,END)
    Roll_entry.delete(0,END)
    Gurdian_entry.delete(0,END)
    Form_entry.delete(0,END)

def edit_btn():
    db.edit(selected_data[0],Student_Name.get(),Class.get(),Section.get(),Roll_No.get(),Gurdian_Contact.get(),Form_Fee.get())
    datainlistbox()

def delete_btn():
    db.deletedata(selected_data[0])
    clear_btn()
    datainlistbox()
    

app=Tk()

# application content

# app label
app_label=Label(app,text='''REGISTRATION
 FORM''',font=('bold',14)).grid(row=0,column=2,pady=20,padx=20)

# Student Name 
Student_Name=StringVar()
Student_label=Label(app,text="STUDENT NAME",font=('bold',14))
Student_label.grid(row=1,column=0,pady=20)
Student_entry=Entry(app,textvariable=Student_Name,)
Student_entry.grid(row=1,column=1)

# Class 
Class=StringVar()
Class_label=Label(app,text="CLASS",font=('bold',14))
Class_label.grid(row=1,column=2,pady=20)
Class_entry=Entry(app,textvariable=Class)
Class_entry.grid(row=1,column=3,)

# Section 
Section=StringVar()
Section_label=Label(app,text="SECTION",font=('bold',14))
Section_label.grid(row=2,column=0,pady=20)
Section_entry=Entry(app,textvariable=Section)
Section_entry.grid(row=2,column=1)

# Roll No 
Roll_No=StringVar()
Roll_label=Label(app,text="ROLL NO",font=('bold',14))
Roll_label.grid(row=2,column=2,pady=20)
Roll_entry=Entry(app,textvariable=Roll_No)
Roll_entry.grid(row=2,column=3)

# Gurdian Number
Gurdian_Contact=StringVar()
Gurdian_label=Label(app,text="GURDIAN CONTACT",font=('bold',14))
Gurdian_label.grid(row=3,column=0,pady=20)
Gurdian_entry=Entry(app,textvariable=Gurdian_Contact)
Gurdian_entry.grid(row=3,column=1)

# Form Fee
Form_Fee=StringVar()
Form_label=Label(app,text="FORM FEE",font=('bold',14))
Form_label.grid(row=3,column=2,pady=20)
Form_entry=Entry(app,textvariable=Form_Fee)
Form_entry.grid(row=3,column=3)

# Add Button

# Button Widget 1
add_btn1=Button(app,text="EDIT",width=12,command=edit_btn)
add_btn1.grid(row=4,column=0,pady=20)

# Button Widget 2
add_btn1=Button(app,text="CLEAR",width=12,command=clear_btn)
add_btn1.grid(row=4,column=1,pady=20)

# Button Widget 3
add_btn1=Button(app,text="DELETE",width=12,command=delete_btn)
add_btn1.grid(row=4,column=2,pady=20)

# Button Widget 4
add_btn1=Button(app,text="SUBMIT",width=12,command=submit_btn)
add_btn1.grid(row=4,column=3,pady=20)

# List Box
data_list=Listbox(app,height=10,width=70,border=1)
data_list.grid(row=5,column=0,columnspan=4,rowspan=8,pady=20,padx=20)

# scroll bar
scroll_bar=Scrollbar(app)
scroll_bar.grid(row=5,column=3)

# Binding select function
data_list.bind("<<ListboxSelect>>",select_data)

datainlistbox()

app.configure(bg="skyblue")
app.title("REGISTRATION APP")
app.geometry("700x350")
app.mainloop()