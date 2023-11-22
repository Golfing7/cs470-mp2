from OpenGL.GL import *
from OpenGL.GLU import *

import sys
import pygame

import geometry
import game
import time
import numpy as np
from game import player
from pygame.locals import *


houses = [
    geometry.HouseModel(np.array([0, 0, 0])),
    geometry.HouseModel(np.array([0, 0, 15])),
    geometry.HouseModel(np.array([15, 0, 15])),
    geometry.HouseModel(np.array([15, 0, 0]))
]


def draw_scene():
    geometry.draw_skybox()
    geometry.draw_ground_plane()
    for house in houses:
        geometry.draw_house(house)


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
    display = (800, 800)
    window = pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    set_projection(*window.get_size())
    last_tick = 0
    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)
    game_obj = game.GAME

    day_light = [0.4, 0.4, 0.4, 0]
    night_light = [0.02, 0.02, 0.02, 0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == ord('o'):
                    for house in houses:
                        distance = np.linalg.norm(house.position - player.PLAYER_OBJECT.position)
                        if distance < 5:
                            house.doorOpen = not house.doorOpen
            game.handle_input(game_obj, event)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Perform the offset for the camera
        glLoadIdentity()
        glClearColor(0., 0.5, 0.75, 0.)
        glShadeModel(GL_FLAT)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_BLEND)
        glEnable(GL_LIGHT1)
        glEnable(GL_DEPTH_TEST)
        glRotate(player.PLAYER_OBJECT.yaw, 0, 1, 0)
        glTranslatef(*-player.PLAYER_OBJECT.position)
        light_diffuse = [0.6, 0.6, 0.6, 1.0]
        light_specular = [0.4, 0.4, 0.4, 1.0]
        light_position = [0, 10, 0, 0.0]

        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
        glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)

        glLightfv(GL_LIGHT1, GL_AMBIENT, day_light if game_obj.day else night_light)

        # Draw scene
        draw_scene()

        pygame.display.flip()

        # Tick game
        if time.time_ns() - last_tick > (1000000000 / 144):
            last_tick = time.time_ns()
            game.tick()

        pygame.time.wait(10)


if __name__ == '__main__':
    main()
