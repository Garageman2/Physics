
from Math.Vector2 import Vector2 as Vec2


class Force:
    pass

class Body:
    """Information About a Physics Object"""
    Position: Vec2 = None
    Velocity: Vec2 = None
    Acceleration: Vec2 = None
    Mass: float = None
    Forces = []

    #TODO: look at lambdas or ways of passing in a function into Velocity/Acc/Pos etc.
    #TODO: Utilities to read and start calculating position

    def __init__(self, position: Vec2 = Vec2.from_components(0, 0), velocity: Vec2 = Vec2.from_components(0, 0),
                 acceleration: Vec2 = Vec2.from_components(0, 0), mass: float = 1.0, *forces: Force) -> object:
        self.Position = position
        self.Velocity = velocity
        self.Acceleration = acceleration
        self.Mass = mass
        self.Forces.append(forces)



def Main():
    Projectile = Body(Vec2.from_components(5.0,0.0))
    pass