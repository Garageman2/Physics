from Body import *


def main():
    CircBot = Body()
    CircTop = Body(Vec2.from_components(2, 0))
    print(CircTop.Collider.hit_result(CircBot.Collider,CircTop.Collider.find_nearest(CircBot.Collider),CircBot.Collider.
                                find_nearest(CircTop.Collider)))

    pass
