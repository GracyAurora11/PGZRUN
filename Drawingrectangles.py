import pgzrun, random
WIDTH=1000
HEIGHT=600
def draw():
    r=255
    g=0
    b=random.randint(0,255)
    hei=HEIGHT
    wid=WIDTH - 280
    for i in range(30):
        rec=Rect((0,0),(wid,hei))
        rec.center=(500,300)
        screen.draw.rect(rec,(r,g,b))
        hei-=5
        wid+=10
        r-=7
        g+=8
def update():
    pass
pgzrun.go()