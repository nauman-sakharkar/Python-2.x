from tkinter import *
gui=Tk()
def c():
    x=int(e1.get())
    n=int(e2.get())
    xx=x
    x=(x*3.142)/(180)
    t=1
    s=-1
    sum=0
    sum=sum+t
    for i in range(1,n):
        t=(x*x*t*s)/((2*i)+(2*(i-1)))
        sum=t+sum
    Label(gui,text="Cosine Value of %s is %s"%(xx,sum)) .grid(row=4)
Label(gui,text="Please Enter The Number").grid(row=0)
Label(gui,text="Please Enter The Number Of Steps").grid(row=2)
e1=Entry(gui)
e1.grid(row=1)
e2=Entry(gui)
e2.grid(row=3)
Label(gui,text="Anwers : ").grid(row=4)
Button(gui,text="Answer!!!",command=c).grid(row=5)


