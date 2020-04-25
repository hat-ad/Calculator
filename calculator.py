from tkinter import *
exp=""
def __display():
    value=entry.get()
    for val in value:
        if val=='x':
            value=value.replace('x','*')
    equn.set(str(eval(value)))

def __input(value):
    global exp
    exp=exp+str(value)
    equn.set(exp)

def clear():
    global exp
    exp= ""
    equn.set("")

master=Tk()

master.title("Calculator")
master.iconbitmap('icons.ico')
master.minsize(width=338,height=365)
master.maxsize(width=338,height=365)

# Creating the buttons
button1 = Button(master, text="1", bd=4, font=("Arial 26 "), padx=16, command=lambda :__input('1'), activebackground="cyan")
button2 = Button(master, text="2", font=("Arial 26 "), bd=4, padx=16, command=lambda :__input('2'), activebackground="cyan")
button3 = Button(master, text="3", font=("Arial 26 "), bd=4, padx=16, command=lambda :__input('3'), activebackground="cyan")
button4 = Button(master, text="4", font=("Arial 26 "), bd=4, padx=16, command=lambda :__input('4'), activebackground="cyan")
button5 = Button(master, text="5", font=("Arial 26 "), bd=4, padx=16, command=lambda :__input('5'), activebackground="cyan")
button6 = Button(master, text="6", font=("Arial 26 "), bd=4, padx=16, command=lambda :__input('6'), activebackground="cyan")
button7 = Button(master, text="7", font=("Arial 26 "), bd=4, padx=16, command=lambda :__input('7'), activebackground="cyan")
button8 = Button(master, text="8", font=("Arial 26 "), bd=4, padx=16, command=lambda :__input('8'), activebackground="cyan")
button9 = Button(master, text="9", font=("Arial 26 "), bd=4, padx=16, command=lambda :__input('9'), activebackground="cyan")
button0 = Button(master, text="0", font=("Arial 26 "), bd=4, padx=16, command=lambda :__input('0'), activebackground="cyan")


#creating Entry Field
equn=StringVar()
entry=Entry(master,font=("Arial",20),bd=16,justify=RIGHT,insertwidth=4,textvariable=equn)

plus = Button(master, text="+", font=("Arial 26 "), bd=4, padx=15, command=lambda :__input('+'), activebackground="cyan")
minus = Button(master, text="-", font=("Arial 26 "), bd=4, padx=18, command=lambda :__input('-'), activebackground="cyan")
multiplication = Button(master, text="x", font=("Arial 26 "), bd=4, padx=16, command=lambda :__input('x'), activebackground="cyan")
division = Button(master, text="/", font=("Arial 26 "), bd=4, padx=19, command=lambda :__input('/'), activebackground="cyan")
equ = Button(master, text="=", font=("Arial 26 "), bd=4, padx=16, command=__display, activebackground="cyan")
clear = Button(master, text="C",font=("Arial 26 "),bd=4,padx=14,command=clear,activebackground="cyan")



#packing it in the layout
entry.grid(row=0,columnspan=4)
button9.grid(row=1,column=0)
button8.grid(row=1,column=1)
button7.grid(row=1,column=2)
button6.grid(row=2,column=0)
button5.grid(row=2,column=1)
button4.grid(row=2,column=2)
button3.grid(row=3,column=0)
button2.grid(row=3,column=1)
button1.grid(row=3,column=2)
button0.grid(row=4,column=0)
plus.grid(row=1,column=3)
minus.grid(row=2,column=3)
multiplication.grid(row=3,column=3)
division.grid(row=4,column=3)
equ.grid(row=4,column=2)
clear.grid(row=4,column=1)


master.mainloop()


