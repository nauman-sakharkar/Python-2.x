from tkinter import *
gui=Tk()
gui.title("Basic Calculator")
aa=0

def insert(a):
    e.config(state='normal')
    global aa
    e.insert(aa,a)
    aa=aa+1
    e.config(state='readonly')

def cal():
    e.config(state='normal')    
    a=e.get()
    e.delete(0, END)
    e.insert(0,eval(a))
    e.config(state='readonly')

def clear():
    e.config(state='normal') 
    e.delete(0, END)
    e.insert(0,0)
    e.config(state='readonly')
    
e=Entry(gui,state='readonly',justify='right',bg='gray0',fg='red3')
e.grid(row=0,columnspan=4,column=0,sticky="news")

Button(gui,text="C",width=5,command=clear,relief='groove',bg='navajo white').grid(row=1,column=0)
Button(gui,text="/",width=5,command=lambda:insert('/'),relief='groove',bg='lavender').grid(row=1,column=1)
Button(gui,text="*",width=5,command=lambda:insert('*'),relief='groove',bg='lavender').grid(row=1,column=2)
Button(gui,text="-",width=5,command=lambda:insert('-'),relief='groove',bg='lavender').grid(row=1,column=3)

Button(gui,text="7",width=5,command=lambda:insert(7),bg='misty rose',relief='groove').grid(row=2,column=0)
Button(gui,text="8",width=5,command=lambda:insert(8),bg='misty rose',relief='groove').grid(row=2,column=1)
Button(gui,text="9",width=5,command=lambda:insert(9),bg='misty rose',relief='groove').grid(row=2,column=2)
Button(gui,text="+",width=5,command=lambda:insert('+'),relief='groove',bg='lavender').grid(row=2,column=3,rowspan=2,sticky='ns')

Button(gui,text="4",width=5,command=lambda:insert(4),relief='groove',bg='misty rose').grid(row=3,column=0)
Button(gui,text="5",width=5,command=lambda:insert(5),relief='groove',bg='misty rose').grid(row=3,column=1)
Button(gui,text="6",width=5,command=lambda:insert(6),relief='groove',bg='misty rose').grid(row=3,column=2)

Button(gui,text="1",width=5,command=lambda:insert(1),relief='groove',bg='misty rose').grid(row=4,column=0)
Button(gui,text="2",width=5,command=lambda:insert(2),relief='groove',bg='misty rose').grid(row=4,column=1)
Button(gui,text="3",width=5,command=lambda:insert(3),relief='groove',bg='misty rose').grid(row=4,column=2)
Button(gui,text="=",width=5,command=cal,relief='groove',bg='navajo white').grid(row=4,column=3,rowspan=2,sticky='ns')

Button(gui,text="0",width=5,command=lambda:insert(0),relief='groove',bg='misty rose').grid(row=5,column=0,columnspan=2,sticky='we')
Button(gui,text=".",width=5,command=lambda:insert('.'),relief='groove',bg='lemon chiffon').grid(row=5,column=2)

Label(gui,text="-----------------------------------\nNauman - 648\n-----------------------------------").grid(row=6,column=0,columnspan=4,sticky='ew')
