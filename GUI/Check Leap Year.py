from tkinter import *
gui=Tk()
def c():
    a=int(e1.get())
    if a%4==0:
        messagebox.showinfo('Answer',"%s Is A Leap Year"%a)
    else:
        messagebox.showinfo('Answer',"%s Is Not A Leap Year"%a)
Label(gui,text="Please Enter The Year").grid(row=0)
e1=Entry(gui)
e1.grid(row=1)
Button(gui,text="Check!!!",command=c).grid(row=3)


