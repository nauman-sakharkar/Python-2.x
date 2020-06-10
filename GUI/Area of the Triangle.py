from tkinter import *
gui=Tk()
def t():
    a=.5*int(e1.get())*int(e2.get())
    l.configure(text="Area of the Triangle is %s cm"%a)
b=Label(gui,text='Enter the Height of the Triangle(cm)').grid(row=0)
h=Label(gui,text='Enter the Base of the Triangle(cm)').grid(row=2)
b1=Button(gui,text='Get',command=t).grid(row=5)
e1=Entry(gui)
e1.grid(row=1)
e2=Entry(gui)
e2.grid(row=3)
l=Label(gui,text="Area of the Triangle is ")
l.grid(row=6)
