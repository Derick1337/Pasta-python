import pyxel as px

direita  = [0, 14, 28, 42]
esquerda = [0, 14, 28, 42]
subir = [0, 14, 28, 42]
descer = [0, 14, 28, 42]
quadro   = 0
estado   = 'direita'
x = 50
y = 50
def update():
    global estado, quadro, x , y
    if px.btn(px.KEY_RIGHT):
        estado = 'direita'
        x = x + 8
        quadro = (quadro + 1) % 4
    elif px.btn(px.KEY_LEFT):
        estado = 'esquerda'
        x = x - 8
        quadro = (quadro + 1) % 4
    elif px.btn(px.KEY_UP):
        estado = 'subir'
        quadro = (quadro + 1) % 4
        y = y - 8
    elif px.btn(px.KEY_DOWN):
        estado = 'descer'
        y = y + 8
        quadro = (quadro + 1) % 4
   
def draw():
    px.cls(3)
    if estado == 'direita':
        #  blt(x,  y, img,                u,  v,  w,  h, [colkey])
        px.blt(x, y,   0,  direita[quadro], 54, 14, 18,        7)
    if estado == 'subir':
        px.blt(x,y,0,subir[quadro],18,14,18,7)
    if estado == 'descer':
        px.blt(x,y,0,descer[quadro],0,14,18,7)
    elif estado == 'esquerda':
        px.blt(x, y,   0, esquerda[quadro], 36, 14, 18,        7)

px.init(600, 300, title='Pyxel', fps=15)
px.image(0).load(0, 0, 'personagem_56x72.png')
px.run(update, draw)