from tkinter import *

win = Tk()

win.geometry("600x400")
mymenu=Menu(win)

win.config(menu=mymenu)

mymenu.add_cascade(label="File")
mymenu.add_cascade(label="Edit")

win.mainloop()
