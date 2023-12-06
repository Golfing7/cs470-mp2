from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import pygame

import geometry
import game
import time
import numpy as np
from game import player
from pygame.locals import *


houses = [
    geometry.HouseModel(np.array([0, 0, 0]), scale=np.array([1.25, 1.25, 1.25])),
    geometry.HouseModel(np.array([0, 0, 15]), angle=180, scale=np.array([1.5, 1.5, 1.5])),
    geometry.HouseModel(np.array([15, 0, 15]), angle=180),
    geometry.HouseModel(np.array([15, 0, 0]))
]

house_lights = [
    GL_LIGHT2,
    GL_LIGHT3,
    GL_LIGHT4,
    GL_LIGHT5
]

pyramids = [
    geometry.PyramidModel(np.array([-20, 0, 7.5]), angle=0, scale=np.array([10, 10, 10]))
]

trees = [
    geometry.BasicModel(np.array([-5, 0, 7.5]))
]

human = geometry.HumanModel(np.array([5, 0, 0]))


def draw_scene():
    geometry.draw_skybox()
    geometry.draw_ground_plane()
    for house in houses:
        geometry.draw_house(house)
    for pyramid in pyramids:
        geometry.draw_pyramid(pyramid)
    geometry.draw_human(human)
    for tree in trees:
        geometry.draw_tree(tree)


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


def run_loop():
    set_projection(800, 800)

    game_obj = game.GAME
    day_light = [0.4, 0.4, 0.4, 1]
    night_light = [0.02, 0.02, 0.02, 1]
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Perform the offset for the camera
    glLoadIdentity()
    glClearColor(0., 0., 0., 0.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glRotate(-player.PLAYER_OBJECT.pitch, 1, 0, 0)
    glRotate(player.PLAYER_OBJECT.yaw, 0, 1, 0)
    glTranslatef(*-player.PLAYER_OBJECT.position)
    glMatrixMode(GL_MODELVIEW)
    light_ambient = [0.0, 0.0, 0.0, 1.0]
    light_diffuse = [0.7, 0.7, 0.7, 1.0]
    light_specular = [0.3, 0.3, 0.3, 1.0]
    light_position = [10.0, 100.0, 10.0, 1.0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, day_light if game_obj.day else night_light)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    if not game_obj.day:
        for i, light_id in enumerate(house_lights):
            glEnable(light_id)

            house = houses[i]
            light_position = [house.position[0], house.position[1] + 0.5, house.position[2], 1.0]
            glLightfv(light_id, GL_AMBIENT, [0.0, 0.0, 0.0, 1.0])
            glLightfv(light_id, GL_DIFFUSE, [0.15, 0.15, 0.01, 1])
            glLightfv(light_id, GL_SPECULAR, [0.15, 0.15, 0.01, 1])
            glLightfv(light_id, GL_POSITION, light_position)
    else:
        for i, light_id in enumerate(house_lights):
            glDisable(light_id)

    for obj in game_obj.game_objects:
        obj.tick()

    if np.linalg.norm(player.PLAYER_OBJECT.position - human.position) < 2:
        human.start_waving()

    game.tick()

    # Draw scene
    draw_scene()
    glutSwapBuffers()


def timer(time_thing):
    glutPostRedisplay()
    glutTimerFunc(ctypes.c_int(10), timer, 0)


def main():
    game_obj = game.GAME
    for house in houses:
        game_obj.add_game_object(house)
    game_obj.add_game_object(human)
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"A house")
    glutDisplayFunc(run_loop)
    glutKeyboardFunc(game.handle_kd)
    glutSpecialFunc(game.handle_kd)
    glutKeyboardUpFunc(game.handle_ku)
    glutSpecialUpFunc(game.handle_ku)
    timer(1)
    glutMainLoop()


if __name__ == '__main__':
    main()
