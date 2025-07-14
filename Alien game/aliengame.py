import pgzrun
import random
TITLE = 'Alien Game'
WIDTH=800
HEIGHT=650
#creating alien actor
act1=Actor('alien.png')
def draw():
    act1.draw()
pgzrun.go()