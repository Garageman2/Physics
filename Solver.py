from Math.Vector2 import Vector2 as Vec2
from Body import Body


def main():
    projectile = Body(Vec2.from_components(5.0, 0.0), Vec2.from_components(0.0,0.0), 1000)
    projectile.apply_gravity()
    print(projectile.evaluate_position(1.0))
    pass
