from Math.Vector2 import Vector2 as Vec2
import warnings


class Force:
    pass


class Body:
    """Information About a Physics Object"""
    Position: Vec2 = None
    Velocity: Vec2 = None
    Acceleration: Vec2 = None
    Mass: float = None
    Forces = []

    # TODO: look at lambdas or ways of passing in a function into Velocity/Acc/Pos etc.
    # TODO: Utilities to read and start calculating position

    def __init__(self, position: Vec2 = Vec2.from_components(0, 0), velocity: Vec2 = Vec2.from_components(0, 0),
                 acceleration: Vec2 = Vec2.from_components(0, 0), mass: float = 1.0, *forces: Force):
        self.Position = position
        self.Velocity = velocity
        self.Acceleration = acceleration
        self.Mass = mass
        self.Forces.append(forces)

    # TODO: Replace Evaluate functions with ones that update and accumulate rather than evaluate

    def evaluate_position(self, time: float = 0.0):
        warnings.warn("Only for Static Calculation, to be deprecated", DeprecationWarning)
        return self.Position + (self.Velocity * time) + (self.Acceleration * time * time * .5)

    def evaluate_velocity(self, time: float = 0.0):
        warnings.warn("Only for Static Calculation, to be deprecated", DeprecationWarning)
        return self.Velocity + (self.Acceleration * time)


def main():
    projectile = Body(Vec2.from_components(5.0, 0.0), Vec2.from_components(0.0, 0.0), Vec2.from_components(0.0, -9.81))
    print(projectile.evaluate_position(3.0))
    pass
