import pgzrun
import random
TITLE = 'Alien Game'
WIDTH=800
HEIGHT=650
mes=''
#creating alien actor
act1=Actor('alien.png')
def draw():
    screen.clear()
    screen.fill('blue')
    act1.draw()
    screen.draw.text(mes,(400,550),fontsize=30)
    screen.draw.text('The alien game',(300,50),fontsize=40)
def alien():
    act1.x=random.randint(50,750)
    act1.y=random.randint(50,600)
def on_mouse_down(pos):
    global mes
    if act1.collidepoint(pos):
        alien()
        mes='Good job!'
    else:
        mes='Good try!'
def update():
    pass
pgzrun.go()
