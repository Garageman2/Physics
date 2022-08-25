from Math.Vector2 import Vector2 as Vec2
from Body import Body

from Shapes import *


def main():
    item = Square(Vec2.from_components(10, 0), 10)
    item2 = Circle(Vec2.from_components(0, 0), 10)
    print(item.find_nearest(item2))
    pass
