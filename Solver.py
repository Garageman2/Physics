from Body import *


def main():
    CircBot = Body()
    CircTop = Body(Vec2.from_components(2, 1), size = 2, collider = Circle)
    print(CircTop.test_collision(CircBot))

    pass
