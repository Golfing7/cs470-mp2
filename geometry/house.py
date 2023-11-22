from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from game import player
from geometry import model
import numpy as np

HOUSE_WIDTH = 2
HOUSE_HEIGHT = 2.5
ROOF_HEIGHT_RATIO = 5

DOOR_HEIGHT = 2
DOOR_WIDTH = 0.75


class HouseModel(model.Model):
    def __init__(self, position=np.array([0, 0, 0])):
        super().__init__(position)

        self.doorOpen = True


def draw_door(house: HouseModel) -> None:
    glPushMatrix()
    glTranslatef(-DOOR_WIDTH, 0, HOUSE_WIDTH)
    if house.doorOpen:
        glRotatef(90, 0, 1, 0)

    glMaterialfv(GL_FRONT, GL_AMBIENT, [0., 0., 1., 1.])
    glBegin(GL_QUADS)

    # Draw door
    glVertex3fv(np.array([0, 0, 0]))
    glVertex3fv(np.array([DOOR_WIDTH * 2, 0, 0]))
    glVertex3fv(np.array([DOOR_WIDTH * 2, DOOR_HEIGHT, 0]))
    glVertex3fv(np.array([0, DOOR_HEIGHT, 0]))

    glEnd()
    glPopMatrix()


def draw_north_wall(house: HouseModel) -> None:
    glBegin(GL_QUADS)
    # Left portion
    glVertex3fv(np.array([-HOUSE_WIDTH, 0, HOUSE_WIDTH]))
    glVertex3fv(np.array([-DOOR_WIDTH, 0, HOUSE_WIDTH]))
    glVertex3fv(np.array([-DOOR_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))
    glVertex3fv(np.array([-HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))

    # Right portion
    glVertex3fv(np.array([HOUSE_WIDTH, 0, HOUSE_WIDTH]))
    glVertex3fv(np.array([DOOR_WIDTH, 0, HOUSE_WIDTH]))
    glVertex3fv(np.array([DOOR_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))
    glVertex3fv(np.array([HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))

    # Top portion
    glVertex3fv(np.array([DOOR_WIDTH, DOOR_HEIGHT, HOUSE_WIDTH]))
    glVertex3fv(np.array([-DOOR_WIDTH, DOOR_HEIGHT, HOUSE_WIDTH]))
    glVertex3fv(np.array([-DOOR_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))
    glVertex3fv(np.array([DOOR_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))
    glEnd()

    # Draw the door
    draw_door(house)


def draw_house(house: HouseModel) -> None:
    """
    Draws the ground plane of the scene
    """
    glPushMatrix()

    # Continue drawing
    glMaterialfv(GL_FRONT, GL_AMBIENT, [1., 1., 0., 1.])
    glTranslatef(*house.position)

    # North wall
    draw_north_wall(house)

    # South wall
    glMaterialfv(GL_FRONT, GL_AMBIENT, [1., 1., 0., 1.])
    glBegin(GL_QUADS)
    glVertex3fv(np.array([-HOUSE_WIDTH, 0, -HOUSE_WIDTH]))
    glVertex3fv(np.array([HOUSE_WIDTH, 0, -HOUSE_WIDTH]))
    glVertex3fv(np.array([HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH]))
    glVertex3fv(np.array([-HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH]))

    # East wall
    glVertex3fv(np.array([HOUSE_WIDTH, 0, -HOUSE_WIDTH]))
    glVertex3fv(np.array([HOUSE_WIDTH, 0, HOUSE_WIDTH]))
    glVertex3fv(np.array([HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))
    glVertex3fv(np.array([HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH]))

    # West wall
    glVertex3fv(np.array([-HOUSE_WIDTH, 0, -HOUSE_WIDTH]))
    glVertex3fv(np.array([-HOUSE_WIDTH, 0, HOUSE_WIDTH]))
    glVertex3fv(np.array([-HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))
    glVertex3fv(np.array([-HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH]))
    glEnd()
    glPopMatrix()

    # Create the pitched roof.
    glPushMatrix()
    glTranslatef(*house.position)
    glBegin(GL_QUADS)
    glMaterialfv(GL_FRONT, GL_AMBIENT, [1., 0., 0., 1.])
    # West facing
    glVertex3fv(np.array([-HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))
    glVertex3fv(np.array([-HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH]))
    glVertex3fv(np.array([0, HOUSE_HEIGHT + (HOUSE_HEIGHT / ROOF_HEIGHT_RATIO), -HOUSE_WIDTH]))
    glVertex3fv(np.array([0, HOUSE_HEIGHT + (HOUSE_HEIGHT / ROOF_HEIGHT_RATIO), HOUSE_WIDTH]))

    # East facing
    glVertex3fv(np.array([HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))
    glVertex3fv(np.array([HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH]))
    glVertex3fv(np.array([0, HOUSE_HEIGHT + (HOUSE_HEIGHT / ROOF_HEIGHT_RATIO), -HOUSE_WIDTH]))
    glVertex3fv(np.array([0, HOUSE_HEIGHT + (HOUSE_HEIGHT / ROOF_HEIGHT_RATIO), HOUSE_WIDTH]))

    glEnd()
    glBegin(GL_TRIANGLES)

    # North facing tri
    glVertex3fv(np.array([HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))
    glVertex3fv(np.array([-HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH]))
    glVertex3fv(np.array([0, HOUSE_HEIGHT + (HOUSE_HEIGHT / ROOF_HEIGHT_RATIO), HOUSE_WIDTH]))

    # South facing tri
    glVertex3fv(np.array([HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH]))
    glVertex3fv(np.array([-HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH]))
    glVertex3fv(np.array([0, HOUSE_HEIGHT + (HOUSE_HEIGHT / ROOF_HEIGHT_RATIO), -HOUSE_WIDTH]))

    glEnd()

    glPopMatrix()
