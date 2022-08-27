from Math.Vector2 import Vector2 as Vec2
from Shapes import *


class Body:
    """Information About a Physics Object"""
    Name: str = None
    Position: Vec2 = None
    Velocity: Vec2 = None
    Acceleration: Vec2 = None
    Mass: float = None
    Collider: Shape = None
    Forces = []

    def __init__(self, name: str, position: Vec2 = Vec2.from_components(0, 0), velocity: Vec2 = Vec2.from_components(0, 0),
                 mass: float = 1.0, collider_shape: object = Circle, size: float = 1.0, *forces: Vec2) :
        self.Forces = []

        if not issubclass(collider_shape,Shape):
            raise TypeError
        self.Name = name
        self.Collider = collider_shape(position, abs(size))
        self.Position = position
        self.Velocity = velocity
        self.Mass = mass
        for force in forces:
            if force != None:
                self.Forces.append(force)

    def process_physics(self, delta_time: float):
        self._solve_forces()
        self.Velocity += (self.Acceleration * delta_time)
        self.Position += (self.Velocity * delta_time)
        self.Collider.center = self.Position

    # TODO: Replace Evaluate functions with ones that update and accumulate rather than evaluate

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