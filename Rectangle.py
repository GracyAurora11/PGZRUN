import pgzrun,random
WIDTH=800
HEIGHT=650
#main function
def draw():
    r=255
    g=0
    b=random.randint(0,255)
    hei=HEIGHT
    wid=WIDTH - 280
    for i in range(40):

        rec=Rect((0,0),(wid,hei))
        rec.center=(400,325)
        screen.draw.rect(rec,(r,g,b))
        hei -=10
        wid +=10
        g+=5
        r-=5
def update():
    pass
pgzrun.go()
