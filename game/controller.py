import sys
from OpenGL.GLUT import *

import numpy as np

import game
from game import player

MOVEMENT_MODIFIER = 25

keys_pressed = {}
last_mouse_movement = np.array([0, 0])
last_mouse_position = None


def is_key_pressed(key):
    if isinstance(key, str):
        key = str.encode(key)
    return key in keys_pressed and keys_pressed[key] is True


def handle_kd(key, x, y):
    keys_pressed[key] = True
    game_obj = game.GAME

    if is_key_pressed('n'):
        game_obj.day = not game_obj.day


def handle_ku(key, x, y):
    keys_pressed[key] = False


def tick():
    global last_mouse_movement
    if is_key_pressed('w'):
        movement = player.PLAYER_OBJECT.get_heading() / MOVEMENT_MODIFIER
        player.PLAYER_OBJECT.move_to(player.PLAYER_OBJECT.position + movement)
    if is_key_pressed('s'):
        movement = -player.PLAYER_OBJECT.get_heading() / MOVEMENT_MODIFIER
        player.PLAYER_OBJECT.move_to(player.PLAYER_OBJECT.position + movement)

    if is_key_pressed('a'):
        movement = -player.PLAYER_OBJECT.get_heading(delta_yaw=90) / MOVEMENT_MODIFIER
        player.PLAYER_OBJECT.move_to(player.PLAYER_OBJECT.position + movement)
    if is_key_pressed('d'):
        movement = -player.PLAYER_OBJECT.get_heading(delta_yaw=-90) / MOVEMENT_MODIFIER
        player.PLAYER_OBJECT.move_to(player.PLAYER_OBJECT.position + movement)

    if is_key_pressed(GLUT_KEY_LEFT):
        player.PLAYER_OBJECT.yaw -= 3

    if is_key_pressed(GLUT_KEY_RIGHT):
        player.PLAYER_OBJECT.yaw += 3

    if is_key_pressed('q'):
        sys.exit()
