from OpenGL.GL import *
import numpy as np


def draw_ground_plane(position=np.zeros(3)) -> None:
    """
    Draws the ground plane of the scene
    """
    import textures
    glPushMatrix()
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textures.GRASS)
    glBegin(GL_QUADS)

    # Grassy plain
    glTexCoord2f(0.0, 0.0)
    glVertex3fv(position + np.array([-100, 0, -100]))
    glTexCoord2f(0.0, 10.0)
    glVertex3fv(position + np.array([-100, 0, 100]))
    glTexCoord2f(10.0, 10.0)
    glVertex3fv(position + np.array([100, 0, 100]))
    glTexCoord2f(10.0, 0.0)
    glVertex3fv(position + np.array([100, 0, -100]))
    glEnd()
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()

    # Street
    glPushMatrix()
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textures.BLACK_CONCRETE_POWDER)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3fv(position + np.array([-100, 0.01, 5]))
    glTexCoord2f(0.0, 1.0)
    glVertex3fv(position + np.array([-100, 0.01, 10]))
    glTexCoord2f(100.0, 1.0)
    glVertex3fv(position + np.array([100, 0.01, 10]))
    glTexCoord2f(100.0, 0.0)
    glVertex3fv(position + np.array([100, 0.01, 5]))
    glEnd()
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()
