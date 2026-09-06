import random
import pygame
from settings import (
    EATEN_SPEED,
    FRIGHTENED_BLUE,
    FRIGHTENED_DURATION,
    FRIGHTENED_SPEED,
    GHOST_RESPAWN_DELAY,
    GHOST_SPEED,
    GRID_COLUMNS,
    GRID_ROWS,
    LEFT,
    OPPOSITE_DIRECTION,
    STOP,
    TILE_SIZE,
    UP,
    WHITE,
)


class Ghost:
    IN_HOUSE = "in_house"
    LEAVING = "leaving"
    CHASE = "chase"
    SCATTER = "scatter"
    FRIGHTENED = "frightened"
    EATEN = "eaten"

    def __init__(
        self,
        maze,
        start_tile,
        color,
        personality,
        scatter_target,
        release_delay,
    ):
        self.maze = maze
        self.start_tile = start_tile
        self.color = color
        self.personality = personality
        self.scatter_target = scatter_target
        self.release_delay = release_delay
        self.radius = 11
        self.reset()

    def reset(self):
        self.position = self.maze.tile_center(self.start_tile)
        self.direction = UP
        self.state = self.IN_HOUSE
        self.release_at = float("inf")
        self.frightened_until = 0

    def start_round(self, current_time):
        self.release_at = current_time + self.release_delay

    def shift_timers(self, milliseconds):
        if self.release_at != float("inf"):
            self.release_at += milliseconds
        if self.frightened_until:
            self.frightened_until += milliseconds

    def current_tile(self):
        return self.maze.pixel_to_tile(self.position)

    def is_frightened(self):
        return self.state == self.FRIGHTENED

    def is_collidable(self):
        return self.state not in (self.IN_HOUSE, self.EATEN)

    def frighten(self, current_time):
        if self.state not in (self.CHASE, self.SCATTER):
            return

        self.state = self.FRIGHTENED
        self.frightened_until = current_time + FRIGHTENED_DURATION
        self.direction = OPPOSITE_DIRECTION[self.direction]

    def eaten(self):
        """Become eyes and navigate back to the individual home tile."""
        if self.state != self.FRIGHTENED:
            return

        self.state = self.EATEN
        self.frightened_until = 0
        self.direction = OPPOSITE_DIRECTION[self.direction]

    def _at_tile_center(self, speed):
        center = self.maze.tile_center(self.current_tile())
        return self.position.distance_to(center) <= speed / 2

    def update(self, player, ghosts, current_time, global_mode):
        if self.state == self.IN_HOUSE:
            if current_time >= self.release_at:
                self.state = self.LEAVING
                self.direction = UP
            else:
                return

        if self.state == self.FRIGHTENED and current_time >= self.frightened_until:
            self.state = global_mode

        if self.state in (self.CHASE, self.SCATTER):
            self.state = global_mode

        speed = self._movement_speed()

        if self._at_tile_center(speed):
            tile = self.current_tile()
            self.position = self.maze.tile_center(tile)

            if self.state == self.EATEN and tile == self.start_tile:
                self.state = self.IN_HOUSE
                self.release_at = current_time + GHOST_RESPAWN_DELAY
                self.direction = UP
                return

            if self.state == self.LEAVING and tile == self.maze.ghost_exit:
                self.state = global_mode

            self.direction = self._choose_direction(
                tile,
                player,
                ghosts,
            )

        self.position += pygame.Vector2(self.direction) * speed
        self._wrap_through_tunnel()

    def _movement_speed(self):
        if self.state == self.FRIGHTENED:
            return FRIGHTENED_SPEED
        if self.state == self.EATEN:
            return EATEN_SPEED
        return GHOST_SPEED

    def _choose_direction(self, tile, player, ghosts):
        if self.state == self.EATEN:
            return self.maze.shortest_direction(
                tile,
                self.start_tile,
                allow_house=True,
            )

        if self.state == self.LEAVING:
            return self.maze.shortest_direction(
                tile,
                self.maze.ghost_exit,
                allow_house=True,
            )

        choices = self.maze.legal_directions(tile, allow_house=False)
        reverse = OPPOSITE_DIRECTION[self.direction]
        forward_choices = [choice for choice in choices if choice != reverse]
        if forward_choices:
            choices = forward_choices

        if not choices:
            return STOP

        if self.state == self.FRIGHTENED:
            return random.choice(choices)

        target = self._select_target(player, ghosts)
        return self.maze.shortest_direction(
            tile,
            target,
            allow_house=False,
            allowed_directions=choices,
        )

    def _select_target(self, player, ghosts):
        if self.state == self.SCATTER:
            return self.scatter_target

        player_tile = player.current_tile()

        if self.personality == "blinky":
            return player_tile

        if self.personality == "pinky":
            return self._tile_ahead(player_tile, player.direction, 4)

        if self.personality == "inky":
            pivot = self._tile_ahead(player_tile, player.direction, 2)
            blinky_tile = ghosts[0].current_tile()
            return self._clamp_target(
                (
                    pivot[0] + (pivot[0] - blinky_tile[0]),
                    pivot[1] + (pivot[1] - blinky_tile[1]),
                )
            )

        distance_to_player = self._manhattan(self.current_tile(), player_tile)
        return player_tile if distance_to_player > 8 else self.scatter_target

    @staticmethod
    def _tile_ahead(tile, direction, steps):
        row, column = tile
        dx, dy = direction
        return Ghost._clamp_target((row + dy * steps, column + dx * steps))

    @staticmethod
    def _clamp_target(tile):
        row, column = tile
        return (
            max(0, min(row, GRID_ROWS - 1)),
            max(0, min(column, GRID_COLUMNS - 1)),
        )

    @staticmethod
    def _manhattan(first_tile, second_tile):
        return abs(first_tile[0] - second_tile[0]) + abs(
            first_tile[1] - second_tile[1]
        )

    def _wrap_through_tunnel(self):
        board_width = GRID_COLUMNS * TILE_SIZE
        if self.position.x < -self.radius:
            self.position.x = board_width + self.radius
        elif self.position.x > board_width + self.radius:
            self.position.x = -self.radius

    def draw(self, surface, current_time):
        center_x = round(self.position.x)
        center_y = round(self.position.y)

        if self.state == self.EATEN:
            self._draw_eyes(surface, center_x, center_y)
            return

        body_color = self._display_color(current_time)
        self._draw_body(surface, center_x, center_y, body_color)

        if self.state == self.FRIGHTENED:
            self._draw_frightened_face(surface, center_x, center_y)
        elif self.state == self.IN_HOUSE and current_time < self.release_at:
            self._draw_sleeping_face(surface, center_x, center_y)
        else:
            self._draw_eyes(surface, center_x, center_y)

    def _display_color(self, current_time):
        if self.state != self.FRIGHTENED:
            return self.color

        time_left = self.frightened_until - current_time
        if time_left < 2_000 and (current_time // 180) % 2 == 0:
            return WHITE
        return FRIGHTENED_BLUE

    def _draw_body(self, surface, center_x, center_y, color):
        pygame.draw.circle(
            surface,
            color,
            (center_x, center_y - 2),
            self.radius,
        )

        body_points = [
            (center_x - self.radius, center_y - 2),
            (center_x - self.radius, center_y + self.radius),
            (center_x - 7, center_y + 6),
            (center_x, center_y + self.radius),
            (center_x + 7, center_y + 6),
            (center_x + self.radius, center_y + self.radius),
            (center_x + self.radius, center_y - 2),
        ]
        pygame.draw.polygon(surface, color, body_points)

    def _draw_eyes(self, surface, center_x, center_y):
        direction_vector = pygame.Vector2(self.direction)
        pupil_offset = direction_vector * 2

        for eye_offset in (-5, 5):
            eye_center = (center_x + eye_offset, center_y - 4)
            pygame.draw.circle(surface, WHITE, eye_center, 4)
            pupil_center = (
                round(eye_center[0] + pupil_offset.x),
                round(eye_center[1] + pupil_offset.y),
            )
            pygame.draw.circle(surface, (30, 45, 110), pupil_center, 2)

    @staticmethod
    def _draw_sleeping_face(surface, center_x, center_y):
        pygame.draw.line(
            surface,
            WHITE,
            (center_x - 8, center_y - 3),
            (center_x - 2, center_y - 3),
            2,
        )
        pygame.draw.line(
            surface,
            WHITE,
            (center_x + 2, center_y - 3),
            (center_x + 8, center_y - 3),
            2,
        )

    @staticmethod
    def _draw_frightened_face(surface, center_x, center_y):
        pygame.draw.circle(surface, WHITE, (center_x - 4, center_y - 4), 2)
        pygame.draw.circle(surface, WHITE, (center_x + 4, center_y - 4), 2)
        pygame.draw.line(
            surface,
            WHITE,
            (center_x - 6, center_y + 5),
            (center_x + 6, center_y + 5),
            2,
        )
