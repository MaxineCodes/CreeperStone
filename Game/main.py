import pygame as pygame
import sys

from GameCore.game import Game as GameInstance
from settings import *


if __name__ == "__main__":
    # Create an instance of the game
    game = GameInstance(FPS, WIDTH, HEIGHT)
    game.run()