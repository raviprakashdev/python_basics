from tkinter import *

win = Tk()

def func():
    win1=Tk()
    x=Label(win1,text="hello")
    x.pack()
    
my_label = Button(win,text="click me",command=func)

my_label.pack()

win.mainloop()
