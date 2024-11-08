import pyxel as px
x=500
y=500
r=250
def update():
    global x,y
    x=x+1
    y=y+1
    if x > 1000+r:
        x = -r
    if y >1000+r:
        y=-r
def draw():
    '''px.cls(0)'''
    px.circ(x,y,r,px.frame_count % 16)
px.init(1000,1000)
px.run(update,draw)
