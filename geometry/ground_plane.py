from OpenGL.GL import *
import numpy as np


def draw_ground_plane(position=np.zeros(3)) -> None:
    """
    Draws the ground plane of the scene
    """
    import textures
    glPushMatrix()
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    no_mat = [1, 1, 1, 1.0]
    mat_diffuse = [0.7, 0.7, 0.7, 1.0]
    no_shininess = [0.0]
    mat_emission = [0.2, 0.2, 0.2, 0.0]
    glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, no_mat)
    glMaterialfv(GL_FRONT, GL_SHININESS, no_shininess)
    glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission)
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
