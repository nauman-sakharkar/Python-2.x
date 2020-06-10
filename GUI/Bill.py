from tkinter import *
gui=Tk()
gui.configure(bg='snow')
Label(gui,text='                                                             Saud Juice Center                                                                   ',anchor='center',padx=3,justify='center'\
      ,bg='SlateBlue1',fg='snow',font='bold',bd=5).grid(row=0,column=0,rowspan=2,columnspan=8)
Label(gui,text='                                                                                                                                                                                                                         ',bg='yellow').grid(row=3,column=0,columnspan=8)
Label(gui,text='                                                                                                                                                                                                                         ',bg='yellow').grid(row=2,column=0,columnspan=8)

s1=10
s2=10
s3=10
s4=10
s5=10
s6=10
s7=10
s8=10
s9=10
s10=10
Label(gui,text="Sr.No.",padx=3,bg='yellow',fg='red',pady=3).grid(row=2,column=0)
Label(gui,text="Juices",padx=3,bg='yellow',fg='red',pady=3).grid(row=2,column=1)

Label(gui,text="Half (Stock)",padx=3,bg='yellow',fg='red',pady=3).grid(row=3,column=2)
Label(gui,text="Full (Stock)",padx=3,bg='yellow',fg='red',pady=3).grid(row=3,column=3)
Label(gui,text="Half",padx=3,bg='yellow',fg='red',pady=3).grid(row=3,column=4)
Label(gui,text="Full",padx=3,bg='yellow',fg='red',pady=3).grid(row=3,column=5)
Label(gui,text="Calculate",padx=3,bg='yellow',fg='red',pady=3).grid(row=2,column=6)
Label(gui,text="Total Cost",padx=3,bg='yellow',fg='red',pady=3).grid(row=2,column=7)

Label(gui,text='                                                                                                                                                                                                                          ',bg='red').grid(row=4,column=0,columnspan=8)
Label(gui,text="1",padx=3,bg='red',fg='white').grid(row=4,column=0)
Label(gui,text="Apple",padx=3,bg='red',fg='white').grid(row=4,column=1)
Label(gui,text="30 (10)",padx=3,bg='red',fg='white').grid(row=4,column=2)
Label(gui,text="50 (10)",padx=3,bg='red',fg='white').grid(row=4,column=3)
e1=Spinbox(gui, from_=0, to=s1,width=6,justify='center',bg='snow',fg='red',bd=3,state='readonly')
e1.grid(row=4,column=4)
e2=Spinbox(gui, from_=0, to=s2,width=6,justify='center',bg='snow',fg='red',bd=3,state='readonly')
e2.grid(row=4,column=5)
ea=Entry(gui,width=10,justify='center',bd=3,bg='snow',fg='red')
ea.grid(row=4,column=7)
ea.insert(0,0)
ea.config(state='readonly',bg='snow',)

Label(gui,text='                                                                                                                                                                                                                          ',bg='dark orange').grid(row=5,column=0,columnspan=8)
Label(gui,text="2",padx=3,bg='dark orange',fg='white').grid(row=5,column=0)
Label(gui,text="Mango",padx=3,bg='dark orange',fg='white').grid(row=5,column=1)
Label(gui,text="25 (10)",padx=3,bg='dark orange',fg='white').grid(row=5,column=2)
Label(gui,text="40 (10)",padx=3,bg='dark orange',fg='white').grid(row=5,column=3)
e3=Spinbox(gui, from_=0, to=s3,width=6,justify='center',bg='snow',fg='dark orange',bd=3,state='readonly')
e3.grid(row=5,column=4)
e4=Spinbox(gui, from_=0, to=s4,width=6,justify='center',bg='snow',fg='dark orange',bd=3,state='readonly')
e4.grid(row=5,column=5)
em=Entry(gui,width=10,justify='center',bg='snow',fg='dark orange',bd=3)
em.grid(row=5,column=7)
em.insert(0,0)
em.config(state='readonly')

