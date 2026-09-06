from collections import deque
import math
import pygame

from settings import (
    BLACK,
    DIRECTIONS,
    GRID_COLUMNS,
    GRID_ROWS,
    PELLET_COLOR,
    PINK,
    STOP,
    TILE_SIZE,
    WALL_BLUE,
    WALL_INNER,
)


MAZE_LAYOUT = [
    "###################",
    "#o.......#.......o#",
    "#.###.##.#.##.###.#",
    "#.................#",
    "#.###.#.###.#.###.#",
    "#.....#..#..#.....#",
    "#####.##.#.##.#####",
    "#####.#.....#.#####",
    "#####.#.#=#.#.#####",
    "#......#GGG#......#",
    " ......#HGH#...... ",
    "#....#.#####.#....#",
    "####.#.......#.####",
    "#.................#",
    "#.###.##.#.##.###.#",
    "#o..#....#....#..o#",
    "##.#.#.#####.#.#.##",
    "#.....#..#..#.....#",
    "#.####.......####.#",
    "#........P........#",
    "###################",
]

TUNNEL_ROW = 10
GHOST_EXIT_TILE = (7, 9)


class Maze:
    """Owns the board and the navigation rules for players and ghosts."""

    def __init__(self):
        self._validate_layout()

        self.walls = set()
        self.door_tiles = set()
        self.house_tiles = set()
        self.walkable_tiles = set()
        self.player_walkable_tiles = set()
        self.initial_pellets = set()
        self.initial_power_pellets = set()
        self.player_start = None
        self.ghost_starts = []
        self.ghost_exit = GHOST_EXIT_TILE

        self._parse_layout()
        self.reset_collectibles()

    @staticmethod
    def _validate_layout():
        if len(MAZE_LAYOUT) != GRID_ROWS:
            raise ValueError("Maze row count does not match GRID_ROWS.")

        if any(len(row) != GRID_COLUMNS for row in MAZE_LAYOUT):
            raise ValueError("Every maze row must match GRID_COLUMNS.")

    def _parse_layout(self):
        for row_index, row in enumerate(MAZE_LAYOUT):
            for column_index, character in enumerate(row):
                tile = (row_index, column_index)

                if character == "#":
                    self.walls.add(tile)
                    continue

                self.walkable_tiles.add(tile)

                if character == ".":
                    self.initial_pellets.add(tile)
                elif character == "o":
                    self.initial_power_pellets.add(tile)
                elif character == "P":
                    self.player_start = tile
                elif character == "=":
                    self.door_tiles.add(tile)
                elif character == "G":
                    self.ghost_starts.append(tile)
                    self.house_tiles.add(tile)
                elif character == "H":
                    self.house_tiles.add(tile)

        self.player_walkable_tiles = (
            self.walkable_tiles - self.house_tiles - self.door_tiles
        )

        if self.player_start is None:
            raise ValueError("The maze needs one player start tile.")

        if len(self.ghost_starts) != 4:
            raise ValueError("The maze needs exactly four ghost start tiles.")

    def reset_collectibles(self):
        self.pellets = self.initial_pellets.copy()
        self.power_pellets = self.initial_power_pellets.copy()

    @staticmethod
    def tile_center(tile):
        row, column = tile
        return pygame.Vector2(
            column * TILE_SIZE + TILE_SIZE // 2,
            row * TILE_SIZE + TILE_SIZE // 2,
        )

    @staticmethod
    def pixel_to_tile(position):
        row = int(position.y // TILE_SIZE)
        column = int(position.x // TILE_SIZE) % GRID_COLUMNS
        row = max(0, min(row, GRID_ROWS - 1))
        return row, column

    @staticmethod
    def next_tile(tile, direction):
        row, column = tile
        dx, dy = direction
        return row + dy, (column + dx) % GRID_COLUMNS

    def is_blocked(self, tile, allow_house=False):
        row, column = tile
        normalized_tile = (row, column % GRID_COLUMNS)

        if row < 0 or row >= GRID_ROWS:
            return True

        if normalized_tile in self.walls:
            return True

        if not allow_house and (
            normalized_tile in self.house_tiles
            or normalized_tile in self.door_tiles
        ):
            return True

        return False

    def can_move(self, tile, direction, allow_house=False):
        if direction == STOP:
            return False

        row, column = tile
        dx, _ = direction

        if dx and row != TUNNEL_ROW and column + dx not in range(GRID_COLUMNS):
            return False

        next_tile = self.next_tile(tile, direction)
        return not self.is_blocked(next_tile, allow_house)

    def legal_directions(self, tile, allow_house=False):
        return [
            direction
            for direction in DIRECTIONS
            if self.can_move(tile, direction, allow_house)
        ]

    def closest_walkable_tile(self, target, allow_house=False):
        candidates = self.walkable_tiles if allow_house else self.player_walkable_tiles
        return min(
            candidates,
            key=lambda tile: self._manhattan(tile, target),
        )

    def path_distance(self, start, target, allow_house=False):
        """Return the shortest tile distance, or infinity if unreachable."""
        target = self.closest_walkable_tile(target, allow_house)

        if start == target:
            return 0

        queue = deque([(start, 0)])
        visited = {start}

        while queue:
            tile, distance = queue.popleft()

            for direction in self.legal_directions(tile, allow_house):
                neighbor = self.next_tile(tile, direction)
                if neighbor in visited:
                    continue
                if neighbor == target:
                    return distance + 1

                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

        return float("inf")

    def shortest_direction(
        self,
        start,
        target,
        allow_house=False,
        allowed_directions=None,
    ):
        """Choose the first step of a shortest path to the target."""
        choices = allowed_directions or self.legal_directions(start, allow_house)
        if not choices:
            return STOP

        target = self.closest_walkable_tile(target, allow_house)
        return min(
            choices,
            key=lambda direction: self.path_distance(
                self.next_tile(start, direction),
                target,
                allow_house,
            ),
        )

    def consume(self, tile):
        """Return (points, activated_power_mode) for the current tile."""
        if tile in self.power_pellets:
            self.power_pellets.remove(tile)
            return 50, True

        if tile in self.pellets:
            self.pellets.remove(tile)
            return 10, False

        return 0, False

    def has_collectibles(self):
        return bool(self.pellets or self.power_pellets)

    def draw(self, surface):
        self._draw_house_floor(surface)
        self._draw_walls(surface)
        self._draw_door(surface)
        self._draw_collectibles(surface)
        self._draw_tunnel_openings(surface)

    def _draw_house_floor(self, surface):
        for row, column in self.house_tiles:
            rectangle = pygame.Rect(
                column * TILE_SIZE,
                row * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE,
            )
            pygame.draw.rect(surface, (14, 14, 30), rectangle)

    def _draw_walls(self, surface):
        for row, column in self.walls:
            wall_rectangle = pygame.Rect(
                column * TILE_SIZE,
                row * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE,
            )
            pygame.draw.rect(surface, WALL_BLUE, wall_rectangle, border_radius=6)

            inner_rectangle = wall_rectangle.inflate(-8, -8)
            pygame.draw.rect(surface, WALL_INNER, inner_rectangle, border_radius=4)

    def _draw_door(self, surface):
        for row, column in self.door_tiles:
            start = (column * TILE_SIZE + 3, row * TILE_SIZE + TILE_SIZE // 2)
            end = ((column + 1) * TILE_SIZE - 3, row * TILE_SIZE + TILE_SIZE // 2)
            pygame.draw.line(surface, PINK, start, end, 4)

    def _draw_collectibles(self, surface):
        for tile in self.pellets:
            pygame.draw.circle(surface, PELLET_COLOR, self.tile_center(tile), 3)

        pulse = int(2 * abs(math.sin(pygame.time.get_ticks() / 220)))
        for tile in self.power_pellets:
            pygame.draw.circle(
                surface,
                PELLET_COLOR,
                self.tile_center(tile),
                6 + pulse,
            )

    @staticmethod
    def _draw_tunnel_openings(surface):
        pygame.draw.rect(
            surface,
            BLACK,
            pygame.Rect(0, TUNNEL_ROW * TILE_SIZE, 3, TILE_SIZE),
        )
        pygame.draw.rect(
            surface,
            BLACK,
            pygame.Rect(
                GRID_COLUMNS * TILE_SIZE - 3,
                TUNNEL_ROW * TILE_SIZE,
                3,
                TILE_SIZE,
            ),
        )

    @staticmethod
    def _manhattan(first_tile, second_tile):
        return abs(first_tile[0] - second_tile[0]) + abs(
            first_tile[1] - second_tile[1]
        )
