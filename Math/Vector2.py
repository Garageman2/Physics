import math

class Vector2:
    """A 2 Component Vector That Stores an Angle in Degrees by Default"""
    X: float = 0.0
    Y: float = 0.0
    Length: float = 0.0
    Angle: float = 0.0

    def __init__(self):
        pass

    # def __init__(self, x: float = 0, y: float = 0, length: float = 1, angle: float = 0):
    #     if x and y:
    #         self.X = x
    #         self.Y = y
    #     if length and angle:
    #         self.Length = length
    #         self.Angle = angle
    #     if not x and not y:
    #         self.X = self.Length * math.acos(self.Angle)

    @classmethod
    def from_components(cls, x: float, y: float):
        result: Vector2 = Vector2()
        result.X = x
        result.Y = y
        result.Length = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
        result.Angle = math.degrees(math.acos(x / result.Length))
        return result

    @classmethod
    def from_length(cls, length: float, angle: float, precision: int=3):
        result: Vector2 = Vector2()
        result.Length = length
        result.Angle = angle
        result.X = round(length * math.cos(math.radians(angle)), precision)
        result.Y = round(length * math.sin(math.radians(angle)), precision)
        return result



    def __add__(self, other):
        return Vector2((self.X + other.X), (self.Y + other.Y))
