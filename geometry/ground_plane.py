from OpenGL.GL import *
from OpenGL.GLU import *
from game import player
import numpy as np

def draw_ground_plane(position=np.zeros(3)) -> None:
    """
    Draws the ground plane of the scene
    """
    glPushMatrix()
    glEnable(GL_DEPTH_TEST)
    glMaterialfv(GL_FRONT, GL_AMBIENT, [0., 1., 0., 1.])
    glBegin(GL_QUADS)

    # Grassy plain
    glVertex3fv(position + np.array([-100, 0, -100]))
    glVertex3fv(position + np.array([-100, 0, 100]))
    glVertex3fv(position + np.array([100, 0, 100]))
    glVertex3fv(position + np.array([100, 0, -100]))

    # Street
    glMaterialfv(GL_FRONT, GL_AMBIENT, [0.8, 0.8, 0.8, 1.])
    glVertex3fv(position + np.array([-100, 0.01, 5]))
    glVertex3fv(position + np.array([-100, 0.01, 10]))
    glVertex3fv(position + np.array([100, 0.01, 10]))
    glVertex3fv(position + np.array([100, 0.01, 5]))
    glEnd()
    glPopMatrix()
