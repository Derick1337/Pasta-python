import pyxel as px
import constants as const

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.right = [0, 14, 28, 42]
        self.left = [0, 14, 28, 42]
        self.up = [0, 14, 28, 42]
        self.down = [0, 14, 28, 42]
        self.animation_frame = 0
        self.direction = 'down'

    def update(self):
        new_x = self.x
        new_y = self.y

        if px.btn(px.KEY_S):
            new_y += 2
            self.direction = 'down'
            self.animation_frame = (self.animation_frame + 1) % 4
        if px.btn(px.KEY_W):
            new_y -= 2
            self.direction = 'up'
            self.animation_frame = (self.animation_frame + 1) % 4
        if px.btn(px.KEY_A):
            new_x -= 2
            self.direction = 'left'
            self.animation_frame = (self.animation_frame + 1) % 4
        if px.btn(px.KEY_D):
            new_x += 2
            self.direction = 'right'
            self.animation_frame = (self.animation_frame + 1) % 4

        if new_x > const.screen_x - 21:
            new_x = const.screen_x - 21
        if new_x < 8:
            new_x = 8
        if new_y > const.screen_y - 35:
            new_y = const.screen_y - 35
        if new_y < 10:
            new_y = 10

        self.x = new_x
        self.y = new_y

    def draw(self):
        if self.direction == 'down':
            px.blt(self.x, self.y, 0,
                   self.down[self.animation_frame], 0, 14, 18, 0)
        elif self.direction == 'up':
            px.blt(self.x, self.y, 0,
                   self.up[self.animation_frame], 18, 14, 18, 0)
        elif self.direction == 'left':
            px.blt(self.x, self.y, 0,
                   self.left[self.animation_frame], 36, 14, 18, 0)
        elif self.direction == 'right':
            px.blt(self.x, self.y, 0,
                   self.right[self.animation_frame], 54, 14, 18, 0)

class LaunchScreen:
    def __init__(self):
        px.init(const.screen_y, const.screen_y, title="Tela Inicial", fps=30)
        px.image(0).load(0, 0, "placeholder-250x250-1.png")  
        self.show_launch_screen = True
        px.run(self.update, self.draw)
    def update(self):
        if px.btnp(px.KEY_SPACE):
            self.show_launch_screen = False
            self.start_game = True  
    
    def draw(self):
        px.cls(0)
        if self.show_launch_screen:
            px.blt(0, 0, 0, 0, 0, const.screen_x, const.screen_y, 0)
        elif self.start_game:
            game = Game()
            px.run(game.update, game.draw)



class Game:
    def __init__(self):
        px.image(0).load(0, 0, "personagem.png")  # personagem principal
        px.image(1).load(0, 0, "Mapinha1.png")  # fase 1
        px.image(2).load(0, 0, "Mapinha2.png")  # fase 2
        px.image(3).load(0, 0, "Mapinha3.png")  # fase 3
        px.image(4).load(0, 0, "Mapinha4.png")  # fase 4

        self.character = Character(const.character_initial_x, const.character_initial_y)

    def is_collision1(self, other_x, other_y):
        character_left = other_x
        character_right = other_x + const.character_width
        character_top = other_y
        character_bottom = other_y + const.character_height
        rect_left = 68
        rect_right = 77
        rect_top = 78
        rect_bottom = 90

        if (character_left < rect_right and
            character_right > rect_left and
            character_top < rect_bottom and
            character_bottom > rect_top):
            return True
        return False
    
    def is_collision2(self, other_x, other_y):
        character_left = other_x
        character_right = other_x + const.character_width
        character_top = other_y
        character_bottom = other_y + const.character_height
        rect_left = 85
        rect_right = 142
        rect_top = 84
        rect_bottom = 92

        if (character_left < rect_right and
            character_right > rect_left and
            character_top < rect_bottom and
            character_bottom > rect_top):
            return True
        return False
    
    def is_collision3(self, other_x, other_y):
        character_left = other_x
        character_right = other_x + const.character_width
        character_top = other_y
        character_bottom = other_y + const.character_height
        rect_left = 148
        rect_right = 159
        rect_top = 80
        rect_bottom = 92

        if (character_left < rect_right and
            character_right > rect_left and
            character_top < rect_bottom and
            character_bottom > rect_top):
            return True
        return False
    def is_collision4(self, other_x, other_y):
        character_left = other_x
        character_right = other_x + const.character_width
        character_top = other_y
        character_bottom = other_y + const.character_height
        rect_left = 75
        rect_right = 75
        rect_top = 105
        rect_bottom = 110

        if (character_left < rect_right and
            character_right > rect_left and
            character_top < rect_bottom and
            character_bottom > rect_top):
            return True
        return False
    
    def is_collision5(self, other_x, other_y):
        character_left = other_x
        character_right = other_x + const.character_width
        character_top = other_y
        character_bottom = other_y + const.character_height
        rect_left = 155
        rect_right = 155
        rect_top = 107
        rect_bottom = 115

        if (character_left < rect_right and
            character_right > rect_left and
            character_top < rect_bottom and
            character_bottom > rect_top):
            return True
        return False
    def is_collision6(self, other_x, other_y):
        character_left = other_x
        character_right = other_x + const.character_width
        character_top = other_y
        character_bottom = other_y + const.character_height
        rect_left = 67
        rect_right = 75
        rect_top = 145
        rect_bottom = 160

        if (character_left < rect_right and
            character_right > rect_left and
            character_top < rect_bottom and
            character_bottom > rect_top):
            return True
        return False
    def is_collision7(self, other_x, other_y):
        character_left = other_x
        character_right = other_x + const.character_width
        character_top = other_y
        character_bottom = other_y + const.character_height
        rect_left = 66
        rect_right = 115
        rect_top = 153
        rect_bottom = 160

        if (character_left < rect_right and
            character_right > rect_left and
            character_top < rect_bottom and
            character_bottom > rect_top):
            return True
        return False
    def is_collision8(self, other_x, other_y):
        character_left = other_x
        character_right = other_x + const.character_width
        character_top = other_y
        character_bottom = other_y + const.character_height
        rect_left = 120
        rect_right = 140
        rect_top = 160
        rect_bottom = 160

        if (character_left < rect_right and
            character_right > rect_left and
            character_top < rect_bottom and
            character_bottom > rect_top):
            return True
        return False
    def is_collision9(self, other_x, other_y):
        character_left = other_x
        character_right = other_x + const.character_width
        character_top = other_y
        character_bottom = other_y + const.character_height
        rect_left = 135
        rect_right = 147
        rect_top = 153
        rect_bottom = 150

        if (character_left < rect_right and
            character_right > rect_left and
            character_top < rect_bottom and
            character_bottom > rect_top):
            return True
        return False
    def is_collision10(self, other_x, other_y):
        character_left = other_x
        character_right = other_x + const.character_width
        character_top = other_y
        character_bottom = other_y + const.character_height

        rect_left = 150
        rect_right = 158
        rect_top = 145
        rect_bottom = 160

        if (character_left < rect_right and
            character_right > rect_left and
            character_top < rect_bottom and
            character_bottom > rect_top):
            return True
        return False

    def draw(self):
        px.cls(0)
        # Desenhe o mapa ou background aqui
        px.blt(0, 0, 1, 0, 0, 250, 250, 0)
        px.blt(250, 0, 2, 0, 0, 250, 250, 0)
        px.blt(250, 250, 3, 0, 0, 250, 250, 0)
        px.blt(0, 250, 4, 0, 0, 250, 250, 0)

if __name__ == "__main__":
    launch_screen = LaunchScreen()
    game = Game()
    px.run(game.update, game.draw)
