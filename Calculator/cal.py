from tkinter import *
import tkinter.font as font
window = Tk()
window.title("Calculator")
window.geometry('400x500')
window.resizable(False,False)
exp = ""
def insert(item):
    global exp
    exp = exp.join(str(item))
    t1.insert(END,exp)
    #3print(exp)
    #print(exp)
def clear():
    print('clicked clear')
    global exp
    exp = ""
    t1.delete("1.0",END)

def cal():
    global exp
    #print(exp)

    result = str(eval(t1.get("1.0",END)))
    print(result)
    t1.delete("1.0",END)
    t1.insert(END,result)
    exp=" "


helv36 = font.Font(family='Helvetica',size=36,weight='bold')

bc = Button(window,text="C",bg="green",fg="white",width=3,font=helv36,command=lambda:clear())
bc.grid(row=0,column=0)

t1 = Text(window,width=20,height=2,font=helv36)
t1.grid(row=0,columnspan=100,column=1)


b9 = Button(window,text="9",bg="green",fg="white",width=3,font=helv36,command=lambda:insert(9))
b9.grid(row=1,column=0)
#b9.bind('<Button-2>',insert(b9))

b8 =  Button(window,text="8",bg="green",fg="white",width=3,font=helv36,command=lambda:insert(8))
b8.grid(row=1,column=1)

b7 = Button(window,text="7",bg="green",fg="white",width=3,font=helv36,command=lambda:insert(7))
b7.grid(row=1,column=2)

bdiv = Button(window,text="/",bg="green",fg="white",width=3,font=helv36,command=lambda:insert("/"))
bdiv.grid(row=1,column=3)
#-----

b6 = Button(window,text="6",bg="green",fg="white",width=3,font=helv36,command=lambda:insert(6))
b6.grid(row=2,column=0)

b5 = Button(window,text="5",bg="green",fg="white",width=3,font=helv36,command=lambda:insert(5))
b5.grid(row=2,column=1)

b4 = Button(window,text="4",bg="green",fg="white",width=3,font=helv36,command=lambda:insert(4))
b4.grid(row=2,column=2)

bmul = Button(window,text="*",bg="green",fg="white",width=3,font=helv36,command=lambda:insert("*"))
bmul.grid(row=2,column=3)
#--

b3 = Button(window,text="3",bg="green",fg="white",width=3,font=helv36,command=lambda:insert(3))
b3.grid(row=3,column=0)

b2 = Button(window,text="2",bg="green",fg="white",width=3,font=helv36,command=lambda:insert(2))
b2.grid(row=3,column=1)

b1 = Button(window,text="1",bg="green",fg="white",width=3,font=helv36,command=lambda:insert(1))
b1.grid(row=3,column=2)

bsub = Button(window,text="-",bg="green",fg="white",width=3,font=helv36,command=lambda:insert("-"))
bsub.grid(row=3,column=3)
#---

bdot = Button(window,text=".",bg="green",fg="white",width=3,font=helv36,command=lambda:insert("."))
bdot.grid(row=4,column=0)

b0 = Button(window,text="0",bg="green",fg="white",width=3,font=helv36,command=lambda:insert(0))
b0.grid(row=4,column=1)

beq = Button(window,text="=",bg="green",fg="white",width=3,font=helv36,command=lambda:cal())
beq.grid(row=4,column=2)

bplus = Button(window,text="+",bg="green",fg="white",width=3,font=helv36,command=lambda:insert("+"))
bplus.grid(row=4,column=3)


window.mainloop()
