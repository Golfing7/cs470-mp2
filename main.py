import sys
import pygame
import geometry
import game
import time
import numpy as np
from game import player
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class Cube:
    def __init__(self):
        self.faces = {
            "up": [(1, 1, 1), (1, 1, -1), (-1, 1, -1), (-1, 1, 1)],
            "down": [(1, -1, 1), (1, -1, -1), (-1, -1, -1), (-1, -1, 1)],
            "north": [(1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1)],
            "south": [(1, 1, -1), (1, -1, -1), (-1, -1, -1), (-1, 1, -1)],
            "east": [(1, 1, 1), (1, -1, 1), (1, -1, -1), (1, 1, -1)],
            "west": [(-1, 1, 1), (-1, -1, 1), (-1, -1, -1), (-1, 1, -1)]
        }
        # The colors of every face.
        self.colors = {
            "up": (1, 0, 0),
            "down": (0, 1, 0),
            "north": (0, 0, 1),
            "south": (1, 1, 0),
            "east": (1, 0, 1),
            "west": (1, 1, 1)
        }

        self.rotX = 0
        self.rotY = 0
        self.rotZ = 0

    def draw(self):
        glPushMatrix()
        glTranslate(-4, 0, 0)
        glRotatef(self.rotX, 1, 0, 0)
        glRotatef(self.rotY, 0, 1, 0)
        glRotatef(self.rotZ, 0, 0, 1)

        glEnable(GL_DEPTH_TEST)
        glBegin(GL_QUADS)
        for key in self.faces:
            glMaterialfv(GL_FRONT, GL_AMBIENT, self.colors[key])

            for vert in self.faces[key]:
                glVertex3f(vert[0], vert[1], vert[2])
        glEnd()
        glPopMatrix()


def draw_scene():
    geometry.draw_ground_plane()
    geometry.draw_house()
    geometry.draw_house(position=np.array([0, 0, 15]))

def set_projection(w, h):
    """
    Sets the projection mode to perspective.
    :param w: the width of the screen
    :param h: the height of the screen
    """
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, w / h, 0.1, 1000.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    pygame.init()
    display = (800,800)
    window = pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    set_projection(*window.get_size())
    cube = Cube()
    last_tick = 0
    pygame.mouse.set_visible(False)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            game.handle_input(event)

        pygame.mouse.set_pos(window.get_width() / 2, window.get_height() / 2)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Perform the offset for the camera
        glLoadIdentity()
        glClearColor(0., 0.5, 0.75, 0.)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHT1)
        glEnable(GL_DEPTH_TEST)
        glRotate(player.PLAYER_OBJECT.yaw, 0, 1, 0)
        glTranslatef(*-player.PLAYER_OBJECT.position)
        glLightfv(GL_LIGHT0, GL_POSITION, [0, 10, 0, 1])
        glLightfv(GL_LIGHT1, GL_AMBIENT, [0.2, 0.2, 0.2, 0])

        # Draw scene
        cube.draw()
        draw_scene()

        pygame.display.flip()

        # Tick game
        if time.time_ns() - last_tick > (1000000000 / 144):
            last_tick = time.time_ns()
            game.tick()

        pygame.time.wait(10)


main()
