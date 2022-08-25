from Math.Vector2 import Vector2 as Vec2
from Body import Body

from Shapes import *

def main():
    projectile = Body(Vec2.from_components(5.0, 0.0), Vec2.from_components(0.0,0.0), 1000)
    projectile.apply_gravity()
    print(projectile.evaluate_position(10.0))

    item = Circle(Vec2.from_components(0, 0), 10)
    item2 = Circle(Vec2.from_components(25, 10), 10)
    print(item.find_nearest(item2))
    pass
