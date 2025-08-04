import pgzrun,random
WIDTH=800
HEIGHT=650
TITLE='Treasure hunting game'
pirate=Actor('pirate.png')
pirate.pos=400,325
chest=Actor('treasure chest.png')
def draw():
    screen.blit('beach.jpg',(0,0))
    pirate.draw()
    chest.draw()
def update():
    pass
    if keyboard.left:
        pirate.x=pirate.x-5
pgzrun.go()