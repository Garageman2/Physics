import warnings
import math
from Math.Vector2 import Vector2 as Vec2
from Shapes import *


class Body:
    """Information About a Physics Object"""
    Position: Vec2 = None
    Velocity: Vec2 = None
    Acceleration: Vec2 = None
    Mass: float = None
    Collider: Shape = None
    Forces = []

    def __init__(self, position: Vec2 = Vec2.from_components(0, 0), velocity: Vec2 = Vec2.from_components(0, 0),
                 mass: float = 1.0, collider: object = Circle, size: float = 1.0, *forces: Vec2) :

        if not issubclass(collider,Shape):
            raise TypeError
        self.Collider = collider(position, abs(size))
        self.Position = position
        self.Velocity = velocity
        self.Mass = mass
        for force in forces:
            self.Forces.append(force)
        self._solve_forces()

    def process_physics(self, delta_time: float):
        self._solve_forces()
        print("Acceleration " , self.Acceleration)
        self.Velocity += (self.Acceleration * delta_time)
        self.Position += (self.Velocity* delta_time)
        self.Collider.center = self.Position

    # TODO: Replace Evaluate functions with ones that update and accumulate rather than evaluate

    def evaluate_position(self, time: float = 0.0) -> Vec2:
        warnings.warn("Only for Static Calculation, to be deprecated", DeprecationWarning)
        return self.Position + (self.Velocity * time) + (self.Acceleration * time * time * .5)

    def evaluate_displacement(self, time: float = 0.0) -> Vec2:
        warnings.warn("Only for Static Calculation, to be deprecated", DeprecationWarning)
        return self.evaluate_position(time) - self.Position

    def evaluate_velocity(self, time: float = 0.0):
        warnings.warn("Only for Static Calculation, to be deprecated", DeprecationWarning)
        return self.Velocity + (self.Acceleration * time)

    def _solve_forces(self, angle: float = 0.0):

        # TODO: Test implementation of incline

        sigma_force = Vec2.from_components(0.0, 0.0)
        for force in self.Forces:
            if isinstance(force, Vec2):
                sigma_force.X += force.X
                sigma_force.Y += force.Y
        self.Acceleration = sigma_force / self.Mass

    def apply_gravity(self):
        self.Forces.append(Vec2.from_components(0.0, self.Mass * -9.81))
        self._solve_forces()

        # TODO: Make angle of Force accessible, maybe a struct passing in forces
    def test_collision(self, other: "Body") -> bool:
        return self.Collider.hit_result(other.Collider)