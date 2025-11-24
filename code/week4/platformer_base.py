"""
platformer_game_template.py

STUDENT STARTER FILE – ONLY THE GAME LOGIC IS MISSING.
The visual part (the main loop at the bottom) already works – you just
have to fill in the helper functions and the two classes.

IMPORTANT:
* Do **not** change any function or class name – the automated tests import
  this file and call them directly.
* Keep the type hints (they are part of the public API).
* You may change constant values (speed, gravity, colours, etc.) if you wish,
  but leave the constant *names* unchanged – the tests reference them.

When you think you are finished, run:

    python platformer_game_template.py

and you should see a small window where a green rectangle (the player)
catches falling red squares (the blocks).  The score appears in the
top‑right corner.
"""

# -------------------------------------------------
# Imports & Constants (feel free to tweak numeric values)
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
    Return True if ``player_rect`` and ``block_rect`` overlap,
    otherwise False.

    HINT:
        * pygame.Rect already provides a ``colliderect`` method.
        * No need to loop over pixels – the built‑in test is O(1).

    What you need to do:
        1. Call the appropriate pygame method.
        2. Return the resulting boolean.
    """
    # --------------------- INSERT YOUR CODE ---------------------
    pass
    # -----------------------------------------------------------


def generate_block_rect(
    screen_width: int, block_width: int, block_height: int
) -> pygame.Rect:
    """
    Build a ``pygame.Rect`` that represents a newly‑spawned block.

    Requirements:
    * The block must be fully inside the horizontal bounds of the window.
    * Its ``y`` coordinate must start just *above* the visible area
      (i.e. ``-block_height``) so it appears to fall in from the top.

    What you need to do:
        1. Compute the maximum allowed x‑position:
           ``max_x = screen_width - block_width``.
        2. Choose a random integer ``x`` in the inclusive range
           ``[0, max_x]``.
        3. Create and return ``pygame.Rect(x, -block_height,
           block_width, block_height)``.
    """
    # --------------------- INSERT YOUR CODE ---------------------
    pass
    # -----------------------------------------------------------


def move_player(rect: pygame.Rect, dx: int, screen_width: int) -> pygame.Rect:
    """
    Shift ``rect`` horizontally by ``dx`` pixels while keeping it onscreen.

    * ``dx`` may be negative (move left) or positive (move right).
    * The player must never leave the window – clamp the new ``x`` value
      to the interval ``[0, screen_width - rect.width]``.
    * Return the (possibly) modified rectangle – the same object is fine,
      but returning it makes the function easy to test.

    What you need to do:
        1. Compute ``new_x = rect.x + dx``.
        2. Clamp ``new_x`` using ``max`` and ``min``.
        3. Assign the clamped value back to ``rect.x``.
        4. Return ``rect``.
    """
    # --------------------- INSERT YOUR CODE ---------------------
    pass
    # -----------------------------------------------------------


def apply_gravity(
    rect: pygame.Rect, vel_y: float, dt: float, gravity: float
) -> tuple[pygame.Rect, float]:
    """
    Simulate a simple physics step for a falling object.

    * ``vel_y`` – current vertical velocity (pixels per frame).
    * ``dt``    – time‑step; for a fixed‑step loop this will always be ``1``.
    * ``gravity`` – the amount to add to ``vel_y`` each step.

    What you need to do:
        1. Update the velocity: ``vel_y += gravity * dt``.
        2. Move the rectangle down by the integer part of the new velocity:
           ``rect.y += int(vel_y)`` (pygame stores integer coordinates).
        3. Return a tuple ``(rect, vel_y)`` so the caller can keep the updated speed.

    NOTE:
        * Returning the new ``vel_y`` is essential – otherwise the block will
          keep falling at the same speed every frame.
    """
    # --------------------- INSERT YOUR CODE ---------------------
    pass
    # -----------------------------------------------------------


def update_score(score: int, caught: bool) -> int:
    """
    Increment the score if the player caught a block.

    * ``caught`` is ``True`` when a collision was detected this frame.
    * Return the *new* score value (do **not** modify the original variable).

    What you need to do:
        1. If ``caught`` is true, return ``score + 1``.
        2. Otherwise, return ``score`` unchanged.
    """
    # --------------------- INSERT YOUR CODE ---------------------
    pass
    # -----------------------------------------------------------


# -------------------------------------------------
# 2. Classes – IMPLEMENT EACH METHOD
# -------------------------------------------------
class Player:
    """
    The player is a simple rectangle that can move left/right.
    All movement logic lives in ``handle_input`` – the class itself only
    stores the rectangle and offers an ``update`` wrapper used in the game loop.
    """

    def __init__(self, x: int, y: int):
        """
        Create the player rectangle at position ``(x, y)``.
        Store it as ``self.rect`` – the rest of the code (and the tests)
        expect a ``pygame.Rect`` instance there.
        """
        # --------------------- INSERT YOUR CODE ---------------------
        pass
        # -----------------------------------------------------------

    def handle_input(self, keys: dict):
        """
        Examine the ``keys`` dictionary (as returned by ``pygame.key.get_pressed()``)
        and move the player left/right.

        * Move left when ``pygame.K_LEFT`` **or** ``pygame.K_a`` is pressed.
        * Move right when ``pygame.K_RIGHT`` **or** ``pygame.K_d`` is pressed.
        * Use the ``move_player`` helper defined above – it already clamps the
          rectangle to the screen bounds.

        The method does **not** return anything; it updates ``self.rect`` in‑place.
        """
        # --------------------- INSERT YOUR CODE ---------------------
        pass
        # -----------------------------------------------------------

    def update(self, keys: dict):
        """
        Called once per frame from the main loop.
        Currently the only thing we need to do each frame is handle the
        keyboard input, so delegate to ``handle_input``.
        """
        # --------------------- INSERT YOUR CODE ---------------------
        pass
        # -----------------------------------------------------------


class Block:
    """
    A falling block that is affected by gravity.
    The class stores its rectangle (``self.rect``) and its current vertical
    velocity (``self.vel_y``).  ``update`` advances the physics one step.
    """

    def __init__(self, x: int):
        """
        Initialise a block at horizontal position ``x``.
        The block starts just above the window (``y = -BLOCK_HEIGHT``).
        Initialise the vertical speed ``self.vel_y`` to ``0.0``.
        Store the rectangle as ``self.rect``.
        """
        # --------------------- INSERT YOUR CODE ---------------------
        pass
        # -----------------------------------------------------------

    def update(self):
        """
        Apply gravity to the block for the current frame.
        Use the ``apply_gravity`` helper – it returns the updated rect and
        the new vertical velocity.  Store both back onto the instance.
        """
        # --------------------- INSERT YOUR CODE ---------------------
        pass
        # -----------------------------------------------------------


# -------------------------------------------------
# 3. MAIN GAME LOOP – YOU DO NOT NEED TO MODIFY THIS SECTION
# -------------------------------------------------
if __name__ == "__main__":
    # Initialise pygame and create the window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simple Catcher")

    # Font used for the score display
    font = pygame.font.SysFont(None, 36)

    # Create the player – centre it horizontally near the bottom of the screen
    player = Player(
        SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2, SCREEN_HEIGHT - PLAYER_HEIGHT - 10
    )

    # List that will hold all active falling blocks
    blocks: list[Block] = []

    # Game state variables
    score = 0
    clock = pygame.time.Clock()

    # Tell pygame to fire ``SPAWN_BLOCK_EVENT`` every ``SPAWN_INTERVAL_MS`` ms
    pygame.time.set_timer(SPAWN_BLOCK_EVENT, SPAWN_INTERVAL_MS)

    running = True
    while running:
        # ``dt`` is the elapsed time in seconds since the previous frame.
        # For this simple demo we don't actually use it, but the variable is handy
        # if you ever want to make the physics time‑independent.
        dt = clock.tick(60) / 1000.0

        # -------------------------------------------------
        # Event handling
        # -------------------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == SPAWN_BLOCK_EVENT:
                # Spawn a new block at a random x‑position.
                # ``generate_block_rect`` already picks a legal x for us.
                new_block_rect = generate_block_rect(
                    SCREEN_WIDTH, BLOCK_WIDTH, BLOCK_HEIGHT
                )
                blocks.append(Block(new_block_rect.x))

        # -------------------------------------------------
        # Game‑object updates
        # -------------------------------------------------
        keys = pygame.key.get_pressed()
        player.update(keys)

        # Update every block; handle collisions and removal
        for block in blocks[:]:  # iterate over a *copy* so we can delete safely
            block.update()

            # 1️⃣ Collision with the player?
            if detect_collision(player.rect, block.rect):
                score = update_score(score, True)
                blocks.remove(block)
                continue

            # 2️⃣ Fell off the bottom of the screen?
            if block.rect.top > SCREEN_HEIGHT:
                blocks.remove(block)

        # -------------------------------------------------
        # Rendering
        # -------------------------------------------------
        screen.fill(BLACK)  # background

        # Draw the player
        pygame.draw.rect(screen, PLAYER_COLOR, player.rect)

        # Draw all falling blocks
        for block in blocks:
            pygame.draw.rect(screen, BLOCK_COLOR, block.rect)

        # Draw the current score in the top‑right corner
        score_surf = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surf, (SCREEN_WIDTH - score_surf.get_width() - 10, 10))

        pygame.display.flip()

    pygame.quit()
