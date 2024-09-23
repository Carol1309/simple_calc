from tkinter import *

window = Tk()
window.title('Simple Calculator') 
window.iconbitmap("C:/Users/CAROLINE/OneDrive/Pictures/calculator.ico")

e=Entry(width=41,borderwidth=23,fg='white',bg='black')
e.grid(row=0,column=0,columnspan=3)
def ButtonClick(number):
    current = e.get()
    e.delete(0,END)
    e.insert(1,str(current)+str(number))

def ButtonClear():
    e.delete(0,END)

def ButtonAdd():
    global fnum,math
    math = 1
    first_number = e.get()
    e.delete(0,END)
    fnum = int(first_number)

def ButtonSub():
    global fnum,math
    math = 2
    first_number = e.get()
    e.delete(0,END)
    fnum = int(first_number)

def ButtonMul():
    global fnum,math
    math = 3
    first_number = e.get()
    e.delete(0,END)
    fnum = int(first_number)

def ButtonDiv():
    global fnum,math
    math = 4
    first_number = e.get()
    e.delete(0,END)
    fnum = int(first_number)

def ButtonEqual():
    second_number = e.get()
    e.delete(0,END)
    snum = int(second_number)

    if math == 1 :
        e.insert(2,fnum+snum)

    elif math == 2:
        e.insert(2,fnum-snum)

    elif math == 3:
        e.insert(2,fnum*snum)

    else:
        try:
            e.insert(2,fnum/snum) 
        except:
            e.insert(2,'Error') 

button1 = Button(text=1,padx=42,pady=21,fg='black',bg='#f59998',command=lambda : ButtonClick(1)).grid(row=1,column=0)
button2 = Button(text=2,padx=42,pady=21,fg='black',bg='#a7f598',command=lambda : ButtonClick(2)).grid(row=2,column=0)
button3 = Button(text=3,padx=42,pady=21,fg='black',bg='#f59998',command=lambda : ButtonClick(3)).grid(row=3,column=0)

button4 = Button(text=4,padx=42,pady=21,fg='black',bg='#a7f598',command=lambda : ButtonClick(4)).grid(row=1,column=1)
button5 = Button(text=5,padx=42,pady=21,fg='black',bg='#f59998',command=lambda : ButtonClick(5)).grid(row=2,column=1)
button6 = Button(text=6,padx=42,pady=21,fg='black',bg='#a7f598',command=lambda : ButtonClick(6)).grid(row=3,column=1)

button7 = Button(text=7,padx=42,pady=21,fg='black',bg='#f59998',command=lambda : ButtonClick(7)).grid(row=1,column=2)
button8 = Button(text=8,padx=42,pady=21,fg='black',bg='#a7f598',command=lambda : ButtonClick(8)).grid(row=2,column=2)
button9 = Button(text=9,padx=42,pady=21,fg='black',bg='#f59998',command=lambda : ButtonClick(9)).grid(row=3,column=2)

button0 = Button(text=0,padx=42,pady=21,fg='black',bg='#0fabab',command=lambda : ButtonClick(0)).grid(row=4,column=2)
buttonclear = Button(text='Clear',padx=80,pady=21,fg='black',bg='#7dd1d0',command=ButtonClear).grid(row=4,column=0,columnspan=2)

buttonadd = Button(text='+',padx=38,pady=21,fg='black',bg='#0fabab',command=ButtonAdd).grid(row=0,column=4)
buttonsub = Button(text='-',padx=39,pady=21,fg='black',bg='#0fabab',command=ButtonSub).grid(row=1,column=4)

buttonmul = Button(text='*',padx=39,pady=21,fg='black',bg='#0fabab',command=ButtonMul).grid(row=2,column=4)
buttondiv = Button(text='/',padx=39,pady=21,fg='black',bg='#0fabab',command=ButtonDiv).grid(row=3,column=4)
buttonequal = Button(text='=',padx=38,pady=21,fg='black',bg='#0fabab',command=ButtonEqual).grid(row=4,column=4)
window.mainloop()
