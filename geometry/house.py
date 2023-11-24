from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from game import player
from geometry import model
from game import game_object
import numpy as np

HOUSE_WIDTH = 2
HOUSE_HEIGHT = 2.5
ROOF_HEIGHT_RATIO = 5

DOOR_HEIGHT = 2
DOOR_WIDTH = 0.75

WINDOW_LEVEL = 0.5
WINDOW_HEIGHT = 1
WINDOW_WIDTH = 0.5


class HouseModel(model.Model, game_object.GameObject):
    def __init__(self, position=np.zeros(3), angle=0, scale=np.ones(3)):
        super().__init__(position, angle, scale)

        self.doorOpen = True
        self.doorLerp = 0

    def tick(self):
        if self.doorOpen:
            self.doorLerp = min(90, self.doorLerp + 1)
        else:
            self.doorLerp = max(0, self.doorLerp - 1)

    def interact(self):
        self.doorOpen = not self.doorOpen

    def get_door_angle(self):
        return self.doorLerp


def draw_door(house: HouseModel) -> None:
    glPushMatrix()
    glTranslatef(-DOOR_WIDTH, 0, HOUSE_WIDTH)
    glRotatef(house.get_door_angle(), 0, 1, 0)

    glMaterialfv(GL_FRONT, GL_AMBIENT, [0., 0., 1., 1.])
    glBegin(GL_QUADS)

    # Draw door
    glVertex3fv([0, 0, 0])
    glVertex3fv([DOOR_WIDTH * 2, 0, 0])
    glVertex3fv([DOOR_WIDTH * 2, DOOR_HEIGHT, 0])
    glVertex3fv([0, DOOR_HEIGHT, 0])

    glEnd()
    glPopMatrix()


def draw_north_wall(house: HouseModel) -> None:
    glBegin(GL_QUADS)
    # Left portion
    glVertex3fv([-HOUSE_WIDTH, 0, HOUSE_WIDTH])
    glVertex3fv([-DOOR_WIDTH, 0, HOUSE_WIDTH])
    glVertex3fv([-DOOR_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH])
    glVertex3fv([-HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH])

    # Right portion
    glVertex3fv([HOUSE_WIDTH, 0, HOUSE_WIDTH])
    glVertex3fv([DOOR_WIDTH, 0, HOUSE_WIDTH])
    glVertex3fv([DOOR_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH])
    glVertex3fv([HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH])

    # Top portion
    glVertex3fv([DOOR_WIDTH, DOOR_HEIGHT, HOUSE_WIDTH])
    glVertex3fv([-DOOR_WIDTH, DOOR_HEIGHT, HOUSE_WIDTH])
    glVertex3fv([-DOOR_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH])
    glVertex3fv([DOOR_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH])
    glEnd()

    # Draw the door
    draw_door(house)


def draw_windowed_wall(house: HouseModel, angle_offset) -> None:
    glPushMatrix()
    glRotatef(angle_offset, 0, 1, 0)
    glBegin(GL_QUADS)
    
    # Draw bottom portion
    glVertex3fv([-HOUSE_WIDTH, 0, HOUSE_WIDTH])
    glVertex3fv([HOUSE_WIDTH, 0, HOUSE_WIDTH])
    glVertex3fv([HOUSE_WIDTH, WINDOW_LEVEL, HOUSE_WIDTH])
    glVertex3fv([-HOUSE_WIDTH, WINDOW_LEVEL, HOUSE_WIDTH])

    # Draw top portion
    glVertex3fv([-HOUSE_WIDTH, WINDOW_LEVEL + WINDOW_HEIGHT, HOUSE_WIDTH])
    glVertex3fv([HOUSE_WIDTH, WINDOW_LEVEL + WINDOW_HEIGHT, HOUSE_WIDTH])
    glVertex3fv([HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH])
    glVertex3fv([-HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH])

    # Draw east box
    glVertex3fv([WINDOW_WIDTH, WINDOW_LEVEL, HOUSE_WIDTH])
    glVertex3fv([HOUSE_WIDTH, WINDOW_LEVEL, HOUSE_WIDTH])
    glVertex3fv([HOUSE_WIDTH, WINDOW_LEVEL + WINDOW_HEIGHT, HOUSE_WIDTH])
    glVertex3fv([WINDOW_WIDTH, WINDOW_LEVEL + WINDOW_HEIGHT, HOUSE_WIDTH])

    # Draw west box
    glVertex3fv([-WINDOW_WIDTH, WINDOW_LEVEL, HOUSE_WIDTH])
    glVertex3fv([-HOUSE_WIDTH, WINDOW_LEVEL, HOUSE_WIDTH])
    glVertex3fv([-HOUSE_WIDTH, WINDOW_LEVEL + WINDOW_HEIGHT, HOUSE_WIDTH])
    glVertex3fv([-WINDOW_WIDTH, WINDOW_LEVEL + WINDOW_HEIGHT, HOUSE_WIDTH])

    # Draw west box
    glEnd()
    glPopMatrix()


