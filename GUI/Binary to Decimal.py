from tkinter import *
gui=Tk()
def c():
    j=1
    o=0
    a=int(e1.get())
    while True:
        if a<1:
            break
        else:
            s=a%10
            o=o+s*j
            a=a//10
            j=j*2
    Label(gui,text="Answer : %s"%o).grid(row=2) 
Label(gui,text="Please Enter Your Binary Number").grid(row=0)
e1=Entry(gui)
e1.grid(row=1)
Label(gui,text="Answer : ").grid(row=2)
Button(gui,text="Convert!!!",command=c).grid(row=3)


