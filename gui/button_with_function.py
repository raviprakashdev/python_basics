from tkinter import *

win = Tk()

def func():
    print("Ravi Prakash")
my_label = Button(win,text="click me",command=func)

my_label.pack()

win.mainloop()
