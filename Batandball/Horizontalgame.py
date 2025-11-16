import random, pgzrun, pygame
speedx=2
speedy=2
WIDTH=490
HEIGHT=600
#X and Y coordinates, Width and height numbers
#Squares and rectangles code is same just with different lengths
score=0
bat=Rect((0,300),(50,75))
ball=Rect((245,300),(35,35))
def draw():
#clear the screen
    screen.clear()
    screen.fill('dark green')
    screen.draw.filled_rect(bat,'white')
    screen.draw.filled_rect(ball,'yellow')
    screen.draw.text('Score:'+str(score),(50,50),color='white')
def update():
    global speedx, speedy,score
    ball.x += speedx
    ball.y += speedy
    if ball.right>WIDTH:
        speedx = -speedx
    if ball.left<0:
        speedx=-speedx
    if ball.colliderect(bat):
        speedx=-speedx
#speed of the ball, if the ball goes out of the screen it has to pull it back in
    if ball.top<0:
        speedy = -speedy
        score+=1
    if ball.bottom>HEIGHT:
        speedy=-speedy
#   if ball.bottom>HEIGHT:
#        exit()
#when the ball goes out of the screen, the game ends
    if keyboard.up:
        bat.y -= 3
    if keyboard.down:
        bat.y += 3
#the speed of the bat
pgzrun.go()