from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime("%H:%M:%S %p")
    # setting time to label
    label.config(text = string)
    # calling time function
    label.after(1000, time)

# storing clock
label = Label(root, font = ("ds-digital", 60), background = "black", foreground = "green yellow")
label.pack(anchor = "center")
time()

mainloop()