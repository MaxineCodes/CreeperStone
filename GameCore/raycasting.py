import pygame as pygame
import math
from Game.settings import *


class RayCasting:
    def __init__(self, game):
        self.game = game

    def raycast(self):
        player_x, player_y = self.game.player.position
        map_x, map_y = self.game.player.map_position

        ray_angle = self.game.player.angle - (FOV / 2) + 0.0001
        for ray in range(NUMBER_OF_RAYS):
            sin_angle = math.sin(ray_angle)
            cosin_angle = math.cos(ray_angle)

            # horizontal
            y_hoizontal, direction_y = (map_y + 1, 1) if sin_angle > 0 else (map_y - 1e-6, -1)
            depth_horizontal = (y_hoizontal - player_y) / sin_angle
            x_horizontal = player_x + depth_horizontal * cosin_angle

            delta_depth = direction_y / sin_angle
            direction_x = delta_depth * cosin_angle

            for i in range (MAXIMUM_DEPTH):
                tile_horizontal = int(x_horizontal), int(y_hoizontal)
                if tile_horizontal in self.game.map.world_map: break
                x_horizontal += direction_x
                y_hoizontal += direction_y
                depth_horizontal += delta_depth

            #vertical
            x_vertical, direction_x = (map_x + 1, 1) if cosin_angle > 0 else (map_x - 1e-6, -1)
            depth_vertical = (x_vertical - player_x) / cosin_angle
            y_vertical = player_y + depth_vertical * sin_angle

            delta_depth = direction_x / cosin_angle
            direction_y = delta_depth * sin_angle

            for i in range(MAXIMUM_DEPTH):
                tile_vertical = int(x_vertical), int(y_vertical)
                if tile_vertical in self.game.map.world_map: break
                x_vertical += direction_x
                y_vertical += direction_y
                depth_vertical += delta_depth

            # depth
            if depth_vertical < depth_horizontal: depth = depth_vertical
            else : depth = depth_horizontal

            # draw for debug
            pygame.draw.line(self.game.screen,
                             'red',
                             (100 * player_x, 100 * player_y),
                             (100 * player_x + 100 * depth * cosin_angle, 100 * player_y + 100 * depth * sin_angle),
                             2)

            ray_angle += DELTA_ANGLE

    def update(self): self.raycast()