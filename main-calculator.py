from funcs import *
from matplotlib.pyplot import *
from numpy import *
from sympy.solvers import solve
from sympy import Symbol
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()
w = tk.Label(root, text="Hello Tkinter!")
canvas1.create_window(200, 100, window=w)
entry1 = tk.Entry (root)
canvas1.create_window(200, 140, window=entry1)

def getCalc():
    x1 = entry1.get()
    if x1 == "1":
        graph()
    elif x1 == "2":
        basicTingz()

button1 = tk.Button(text='Execute', command=getCalc)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
