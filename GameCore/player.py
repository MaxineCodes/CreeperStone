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
        direction_x = 0
        direction_y = 0

        movement_speed  = PLAYER_SPEED * self.game.delta_time
        movement_sin    = movement_speed * math.sin(self.angle)
        movement_cosine = movement_speed * math.cos(self.angle)

        keys = pygame.key.get_pressed()
        # moving WASD
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            direction_x += movement_cosine
            direction_y += movement_sin
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            direction_x -= movement_cosine
            direction_y -= movement_sin
        if keys[pygame.K_a]:
            direction_x += movement_sin
            direction_y -= movement_cosine
        if keys[pygame.K_d]:
            direction_x -= movement_sin
            direction_y += movement_cosine

        # Apply movement with collision detection
        self.check_wall_collision(direction_x, direction_y)

        # rotating arrow buttons
        if keys[pygame.K_LEFT]:  self.angle -= PLAYER_ROTATION_SPEED * self.game.delta_time
        if keys[pygame.K_RIGHT]: self.angle += PLAYER_ROTATION_SPEED * self.game.delta_time
        self.angle %= math.tau

    def check_for_wall(self, x, y): return (x,y) not in self.game.map.world_map

    def check_wall_collision(self, direction_x, direction_y):
        if self.check_for_wall(int(self.x + direction_x), int(self.y)):
            self.x += direction_x
        if self.check_for_wall(int(self.x), int(self.y + direction_y)):
            self.y += direction_y

    def draw(self):
        pygame.draw.line(self.game.screen,
                       'yellow',
                    (self.x * 100, self.y * 100),
                     (self.x * 100 + WIDTH * math.cos(self.angle), self.y * 100 + WIDTH * math.sin(self.angle)),
                       2)
        pygame.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def update(self):
        self.movement()

    @property
    def position(self):
        return self.x, self.y

    @property
    def map_position(self):
        return int(self.x), int(self.y)