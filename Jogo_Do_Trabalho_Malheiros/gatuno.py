import pyxel as px

def update():
    if px.btnp(px.KEY_Q):
        px.quit()
def draw():
    px.blt(0, 0, 0, 0, 0, 250, 250)
px.init(250, 250, title='Happy cat')
px.image(0).load(0,0,'Mapinha1.png')
px.run(update, draw)