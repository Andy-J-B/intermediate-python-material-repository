"""
platformer_game_template.py

STUDENT STARTER FILE – ONLY THE GAME LOGIC IS MISSING.
The visual part (the main loop) also needs to be written, so you will
implement a complete “run_game()” function that contains the usual
pygame initialisation, the event‑handling loop, updates and rendering.

⚠️  DO NOT rename any function / class / constant.  The automated test
script imports this file and calls the symbols directly.
"""

# -------------------------------------------------
# Imports & Constants – you may adjust the numeric values,
# but keep the *names* unchanged.
# -------------------------------------------------
import pygame
import random

# ----------------------------------------------------------------
# 0. GLOBAL SETTINGS – DO NOT REMOVE OR RE‑NAME ANY OF THESE
# ----------------------------------------------------------------
SCREEN_WIDTH = 600  # window width  (pixels)
SCREEN_HEIGHT = 800  # window height (pixels)

WHITE = (255, 255, 255)  # colour for the score text
BLACK = (0, 0, 0)  # background colour
PLAYER_COLOR = (50, 200, 50)  # colour of the player rectangle
BLOCK_COLOR = (200, 50, 50)  # colour of the falling blocks

PLAYER_WIDTH = 80  # player rectangle width
PLAYER_HEIGHT = 20  # player rectangle height
PLAYER_SPEED = 7  # horizontal speed (pixels per frame)

BLOCK_WIDTH = 30  # block (falling square) width
BLOCK_HEIGHT = 30  # block height
GRAVITY = 0.4  # vertical acceleration (pixels / frame²)

# Custom pygame event that tells us when to spawn a new block
SPAWN_BLOCK_EVENT = pygame.USEREVENT + 1
SPAWN_INTERVAL_MS = 1500  # a new block every 1.5 seconds


# -------------------------------------------------
# 1. Helper Functions – IMPLEMENT EACH ONE
# -------------------------------------------------
def detect_collision(player_rect: pygame.Rect, block_rect: pygame.Rect) -> bool:
    """
    Return True if the two rectangles overlap, otherwise False.

    HINT: pygame.Rect already provides a ``colliderect`` method.
    """
    # --------------------- INSERT YOUR CODE ---------------------
    raise NotImplementedError
    # -----------------------------------------------------------


def generate_block_rect(
    screen_width: int, block_width: int, block_height: int
) -> pygame.Rect:
    """
    Build a pygame.Rect that represents a newly‑spawned block.

    * The block must be fully inside the horizontal bounds of the window.
    * Its y‑coordinate starts just *above* the visible area
      (``-block_height``) so it falls in from the top.
    """
    # --------------------- INSERT YOUR CODE ---------------------
    raise NotImplementedError
    # -----------------------------------------------------------


def move_player(rect: pygame.Rect, dx: int, screen_width: int) -> pygame.Rect:
    """
    Shift ``rect`` horizontally by ``dx`` pixels while keeping it onscreen.

    * Clamp the new x‑position to the interval
      ``[0, screen_width - rect.width]``.
    * Return the (possibly) modified rectangle.
    """
    # --------------------- INSERT YOUR CODE ---------------------
    raise NotImplementedError
    # -----------------------------------------------------------


def apply_gravity(
    rect: pygame.Rect, vel_y: float, dt: float, gravity: float
) -> tuple[pygame.Rect, float]:
    """
    Simulate a simple physics step for a falling object.

    1. ``vel_y += gravity * dt``.
    2. Move the rectangle down by ``int(vel_y)`` (pygame stores integer coords).
    3. Return ``(rect, vel_y)`` – the caller needs the updated velocity.
    """
    # --------------------- INSERT YOUR CODE ---------------------
    raise NotImplementedError
    # -----------------------------------------------------------


def update_score(score: int, caught: bool) -> int:
    """
    Increment the score if the player caught a block.
    Return the new score (do **not** modify the original variable).
    """
    # --------------------- INSERT YOUR CODE ---------------------
    raise NotImplementedError
    # -----------------------------------------------------------


