from dataclasses import dataclass
import pyxel as px
import math

@dataclass
class Circle:
    x:  float
    y:  float
    vx: float = 0.0
    vy: float = 0.0
    m: float = 1.0
    r:  int = 10
    c: int = 6
    
    def update(self):
        self.x = (self.x + self.vx * dt) % px.width
        self.y = (self.y + self.vy * dt) % px.height

    def draw(self):
        px.circb(self.x, self.y, self.r, 6)

c1 = Circle(50, 50 , 10, 0)
c2 = Circle(90, 90, 0, 0, c=10)
dt = 0.2
circ_restitution = 0.8


def update():
    nx = c1.x - c2.x; ny = c1.y - c2.y
    sr = c1.r + c2.r
    if nx * nx + ny*ny < sr*sr:
        print("Colisão")
    c1.update()
    c2.update()

def draw():
    px.cls(0)
    c1.draw()
    c2.draw()

px.init(200, 200)
px.run(update, draw)
