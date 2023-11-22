import math
import numpy


class Player(object):
    def __init__(self):
        self.position = numpy.array([0, 1, 0])
        self.yaw = -90
        self.pitch = 0

    def move_to(self, position):
        self.position = position

    def get_heading(self, delta_yaw=0):
        return -numpy.array([math.cos(math.radians(self.yaw + delta_yaw + 90)),
                            0,
                            math.sin(math.radians(self.yaw + delta_yaw + 90))])


PLAYER_OBJECT = Player()
