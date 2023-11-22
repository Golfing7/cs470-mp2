from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from game import player
import numpy as np

HOUSE_WIDTH = 2
HOUSE_HEIGHT = 2.5
ROOF_HEIGHT_RATIO = 5
angle = 0

def draw_house(position=np.zeros(3)) -> None:
    """
    Draws the ground plane of the scene
    """
    global angle
    glPushMatrix()

    # Apply angle
    glTranslatef(*position)
    glRotated(angle, 0, 1, 0)
    glTranslatef(*-position)

    # Continue drawing
    glEnable(GL_DEPTH_TEST)
    glBegin(GL_QUADS)
    glMaterialfv(GL_FRONT, GL_AMBIENT, [1., 1., 0., 1.])
    # North wall
    glVertex3fv(position + np.array([-HOUSE_WIDTH, 0, HOUSE_WIDTH]))
    glVertex3fv(position + np.array([HOUSE_WIDTH, 0, HOUSE_WIDTH]))
    glVertex3fv(position + np.array([HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))
    glVertex3fv(position + np.array([-HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))

    # South wall
    glVertex3fv(position + np.array([-HOUSE_WIDTH, 0, -HOUSE_WIDTH]))
    glVertex3fv(position + np.array([HOUSE_WIDTH, 0, -HOUSE_WIDTH]))
    glVertex3fv(position + np.array([HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH]))
    glVertex3fv(position + np.array([-HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH]))

    # East wall
    glVertex3fv(position + np.array([HOUSE_WIDTH, 0, -HOUSE_WIDTH]))
    glVertex3fv(position + np.array([HOUSE_WIDTH, 0, HOUSE_WIDTH]))
    glVertex3fv(position + np.array([HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))
    glVertex3fv(position + np.array([HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH]))

    # West wall
    glVertex3fv(position + np.array([-HOUSE_WIDTH, 0, -HOUSE_WIDTH]))
    glVertex3fv(position + np.array([-HOUSE_WIDTH, 0, HOUSE_WIDTH]))
    glVertex3fv(position + np.array([-HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))
    glVertex3fv(position + np.array([-HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH]))

    # Create the pitched roof.
    glMaterialfv(GL_FRONT, GL_AMBIENT, [1., 0., 0., 1.])
    # West facing
    glVertex3fv(position + np.array([-HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))
    glVertex3fv(position + np.array([-HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH]))
    glVertex3fv(position + np.array([0, HOUSE_HEIGHT + (HOUSE_HEIGHT / ROOF_HEIGHT_RATIO), -HOUSE_WIDTH]))
    glVertex3fv(position + np.array([0, HOUSE_HEIGHT + (HOUSE_HEIGHT / ROOF_HEIGHT_RATIO), HOUSE_WIDTH]))

    # East facing
    glVertex3fv(position + np.array([HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))
    glVertex3fv(position + np.array([HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH]))
    glVertex3fv(position + np.array([0, HOUSE_HEIGHT + (HOUSE_HEIGHT / ROOF_HEIGHT_RATIO), -HOUSE_WIDTH]))
    glVertex3fv(position + np.array([0, HOUSE_HEIGHT + (HOUSE_HEIGHT / ROOF_HEIGHT_RATIO), HOUSE_WIDTH]))

    glEnd()
    glBegin(GL_TRIANGLES)

    # North facing tri
    glVertex3fv(position + np.array([HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))
    glVertex3fv(position + np.array([-HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))
    glVertex3fv(position + np.array([0, HOUSE_HEIGHT + (HOUSE_HEIGHT / ROOF_HEIGHT_RATIO), HOUSE_WIDTH]))

    # South facing tri
    glVertex3fv(position + np.array([HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH]))
    glVertex3fv(position + np.array([-HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH]))
    glVertex3fv(position + np.array([0, HOUSE_HEIGHT + (HOUSE_HEIGHT / ROOF_HEIGHT_RATIO), -HOUSE_WIDTH]))

    glEnd()

    glPopMatrix()
