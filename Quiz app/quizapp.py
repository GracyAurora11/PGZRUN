import pgzrun
WIDTH=800
HEIGHT=650
#rectangle objects
movingbox=Rect(0,0,800,100)
qbox=Rect(20,120,600,150)
opt1box=Rect(20,300,260,140)
opt2box=Rect(300,300,260,140)
opt3box=Rect(20,480,260,140)
opt4box=Rect(300,480,260,140)
timebox=Rect(640,120,145,150)
skipbox=Rect(640,300,145,315)
def draw():
    screen.fill('light blue')
    screen.draw.filled_rect(movingbox,('light pink'))
    screen.draw.filled_rect(qbox,('light pink'))
    screen.draw.filled_rect(opt1box,('palevioletred'))
    screen.draw.filled_rect(opt2box,('palevioletred'))
    screen.draw.filled_rect(opt3box,('palevioletred'))
    screen.draw.filled_rect(opt4box,('palevioletred'))
    screen.draw.filled_rect(timebox,('cornflowerblue'))
    screen.draw.filled_rect(skipbox,('cornflowerblue'))
    #textboxes
    screen.draw.textbox('SKIP',skipbox,color='powderblue',angle=-90)
def update():
    pass
pgzrun.go()
