from tkinter import *
from tkinter.ttk import *

from time import strftime
from tkinter import font
#helv36 = tkFont.Font(family="Helvetica",size=36,weight="bold")
my_font = font.NORMAL


root = Tk()
root.title("Clock")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=(my_font, 80), background="Black", foreground="white")
label.pack(anchor="center")
time()
mainloop()