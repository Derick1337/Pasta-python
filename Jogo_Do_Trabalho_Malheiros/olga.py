import pyxel as px
x = 50
y = 50
pose =0
parede = 6
def update():
    global x,y
    if px.btn(px.KEY_RIGHT):
        if px.pget(x+7,y) != parede:
            x = x + 1
    if px.btn(px.KEY_LEFT):
        if px.pget(x-1,y) != parede:
            x = x - 1
    if px.btn(px.KEY_UP):
        if px.pget(x,y-1) != parede:
            y = y - 1
    if px.btn(px.KEY_DOWN):
        if px.pget(x,y+8) != parede:
            y = y + 1
def draw():
    global pose
    px.cls(11)
    px.rect(99,-9,10,1000,parede)
    px.rect(-9,-9,10,1000,parede)
    px.rect(-9,-9,1000,10,parede)
    px.rect(-9,99,1000,10,parede) 
    if int(pose)==0:
        # blt( x , y , img , u . v , w , h)
        px.blt(x,y,0,64,16,8,8,0)
    else:
        px.blt(x,y,0,72,16,8,8,0)
    pose = pose + 0.1
    if pose > 2:
        pose = 0
    px.text(0,0,'x='+str(x),7)
    px.text(18,0,'y='+str(y),7)
px.init(100,100)
px.image(0).load(0,0,'noguchi_128x128.png')
px.run(update,draw)