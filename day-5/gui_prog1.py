# submit to csv
# refer D J Oamen youtube channel
# create library management system in python - full tutorial
from tkinter import *
import csv

root = Tk()

root.title("Simple Calculator")
root.geometry("300x300") # size of window

Label(root,text = "Name").grid(column=0,row=1)

Label(root,text = "Phone").grid(column=0,row=2)

Label(root,text = "Age").grid(column=0,row=3)

Label(root,text = "Address").grid(column=0,row=4)

name = Entry(root)
name.grid(column=1,row = 1)

ph = Entry(root)
ph.grid(column=1,row = 2)

age = Entry(root)
age.grid(column=1,row = 3)

addr = Entry(root)
addr.grid(column=1,row = 4)

def addData():
    f = open("gui_db1.csv","a",newline="")
    obj = csv.writer(f)
    list1 = [name.get(),ph.get(),int(age.get()),addr.get()]
    obj.writerow(list1)
    f.close()

Button(root,text="Add Data",command = addData).grid(column=1,row=5)

root.mainloop()
