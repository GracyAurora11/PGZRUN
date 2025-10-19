import random, pgzrun, pygame
speedx=1
speedy=1
WIDTH=500
HEIGHT=490
#X and Y coordinates, Width and height numbers
#Squares and rectangles code is same just with different lengths

bat=Rect((150,475),(75,50))
ball=Rect((235,240),(35,35))
def draw():
#clear the screen
    screen.clear()
    screen.fill('dark green')
    screen.draw.filled_rect(bat,'white')
    screen.draw.filled_rect(ball,'yellow')

def update():
    global speedx, speedy
    ball.x += speedx
    ball.y += speedy
    if ball.right>WIDTH or ball.left<0:
        speedx = -speedx
    if ball.top<0 or ball.colliderect(bat):
        speedy = -speedy
    if keyboard.right:
        bat.x += 2
    if keyboard.left:
        bat.x -= 2

pgzrun.go()