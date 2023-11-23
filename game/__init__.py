import sys

from .player import Player
from .controller import *
from .game_object import GameObject


class Game:
    def __init__(self):
        self.day = True
        self.game_objects = []

    def add_game_object(self, go: game_object.GameObject):
        self.game_objects.append(go)


GAME = Game()
