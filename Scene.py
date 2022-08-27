from Body import *
import time


class Scene:
    Bodies: list[Body] = []
    time: float = 0.0

    def __init__(self):
        self.time = 0.0

    def add_body(self, name: str, position: Vec2 = Vec2.from_components(0, 0), velocity: Vec2 = Vec2.from_components(0, 0),
                 mass: float = 1.0, collider: object = Circle, size: float = 1.0, enable_gravity: bool = False, *forces: Vec2):
        # TODO: attach names to bodies
        """ Creates a new body in the scene and handles it """
        new_body = Body(name, position, velocity, mass, collider, size, forces)
        if enable_gravity:
            new_body.apply_gravity()
        self.Bodies.append(new_body)

    def run(self, max_time: float = 10):
        time_elapsed: float = 0.0
        delta_time: float = 0.0
        while time_elapsed <= max_time + .0005:
            start: float = time.time()
            for body in self.Bodies:
                # this could have more updates that need to be stored on the body here?
                for other in self.Bodies:
                    if other != body:
                        body.test_collision(other)
                body.process_physics(delta_time)
            end: float = time.time()
            delta_time = end-start
            time_elapsed += delta_time
        else:
            for body in self.Bodies:
                print(body.Name, round(body.Position,3))