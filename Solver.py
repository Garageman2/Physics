from Scene import *

# needs to check for collisions to generate forces, then pass to each body a process function with the new time
# so the forces can be solved, acceleration, and velocity can be calculated allowing a new position


def main():
    #maybe a struct with a flag for persistent or not
    world = Scene()
    world.add_body("stationary", enable_gravity=False)
    world.add_body("Moving", Vec2.from_components(0, 10), velocity=Vec2.from_components(10.0, 0), size=10,
                   enable_gravity=False)
    world.run(3)

