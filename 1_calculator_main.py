"""Simple layout"""
from tkinter import *

wholestring=''
calstaring=''
sym=0

def getnum(value):
    global wholestring
    global calstaring
    global sym

    sym=0
    wholestring=wholestring+str(value)
    calstaring=calstaring+str(value)

    label.config(text=wholestring)

def getsym(value):
    global wholestring
    global calstaring
    global sym

    sym=1
    calstaring=calstaring+value
    wholestring=wholestring+" "+value+" "

    label.config(text=wholestring)

def cut():
    global wholestring
    global calstaring
    global sym

    if(sym==1):
        wholestring=wholestring[:-3]
    else:
        wholestring=wholestring[:-1]

    calstaring=calstaring[:-1]
    label.config(text=wholestring)

def geteq():
    global wholestring
    global calstaring

    value=eval(calstaring)
    pr=str(value)
    label.config(text=pr)

    wholestring=''
    calstaring=''
    

def clr():
    global wholestring
    global calstaring

    wholestring=''
    calstaring=''

    label.config(text='')   

if __name__ == "__main__":
    sandeep=Tk() 
    sandeep.geometry('360x400')
    sandeep.minsize(360,400)


    frame0=Frame(master=sandeep,bg="white")
    frame0.pack(fill=BOTH,expand=True)

    label=Label(master=frame0,text="",font="calibari 20",height=3,bg='white')
    label.pack(fil=BOTH,side='right')

    frame1=Frame(master=sandeep,bg="red",height=20,width=20)
    frame1.pack(fill=BOTH,expand=True)

    button1=Button(master=frame1,text="1",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',command=lambda:getnum(1))
    button1.grid(row=0,column=0)   

    button2=Button(master=frame1,text="2",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',command=lambda:getnum(2))
    button2.grid(row=0,column=1)   

    button3=Button(master=frame1,text="3",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',command=lambda:getnum(3))
    button3.grid(row=0,column=2)   

    button4=Button(master=frame1,text="4",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',command=lambda:getnum(4))
    button4.grid(row=1,column=0)   

    button5=Button(master=frame1,text="5",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',command=lambda:getnum(5))
    button5.grid(row=1,column=1)   

    button6=Button(master=frame1,text="6",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',command=lambda:getnum(6))
    button6.grid(row=1,column=2)   

    button7=Button(master=frame1,text="7",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',command=lambda:getnum(7))
    button7.grid(row=2,column=0)   

    button8=Button(master=frame1,text="8",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',command=lambda:getnum(8))
    button8.grid(row=2,column=1)   

    button9=Button(master=frame1,text="9",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',command=lambda:getnum(9))
    button9.grid(row=2,column=2)   

    buttonadd=Button(master=frame1,text="0",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',command=lambda:getnum("0")) 
    buttonadd.grid(row=3,column=0)

    buttoncut=Button(master=frame1,text="❌",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',command=lambda:cut()) 
    buttoncut.grid(row=3,column=1)

    buttoneq=Button(master=frame1,text="=",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',command=lambda:geteq()) 
    buttoneq.grid(row=3,column=2)


    buttonadd=Button(master=frame1,text="+",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',command=lambda:getsym("+"))
    buttonadd.grid(row=0,column=3)   

    buttonsub=Button(master=frame1,text="-",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',command=lambda:getsym("-"))
    buttonsub.grid(row=1,column=3)   

    buttonmul=Button(master=frame1,text="*",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',command=lambda:getsym("*"))
    buttonmul.grid(row=2,column=3) 

    buttondiv=Button(master=frame1,text="/",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',command=lambda:getsym("/"))
    buttondiv.grid(row=3,column=3) 



    for i in range(4):
        for j in range(4):
            frame1.columnconfigure(i, weight=1,pad=10)
            frame1.rowconfigure(j, weight=1,pad=10)


    sandeep.mainloop()
