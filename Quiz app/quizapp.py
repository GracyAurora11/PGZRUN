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
#gaming variables
sco=0
tcs=10
qfn='textfile.txt'
gao=False
list1=[]
index=0
qec=0
opt=[opt1box,opt2box,opt3box,opt4box]
def draw():
    screen.fill('light blue')
    screen.draw.filled_rect(movingbox,('lightblue'))
    screen.draw.filled_rect(qbox,('light pink'))
    screen.draw.filled_rect(opt1box,('palevioletred'))
    screen.draw.filled_rect(opt2box,('palevioletred'))
    screen.draw.filled_rect(opt3box,('palevioletred'))
    screen.draw.filled_rect(opt4box,('palevioletred'))
    screen.draw.filled_rect(timebox,('cornflowerblue'))
    screen.draw.filled_rect(skipbox,('cornflowerblue'))
    #textboxes
    screen.draw.textbox('SKIP',skipbox,color='powderblue',angle=-90)
    screen.draw.textbox(str(tcs),timebox,color='powderblue')
    mes='Welcome to the quiz app game!'
    screen.draw.textbox(mes,movingbox,color='mediumaquamarine')
    screen.draw.textbox(question[0].strip(),qbox,color='mediumaquamarine')
    fin=1
    for i in opt:
        screen.draw.textbox(question[fin].strip(),i,color='mediumaquamarine')
        fin+=1
def update():
    pass
    mov()
#updating timer
def timer():
    global tcs
    if tcs>0:
        tcs-=1
#moving the marquee box
def mov():
    movingbox.x-=5
    if movingbox.right<0:
        movingbox.left=800
#reading the file
def rtf():
    global qec,index,list1
    otv=open(qfn,'r')
    for question in otv:
        list1.append(question)
        qec+=1
    otv.close()
#extracting only questions
def eoq():
    global index
    index+=1
    return list1.pop(0).split(',')
def on_mouse_down(pos):

rtf()
question=eoq()
clock.schedule_interval(timer,1)
pgzrun.go()
