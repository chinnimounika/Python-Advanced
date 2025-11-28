from tkinter import *
root=Tk()
lbx=Listbox(selectmode=MULTIPLE)
lbx.pack()
items=['pen','pencil','paper','earser','sharpner']
for i in items:
    lbx.insert(END,i)
mainloop()