Label(gui,text='                                                                                                                                                                                                                          ',bg='goldenrod').grid(row=6,column=0,columnspan=8)
Label(gui,text="3",padx=3,bg='goldenrod',fg='white').grid(row=6,column=0)
Label(gui,text="Pinepple",padx=3,bg='goldenrod',fg='white').grid(row=6,column=1)
Label(gui,text="35 (10)",padx=3,bg='goldenrod',fg='white').grid(row=6,column=2)
Label(gui,text="60 (10)",padx=3,bg='goldenrod',fg='white').grid(row=6,column=3)
e5=Spinbox(gui, from_=0, to=s5,width=6,justify='center',bg='snow',fg='goldenrod',bd=3,state='readonly')
e5.grid(row=6,column=4)
e6=Spinbox(gui, from_=0, to=s6,width=6,justify='center',bg='snow',fg='goldenrod',bd=3,state='readonly')
e6.grid(row=6,column=5)
ep=Entry(gui,width=10,justify='center',bg='snow',fg='goldenrod',bd=3)
ep.grid(row=6,column=7)
ep.insert(0,0)
ep.config(state='readonly')

Label(gui,text='                                                                                                                                                                                                                          ',bg='limegreen').grid(row=7,column=0,columnspan=8)
Label(gui,text="4",padx=3,bg='limegreen',fg='white').grid(row=7,column=0)
Label(gui,text="Watermelon",padx=3,bg='limegreen',fg='white').grid(row=7,column=1)
Label(gui,text="45 (10)",padx=3,bg='limegreen',fg='white').grid(row=7,column=2)
Label(gui,text="80 (10)",padx=3,bg='limegreen',fg='white').grid(row=7,column=3)
e7=Spinbox(gui, from_=0, to=s7,width=6,justify='center',bg='snow',fg='limegreen',bd=3,state='readonly')
e7.grid(row=7,column=4)
e8=Spinbox(gui, from_=0, to=s8,width=6,justify='center',bg='snow',fg='limegreen',bd=3,state='readonly')
e8.grid(row=7,column=5)
ew=Entry(gui,width=10,justify='center',bg='snow',fg='limegreen',bd=3)
ew.grid(row=7,column=7)
ew.insert(0,0)
ew.config(state='readonly')

Label(gui,text='                                                                                                                                                                                                                          ',bg='chocolate').grid(row=8,column=0,columnspan=8)
Label(gui,text="5",padx=3,bg='chocolate',fg='white').grid(row=8,column=0)
Label(gui,text="Cocktail",padx=3,bg='chocolate',fg='white').grid(row=8,column=1)
Label(gui,text="35 (10)",padx=3,bg='chocolate',fg='white').grid(row=8,column=2)
Label(gui,text="70 (10)",padx=3,bg='chocolate',fg='white').grid(row=8,column=3)
e9=Spinbox(gui, from_=0, to=s9,width=6,justify='center',fg='chocolate',bg='snow',bd=3,state='readonly')
e9.grid(row=8,column=4)
e10=Spinbox(gui, from_=0, to=s10,width=6,justify='center',fg='chocolate',bg='snow',bd=3,state='readonly')
e10.grid(row=8,column=5)
et=Entry(gui,width=10,justify='center',fg='chocolate',bg='snow',bd=3)
et.grid(row=8,column=7)
et.insert(0,0)
et.config(state='readonly')

