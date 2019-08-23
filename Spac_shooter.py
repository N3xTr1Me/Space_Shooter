import tkinter as tk
import random as rn

master = tk.Tk()
X = 12
Y = 11
step = 80
canvas = tk.Canvas(master, bg = 'black', height = Y*step, width = X*step)
canvas.pack()
master.mainloop()
