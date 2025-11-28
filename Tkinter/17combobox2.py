from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Combobox Example")
def update_label(event):
    selected_value = combobox.get()
    label.config(text=f"Selected: {selected_value}")
selected_value = StringVar()
combobox = ttk.Combobox(root, textvariable=selected_value)
combobox['values'] = ("PEN", "PENCIL", "BOOK")
combobox.current(0)
combobox.pack()
combobox.bind("<<ComboboxSelected>>", update_label)
label = Label(root, text="")
label.pack()
root.mainloop()