def c():
    a,a1=int(e1.get())*30,int(e1.get())
    b,b1=int(e2.get())*50,int(e2.get())
    c,c1=int(e3.get())*25,int(e3.get())
    d,d1=int(e4.get())*40,int(e4.get())
    e,e11=int(e5.get())*35,int(e5.get())
    f,f1=int(e6.get())*60,int(e6.get())
    g,g1=int(e7.get())*45,int(e7.get())
    h,h1=int(e8.get())*80,int(e8.get())
    i,i1=int(e9.get())*35,int(e9.get())
    j,j1=int(e10.get())*70,int(e10.get())
    a1=10-a1
    b1=10-b1
    c1=10-c1
    d1=10-d1
    e11=10-e11
    f1=10-f1
    g1=10-g1
    h1=10-h1
    i1=10-i1
    j1=10-j1
    Label(gui,text="30 (%s)"%a1,padx=3,bg='red',fg='white').grid(row=4,column=2)
    Label(gui,text="50 (%s)"%b1,padx=3,bg='red',fg='white').grid(row=4,column=3)
    Label(gui,text="25 (%s)"%c1,padx=3,bg='dark orange',fg='white').grid(row=5,column=2)
    Label(gui,text="40 (%s)"%d1,padx=3,bg='dark orange',fg='white').grid(row=5,column=3)
    Label(gui,text="35 (%s)"%e11,padx=3,bg='goldenrod',fg='white').grid(row=6,column=2)
    Label(gui,text="60 (%s)"%f1,padx=3,bg='goldenrod',fg='white').grid(row=6,column=3)
    Label(gui,text="45 (%s)"%g1,padx=3,bg='limegreen',fg='white').grid(row=7,column=2)
    Label(gui,text="80 (%s)"%h1,padx=3,bg='limegreen',fg='white').grid(row=7,column=3)
    Label(gui,text="35 (%s)"%i1,padx=3,bg='chocolate',fg='white').grid(row=8,column=2)
    Label(gui,text="70 (%s)"%j1,padx=3,bg='chocolate',fg='white').grid(row=8,column=3)
    e1.config( from_=0, to=a1)
    e2.config( from_=0, to=b1)
    e3.config( from_=0, to=c1)
    e4.config( from_=0, to=d1)
    e5.config( from_=0, to=e11)
    e6.config( from_=0, to=f1)
    e7.config( from_=0, to=g1)
    e8.config( from_=0, to=h1)
    e9.config( from_=0, to=i1)
    e10.config( from_=0, to=j1)
   
    ea.config(state='normal')
    em.config(state='normal')
    ep.config(state='normal')
    ew.config(state='normal')
    et.config(state='normal')
    ea.delete(0,END)
    em.delete(0,END)
    ep.delete(0,END)
    ew.delete(0,END)
    et.delete(0,END)
    ea.insert(0,a+b)
    em.insert(0,c+d)
    ep.insert(0,e+f)
    ew.insert(0,g+h)
    et.insert(0,i+j)
    ea.config(state='readonly')
    em.config(state='readonly')
    ep.config(state='readonly')
    ew.config(state='readonly')
    et.config(state='readonly')
Button(gui,text='Calculate',anchor='center',padx=3,command=c,bg='bisque',fg='chocolate',bd=3,font='bold'\
       ,activebackground='tomato',activeforeground='bisque').grid(row=4,column=6,rowspan=5,sticky=W+E+N+S)

def g():
    az=int(ea.get())
    bz=int(em.get())
    cz=int(ep.get())
    fz=int(ew.get())
    ez=int(et.get())
    eg.config(state='normal')
    eg.delete(0,END)
    eg.insert(0,az+bz+cz+ez+fz)
    eg.config(state='readonly')
                                            
for  i in range(0,8):
    Label(gui,text='''












''',bg='snow',fg='snow').grid(row=2,column=i,rowspan=8,sticky='NW')
Label(gui,text="Price",padx=3,bg='yellow',fg='red',pady=3).grid(row=2,column=2,columnspan=2,sticky=W+E+N+S)
Label(gui,text="Quantiy",padx=3,bg='yellow',fg='red',pady=3).grid(row=2,column=4,columnspan=2,sticky=W+E+N+S)

Label(gui,text='''












''',bg='snow',fg='snow').grid(row=2,column=4,rowspan=8,sticky='NW')
Button(gui,text='Grand Total : ',anchor='center',justify='center',command=g,font='bold',bg='DarkOrchid4',fg='snow'\
       ,activebackground='firebrick1',activeforeground='snow').grid(row=9,column=0,rowspan=2,columnspan=7)
eg=Entry(gui,width=10,justify='center',bd=5,fg='DarkOrchid4',bg='snow')
eg.grid(row=9,column=5)
eg.insert(0,0)
eg.config(state='readonly')


gui.mainloop()
