from dataclasses import dataclass
import pyxel as px
import math

@dataclass
class Circle:
    x:  float
    y:  float
    vx: float = 0.0
    vy: float = 0.0
    r:  int = 10
    c:  int = 6
    m:  float = 1.0
    
    def update(self):
        self.x = (self.x + self.vx * dt) % px.width
        self.y = (self.y + self.vy * dt) % px.height

    def draw(self):
        px.circ(self.x, self.y, self.r, self.c)

c1 = Circle(50, 50, vx=10, vy=8, r=15, m=1)
c2 = Circle(90, 90, vx=0,  vy=0, r=15, m=1, c=10)
dt = 0.2
circ_restitution = 0.8

def update():
    nx = c1.x - c2.x; ny = c1.y - c2.y # contact normal
    sr = c1.r + c2.r # sum of radius
    if nx*nx + ny*ny < sr*sr: # a collision happened
        # move particles apart
        dist = math.sqrt(nx*nx + ny*ny)
        c1.x += 0.5 * (sr - dist) * nx / dist
        c1.y += 0.5 * (sr - dist) * ny / dist
        c2.x -= 0.5 * (sr - dist) * nx / dist
        c2.y -= 0.5 * (sr - dist) * ny / dist
                
        # impulse response
        rx = c1.vx - c2.vx; ry = c1.vy - c2.vy # relative velocity
        impulse = - (1 + circ_restitution) * (rx*nx + ry*ny) / \
                  ((nx*nx + ny*ny) * (1/c1.m + 1/c2.m));

        # update velocities
        c1.vx += impulse * nx / c1.m
        c1.vy += impulse * ny / c1.m
        c2.vx -= impulse * nx / c2.m
        c2.vy -= impulse * ny / c2.m

    c1.update(); c2.update()
    print(c1.vx*c1.m + c2.vx*c2.m, c1.vy*c1.m + c2.vy*c2.m)

def draw():
    px.cls(0)
    c1.draw(); c2.draw()

px.init(100, 100)
px.run(update, draw)
