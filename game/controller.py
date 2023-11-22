import pygame
import numpy as np
from game import player

MOVEMENT_MODIFIER = 25

keys_pressed = {}
last_mouse_movement = np.array([0, 0])

def is_key_pressed(key):
    return key in keys_pressed and keys_pressed[key] is True

def handle_input(pg_input):
    global last_mouse_movement
    if pg_input.type == pygame.KEYDOWN:
        keys_pressed[pg_input.unicode] = True

    if pg_input.type == pygame.KEYUP:
        keys_pressed[pg_input.unicode] = False

    if pg_input.type == pygame.MOUSEMOTION:
        last_mouse_movement = np.array(pg_input.rel)

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

    if last_mouse_movement.nonzero():
        delta_yaw = last_mouse_movement[0] / 15
        last_mouse_movement = np.zeros(2)
        player.PLAYER_OBJECT.yaw = player.PLAYER_OBJECT.yaw + delta_yaw

