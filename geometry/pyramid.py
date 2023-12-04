from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from game import game_object
from geometry import model, util
import numpy as np


class PyramidModel(model.Model, game_object.GameObject):
    def __init__(self, position=np.zeros(3), angle=0, scale=np.ones(3)):
        super().__init__(position, angle, scale)

    def tick(self):
        return


def draw_pyramid(model: model.Model) -> None:
    import textures
    glPushMatrix()

    glEnable(GL_TEXTURE_2D)
    util.set_mat([0.7, 0.7, 0.7, 1.])
    glBindTexture(GL_TEXTURE_2D, textures.SANDSTONE)
    glTranslatef(*model.position)
    glRotatef(model.angle, 0, 1, 0)
    glScale(*model.scale)

    angle = 0
    for i in range(4):
        glRotatef(angle, 0, 1, 0)
        glBegin(GL_TRIANGLES)
        glTexCoord2f(0, 0)
        glVertex3f(1, 0, 1)
        glTexCoord2f(1, 0)
        glVertex3f(1, 0, -1)
        glTexCoord2f(1, 1)
        glVertex3f(0, 1, 0)
        angle += 90
        glEnd()
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()
