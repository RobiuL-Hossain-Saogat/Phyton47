from tkinter import *
# from tkinter.ttk import *
import random

def calculate_love():
	rand=random.randint(1,100)
	rand2=2 
	temp="".join(random.sample(rand,rand2))
	result.config(text=temp)
	
app = Tk()
applabel=Label(app,text="Synergy Calculator????").pack(pady=10)

# 1st name part
name=StringVar()
name_label=Label(app,text="Enter Your Name").pack(pady=5)
name_entry=Entry(app,textvariable=name).pack(pady=5)

# 2nd name part
frnd_name=StringVar()
frnd_name_label=Label(app,text="Enter Your Friend Name").pack(pady=5)
frnd_name_entry=Entry(app,textvariable=frnd_name).pack(pady=5)

# button widget
button=Button(app,text="Calculate",width=12,command=calculate_love).pack()

#result
result=Label(app,text=" ")
result.pack()

app.title("Synergy Culculator????")
app.geometry('400x240')
app.mainloop()