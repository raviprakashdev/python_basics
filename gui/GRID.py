from tkinter import *

win = Tk()
win.geometry("600x400")

nameE=Label(win,text="New username")
pwdE=Label(win,text="Password")

Entryname=Entry(win)
Entrypwd=Entry(win,show='*')
nameE.grid(row=1,column=0,sticky=W)
pwdE.grid(row=2,column=0,sticky=W)
Entryname.grid(row=1,column=1)
Entrypwd.grid(row=2,column=1)

signin=Button(win,text="signin",bg="orange")
signin.grid(columnspan=2)

win.mainloop()
