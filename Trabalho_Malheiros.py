from dataclasses import dataclass as component
import pyxel as px
import esper

# ------------------------ COMPONENTS -----------------------

@component
class Circle:
    x: float
    y: float
    r: int = 10
    m: float = 1.0

@component
class Velocity:
    vx: float = 0.0
    vy: float = 0.0

@component
class Color:
    c: int = 6

# ------------------------ PROCESSORS -----------------------

class MovementProcessor(esper.Processor):
    def process(self):
        for entity, (circle, velocity) in self.world.get_components(Circle, Velocity):
            circle.x += velocity.vx * dt
            circle.y += velocity.vy * dt

class AppearanceProcessor(esper.Processor):
    def process(self):
        for entity, (circle, color) in self.world.get_components(Circle, Color):
            px.circ(circle.x, circle.y, circle.r, color.c)

class WallProcessor(esper.Processor):
    def process(self):
        for entity, (circle, velocity) in self.world.get_components(Circle, Velocity):
            if circle.x < circle.r:  # left wall
                circle.x = circle.r
                velocity.vx *= -wall_restitution
                velocity.vy *= wall_restitution
            elif circle.x > px.width - circle.r:  # right wall
                circle.x = px.width - circle.r
                velocity.vx *= -wall_restitution
                velocity.vy *= wall_restitution
            if circle.y < circle.r:  # ceiling
                circle.y = circle.r
                velocity.vx *= wall_restitution
                velocity.vy *= -wall_restitution
            elif circle.y > px.height - circle.r:  # floor
                circle.y = px.height - circle.r
                velocity.vx *= wall_restitution
                velocity.vy *= -wall_restitution

# ------------------------ MAIN -----------------------

def update():
    world.process()

def draw():
    px.cls(0)
    for processor in processors:
        processor.process()

# globals
dt = 0.2
wall_restitution = 0.8  # Reduced to simulate energy loss

# Initialize the ECS world
world = esper.World()  # Corrigido para 'World', com 'W' maiúsculo

# Add processors to the world
processors = [
    MovementProcessor(),
    AppearanceProcessor(),
    WallProcessor()
]

for processor in processors:
    world.add_processor(processor)

# Create entities with components
world.create_entity(Circle(x=50, y=50, r=10, m=1), Velocity(vx=20, vy=15), Color(c=8))
world.create_entity(Circle(x=90, y=80, r=7, m=1), Velocity(vx=-10, vy=10), Color(c=12))

# Initialize Pyxel
px.init(120, 100, title="ECS Circle Simulation")
px.run(update, draw)
