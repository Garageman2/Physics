import warnings
from Math.Vector2 import Vector2 as Vec2

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
                 mass: float = 1.0, *forces: Vec2):
        self.Position = position
        self.Velocity = velocity
        self.Mass = mass
        for force in forces:
            self.Forces.append(force)
        self._solve_forces()

    # TODO: Replace Evaluate functions with ones that update and accumulate rather than evaluate

    def evaluate_position(self, time: float = 0.0):
        warnings.warn("Only for Static Calculation, to be deprecated", DeprecationWarning)
        return self.Position + (self.Velocity * time) + (self.Acceleration * time * time * .5)

    def evaluate_displacement(self, time: float = 0.0):
        warnings.warn("Only for Static Calculation, to be deprecated", DeprecationWarning)
        return self.evaluate_position(time) - self.Position

    def evaluate_velocity(self, time: float = 0.0):
        warnings.warn("Only for Static Calculation, to be deprecated", DeprecationWarning)
        return self.Velocity + (self.Acceleration * time)

    def _solve_forces(self):
        sigma_force = Vec2.from_components(0,0)
        for force in self.Forces:
            if isinstance(force, Vec2):
                sigma_force.X += force.X
                sigma_force.Y += force.Y
        self.Acceleration = sigma_force / self.Mass

    def apply_gravity(self):
        #this does not account for friction, or an incline
        #TODO: consider incline and friction
        self.Forces.append(Vec2.from_components(0.0, self.Mass * -9.81))
        self._solve_forces()
