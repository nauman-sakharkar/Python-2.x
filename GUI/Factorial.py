from tkinter import *
gui=Tk()
def c():
    a=int(e.get())
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    Label(gui,text="Answer : %s"%fact).grid(row=2)
Label(gui,text="Enter the Number").grid(row=0)
e=Entry(gui)
e.grid(row=1)
Label(gui,text="Answer : ").grid(row=2)
Button(gui,text="Answer : ",command=c).grid(row=3)

