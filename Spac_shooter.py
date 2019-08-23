import tkinter as tk
import random as rn

class Obj():

    def __init__(this, color):
        this.x = this.rng(X)
        this.y = this.rng(Y)
        this.color = color
        this.draw()

    def rng(this, limit):
        return rn.randint(1, limit - 1) * step

    def draw(this):
        canvas.create_rectangle((this.x, this.y),
                               (this.x+step, this.y + step),
                                fill = this.color)

class Player(Obj):

    def __init__(this, color = 'black'):
        this.x = X*step / 2 - step/2
        this.y = Y*step - step
        this.color = color
        super().draw()

class  Hostile(Obj):
    hazards = {-1}

    def __init__(this, color = 'red'):
        this.x = -1
        this.y = 1
        while (this.x) in Hostile.hazards:
            this.x = super().rng(X)
        Hostile.hazards.add(this.x)
        this.color = color
        super().draw()

def enemy_gen():
    for i in range(X):
        enemy = Hostile()

master = tk.Tk()
X = 12
Y = 11
step = 80
canvas = tk.Canvas(master, bg = 'white', height = Y*step, width = X*step)

player = Player()
enemy_gen()

canvas.pack()
master.mainloop()
