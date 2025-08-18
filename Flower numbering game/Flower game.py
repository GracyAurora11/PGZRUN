import random, pgzrun, time
WIDTH=700
HEIGHT=600
#game variables
sat=0
tot=0
lof=[]
lin=[]
flc=0
tnf=8
#function for creating flowers
def ctf():
    for i in range(tnf):
        flo=Actor('flower.png')
        flo.pos=random.randint(50,650),random.randint(50,550)
        lof.append(flo)
    sat=time.time()
def draw():
    screen.blit('sunset field.jpg',(0,0))
    cof=1
    for i in lof:
        i.draw()
        screen.draw.text(str(cof),(i.x,i.y+10),color='dark green')
def update():
    pass
ctf()
pgzrun.go()
