import pygame
from ghost import Ghost
from maze import Maze
from player import Player
from settings import (
    BLACK,
    CYAN,
    FPS,
    GRID_ROWS,
    HUD_BACKGROUND,
    HUD_HEIGHT,
    ORANGE,
    PINK,
    RED,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    STARTING_LIVES,
    TILE_SIZE,
    WHITE,
    YELLOW,
)

class Game:
    READY = "ready"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"
    WON = "won"

    GHOST_MODE_SCHEDULE = (
        (7_000, Ghost.SCATTER),
        (20_000, Ghost.CHASE),
        (7_000, Ghost.SCATTER),
        (20_000, Ghost.CHASE),
        (5_000, Ghost.SCATTER),
    )

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pac-Man Game")

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.title_font = pygame.font.Font(None, 44)
        self.hud_font = pygame.font.Font(None, 29)
        self.small_font = pygame.font.Font(None, 23)

        self.maze = Maze()
        self.player = Player(self.maze)
        self.ghosts = self._create_ghosts()

        self.running = True
        self.high_score = 0
        self.start_new_game()

    def _create_ghosts(self):
        configurations = [
            (RED, "blinky", (0, 18), 500),
            (PINK, "pinky", (0, 0), 2_500),
            (CYAN, "inky", (20, 18), 5_000),
            (ORANGE, "clyde", (20, 0), 7_500),
        ]

        return [
            Ghost(
                self.maze,
                start,
                color,
                personality,
                scatter_target,
                release_delay,
            )
            for start, (color, personality, scatter_target, release_delay) in zip(
                self.maze.ghost_starts,
                configurations,
            )
        ]

    def start_new_game(self):
        self.score = 0
        self.lives = STARTING_LIVES
        self.ghost_chain = 0
        self.maze.reset_collectibles()
        self._reset_positions()
        self.round_started_at = 0
        self.pause_started_at = None
        self.state = self.READY

    def _reset_positions(self):
        self.player.reset()
        for ghost in self.ghosts:
            ghost.reset()

    def run(self):
        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(FPS)

        pygame.quit()

    def _handle_events(self):
        key_directions = {
            pygame.K_UP: (0, -1),
            pygame.K_w: (0, -1),
            pygame.K_DOWN: (0, 1),
            pygame.K_s: (0, 1),
            pygame.K_LEFT: (-1, 0),
            pygame.K_a: (-1, 0),
            pygame.K_RIGHT: (1, 0),
            pygame.K_d: (1, 0),
        }

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_ESCAPE:
                self.running = False
            elif event.key in key_directions:
                self.player.request_direction(key_directions[event.key])
            elif event.key in (pygame.K_SPACE, pygame.K_RETURN):
                if self.state == self.READY:
                    self._start_round()
            elif event.key == pygame.K_p:
                if self.state == self.PLAYING:
                    self._pause_game()
                elif self.state == self.PAUSED:
                    self._resume_game()
            elif event.key == pygame.K_r and self.state in (self.GAME_OVER, self.WON):
                self.start_new_game()

    def _start_round(self, current_time=None):
        if current_time is None:
            current_time = pygame.time.get_ticks()

        for ghost in self.ghosts:
            ghost.start_round(current_time)
        self.round_started_at = current_time
        self.pause_started_at = None
        self.state = self.PLAYING

    def _pause_game(self):
        self.pause_started_at = pygame.time.get_ticks()
        self.state = self.PAUSED

    def _resume_game(self):
        current_time = pygame.time.get_ticks()
        paused_for = current_time - self.pause_started_at
        self.round_started_at += paused_for

        for ghost in self.ghosts:
            ghost.shift_timers(paused_for)

        self.pause_started_at = None
        self.state = self.PLAYING

    def _ghost_mode(self, current_time):
        elapsed = max(0, current_time - self.round_started_at)

        for duration, mode in self.GHOST_MODE_SCHEDULE:
            if elapsed < duration:
                return mode
            elapsed -= duration

        return Ghost.CHASE

    def _update(self, current_time=None):
        if self.state != self.PLAYING:
            return

        if current_time is None:
            current_time = pygame.time.get_ticks()
        global_mode = self._ghost_mode(current_time)
        self.player.update()

        points, power_mode = self.maze.consume(self.player.current_tile())
        self.score += points

        if points:
            self.high_score = max(self.high_score, self.score)

        if power_mode:
            self.ghost_chain = 0
            for ghost in self.ghosts:
                ghost.frighten(current_time)

        for ghost in self.ghosts:
            ghost.update(
                self.player,
                self.ghosts,
                current_time,
                global_mode,
            )

        self._handle_ghost_collisions(current_time)

        if not self.maze.has_collectibles():
            self.high_score = max(self.high_score, self.score)
            self.state = self.WON

    def _handle_ghost_collisions(self, current_time):
        for ghost in self.ghosts:
            if not ghost.is_collidable():
                continue

            if self.player.position.distance_to(ghost.position) >= 20:
                continue

            if ghost.is_frightened():
                self.ghost_chain += 1
                multiplier = min(2 ** (self.ghost_chain - 1), 8)
                self.score += 200 * multiplier
                self.high_score = max(self.high_score, self.score)
                ghost.eaten()
            else:
                self._lose_life()
                return

    def _lose_life(self):
        self.lives -= 1
        self.ghost_chain = 0

        if self.lives <= 0:
            self.high_score = max(self.high_score, self.score)
            self.state = self.GAME_OVER
        else:
            self._reset_positions()
            self.state = self.READY

    def _draw(self):
        self.screen.fill(BLACK)
        self.maze.draw(self.screen)

        if self.state == self.PAUSED:
            current_time = self.pause_started_at
        else:
            current_time = pygame.time.get_ticks()
        for ghost in self.ghosts:
            ghost.draw(self.screen, current_time)

        self.player.draw(self.screen)
        self._draw_hud()
        self._draw_state_message()
        pygame.display.flip()

    def _draw_hud(self):
        hud_top = GRID_ROWS * TILE_SIZE
        pygame.draw.rect(
            self.screen,
            HUD_BACKGROUND,
            pygame.Rect(0, hud_top, SCREEN_WIDTH, HUD_HEIGHT),
        )

        score_text = self.hud_font.render(f"SCORE  {self.score}", True, WHITE)
        high_score_text = self.hud_font.render(
            f"HIGH  {self.high_score}",
            True,
            WHITE,
        )
        self.screen.blit(score_text, (18, hud_top + 13))
        self.screen.blit(
            high_score_text,
            (SCREEN_WIDTH - high_score_text.get_width() - 18, hud_top + 13),
        )

        lives_label = self.small_font.render("LIVES", True, WHITE)
        self.screen.blit(lives_label, (18, hud_top + 49))

        for index in range(self.lives):
            center = (92 + index * 29, hud_top + 60)
            pygame.draw.circle(self.screen, YELLOW, center, 9)
            pygame.draw.polygon(
                self.screen,
                HUD_BACKGROUND,
                [center, (center[0] + 10, center[1] - 5), (center[0] + 10, center[1] + 5)],
            )

        pause_text = self.small_font.render("P: PAUSE   ESC: QUIT", True, WHITE)
        self.screen.blit(
            pause_text,
            (SCREEN_WIDTH - pause_text.get_width() - 18, hud_top + 51),
        )

    def _draw_state_message(self):
        messages = {
            self.READY: ("READY!", "Press SPACE to start"),
            self.PAUSED: ("PAUSED", "Press P to continue"),
            self.GAME_OVER: ("GAME OVER", "Press R to restart"),
            self.WON: ("YOU WIN!", "Press R to play again"),
        }

        if self.state not in messages:
            return

        title, subtitle = messages[self.state]
        overlay = pygame.Surface((340, 104), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 205))
        overlay_rectangle = overlay.get_rect(
            center=(SCREEN_WIDTH // 2, GRID_ROWS * TILE_SIZE // 2)
        )
        self.screen.blit(overlay, overlay_rectangle)

        title_surface = self.title_font.render(title, True, YELLOW)
        subtitle_surface = self.small_font.render(subtitle, True, WHITE)

        self.screen.blit(
            title_surface,
            title_surface.get_rect(
                center=(SCREEN_WIDTH // 2, overlay_rectangle.centery - 18)
            ),
        )
        self.screen.blit(
            subtitle_surface,
            subtitle_surface.get_rect(
                center=(SCREEN_WIDTH // 2, overlay_rectangle.centery + 24)
            ),
        )
