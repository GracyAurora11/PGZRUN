import pgzrun,random
WIDTH=800
HEIGHT=650
TITLE='Treasure hunting game'
pirate=Actor('pirate.png')
pirate.pos=400,325
chest=Actor('treasure chest.png')
sco=0
goc=False
def draw():
    screen.blit('beach.jpg',(0,0))
    screen.draw.text('Treasure hunting game!',(300,50),fontsize=40)
    screen.draw.text('Score:{}'.format(sco),(200,50),fontsize=30)
    pirate.draw()
    chest.draw()
    if goc:
        screen.fill('black')
        screen.draw.text('GAME OVER! Score:{}'.format(sco),(200,325),fontsize=50)
def rch():
    chest.x=random.randint(0,800)
    chest.y=random.randint(0,650)
def gof():
    global goc
    goc=True
def update():
    global sco
    pass
    if keyboard.left:
        pirate.x=pirate.x-8
    if keyboard.right:
        pirate.x=pirate.x+8
    if keyboard.up:
        pirate.y=pirate.y-8
    if keyboard.down:
        pirate.y=pirate.y+8
    if pirate.colliderect(chest):
        rch()
        sco+=10
clock.schedule(gof,20.0)
pgzrun.go()
