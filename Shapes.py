import math
from Math.Vector2 import Vector2 as Vec2


class Shape:
    center: Vec2 = None
    size: float = 1.0

    def __init__(self, position: Vec2, size: float = 1.0):
        self.center = position
        self.size = size

    def find_nearest(self, other: "Shape") -> Vec2:
        line = Vec2.from_components((other.center.X - self.center.X), (other.center.Y - self.center.Y))
        return line

    def hit_result(self, other: "Shape", own_near: Vec2, other_near: Vec2) -> bool:
        limit: float = self.center.distance(own_near)
        test: float = self.center.distance(other_near)
        return test <= limit

    def process(self, position: Vec2):
        # TODO: to be called on every physics step
        pass


# noinspection PyTypeChecker
class Square(Shape):

    def find_nearest(self, other: Shape) -> Vec2:
        other_loc = other.center
        line = super(Square, self).find_nearest(other)
        nearest: Vec2 = None

        if abs(line.Y) > abs(line.X):
            # hits top or bottom
            nearest = Vec2.from_components(0, self.size / 2)
            if line.angle() % 360 > 180:
                # bottom half
                nearest.Y = nearest.Y * -1
            if line.X == 0:
                nearest.X = 0.0
            else:
                nearest.X = round(math.tan(math.radians(line.angle())), 5) / nearest.Y
        elif abs(line.X) > abs(line.Y):
            # hits left or right
            nearest = Vec2.from_components(self.size / 2, 0)
            if 90 < (line.angle() % 360) < 270:
                # left half
                nearest.X = nearest.X * -1
            if line.Y == 0:
                nearest.Y = 0.0
            else:
                nearest.Y = round(math.tan(math.radians(line.angle())), 5) * nearest.X
        else:
            nearest = Vec2.from_components(self.size / 2, self.size / 2)
            if line.angle() % 360 > 180:
                # bottom half
                nearest.Y = nearest.Y * -1
            if 90 < (line.angle() % 360) < 270:
                # left half
                nearest.X = nearest.X * -1
        # now translate from local

        return nearest + self.center


# TODO: now check distance to center against nearest point from other body


class Circle(Shape):

    def find_nearest(self, other: Shape) -> Vec2:
        other_loc = other.center
        line = super(Circle, self).find_nearest(other)
        nearest: Vec2 = Vec2.from_length(self.size, line.angle())
        return nearest + self.center
