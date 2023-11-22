from OpenGL.GL import *
import numpy as np
import game


def draw_skybox(position=np.zeros(3)) -> None:
    """
    Draws the ground plane of the scene
    """
    import textures
    glEnable(GL_TEXTURE_2D)
    no_mat = [1, 1, 1, 1.0]
    mat_diffuse = [0.7, 0.7, 0.7, 1.0]
    no_shininess = [0.0]
    mat_emission = [0.2, 0.2, 0.2, 0.0]
    glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, no_mat)
    glMaterialfv(GL_FRONT, GL_SHININESS, no_shininess)
    glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission)
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
