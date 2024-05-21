from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from mydb import Mydatabase

mydb=Mydatabase("MobileServiceData.db")
mydb=Mydatabase("MobileServiceData1.db")
mydb=Mydatabase("MobileServiceData2.db")


app=Tk()
app.geometry("1000x500")
app.configure(bg="Gold")

# SEND MONEY WINDOW

def openSendMoneyWindow():
    newWindow=Toplevel(app,bg="skyblue")
    newWindow.title("Send Money")
    newWindow.geometry("700x350")
    Label(newWindow,text="Please fill all required fields to make transition",).pack(pady=10)
    def populate_list():
        for pack in mydb.fetch():
            data_list.insert(END,pack)
    def tap_btn():
        if Mobile_Number.get()=="" or Amount.get()=="" or Pin.get()=="":
            messagebox.showerror("Reqired Fields Missing", "Please include all fields")
            return
        mydb.insert(Mobile_Number.get(),Amount.get(),Pin.get(),Pin.get())
        data_list.delete(0,END)
        data_list.insert(END,(Mobile_Number.get(),Amount.get(),Pin.get()))
        populate_list()
    Mobile_Number=StringVar()
    Label(newWindow,text="Mobile Number",font=('bold',14)).pack()
    Entry(newWindow,textvariable=Mobile_Number).pack(pady=10)
    Amount=StringVar()
    Label(newWindow,text="Amount",font=('bold',14),).pack()
    Entry(newWindow,textvariable=Amount).pack(pady=10)
    Pin=StringVar()
    Label(newWindow,text="Pin",font=('bold',14),).pack()
    Entry(newWindow,textvariable=Pin).pack(pady=10)
    data_list=Listbox(newWindow,height=8,width=50,border=1)
    data_list.pack(pady=20)
    add_btn=Button(newWindow,text="TAP",width=12,command=tap_btn)
    add_btn.pack(pady=10)
    pass
    

label=Label(app,text="Welcome to Mobile Financial Service ")
label.pack(pady=20)

# Send Money Button
add_btn1=Button(app,text="Send Money",width=12,command=openSendMoneyWindow)
add_btn1.pack(pady=20)

# CASHOUT WINDOW

def openCashOutWindow():
    newWindow=Toplevel(app,bg="skyblue")
    newWindow.title("Cash Out")
    newWindow.geometry("700x350")
    Label(newWindow,text="Please fill all required fields to make transition").pack(pady=10)
    def populate_list():
        for pack in mydb.fetch():
            data_list.insert(END,pack)
    def tap_btn():
        if Mobile_Number.get()=="" or Amount.get()=="" or Pin.get()=="":
            messagebox.showerror("Reqired Fields Missing", "Please include all fields")
            return
        mydb.insert(Mobile_Number.get(),Amount.get(),Pin.get(),Pin.get())
        data_list.delete(0,END)
        data_list.insert(END,(Mobile_Number.get(),Amount.get(),Pin.get()))
        populate_list()
    Mobile_Number=StringVar()
    Label(newWindow,text="Mobile Number",font=('bold',14),).pack()
    Entry(newWindow,textvariable=Mobile_Number).pack(pady=10)
    Amount=StringVar()
    Label(newWindow,text="Amount",font=('bold',14),).pack()
    Entry(newWindow,textvariable=Amount).pack(pady=10)
    Pin=StringVar()
    Label(newWindow,text="Pin",font=('bold',14),).pack()
    Entry(newWindow,textvariable=Pin).pack(pady=10)
    data_list=Listbox(newWindow,height=8,width=50,border=1)
    data_list.pack(pady=20)
    add_btn=Button(newWindow,text="TAP",width=12,command=tap_btn)
    add_btn.pack(pady=10)

# Cash Out Button
add_btn2=Button(app,text="Cash Out",width=12,command=openCashOutWindow)
add_btn2.pack(pady=20)

# PAYBILL WINDOW

