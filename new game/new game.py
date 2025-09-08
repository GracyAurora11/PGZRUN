import pgzrun
import random
TITLE = 'bee game'
WIDTH=800
HEIGHT=650
mes=''
act1=Actor('bee.png')
sco=0
gov=False
def draw():
    screen.clear()
    screen.fill('blue')
    act1.draw()
    screen.draw.text(mes,(400,550),fontsize=30)
    screen.draw.text('The bee game',(300,50),fontsize=40)
    screen.draw.text('Score:'+str(sco),(400,30),fontsize=30)
    if gov:
        screen.fill('light blue')
        screen.draw.text('Game over!Score:'+str(sco),(260,300),fontsize=40)
def bee():
    act1.x=random.randint(50,750)
    act1.y=random.randint(50,600)
def gos():
    global gov
    gov=True
def on_mouse_down(pos):
    global mes,sco
    if act1.collidepoint(pos):
        sco+=1
        bee()
        mes='Good job!'
    else:
        mes='Good try!'
def update():
    pass
clock.schedule(gos,20)
pgzrun.go()