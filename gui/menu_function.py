from tkinter import *

win = Tk()

win.geometry("600x400")
mymenu=Menu(win)

win.config(menu=mymenu)

def func():
    win1=Tk()
    x=Label(win1,text="file opened")
    x.pack()

mymenu.add_cascade(label="File",command=func)
mymenu.add_cascade(label="Edit")

win.mainloop()
