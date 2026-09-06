import math
import pygame
from settings import (
    LEFT,
    PLAYER_SPEED,
    RIGHT,
    SCREEN_WIDTH,
    STOP,
    UP,
    YELLOW,
)


class Player:
    def __init__(self, maze):
        self.maze = maze
        self.radius = 11
        self.speed = PLAYER_SPEED
        self.start_tile = maze.player_start
        self.position = maze.tile_center(self.start_tile)
        self.direction = LEFT
        self.requested_direction = LEFT

    def reset(self):
        self.position = self.maze.tile_center(self.start_tile)
        self.direction = LEFT
        self.requested_direction = LEFT

    def request_direction(self, direction):
        self.requested_direction = direction

    def current_tile(self):
        return self.maze.pixel_to_tile(self.position)

    def _at_tile_center(self):
        center = self.maze.tile_center(self.current_tile())
        return self.position.distance_to(center) <= self.speed / 2

    def update(self):
        if self._at_tile_center():
            tile = self.current_tile()
            self.position = self.maze.tile_center(tile)

            if self.maze.can_move(tile, self.requested_direction):
                self.direction = self.requested_direction

            if not self.maze.can_move(tile, self.direction):
                self.direction = STOP

        self.position += pygame.Vector2(self.direction) * self.speed
        self._wrap_through_tunnel()

    def _wrap_through_tunnel(self):
        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius

    def draw(self, surface):
        center = (round(self.position.x), round(self.position.y))
        pygame.draw.circle(surface, YELLOW, center, self.radius)

        facing_angles = {
            RIGHT: 0,
            LEFT: math.pi,
            UP: -math.pi / 2,
            (0, 1): math.pi / 2,
            STOP: 0,
        }
        facing = facing_angles[self.direction]
        animation = abs(math.sin(pygame.time.get_ticks() / 115))
        mouth_size = 0.12 + animation * 0.35

        upper_point = (
            center[0] + math.cos(facing - mouth_size) * self.radius,
            center[1] + math.sin(facing - mouth_size) * self.radius,
        )
        lower_point = (
            center[0] + math.cos(facing + mouth_size) * self.radius,
            center[1] + math.sin(facing + mouth_size) * self.radius,
        )

        pygame.draw.polygon(surface, (5, 5, 15), [center, upper_point, lower_point])
