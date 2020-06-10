from tkinter import *
gui=Tk()
def arm():
    b=4
    for i in range(int(e1.get()),int(e2.get())):
        j=i
        r=0
        o=0
        s=0
        if i<99 or i>1000:
            Label(gui,text='Please Enter The Correct Range').grid(row=5)
            break
        else:
            r=i%10
            r1=r**3
            i=i//10
            p=i%10
            p1=p**3
            i=i//10
            s=i%10
            s1=s**3
            f=r1+p1+s1
            if f==j:
                b=b+1
                Label(gui,text="The %s Is A Armstrong Number"%f).grid(row=b)
            else:
                continue
Label(gui,text='Enter the Starting Range').grid(row=0)
Label(gui,text='Enter the Ending Range').grid(row=2)
e1=Entry(gui)
e1.grid(row=1)
e2=Entry(gui)
e2.grid(row=3)
Button(gui,text='Click Me !!!',command=arm).grid(row=4)




        
