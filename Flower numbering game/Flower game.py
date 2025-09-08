import random, pgzrun
from time import time
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
    global sat
    for i in range(tnf):
        flo=Actor('flower.png')
        flo.pos=random.randint(50,650),random.randint(50,550)
        lof.append(flo)
    sat=time()
def draw():
    global sat,tot
    screen.blit('sunset field.jpg',(0,0))
    cof=1
    for i in lof:
        i.draw()
        screen.draw.text(str(cof),(i.x,i.y+10),color='blue')
        cof+=1
    for l in lin:
        screen.draw.line(l[0],l[1],color='white')
    #displaying timer
    if flc<tnf:
        tot=time()-sat
        tot=int(tot)
        #tot=round(tot,1)
        #screen.draw.text(f'{tot:.1f}',(25,25),color='blue',fontsize=50)
        screen.draw.text(str(tot),(25,25),color='blue',fontsize=50)
    else:
        screen.draw.text(str(tot),(25,25),color='blue',fontsize=50)
def update():
    pass
def on_mouse_down(pos):
    global flc,lin
    if flc<tnf:
        if lof[flc].collidepoint(pos):
            if flc:
                lin.append((lof[flc-1].pos,lof[flc].pos))
            flc+=1
        else:
            lin=[]
            flc=0

ctf()
pgzrun.go()
