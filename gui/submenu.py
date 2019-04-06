from tkinter import *

win = Tk()

win.geometry("600x400")
mymenu=Menu(win)


win.config(menu=mymenu)

sub_menu=Menu(mymenu)
sub_edit=Menu(mymenu)

mymenu.add_cascade(label="File",menu=sub_menu)
mymenu.add_cascade(label="Edit",menu=sub_edit)

sub_edit.add_command(label="open")
sub_edit.add_command(label="new")

sub_menu.add_command(label="open")
sub_menu.add_command(label="new")

win.mainloop()
