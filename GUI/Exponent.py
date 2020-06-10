from tkinter import *
gui=Tk()
def c():
    x=int(e1.get())
    n=int(e2.get())
    t=1
    sum=0
    sum=sum+t
    for i in range(1,n):
        t=(x*t)/(i)
        sum=t+sum
    Label(gui,text="Expoent Value of %s is %s"%(x,sum)) .grid(row=4)
Label(gui,text="Please Enter The Number").grid(row=0)
Label(gui,text="Please Enter The Number Of Steps").grid(row=2)
e1=Entry(gui)
e1.grid(row=1)
e2=Entry(gui)
e2.grid(row=3)
Label(gui,text="Anwers : ").grid(row=4)
Button(gui,text="Answer!!!",command=c).grid(row=5)
