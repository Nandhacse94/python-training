# GUI
# tkinter
# web based -> django

from tkinter import *

root = Tk()

root.title("Simple Calculator")
root.geometry("300x300") # size of window

# Label -> to write something
# Entry -> to take the input
# Button

Label(root,text = "This is my first app").grid(column=0,row=0)

num1 = Entry(root)
num1.grid(column=0,row = 1)

num2 = Entry(root)
num2.grid(column=1,row = 1)

def addNum():
    a = int(num1.get())
    b = int(num2.get())
    result = a + b
    Label(root,text=result).grid(column=1,row=2)
    
Button(root,text="Add",command = addNum).grid(column=0,row=2)

def subNum():
    a = int(num1.get())
    b = int(num2.get())
    result = a - b
    Label(root,text=result).grid(column=1,row=3)
    
Button(root,text="Sub",command = subNum).grid(column=0,row=3)

def mulNum():
    a = int(num1.get())
    b = int(num2.get())
    result = a * b
    Label(root,text=result).grid(column=1,row=4)
    
Button(root,text="Mul",command = mulNum).grid(column=0,row=4)
root.mainloop()

