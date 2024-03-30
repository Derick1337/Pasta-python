import pyxel as px
import constants as const

class Game:
    def __init__(self):
        px.init(const.screen_x,const.screen_y , title="Sprite Example",fps = 30)
        px.image(0).load(0, 0, "Personagem.png")  # carrega a imagem das poses do personagem
        px.image(1).load(0, 0, "mapa.png") # carrega a imagem do mapa do jogo
        self.character_x = const.character_initial_x
        self.character_y = const.character_initial_y
        self.right  = [0, 14, 28, 42]
        self.left = [0, 14, 28, 42]
        self.up = [0, 14, 28, 42]
        self.down = [0, 14, 28, 42]
        self.animation_frame = 0
        self.direction = 'down'
        px.run(self.update, self.draw)

    def update(self):
        if px.btn(px.KEY_DOWN):
            self.character_y += 1
            self.direction = 'down'
            self.animation_frame = (self.animation_frame + 1) % 4
        if px.btn(px.KEY_UP):
            self.character_y -= 1
            self.direction = 'up'
            self.animation_frame = (self.animation_frame + 1) % 4
        if px.btn(px.KEY_LEFT):
            self.character_x -= 1
            self.direction = 'left'
            self.animation_frame = (self.animation_frame + 1) % 4
        if px.btn(px.KEY_RIGHT):
            self.character_x += 1
            self.direction = 'right'
            self.animation_frame = (self.animation_frame + 1) % 4
              

    def draw(self):  
        px.cls(0)
        px.blt(0, 0, 1, 0, 0, const.map_width, const.map_height, 7)
        if self.direction == 'down':
            px.blt(self.character_x, self.character_y, 0, self.down[self.animation_frame], 0, 14, 18, 0)
        elif self.direction == 'up':
            px.blt(self.character_x, self.character_y, 0, self.up[self.animation_frame], 18, 14, 18, 0)
        elif self.direction == 'left':
            px.blt(self.character_x, self.character_y, 0, self.left[self.animation_frame], 36, 14, 18, 0)
        elif self.direction == 'right':
            px.blt(self.character_x, self.character_y, 0, self.right[self.animation_frame], 54, 14, 18, 0)
        
        

Game()

        