def openPayBillWindow():
    newWindow=Toplevel(app,bg="skyblue")
    newWindow.title("Pay Bill")
    newWindow.geometry("700x350")
    Label(newWindow,text="Please fill all required fields to make transition").pack(pady=10)
    def populate_list():
        for pack in mydb.fetch():
            data_list.insert(END,pack)
    def tap_btn():
        if Meter_Number.get()=="" or Amount.get()=="" or Mobile_Number.get()=="" or Reference.get()=="" or Pin.get()=="":
            messagebox.showerror("Reqired Fields Missing", "Please include all fields")
            return
        mydb.insert(Meter_Number.get(),Amount.get(),Mobile_Number.get(),Reference.get())
        data_list.delete(0,END)
        data_list.insert(END,(Meter_Number.get(),Amount.get(),Mobile_Number.get(),Reference.get(),Pin.get()))
        populate_list()
    Meter_Number=StringVar()
    Label(newWindow,text="Meter Number",font=('bold',14),).pack()
    Entry(newWindow,textvariable=Meter_Number).pack(pady=10)
    Amount=StringVar()
    Label(newWindow,text="Amount",font=('bold',14),).pack()
    Entry(newWindow,textvariable=Amount).pack(pady=10)
    Mobile_Number=StringVar()
    Label(newWindow,text="Mobile Number",font=('bold',14),).pack()
    Entry(newWindow,textvariable=Mobile_Number).pack(pady=10)
    Reference=StringVar()
    Label(newWindow,text="Reference",font=('bold',14),).pack()
    Entry(newWindow,textvariable=Reference).pack(pady=10)
    Pin=StringVar()
    Label(newWindow,text="Pin",font=('bold',14),).pack()
    Entry(newWindow,textvariable=Pin).pack(pady=10)
    data_list=Listbox(newWindow,height=8,width=50,border=1)
    data_list.pack(pady=20)
    add_btn=Button(newWindow,text="TAP",width=12,command=tap_btn)
    add_btn.pack(pady=10)


# Pay Bill Button
add_btn3=Button(app,text="Pay Bill",width=12,command=openPayBillWindow)
add_btn3.pack(pady=20)


# MAKE PAYMENT WINDOW

def openMakePaymentWindow():
    newWindow=Toplevel(app,bg="skyblue")
    newWindow.title("Make Payment")
    newWindow.geometry("700x350")
    Label(newWindow,text="Please fill all required fields to make transition").pack(pady=10)
    def populate_list():
        for pack in mydb.fetch():
            data_list.insert(END,pack)
    def tap_btn():
        if Merchant_Number.get()=="" or Amount.get()=="" or Reference.get()=="" or Pin.get()=="":
            messagebox.showerror("Reqired Fields Missing", "Please include all fields")
            return
        mydb.insert(Merchant_Number.get(),Amount.get(),Reference.get(),Pin.get())
        data_list.delete(0,END)
        data_list.insert(END,(Merchant_Number.get(),Amount.get(),Reference.get(),Pin.get()))
        populate_list()
    Merchant_Number=StringVar()
    Label(newWindow,text="Merchant Number",font=('bold',14),).pack()
    Entry(newWindow,textvariable=Merchant_Number).pack(pady=10)
    Amount=StringVar()
    Label(newWindow,text="Amount",font=('bold',14),).pack()
    Entry(newWindow,textvariable=Amount).pack(pady=10)
    Reference=StringVar()
    Label(newWindow,text="Reference",font=('bold',14),).pack()
    Entry(newWindow,textvariable=Reference).pack(pady=10)
    Pin=StringVar()
    Label(newWindow,text="Pin",font=('bold',14),).pack()
    Entry(newWindow,textvariable=Pin).pack(pady=10)
    data_list=Listbox(newWindow,height=8,width=50,border=1)
    data_list.pack(pady=20)
    add_btn=Button(newWindow,text="TAP",width=12,command=tap_btn)
    add_btn.pack(pady=10)

# Make Payment Button
add_btn4=Button(app,text="Make Payment",width=13,command=openMakePaymentWindow)
add_btn4.pack(pady=20)


app.title("MOBILE FINANCIAL SERVICE APP")
app.mainloop()
