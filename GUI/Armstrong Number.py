from Tkinter import *
gui=Tk()
def a():
    a=int(e1.get())
    b=a
    if a>99 and a<1000:
        r=a%10
        r1=r**3
        a=a//10
        p=a%10
        p1=p**3
        a=a//10
        s=a%10
        s1=s**3
        f=r1+p1+s1
        if f==b:
            Label(gui,text="The Entered Number Is A Armstrong Number").grid(row=3)
        else:
            Label(gui,text="The Entered Number Is Not A Armstrong Number").grid(row=3)
    else:
        Label(gui,text="Enter the Number Betwee 100 to 999").grid(row=3)
Label(gui,text='Enter The Number').grid(row=0)
b1=Button(gui,text='Get',command=a).grid(row=2)
e1=Entry(gui)
e1.grid(row=1)
gui.mainloop()
