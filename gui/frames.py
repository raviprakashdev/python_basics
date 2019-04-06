from tkinter import *

win = Tk()
win.geometry("600x400")
top=Frame(win)
topf.pack()

bottom=Frame(win)
bottom=pack(side=BOTTOM)

b1=Button(top,text="button1")
b2=Button(top,text="button2")
b3=Button(top,text="button3")
b4=Button(bottom,text="button4")

b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=RIGHT)

win.mainloop()
