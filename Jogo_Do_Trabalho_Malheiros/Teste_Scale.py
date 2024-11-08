import pyxel as px

direita  = [14,76, 144, 207]
esquerda = [15, 74, 145, 214]
subir = [16, 82, 146, 212]
descer = [18, 84, 148, 212]
quadro   = 0
estado   = 'direita'
x = 50
y = 50
def update():
    teclas=['KEY_RIGTH','KEY_LEFT','KEY_UP','KEY_DOWN']
    global estado, quadro, x , y
    if px.btn(px.KEY_RIGHT):
        estado = 'direita'
        x = x + 10
        quadro = (quadro + 1) % 4
    elif px.btn(px.KEY_LEFT):
        estado = 'esquerda'
        x = x - 10
        quadro = (quadro + 1) % 4
    elif px.btn(px.KEY_UP):
        estado = 'subir'
        quadro = (quadro + 1) % 4
        y = y - 10
    elif px.btn(px.KEY_DOWN):
        estado = 'descer'
        y = y + 10
        quadro = (quadro + 1) % 4
   
def draw():
    px.cls(0)
    if estado == 'direita':
        #  blt(x,  y, img,                u,  v,  w,  h, [colkey])
        px.blt(x, y,   0,  direita[quadro], 66, 46, 54,        0)
    if estado == 'subir':
        px.blt(x,y,0,subir[quadro],140,46,54,0)
    if estado == 'descer':
        px.blt(x,y,0,descer[quadro],0,46,54,0)
    elif estado == 'esquerda':
        px.blt(x, y,   0, esquerda[quadro], 197, 46, 54,0)

px.init(600, 300, title='Pyxel', fps=15)
px.image(0).load(0, 0, 'redgoblinsword.png')
px.run(update, draw)