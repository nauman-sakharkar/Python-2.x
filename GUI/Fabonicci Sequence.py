from tkinter import *
gui=Tk()
def c():
    a=int(e1.get())
    n1=0
    n2=1
    sum=1
    output=[0,1]
    if a==0:
        Label(gui,text="Fibonacci Sequence Is 0").grid(row=2)
        Label(gui,text="Sum of Fibonacci Sequence = 0").grid(row=3)
    elif a<0:
        Label(gui,text="Plese enter a positive integer").grid(row=2)
    else:
        for i in range(1,a):
            n=n1+n2
            sum=n1+n2
            n1=n2
            n2=n
            output.append(n)
        Label(gui,text="Fabonicci Sequence").grid(row=2)
        Label(gui,text=output).grid(row=3)
        Label(gui,text="Fabonicci Value of %s is %s"%(a,sum)).grid(row=4)
Label(gui,text="Please Enter the Number").grid(row=0)
e1=Entry(gui)
e1.grid(row=1)
Label(gui,text="Anwers : ").grid(row=2)
Button(gui,text="Answer!!!",command=c).grid(row=5)
