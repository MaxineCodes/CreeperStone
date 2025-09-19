import pygame as pygame
import math

from Game.settings import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x = PLAYER_POSITION[0]
        self.y = PLAYER_POSITION[1]
        self.angle = PLAYER_ANGLE

    def movement(self):
        sin_angle = math.sin(self.angle)
        cosin_angle = math.sin(self.angle)
        direction_x = 0, 0
        direction_y = 0, 0


    def update(self):
        self.movement()

    @property
    def position(self):
        return self.x, self.y

    @property
    def map_position(self):
        return int(self.x), int(self.y)