import Velocity
from Math.Vector2 import Vector2 as Vec2
class Body:
    """Information About a Physics Object"""
    Speed: float = 0.0



def Main():
    print("Initialized!")
    Vel = Vec2.from_length(10,90)
    print(Vel)
    print(Vel.angle())
    print(Vel.length())
    pass