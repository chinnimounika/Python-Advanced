from tkinter import *
root=Tk()
OurMessage='This is Our Message'
messagevar=Message(root,text=OurMessage)
messagevar.config(bg="lightgreen")
messagevar.pack()
root.mainloop()