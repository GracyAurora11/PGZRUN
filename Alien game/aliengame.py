import pgzrun
import random
TITLE = 'Alien Game'
WIDTH=800
HEIGHT=650
mes=''
#creating alien actor
act1=Actor('alien.png')
sco=0
def draw():
    screen.clear()
    screen.fill('blue')
    act1.draw()
    screen.draw.text(mes,(400,550),fontsize=30)
    screen.draw.text('The alien game',(300,50),fontsize=40)
    screen.draw.text('Score:'+str(sco),(400,30),fontsize=30)
def alien():
    act1.x=random.randint(50,750)
    act1.y=random.randint(50,600)
def on_mouse_down(pos):
    global mes,sco
    if act1.collidepoint(pos):
        sco+=1
        alien()
        mes='Good job!'
    else:
        mes='Good try!'
def update():
    pass
pgzrun.go()
