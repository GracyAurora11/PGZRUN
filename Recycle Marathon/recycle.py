import pgzrun,random
WIDTH=800
HEIGHT=800
plastic=['battery.png','chipbag.png','plasticbag.png','waterbottle.png']
finallevel=6
currentlevel=1
startspeed=8
items=[]
animations=[]
gameover=False
gamecomplete=False

def draw():
    global items
    screen.clear()
    screen.blit('background.png',(0,0))
#update function is to check if there are no items in the list then it will create items automatically
    for i in items:
        i.draw()

def update():
    global items
    if len(items)==0:
        items=makeitems(currentlevel)

def makeitems(noofextraitems):
    itemstocreate=getoptionstocreate(noofextraitems)
    newitems=createitems(itemstocreate)
    layoutitems(newitems)
    animateitems(newitems)
    return newitems

#getoptionstocreate makes sure the program will always select atleast one random object and the paperbag
def getoptionstocreate(noofextraitems):
    itemstocreate=['paperbag.png']
    for i in range(0,noofextraitems):
        randomoption=random.choice(plastic)
        itemstocreate.append(randomoption)
    return itemstocreate

#layoutitems help fix the layout of the item based of off what level we are on and the gaps between the items are the same distance
def layoutitems(itemstolayout):
    noofgaps=len(itemstolayout)+1
    gapsize=WIDTH/noofgaps
    random.shuffle(itemstolayout)
    for i,j in enumerate(itemstolayout):
        new_x=(i+1)*gapsize
        j.x=new_x

#createitems adds the objects to the game from the first level and as you prgress it helps add more and more objects to the game
def createitems(itemstocreate):
    newitems=[]
    for i in itemstocreate:
        object=Actor(i)
        newitems.append(object)
    return newitems

#responsible for making the items fall down onto the screen 
def animateitems(itemstoanimate):
    global animations
    for i in itemstoanimate:
        duration=startspeed-currentlevel
        i.anchor=('center','bottom')
        animation=animate(i,duration=duration,y=HEIGHT,on_finished=handlegameover)
        animations.append(animation)

#changing the state of the game from playing the game and to it being over
def handlegameover():
    global gameover
    gamover=True
pgzrun.go()