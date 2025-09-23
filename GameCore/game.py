import pygame as pygame
import sys

from . import raycasting
from .map import *
from .player import *
from .raycasting import RayCasting

class Game:
    def __init__(self, fps, width, height):
        # Define constructor variables
        self.FPS = fps
        self.width = width
        self.height = height
        self.delta_time = 1

        # Initiate pygame window
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.create_new_game()

    def create_new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = RayCasting(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(self.FPS)
        pygame.display.set_caption("Creeperstone " + " FPS:" f'{self.clock.get_fps() : .1f}')

    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()