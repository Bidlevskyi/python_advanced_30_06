import tkinter as tk
from tkinter import *
import math



root = tk.Tk()
root.title("Calculator")
bttn_list = [
    "7", "8", "9", "+", "*",
    "4", "5", "6", "-", "/",
    "1", "2", "3",  "=",
    "0", ".", "C", "(", ")",
]

def calc(key):
    global memory
    if key == "=":
        str1 = "-+0123456789.*/)("
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol is not number!")
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
    elif key == "C":
        calc_entry.delete(0, END)
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

r= 1
c = 0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    tk.Button(root, text=i, command=cmd, width=10).grid(row=r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width = 33)
calc_entry.grid(row=0, column=0, columnspan=5)
root.mainloop()

