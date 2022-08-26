from Body import *
import time


class Scene:
    Bodies: list[Body] = []
    time: float = 0.0

    def __init__(self):
        self.time = 0.0

    def add_body(self, position: Vec2 = Vec2.from_components(0, 0), velocity: Vec2 = Vec2.from_components(0, 0),
                 mass: float = 1.0, collider: object = Circle, size: float = 1.0, *forces: Vec2):
        """ Creates a new body in the scene and handles it """
        new_body = Body(position, velocity, mass, collider, size, forces)
        self.Bodies.append(new_body)

# needs to check for collisions to generate forces, then pass to each body a process function with the new time
# so the forces can be solved, acceleration, and velocity can be calculated allowing a new position


def main():
    circ_bot = Body()
    circ_top = Body(Vec2.from_components(0, 0), velocity=Vec2.from_components(10, 0), size=2, collider=Circle)
    print(circ_top.test_collision(circ_bot))
    total_time = 0
    delta = 0.0
    circ_top.apply_gravity()
    while total_time < 3.0:
        start = time.time()
        circ_top.process_physics(delta)
        print(circ_top.Position)
        end = time.time()
        delta = end - start
        total_time += delta

