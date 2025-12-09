"""
platformer_game.py

Reference implementation of the Basic Platformer project.
All functions, classes and the game loop are completed – running this file
produces a working game.
"""

# -------------------------------------------------
# Imports & Constants
# -------------------------------------------------
import pygame
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (50, 200, 50)
BLOCK_COLOR = (200, 50, 50)

PLAYER_WIDTH = 80
PLAYER_HEIGHT = 20
PLAYER_SPEED = 7

BLOCK_WIDTH = 30
BLOCK_HEIGHT = 30
GRAVITY = 0.4

SPAWN_BLOCK_EVENT = pygame.USEREVENT + 1
SPAWN_INTERVAL_MS = 1500


# -------------------------------------------------
# Helper Functions
# -------------------------------------------------
def detect_collision(player_rect: pygame.Rect, block_rect: pygame.Rect) -> bool:
    """Return True if the two rectangles overlap."""
    return player_rect.colliderect(block_rect)


def generate_block_rect(
    screen_width: int, block_width: int, block_height: int
) -> pygame.Rect:
    """Return a pygame.Rect for a new block positioned somewhere on top."""
    max_x = screen_width - block_width
    x = random.randint(0, max_x)
    return pygame.Rect(x, -block_height, block_width, block_height)


def move_player(rect: pygame.Rect, dx: int, screen_width: int) -> pygame.Rect:
    """Move the player horizontally, clamping to the screen edges."""
    new_x = rect.x + dx
    new_x = max(0, new_x)
    new_x = min(new_x, screen_width - rect.width)
    rect.x = new_x
    return rect


def apply_gravity(
    rect: pygame.Rect, vel_y: float, dt: float, gravity: float
) -> tuple[pygame.Rect, float]:
    """Apply a single gravity step and move the rectangle down."""
    vel_y += gravity * dt
    rect.y += int(vel_y)
    return rect, vel_y


def update_score(score: int, caught: bool) -> int:
    """Increment the score when a block is caught."""
    return score + 1 if caught else score


# -------------------------------------------------
# Classes
# -------------------------------------------------
class Player:
    """The controllable player rectangle."""

    def __init__(self, x: int, y: int):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)

    def handle_input(self, keys: dict):
        dx = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += PLAYER_SPEED
        move_player(self.rect, dx, SCREEN_WIDTH)

    def update(self, keys: dict):
        self.handle_input(keys)


class Block:
    """A falling block that is affected by gravity."""

    def __init__(self, x: int):
        self.rect = pygame.Rect(x, -BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
        self.vel_y = 0.0

    def update(self):
        self.rect, self.vel_y = apply_gravity(
            self.rect, self.vel_y, dt=1.0, gravity=GRAVITY
        )


# -------------------------------------------------
# Game Loop (entry point)
# -------------------------------------------------
def run_game() -> None:
    """Initialise pygame and run the main game loop."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simple Catcher")
    font = pygame.font.SysFont(None, 36)

    # Player centred at the bottom
    player = Player(
        SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2,
        SCREEN_HEIGHT - PLAYER_HEIGHT - 10,
    )

    blocks: list[Block] = []
    score = 0
    clock = pygame.time.Clock()

    pygame.time.set_timer(SPAWN_BLOCK_EVENT, SPAWN_INTERVAL_MS)

    running = True
    while running:
        dt = clock.tick(60) / 1000.0

        # -------------------------------------------------
        # Event handling
        # -------------------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == SPAWN_BLOCK_EVENT:
                block_rect = generate_block_rect(
                    SCREEN_WIDTH, BLOCK_WIDTH, BLOCK_HEIGHT
                )
                blocks.append(Block(block_rect.x))

        # -------------------------------------------------
        # Update objects
        # -------------------------------------------------
        keys = pygame.key.get_pressed()
        player.update(keys)

        for block in blocks[:]:
            block.update()
            if detect_collision(player.rect, block.rect):
                score = update_score(score, True)
                blocks.remove(block)
                continue
            if block.rect.top > SCREEN_HEIGHT:
                blocks.remove(block)

        # -------------------------------------------------
        # Rendering
        # -------------------------------------------------
        screen.fill(BLACK)
        pygame.draw.rect(screen, PLAYER_COLOR, player.rect)
        for block in blocks:
            pygame.draw.rect(screen, BLOCK_COLOR, block.rect)

        # draw the score
        score_surf = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surf, (SCREEN_WIDTH - score_surf.get_width() - 10, 10))
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    run_game()
