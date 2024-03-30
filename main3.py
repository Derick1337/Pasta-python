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
        if px.btn(px.KEY_S):
            self.y += 1
            self.direction = 'down'
            self.animation_frame = (self.animation_frame + 1) % 4
        elif px.btn(px.KEY_W):
            self.y -= 1
            self.direction = 'up'
            self.animation_frame = (self.animation_frame + 1) % 4
        elif px.btn(px.KEY_A):
            self.x -= 1
            self.direction = 'left'
            self.animation_frame = (self.animation_frame + 1) % 4
        elif px.btn(px.KEY_D):
            self.x += 1
            self.direction = 'right'
            self.animation_frame = (self.animation_frame + 1) % 4

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

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self):
        pass

class LaunchScreen:
    def __init__(self):
        px.init(const.screen_y, const.screen_y, title="Chronicles of the Hero", fps=30)
        px.image(0).load(0, 0, "Tela_inicio.png")  
        self.show_launch_screen = True
        px.run(self.update, self.draw)

    def update(self):
        if px.btnp(px.KEY_SPACE):
            self.show_launch_screen = False

    def draw(self):
        px.cls(0)
        if self.show_launch_screen:
            px.blt(0, 0, 0, 0, 0, const.screen_x, const.screen_y, 0)
            
        else:
            self.start_game()

    def start_game(self):
        game = Game()
        px.run(game.update, game.draw)
    

class Game:
    def __init__(self):
        px.image(0).load(0, 0, "personagem.png")  
        px.image(1).load(0, 0, "Mapinha1.png")  
        px.image(2).load(0, 0, "Mapinha4.png")
        self.map_positions = [
            (0, 0),  
            (250, 0),  
            (0, 250),  
            (250, 250)
        ]
        self.character_x = const.character_initial_x
        self.character_y = const.character_initial_y
        self.right = [0, 14, 28, 42]
        self.left = [0, 14, 28, 42]
        self.up = [0, 14, 28, 42]
        self.down = [0, 14, 28, 42]
        self.animation_frame = 0
        self.direction = 'down'
    
    def draw(self):
        px.cls(0)

        # Desenhe os mapas
        for i, (map_x, map_y) in enumerate(self.map_positions):
            px.blt(map_x, map_y, i + 1, 0, 0, 250, 250, 0)

        px.camera(self.character_x - 50, self.character_y - 50)

    def update(self):
        new_x = self.character_x
        new_y = self.character_y
        if px.btn(px.KEY_S):
            new_y += 1
            self.direction = 'down'
            self.animation_frame = (self.animation_frame + 1) % 4
        if px.btn(px.KEY_W):
            new_y -= 1
            self.direction = 'up'
            self.animation_frame = (self.animation_frame + 1) % 4
        if px.btn(px.KEY_A):
            new_x -= 1
            self.direction = 'left'
            self.animation_frame = (self.animation_frame + 1) % 4
        if px.btn(px.KEY_D):
            new_x += 1
            self.direction = 'right'
            self.animation_frame = (self.animation_frame + 1) % 4

        if (not self.is_collision1(new_x, new_y) 
            and not self.is_collision2(new_x, new_y) 
            and not self.is_collision3(new_x, new_y) 
            and not self.is_collision4(new_x, new_y) 
            and not self.is_collision5(new_x, new_y)
            and not self.is_collision6(new_x, new_y)
            and not self.is_collision7(new_x, new_y)
            and not self.is_collision8(new_x, new_y)
            and not self.is_collision9(new_x, new_y)
            and not self.is_collision10(new_x, new_y)
            and not self.is_collision11(new_x, new_y)
            and not self.is_collision12(new_x, new_y)
            and not self.is_collision13(new_x, new_y)):
            self.character_x = new_x
            self.character_y = new_y

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

        rect_left = 0
        rect_right = 8
        rect_top = 0
        rect_bottom = 250

        if (character_left < rect_right and
            character_right > rect_left and
            character_top < rect_bottom and
            character_bottom > rect_top):
            return True
        return False
    def is_collision11(self, other_x, other_y):
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
            self.show_launch_screen = True
            self.start_game = False
            return True
        return False
    def is_collision12(self, other_x, other_y):
        character_left = other_x
        character_right = other_x + const.character_width
        character_top = other_y
        character_bottom = other_y + const.character_height

        rect_left = 0
        rect_right = 250
        rect_top = 238
        rect_bottom = 250

        if (character_left < rect_right and
            character_right > rect_left and
            character_top < rect_bottom and
            character_bottom > rect_top):

            return True
        return False
    def is_collision13(self, other_x, other_y):
        character_left = other_x
        character_right = other_x + const.character_width
        character_top = other_y
        character_bottom = other_y + const.character_height

        rect_left = 0
        rect_right = 250
        rect_top = 0
        rect_bottom = 10

        if (character_left < rect_right and
            character_right > rect_left and
            character_top < rect_bottom and
            character_bottom > rect_top):

            return True
        return False

    def draw(self):
        px.cls(0)
        
        px.blt(0, 0, 1, 0, 0, 250, 250, 0)
        px.blt(0, -250, 2, 0, 0, 250, 250, 0)
        px.camera(self.character_x-50, self.character_y-50)
        
        

        if self.direction == 'down':
            px.blt(self.character_x, self.character_y, 0,
                   self.down[self.animation_frame], 0, 14, 18, 0)
        elif self.direction == 'up':
            px.blt(self.character_x, self.character_y, 0,
                   self.up[self.animation_frame], 18, 14, 18, 0)
        elif self.direction == 'left':
            px.blt(self.character_x, self.character_y, 0,
                   self.left[self.animation_frame], 36, 14, 18, 0)
        elif self.direction == 'right':
            px.blt(self.character_x, self.character_y, 0,
                   self.right[self.animation_frame], 54, 14, 18, 0)

if __name__ == "__main__":
    launch_screen = LaunchScreen()
