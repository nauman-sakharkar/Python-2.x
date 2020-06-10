from tkinter import *
gui=Tk()
gui.configure(bg= 'SlateBlue1')
def d():
    try:
        d=int(e1.get())
    except ValueError:
        e1.focus_set()
    try:
        m=int(e2.get())
    except ValueError:
        e2.focus_set()
    try:
        y=int(e3.get())
    except ValueError:
            e3.focus_set()     
    try:
        n=int(e4.get())
    except ValueError:
             e4.focus_set()   
    try:
        s=int(e5.get())
    except ValueError:
            e5.focus_set()       
            
    if m>12 or d>31 or m<1 or d<1:
        messagebox.showinfo('Answer',"Please Enter The Correct Date/Month(Range for Date(1-31) & Range for Month(1-12)")
    elif s=="+":
        if m==2:
            if y%4==0:
                if d==29:
                    d=1
                    n=n-1
                    d=d+n
                    m=m+1
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
                elif d>29:
                    messagebox.showinfo('Answer',"Feb Doesn't Have more than 29 date (Leap Year)")
                else:
                    d1=d+n
                    if d1>29:
                        d=29-d
                        n=n-d
                        d=n
                        m=1+m
                        messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
                    else:
                        d=d+n
                        messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
            elif d==28:
                d=1
                n=n-1
                d=d+n
                m=m+1
                messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
            elif d>28:
                d=d+n
                messagebox.showinfo('Answer',"Feb Doesn't Have more than 28 date (Leap Year)")
            else:
                d1=d+n
                if d1>28:
                    d=28-d
                    n=n-d
                    d=n
                    m=1+m
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
                else:
                    d=d+n
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
        elif m==12:
            if d==31:
                d=1
                n=n-1
                d=d+n
                m=1
                y=y+1
                messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
            else:
                d1=d+n
                if d1>31:
                    d=31-d
                    n=n-d
                    d=n
                    m=1
                    y=y+1
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
                else:
                    d=d+n
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
        elif m==1 or m==3 or m==5 or m==7 or m==10 or m==8:
            if d==31:
                d=1
                n=n-1
                d=d+n
                m=m+1
                messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
            else:
                d1=d+n
                if d1>31:
                    d=31-d
                    n=n-d
                    d=n
                    m=1+m
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
                else:
                    d=d+n
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
        elif m==4 or m==6 or m==9 or m==11:
            if d==30:
                d=1
                n=n-1
                d=d+n
                m=m+1
                messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
            else:
                d1=d+n
                if d1>30:
                    d=30-d
                    n=n-d
                    d=n
                    m=1+m
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
                else:
                    d=d+n
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
    elif s=="-":
        if m==2:
            if y%4==0:
                if d==1:
                    d=31-n+1
                    m=m-1
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
                elif d>29:
                    messagebox.showinfo('Answer',"Feb Doesn't Have more than 29 date (Leap Year)")
                else:
                    d1=d-n
                    if d1<=0:
                        d=1-d
                        n=n+d-1
                        d=31-n
                        m=m-1
                        messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
                    else:
                        d=d-n
                        messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
            elif d==1:
                d=31-n+1
                m=m-1
                messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
            elif d>28:
                d=d+n
                messagebox.showinfo('Answer',"Feb Doesn't Have more than 28 date (Leap Year)")
            else:
                d1=d-n
                if d1<=0:
                    d=1-d
                    n=n+d-1
                    d=31-n
                    m=m-1
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
                else:
                    d=d-n
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
        elif m==1:
            if d==1:
                d=31-n+1
                m=1
                y=y-1
                messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
            else:
                d1=d-n
                if d1<=0:
                    d=1-d
                    n=n+d-1
                    d=31-n
                    m=1
                    y=y-1
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
                else:
                    d=d-n
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
        elif m==3:
            if y%4==0:
                if d==1:
                    d=29-n+1
                    m=m-1
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
                else:
                    d1=d-n
                    if d1<=0:
                        d=1-d
                        n=n+d-1
                        d=29-n
                        m=m-1
                        messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
                    else:
                        d=d-n
                        messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
            else:
                if d==1:
                    d=28-n+1
                    m=m-1
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
                else:
                    d1=d-n
                    if d1<=0:
                        d=1-d
                        n=n+d-1
                        d=28-n
                        m=m-1
                        messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
                    else:
                        d=d-n
                        messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
                        
        elif m==5 or m==7 or m==10 or m==12:
            if d==1:
                d=30-n+1
                m=m-1
                messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
            else:
                d1=d-n
                if d1<=0:
                    d=1-d
                    n=n+d-1
                    d=30-n
                    m=m-1
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
                else:
                    d=d-n
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
        elif m==8:
            if d==1:
                d=31-n+1
                m=m-1
                messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
            else:
                d1=d-n
                if d1<=0:
                    d=1-d
                    n=n+d-1
                    d=31-n
                    m=m-1
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
                else:
                    d=d-n
                    messagebox.showinfo('Answer',"Your Requested Date : %s/%s/%s"%(d,m,y))
Label(gui,text="▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀",bg='sienna1',fg='snow').grid(row=0,sticky=E)
Label(gui,text="▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄",bg='sienna1',fg='snow').grid(row=100,sticky=E)
Label(gui,text="▄▀▄▀▄▀▄▀▄▀▄",bg='sienna1',fg='snow').grid(row=0,column=1,sticky=E)
Label(gui,text="▀▄▀▄▀▄▀▄▀▄▀",bg='sienna1',fg='snow').grid(row=100,column=1,sticky=E)
Label(gui,text="▀▄▀▄▀▄",bg='sienna1',fg='snow').grid(row=0,column=2,sticky=W)
Label(gui,text="▀▄▀▄▀▄",bg='sienna1',fg='snow').grid(row=100,column=2,sticky=W)
Label(gui,text="Please Enter The Date : ",bg='SpringGreen3',bd=1,fg='snow',font='bold''italic').grid(row=1,column=0,sticky=E)
Label(gui,text="Please Enter The Month : ",bg='SpringGreen3',bd=1,fg='snow',font='bold''italic').grid(row=2,column=0,sticky=E)
Label(gui,text="Please Enter The Year : ",bg='SpringGreen3',bd=1,fg='snow',font='bold''italic').grid(row=3,column=0,sticky=E)
Label(gui,text="Please Enter The Increment/Decrement : ",bg='SpringGreen3',bd=1,fg='snow',font='bold''italic').grid(row=4,column=0,sticky=E)
Label(gui,text="Please Enter The Arithmetic Operation : ",bg='SpringGreen3',bd=1,fg='snow',font='bold''italic').grid(row=5,column=0,sticky=E)
e1=Entry(gui,bd=5,bg='gainsboro',fg='SpringGreen4')
e1.grid(row=1,column=1,sticky=W)
e2=Entry(gui,bd=5,bg='gainsboro',fg='SpringGreen4')
e2.grid(row=2,column=1,sticky=W)
e3=Entry(gui,bd=5,bg='gainsboro',fg='SpringGreen4')
e3.grid(row=3,column=1,sticky=W)
e4=Entry(gui,bd=5,bg='gainsboro',fg='SpringGreen4')
e4.grid(row=4,column=1,sticky=W)
e5=Entry(gui,bd=5,bg='gainsboro',fg='SpringGreen4')
e5.grid(row=5,column=1,sticky=W)
Button(gui,text='Answer',bd=5,font='bold',command=d,bg='DarkOrchid4',fg='snow',activebackground='sienna1',activeforeground='snow').grid(row=3,column=2)


