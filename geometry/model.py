import numpy as np


class Model:
    def __init__(self, position, angle, scale):
        self.position = position
        self.angle = angle
        self.scale = scale


class BasicModel(Model):
    def __init__(self, position=np.zeros(3), angle=0, scale=np.ones(3)):
        super().__init__(position, angle, scale)
