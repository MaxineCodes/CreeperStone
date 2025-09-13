import pygame as pygame
import sys

class Game:
    def __init__(self, fps, width, height):
        # Define constructor variables
        self.FPS = fps
        self.WIDTH = width
        self.HEIGHT = height

        # Initiate pygame window
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

    def create_new_game(self):
        pass

    def update(self):
        pygame.display.flip()
        self.clock.tick(self.FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() : .1f}')

    def draw(self):
        self.screen.fill('black')

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