# -------------------------------------------------
# 2. Classes – IMPLEMENT EACH METHOD
# -------------------------------------------------
class Player:
    """
    The player is a simple rectangle that can move left/right.
    """

    def __init__(self, x: int, y: int):
        """
        Create the player rectangle at position (x, y) and store it as
        ``self.rect``.
        """
        # --------------------- INSERT YOUR CODE ---------------------
        raise NotImplementedError
        # -----------------------------------------------------------

    def handle_input(self, keys: dict):
        """
        Examine the ``keys`` dictionary (as returned by
        ``pygame.key.get_pressed()``) and move the player.

        * Move left when ``pygame.K_LEFT`` **or** ``pygame.K_a`` is pressed.
        * Move right when ``pygame.K_RIGHT`` **or** ``pygame.K_d`` is pressed.
        * Use the ``move_player`` helper – it already clamps the rectangle.
        """
        # --------------------- INSERT YOUR CODE ---------------------
        raise NotImplementedError
        # -----------------------------------------------------------

    def update(self, keys: dict):
        """
        Called once per frame from the main loop.
        Currently the only per‑frame behaviour is handling input.
        """
        # --------------------- INSERT YOUR CODE ---------------------
        raise NotImplementedError
        # -----------------------------------------------------------


# Block class : one argument : x : int
# One method : update
# ______________BLOCK CLASS______________


# -------------------------------------------------
# 3. MAIN GAME LOOP – YOU WILL WRITE THIS TOO
# -------------------------------------------------
def run_game() -> None:
    """
    Initialise pygame, create the window, and run the classic
    “while running:” game loop.

    The block below is a **step‑by‑step skeleton**.  Replace the
    ``# TODO:`` sections with the concrete code that matches the
    description.  When you are finished the game should behave exactly
    like the reference implementation (see the completed file).

    Tip: copy‑paste code from the reference solution line‑by‑line, or
    write it from scratch – both approaches help you understand the
    flow of a real pygame program.
    """
    # -------------------------------------------------
    # 3.1  Initialise pygame, screen, caption, font, clock
    # -------------------------------------------------
    # TODO: call pygame.init()
    # TODO: create the screen with the size (SCREEN_WIDTH, SCREEN_HEIGHT)
    # TODO: set the window title (pygame.display.set_caption)
    # TODO: create a pygame font for the score (pygame.font.SysFont)
    # TODO: create a pygame.time.Clock() instance and store it in ``clock``

    # -------------------------------------------------
    # 3.2  Create game objects / state
    # -------------------------------------------------
    # TODO: instantiate a Player centred at the bottom of the screen
    # TODO: create an empty list called ``blocks`` that will hold Block objects
    # TODO: initialise the score (``score = 0``)
    # TODO: set a pygame timer to fire SPAWN_BLOCK_EVENT every SPAWN_INTERVAL_MS
    # TODO: create a boolean ``running = True`` that will control the loop

    # -------------------------------------------------
    # 3.3  Game loop
    # -------------------------------------------------
    # TODO: while running:
    #     # ---- limit the frame‑rate and get the time‑step ----
    #     dt = clock.tick(60) / 1000.0   # 60 FPS, convert ms → seconds (not used now)

    #     # ---- EVENT HANDLING --------------------------------
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #         elif event.type == SPAWN_BLOCK_EVENT:
    #             # use generate_block_rect() to pick a legal x‑position,
    #             # then create a Block and append it to ``blocks``

    #     # ---- INPUT & UPDATE ---------------------------------
    #     keys = pygame.key.get_pressed()
    #     player.update(keys)

    #     # update every block, check collisions, remove off‑screen blocks
    #     for block in blocks[:]:          # iterate over a *copy* because we may delete items
    #         block.update()
    #         if detect_collision(player.rect, block.rect):
    #             score = update_score(score, True)
    #             blocks.remove(block)
    #             continue
    #         if block.rect.top > SCREEN_HEIGHT:   # fell off the bottom?
    #             blocks.remove(block)

    #     # ---- RENDERING --------------------------------------
    #     screen.fill(BLACK)                       # clear background
    #     pygame.draw.rect(screen, PLAYER_COLOR, player.rect)   # draw player
    #     for block in blocks:                     # draw all blocks
    #         pygame.draw.rect(screen, BLOCK_COLOR, block.rect)

    #     # draw the score in the top‑right corner
    #     score_surf = font.render(f"Score: {score}", True, WHITE)
    #     screen.blit(score_surf,
    #                 (SCREEN_WIDTH - score_surf.get_width() - 10, 10))

    #     pygame.display.flip()                    # update the whole display

    # -------------------------------------------------
    # 3.4  Clean‑up
    # -------------------------------------------------
    # TODO: after the loop ends call pygame.quit()


# -------------------------------------------------
# 4. Entry point – DO NOT MODIFY
# -------------------------------------------------
if __name__ == "__main__":
    run_game()
