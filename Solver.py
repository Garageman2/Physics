import Velocity
import Math.Vector2
class Body:
    """Information About a Physics Object"""
    Speed: float = 0.0



def Main():
    print("Initialized!")
    Vel = Math.Vector2.Vector2.from_length(10,90)
    print(Vel.X)
    print(Vel.Y)
    print(Vel.Length)
    print(Vel.Angle)
    pass