from dataclasses import dataclass as component
import pyxel as px
import esper
import math
import random

# ------------------------ COMPONENTS -----------------------

@component
class Circle:
    x:  float
    y:  float
    r:  int = 10
    m:  float = 1.0

@component
class Velocity:
    vx: float
    vy: float

@component
class Color:
    c:  int

@component
class Life:
    hp: int = 100

@component
class InclinedWall:
    x1: float
    y1: float
    x2: float
    y2: float
    nx: float
    ny: float

# ------------------------ PROCESSORS -----------------------

class GravityProcessor(esper.Processor):
    def process(self):
        for entity, velocity in esper.get_component(Velocity):
            velocity.vy += gravity * dt

class WindProcessor(esper.Processor):
    def process(self):
        for entity, velocity in esper.get_component(Velocity):
            velocity.vx += wind * dt

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

        for entity, (circle, velocity, wall) in esper.get_components(Circle, Velocity, InclinedWall):
            dx = wall.x2 - wall.x1
            dy = wall.y2 - wall.y1
            length = math.sqrt(dx * dx + dy * dy)
            nx = wall.nx / length
            ny = wall.ny / length
            cx = circle.x - wall.x1
            cy = circle.y - wall.y1
            distance = abs(nx * cx + ny * cy)
            if distance < circle.r:
                overlap = circle.r - distance
                circle.x += overlap * nx
                circle.y += overlap * ny
                dot = velocity.vx * nx + velocity.vy * ny
                velocity.vx -= 2 * dot * nx
                velocity.vy -= 2 * dot * ny

class CollisionProcessor(esper.Processor):
    def process(self):
        circles = esper.get_components(Circle, Velocity, Life)
        for i, (entity1, (circle1, velocity1, life1)) in enumerate(circles):
            for entity2, (circle2, velocity2, life2) in circles[i+1:]:
                dx = circle2.x - circle1.x
                dy = circle2.y - circle1.y
                distance = math.sqrt(dx * dx + dy * dy)
                if distance < circle1.r + circle2.r:
                    overlap = 0.5 * (distance - circle1.r - circle2.r)
                    circle1.x -= overlap * (circle1.x - circle2.x) / distance
                    circle1.y -= overlap * (circle1.y - circle2.y) / distance
                    circle2.x += overlap * (circle1.x - circle2.x) / distance
                    circle2.y += overlap * (circle1.y - circle2.y) / distance

                    nx = dx / distance
                    ny = dy / distance
                    p = 2 * (velocity1.vx * nx + velocity1.vy * ny - velocity2.vx * nx - velocity2.vy * ny) / (circle1.m + circle2.m)
                    velocity1.vx -= p * circle2.m * nx
                    velocity1.vy -= p * circle2.m * ny
                    velocity2.vx += p * circle1.m * nx
                    velocity2.vy += p * circle1.m * ny

                    # Reduce life on collision
                    life1.hp -= 10
                    life2.hp -= 10

class LifeProcessor(esper.Processor):
    def process(self):
        for entity, life in esper.get_component(Life):
            if life.hp <= 0:
                esper.delete_entity(entity)

def generate_random_position(radius, min_y, max_y):
    x = random.uniform(radius, px.width - radius)
    y = random.uniform(min_y, max_y)
    return x, y

def is_overlapping(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance < (r1 + r2)

def create_non_overlapping_circle(min_radius, max_radius, min_y, max_y, existing_circles):
    while True:
        radius = random.randint(min_radius, max_radius)
        x, y = generate_random_position(radius, min_y, max_y)
        if all(not is_overlapping(x, y, radius, circle.x, circle.y, circle.r) for circle in existing_circles):
            return x, y, radius

def generate_random_color():
    return random.randint(0, 15)

def update():
    pass

def draw():
    px.cls(0)
    esper.process()

# ------------------------ MAIN -----------------------

# globals
dt = 0.2
gravity = 9.8
wind = 1.0
wall_restitution = 1.0

px.init(100, 100)

# entities
min_y = 20
max_y = px.height - 20
min_radius = 3
max_radius = 10

x1, y1, radius1 = create_non_overlapping_circle(min_radius, max_radius, min_y, max_y, [])
circle1 = Circle(x=x1, y=y1, r=radius1, m=1)
color1 = Color(c=generate_random_color())
esper.create_entity(circle1, Velocity(vx=10, vy=8), color1, Life())

x2, y2, radius2 = create_non_overlapping_circle(min_radius, max_radius, min_y, max_y, [circle1])
circle2 = Circle(x=x2, y=y2, r=radius2, m=1)
color2 = Color(c=generate_random_color())
esper.create_entity(circle2, Velocity(vx=-6, vy=4), color2, Life())

# Adicionando mais círculos
entities = [circle1, circle2]
for i in range(3, 5):
    x, y, radius = create_non_overlapping_circle(min_radius, max_radius, min_y, max_y, entities)
    new_circle = Circle(x=x, y=y, r=radius, m=1)
    color_value = generate_random_color()
    esper.create_entity(new_circle, Velocity(vx=(i * 3) % 10 - 5, vy=(i * 2) % 10 - 5), Color(c=color_value), Life())
    entities.append(new_circle)

esper.create_entity(InclinedWall(x1=20, y1=20, x2=80, y2=80, nx=1, ny=-1))

# processors
esper.add_processor(GravityProcessor())
esper.add_processor(WindProcessor())
esper.add_processor(MovementProcessor())
esper.add_processor(AppearanceProcessor())
esper.add_processor(WallProcessor())
esper.add_processor(CollisionProcessor())
esper.add_processor(LifeProcessor())

px.run(update, draw)