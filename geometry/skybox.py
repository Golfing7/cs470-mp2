from OpenGL.GL import *
import numpy as np
from geometry import model, util
import game


def draw_skybox(position=np.zeros(3)) -> None:
    """
    Draws the ground plane of the scene
    """
    import textures
    glEnable(GL_TEXTURE_2D)
    util.set_mat([1, 1, 1, 1])
    glBindTexture(GL_TEXTURE_2D, textures.LANDSCAPE_DAY if game.GAME.day else textures.LANDSCAPE_NIGHT)
    angle = 0

    # Walls
    glPushMatrix()
    for i in range(0, 4):
        glRotatef(angle, 0, 1, 0)
        angle += 90
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(position + np.array([100, 200, -100]))
        glTexCoord2f(0.0, 1.0)
        glVertex3fv(position + np.array([100, 0, -100]))
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(position + np.array([100, 0, 100]))
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(position + np.array([100, 200, 100]))
        glEnd()
    glPopMatrix()

    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, textures.SKY_DAY if game.GAME.day else textures.SKY_NIGHT)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3fv(position + np.array([100, 200, 100]))
    glTexCoord2f(0.0, 1.0)
    glVertex3fv(position + np.array([100, 200, -100]))
    glTexCoord2f(1.0, 1.0)
    glVertex3fv(position + np.array([-100, 200, -100]))
    glTexCoord2f(1.0, 0.0)
    glVertex3fv(position + np.array([-100, 200, 100]))
    glEnd()
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()
