"""simple layout"""
""" Trying to solve the error handling in this version"""
"""Adding some new features % () clr root power"""
""" Giving some design to it show the result in different frame """

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
    labelsr.config(text="")

def getsym(value):
    global wholestring
    global calstaring
    global sym

    sym=1
    if(value=="^"):
        calstaring=calstaring+"**"
        wholestring=wholestring+" "+"^"+" "
    else:
        calstaring=calstaring+value
        wholestring=wholestring+" "+value+" "

    label.config(text=wholestring)
    labelsr.config(text="")

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
    labelsr.config(text="")

def geteq():
    global wholestring
    global calstaring

    try:
        value=eval(calstaring)
        pr=str(value)
        labelsr.config(text=pr)
    except ZeroDivisionError:
        labelsr.config(text="Error :: division by zero")
    except SyntaxError:
        labelsr.config(text="Error :: invalid syntax")
        

    wholestring=''
    calstaring=''
    

def clr():
    global wholestring
    global calstaring
    global sym

    wholestring=''
    calstaring=''
    sym=0

    label.config(text='')
    labelsr.config(text="")   

if __name__ == "__main__":
    sandeep=Tk() 
    sandeep.geometry('500x500')
    sandeep.minsize(500,500)
    sandeep.title("CALCULATOR")


    frame0=Frame(master=sandeep,bg="blue",relief="sunken",borderwidth=10)
    frame0.pack(fill=BOTH,expand=True)

    frames=Frame(master=frame0,bg='white')
    frames.pack(fill=BOTH,expand=True,side="top")
    
    label=Label(master=frames,text="",font="calibari 16",height=2,bg='white')
    label.pack(fil=BOTH,side='right')
    
    framer=Frame(master=frame0,bg='blue')
    framer.pack(fill=BOTH,expand=True,side="bottom")
    
    labelr=Label(master=framer,text="Result ",font="calibari 15",bg="white",width=5,height=2)
    labelr.grid(row=0,column=0)

    labelsr=Label(master=framer,text="",font="calibari 14",bg="orange",width=400,height=1,relief="sunken",borderwidth=14)
    labelsr.grid(row=0,column=1)

    framer.rowconfigure(0,weight=1)
    framer.columnconfigure(1,weight=8)

    




    frame1=Frame(master=sandeep,bg="black",height=20,width=20,relief="raised",borderwidth=10)
    frame1.pack(fill=BOTH,expand=True)
 
    buttonclr=Button(master=frame1,text="clr",font="calibari 20 bold",width=400,height=200,bg='red',fg='black',relief="raised",borderwidth=10,command=lambda:clr())
    buttonclr.grid(row=0,column=0)   

    frameb=Frame(master=frame1)
    frameb.grid(row=0,column=1)
    buttonlb=Button(master=frameb,text="(",font="calibari 20 bold",width=50,height=10,bg='light green',fg='black',relief="raised",borderwidth=10,command=lambda:getnum("("))
    buttonlb.grid(row=0,column=0)   
    buttonrb=Button(master=frameb,text=")",font="calibari 20 bold",width=50,height=10,bg='light green',fg='black',relief="raised",borderwidth=10,command=lambda:getnum(")"))
    buttonrb.grid(row=0,column=1) 
    for i in range(1):
        for j in range(2):
            frameb.rowconfigure(i, weight=1,pad=200)
            frameb.columnconfigure(j, weight=1,pad=200)



    button1=Button(master=frame1,text="1",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',relief="raised",borderwidth=10,command=lambda:getnum(1))
    button1.grid(row=1,column=0)   

    button2=Button(master=frame1,text="2",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',relief="raised",borderwidth=10,command=lambda:getnum(2))
    button2.grid(row=1,column=1)   

    button3=Button(master=frame1,text="3",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',relief="raised",borderwidth=10,command=lambda:getnum(3))
    button3.grid(row=1,column=2)   

    button4=Button(master=frame1,text="4",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',relief="raised",borderwidth=10,command=lambda:getnum(4))
    button4.grid(row=2,column=0)   

    button5=Button(master=frame1,text="5",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',relief="raised",borderwidth=10,command=lambda:getnum(5))
    button5.grid(row=2,column=1)   

    button6=Button(master=frame1,text="6",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',relief="raised",borderwidth=10,command=lambda:getnum(6))
    button6.grid(row=2,column=2)   

    button7=Button(master=frame1,text="7",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',relief="raised",borderwidth=10,command=lambda:getnum(7))
    button7.grid(row=3,column=0)   

    button8=Button(master=frame1,text="8",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',relief="raised",borderwidth=10,command=lambda:getnum(8))
    button8.grid(row=3,column=1)   

    button9=Button(master=frame1,text="9",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',relief="raised",borderwidth=10,command=lambda:getnum(9))
    button9.grid(row=3,column=2)   

    buttonadd=Button(master=frame1,text="0",font="calibari 20 bold",width=400,height=200,bg='white',fg='black',relief="raised",borderwidth=10,command=lambda:getnum("0")) 
    buttonadd.grid(row=4,column=0)

    buttoncut=Button(master=frame1,text="❌",font="calibari 20 bold",width=400,height=200,bg='pink',fg='black',relief="raised",borderwidth=10,command=lambda:cut()) 
    buttoncut.grid(row=4,column=1)

    buttoneq=Button(master=frame1,text="=",font="calibari 20 bold",width=400,height=200,bg='orange',fg='black',relief="raised",borderwidth=10,command=lambda:geteq()) 
    buttoneq.grid(row=4,column=2)


    buttonadd=Button(master=frame1,text="+",font="calibari 20 bold",width=400,height=200,bg='light green',fg='black',relief="raised",borderwidth=10,command=lambda:getsym("+"))
    buttonadd.grid(row=1,column=3)   

    buttonsub=Button(master=frame1,text="-",font="calibari 20 bold",width=400,height=200,bg='light green',fg='black',relief="raised",borderwidth=10,command=lambda:getsym("-"))
    buttonsub.grid(row=2,column=3)   

    buttonmul=Button(master=frame1,text="*",font="calibari 20 bold",width=400,height=200,bg='light green',fg='black',relief="raised",borderwidth=10,command=lambda:getsym("*"))
    buttonmul.grid(row=3,column=3) 

    buttondiv=Button(master=frame1,text="/",font="calibari 20 bold",width=400,height=200,bg='light green',fg='black',relief="raised",borderwidth=10,command=lambda:getsym("/"))
    buttondiv.grid(row=4,column=3) 

    buttonpow=Button(master=frame1,text="^",font="calibari 20 bold",width=400,height=200,bg='light green',fg='black',relief="raised",borderwidth=10,command=lambda:getsym("^"))
    buttonpow.grid(row=0,column=3)    

    buttonmod=Button(master=frame1,text="%",font="calibari 20 bold",width=400,height=200,bg='light green',fg='black',relief="raised",borderwidth=10,command=lambda:getsym("%"))
    buttonmod.grid(row=0,column=2)  

    for i in range(5):
        for j in range(5):
            frame1.rowconfigure(i, weight=1,pad=10)
            frame1.columnconfigure(j, weight=1,pad=10)


    sandeep.mainloop()
