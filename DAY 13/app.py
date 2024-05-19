from tkinter import *

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
Customer_entry=Entry(app,textvariable=part_text)
Customer_entry.grid(row=1,column=1)

# price
price_text=StringVar()
price_label=Label(app,text="Price",font=('bold',14),pady=20)
price_label.grid(row=0,column=2)
price_entry=Entry(app,textvariable=part_text)
price_entry.grid(row=0,column=3)

# Company
Company_text=StringVar()
Company_label=Label(app,text="Company",font=('bold',14),pady=20)
Company_label.grid(row=1,column=2)
Company_entry=Entry(app,textvariable=part_text)
Company_entry.grid(row=1,column=3)

# button widget1
add_btn=Button(app,text="ADD PART",width=12)
add_btn.grid(row=2,column=0,pady=20)

# button widget2
add_btn=Button(app,text="UPDATE",width=12)
add_btn.grid(row=2,column=1,pady=20)

# button widget3
add_btn=Button(app,text="DELETE",width=12)
add_btn.grid(row=2,column=2,pady=20)

# button widget1
add_btn=Button(app,text="CLEAR",width=12)
add_btn.grid(row=2,column=3,pady=20)

# list box widget
parts_list=Listbox(app,height=8,width=50,border=1)
parts_list.grid(row=3,column=0,columnspan=3,rowspan=6,pady=20,padx=20)

# scroll bar
scroll_bar=Scrollbar(app)
scroll_bar.grid(row=3,column=3)

app.title("Demo App")
app.geometry("1000x500")

app.mainloop()