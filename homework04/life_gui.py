"""Life GUI module.""" # pylint: disable=no-member

import pygame

from life import GameOfLife
from ui import UI


class GUI(UI):
    """GUI class."""

    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        """Initialize GUI with given parameters."""
        super().__init__(life)
        self.cell_size = cell_size
        self.speed = speed
        self.is_paused = False

        self.width = life.cols * cell_size
        self.height = life.rows * cell_size

        pygame.init()  # pylint: disable=no-member
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game of Life")
        self.clock = pygame.time.Clock()

    def draw_lines(self) -> None:
        """Draw grid lines on the screen."""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, (200, 200, 200), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, (200, 200, 200), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        """Draw alive cells on the screen."""
        for row in range(self.life.rows):
            for col in range(self.life.cols):
                if self.life.curr_generation[row][col]:
                    rect = pygame.Rect(
                        col * self.cell_size,
                        row * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    )
                    pygame.draw.rect(self.screen, (0, 200, 0), rect)

    def run(self) -> None:
        """Run the main game loop."""
        running = True

        while running:
            self.clock.tick(self.speed)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # pylint: disable=no-member
                    running = False

                if event.type == pygame.KEYDOWN:  # pylint: disable=no-member
                    if event.key == pygame.K_SPACE:  # pylint: disable=no-member
                        self.is_paused = not self.is_paused

                if event.type == pygame.MOUSEBUTTONDOWN and self.is_paused:  # pylint: disable=no-member
                    x_pos, y_pos = pygame.mouse.get_pos()
                    col = x_pos // self.cell_size
                    row = y_pos // self.cell_size

                    if 0 <= row < self.life.rows and 0 <= col < self.life.cols:
                        self.life.curr_generation[row][col] ^= 1

            if not self.is_paused:
                self.life.step()

            self.screen.fill((255, 255, 255))
            self.draw_grid()
            self.draw_lines()
            pygame.display.flip()

        pygame.quit()  # pylint: disable=no-member
