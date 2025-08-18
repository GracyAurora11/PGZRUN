import pgzrun,random
WIDTH=1150
HEIGHT=639
TITLE='Tig playground game!'
boy=Actor(r'C:\Users\rosel\OneDrive\Desktop\VS Code\PGZRUN\Tig playground game\images\boy.png')
boy.pos=400,325
girl=Actor(r'C:\Users\rosel\OneDrive\Desktop\VS Code\PGZRUN\Tig playground game\images\girl.png')
sco=0
goc=False
def draw():
    screen.blit(r'C:\Users\rosel\OneDrive\Desktop\VS Code\PGZRUN\Tig playground game\images\playground.jpg',(0,0))
    screen.draw.text('Tig playground game!',(300,50),fontsize=40,color=('red'))
    screen.draw.text('Score:{}'.format(sco),(200,50),fontsize=30,color=('red'))
    boy.draw()
    girl.draw()
    if goc:
        screen.fill('black')
        screen.draw.text('GAME OVER! Score:{}'.format(sco),(350,350),fontsize=50)
def rch():
    girl.x=random.randint(50,1100)
    girl.y=random.randint(50,550)
def gof():
    global goc
    goc=True
def update():
    global sco
    pass
    if keyboard.left:
        boy.x=boy.x-8
    if keyboard.right:
        boy.x=boy.x+8
    if keyboard.up:
        boy.y=boy.y-8
    if keyboard.down:
        boy.y=boy.y+8
    if boy.colliderect(girl):
        rch()
        sco+=10
clock.schedule(gof,20.0)
pgzrun.go()