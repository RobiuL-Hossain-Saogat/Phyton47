from tkinter import *
from tkinter import messagebox
from db import Database


db=Database("store.db")

def populate_list():
    parts_list.delete(0,END)
    for row in db.fetch():
        items_space = ' '.join(map(str, row))
        parts_list.insert(END,items_space)

def add_item():
    if part_text.get()=="" or Customer_text.get()=="" or price_text.get()=="" or Company_text.get()=="":
        messagebox.showerror("Required Fields Missing", "Please include all fields")
        return
    db.insert(part_text.get(),Customer_text.get(),price_text.get(),Company_text.get())
    parts_list.delete(0,END)
    parts_list.insert(END,(part_text.get(),Customer_text.get(),price_text.get(),Company_text.get()))
    clear_text()
    populate_list()

def select_item(event):
    global selected_item
    index=parts_list.curselection()[0]
    selected_item=parts_list.get(index)
    part_entry.delete(0,END)
    part_entry.insert(END,selected_item[1])
    Customer_entry.delete(0,END)
    Customer_entry.insert(END,selected_item[2])
    price_entry.delete(0,END)
    price_entry.insert(END,selected_item[3])
    Company_entry.delete(0,END)
    Company_entry.insert(END,selected_item[4])

def Delete_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_item():
    db.update(selected_item[0],part_text.get(),Customer_text.get(),price_text.get(),Company_text.get())
    populate_list()

def clear_text():
    part_entry.delete(0,END)
    Customer_entry.delete(0,END)
    price_entry.delete(0,END)
    Company_entry.delete(0,END)


# creating oobject from Tk class
app=Tk()

# application content

# part name
part_text=StringVar()
part_label=Label(app,text="Part Name",font=('bold',14),pady=20)
part_label.grid(row=0,column=0)
part_entry=Entry(app,textvariable=part_text)
part_entry.grid(row=0,column=1)

# Customer Name
Customer_text=StringVar()
Customer_label=Label(app,text="Customer Name",font=('bold',14),pady=20)
Customer_label.grid(row=1,column=0)
Customer_entry=Entry(app,textvariable=Customer_text)
Customer_entry.grid(row=1,column=1)

# price
price_text=StringVar()
price_label=Label(app,text="Price",font=('bold',14),pady=20)
price_label.grid(row=0,column=2)
price_entry=Entry(app,textvariable=price_text)
price_entry.grid(row=0,column=3)

# Company
Company_text=StringVar()
Company_label=Label(app,text="Company",font=('bold',14),pady=20)
Company_label.grid(row=1,column=2)
Company_entry=Entry(app,textvariable=Company_text)
Company_entry.grid(row=1,column=3)

# list box widget
parts_list=Listbox(app,height=8,width=50,border=1)
parts_list.grid(row=3,column=0,columnspan=3,rowspan=6,pady=20,padx=20)

# scroll bar
scroll_bar=Scrollbar(app)
scroll_bar.grid(row=3,column=3)

# Binding select fuction
parts_list.bind('<<ListboxSelect>>',select_item)

# button widget1
add_btn=Button(app,text="ADD PART",width=12,command=add_item)
add_btn.grid(row=2,column=0,pady=20)

# button widget2
add_btn=Button(app,text="UPDATE",width=12,command=update_item)
add_btn.grid(row=2,column=1,pady=20)

# button widget3
add_btn=Button(app,text="DELETE",width=12,command=Delete_item)
add_btn.grid(row=2,column=2,pady=20)

# button widget1
add_btn=Button(app,text="CLEAR",width=12,command=clear_text)
add_btn.grid(row=2,column=3,pady=20)


populate_list()

app.title("Demo App")
app.geometry("1000x500")

app.mainloop()