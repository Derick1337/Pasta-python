from dataclasses import dataclass as component
import pyxel as px
import esper
import math

# ------------------------ COMPONENTS -----------------------

@component
class Circle:
    x:  float
    y:  float
    r:  int = 10
    m:  float = 1.0

@component
class Velocity:
    vx: float = 0.0
    vy: float = 0.0

@component
class Color:
    c:  int = 6

# ------------------------ PROCESSORS -----------------------

class MovementProcessor(esper.Processor):
    def process(self):
        for entity, (circle, velocity) in esper.get_components(Circle, Velocity):
            circle.x += velocity.vx * dt
            circle.y += velocity.vy * dt

class AppearanceProcessor(esper.Processor):
    def process(self):
        for entity, (circle, color) in esper.get_components(Circle, Color):
            px.circ(circle.x, circle.y, circle.r, color.c)

class WallProcessor(esper.Processor):
    def process(self):
        for entity, (circle, velocity) in esper.get_components(Circle, Velocity):
            if circle.x < circle.r: # left wall
                circle.x = circle.r
                velocity.vx *= - wall_restitution
                velocity.vy *=   wall_restitution
            elif circle.x > px.width - circle.r: # right wall
                circle.x = px.width - circle.r
                velocity.vx *= - wall_restitution
                velocity.vy *=   wall_restitution        
            if circle.y < circle.r: # ceiling
                circle.y = circle.r
                velocity.vx *=   wall_restitution
                velocity.vy *= - wall_restitution        
            elif circle.y > px.height - circle.r: # floor
                circle.y = px.height - circle.r
                velocity.vx *=   wall_restitution
                velocity.vy *= - wall_restitution

def update():
    pass

def draw():
    px.cls(0)
    esper.process()

# ------------------------ MAIN -----------------------

# globals
dt = 0.2
wall_restitution = 1.0

# processors
esper.add_processor(MovementProcessor())
esper.add_processor(AppearanceProcessor())
esper.add_processor(WallProcessor())

# entities
esper.create_entity(Circle(x=50, y=50, r=5, m=1), Velocity(vx=10, vy=8), Color())
esper.create_entity(Circle(x=90, y=90, r=2, m=1), Velocity(vx=-6, vy=4), Color(c=10))

px.init(100, 100)
px.run(update, draw)