def draw_house(house: HouseModel) -> None:
    """
    Draws the ground plane of the scene
    """
    glPushMatrix()

    # Continue drawing
    glMaterialfv(GL_FRONT, GL_AMBIENT, [1., 1., 0., 1.])
    glTranslatef(*house.position)
    glRotatef(house.angle, 0, 1, 0)
    glScalef(*house.scale)

    # North wall
    draw_north_wall(house)

    # South wall
    glMaterialfv(GL_FRONT, GL_AMBIENT, [1., 1., 0., 1.])
    draw_windowed_wall(house, 180)
    # East wall
    glMaterialfv(GL_FRONT, GL_AMBIENT, [0, 1., 0., 1.])
    draw_windowed_wall(house, 90)
    # West wall
    glMaterialfv(GL_FRONT, GL_AMBIENT, [0, 1., 1., 1.])
    draw_windowed_wall(house, -90)
    glPopMatrix()

    # Create the pitched roof.
    glPushMatrix()
    glTranslatef(*house.position)
    glRotatef(house.angle, 0, 1, 0)
    glScalef(*house.scale)
    glBegin(GL_QUADS)
    glMaterialfv(GL_FRONT, GL_AMBIENT, [1., 0., 0., 1.])
    # West facing
    glVertex3fv([-HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH])
    glVertex3fv([-HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH])
    glVertex3fv([0, HOUSE_HEIGHT + (HOUSE_HEIGHT / ROOF_HEIGHT_RATIO), -HOUSE_WIDTH])
    glVertex3fv([0, HOUSE_HEIGHT + (HOUSE_HEIGHT / ROOF_HEIGHT_RATIO), HOUSE_WIDTH])

    # East facing
    glVertex3fv([HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH])
    glVertex3fv([HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH])
    glVertex3fv([0, HOUSE_HEIGHT + (HOUSE_HEIGHT / ROOF_HEIGHT_RATIO), -HOUSE_WIDTH])
    glVertex3fv([0, HOUSE_HEIGHT + (HOUSE_HEIGHT / ROOF_HEIGHT_RATIO), HOUSE_WIDTH])

    glEnd()
    glBegin(GL_TRIANGLES)

    # North facing tri
    glVertex3fv([HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH])
    glVertex3fv([-HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_WIDTH])
    glVertex3fv([0, HOUSE_HEIGHT + (HOUSE_HEIGHT / ROOF_HEIGHT_RATIO), HOUSE_WIDTH])

    # South facing tri
    glVertex3fv([HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH])
    glVertex3fv([-HOUSE_WIDTH, HOUSE_HEIGHT, -HOUSE_WIDTH])
    glVertex3fv([0, HOUSE_HEIGHT + (HOUSE_HEIGHT / ROOF_HEIGHT_RATIO), -HOUSE_WIDTH])

    glEnd()

    glPopMatrix()
