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
        this.body = canvas.create_rectangle((this.x, this.y),
                                            (this.x+step, this.y + step),
                                             fill = this.color)

class Player(Obj):

    def __init__(this, color = 'black'):
        this.x = X*step / 2 - step/2
        this.y = Y*step - step
        this.color = color
        super().draw()

    def reDraw(this, x, y):
        old_x, old_y = this.x, this.y
        this.x = (this.x + x) % (step*X)
        this.y = (this.y + y) % (step*Y)
        canvas.move(this.body, (this.x - old_x), (this.y - old_y))
    
class  Hostile(Obj):
    hazards = {-1}

    def __init__(this, color = 'red'):
        this.x = -1
        this.y = 1
        while this.x in Hostile.hazards:
            this.x = super().rng(X)
        Hostile.hazards.add(this.x)
        this.color = color
        super().draw()

class Meteor(Hostile):
    def __init__(this):
        super().__init__('brown')

def enemy_gen():
    for i in range(X-2):
        p=20
        r=rn.randint(1,100)
        if (r<p):
            enemy = Meteor()
        else:
            enemy = Hostile()

def k_prss(event):
    keys = {'Up', 'w', 'Down', 's', 'Left', 'a', 'Right', 'd'}
    if event.keysym in keys:
        keyListener(event.keysym)

def keyListener(key):
    if key == 'Up' or key == 'w':
        player.reDraw(0, -(step))
    elif key == 'Down' or key == 's':
        player.reDraw(0, step)
    elif key == 'Left' or key == 'a':
        player.reDraw(-(step), 0)
    elif key == 'Right' or key == 'd':
        player.reDraw(step, 0)
    
master = tk.Tk()
X = 12
Y = 11
step = 80
canvas = tk.Canvas(master, bg = 'white', height = Y*step, width = X*step)

player = Player()
enemy_gen()

canvas.pack()
master.bind('<KeyPress>', k_prss)
master.mainloop()
