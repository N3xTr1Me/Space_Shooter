import tkinter as tk
import random as rn
import time as tm

class Obj():

    def __init__(this, color):
        this.x = this.rng(X)
        this.y = this.rng(Y)
        this.color = color
        this.draw()

    def rng(this, limit):
        return rn.randint(1, limit - 1) * step

    def draw(this):
        this.body = canvas.create_image((this.x, this.y), image=player_image, anchor="nw")

class Player(Obj):
    hp = 4

    def __init__(this, color = 'black'):
        this.x = X*step / 2
        this.y = Y*step - step
        this.color = color
        super().draw()

    def comparePoz(this, ot_x, ot_y):
        return this.x == ot_x and this.y == ot_y

    def reDraw(this, x, y):
        old_x, old_y = this.x, this.y
        this.x = (this.x + x) % (step*X)
        this.y = (this.y + y) % (step*Y)
        canvas.move(this.body, (this.x - old_x), (this.y - old_y))
    
class  Hostile(Obj):
    hazards = {-1}
    enemies = []
    hp = 20

    def __init__(this, color = 'red'):
        this.x = -1
        this.y = 0
        while this.x in Hostile.hazards:
            this.x = super().rng(X)
        Hostile.hazards.add(this.x)
        this.color = color
        this.draw()

    def draw(this):
        this.body = canvas.create_rectangle((this.x, this.y),
                                        (this.x+step, this.y + step),
                                         fill = this.color)
        this.enemies.append(this)

    def move(enemy):
        x, y = coord_get(enemy.body)
        print(x,y)
        if y <= Y*step:
            canvas.move(enemy.body, 0, step)
        else:
            Hostile.enemies.remove(enemy)

class Meteor(Hostile):
    hp = 40
    def __init__(this):
        super().__init__('brown')

def enemy_gen(Q):
    for i in range(Q):
        #p=20
        
        #r=rn.randint(1,100)
        #if (r<p):
            #enemy = Meteor()
        #else:
        enemy = Hostile()
        threats.append(enemy)

def k_prss(event):
    keys = {'Up', 'w', 'Down', 's', 'Left', 'a', 'Right', 'd'}
    if event.keysym in keys:
        keyListener(event.keysym)

def keyListener(key):
    if key == 'Up' or key == 'w':
        player.reDraw(0, -(step))
        damage()
        gameOver()
    elif key == 'Down' or key == 's':
        player.reDraw(0, step)
        damage()
        gameOver()
    elif key == 'Left' or key == 'a':
        player.reDraw(-(step), 0)
        damage()
        gameOver()
    elif key == 'Right' or key == 'd':
        player.reDraw(step, 0)
        damage()
        gameOver()

def damage():
    for enemy in Hostile.enemies:
        x,y = coord_get(enemy.body)
        if player.comparePoz(x, y):
            player.hp -= 1
            break

def gameOver():
    if player.hp < 1:
        print('You lose')
        print('Game over')

def coord_get(obj_id):
    x, y = canvas.coords(obj_id)[:2]
    return x, y

def movement():
    for enemy in Hostile.enemies:
        enemy.move()
    
gui = tk.Tk()
X = 12
Y = 12
step = 80
res = f'{X*step}x{Y*step}'
gui.geometry(res)
sX, sY = 0,1
delay = 0
Q = 8
threats = []
canvas = tk.Canvas(gui, bg = 'black', height = Y*step, width = X*step)
player_image = tk.PhotoImage(file="images/player.png")
enemy_image = tk.PhotoImage(file="images/enemy.png")
meteor_image = tk.PhotoImage(file="images/meteor.png")

player = Player()
enemy_gen(Q)

canvas.pack()
gui.bind('<KeyPress>', k_prss)
while True:
    if delay >= 200:
        delay = 0
        movement()
        enemy_gen(Q)
        gui.update()
    else:
        delay += 1
        tm.sleep(0.05)
        gui.update()








