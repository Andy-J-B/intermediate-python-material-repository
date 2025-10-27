# ------------------------------------------------------------
# hangman_start.py
# ------------------------------------------------------------
# This is the *starter* file you will give the student.
# It contains the public API (function names) that the
# autograder / test script will call – **DO NOT CHANGE** those
# signatures.
# The student fills‑in the bodies marked with TODO.
# ------------------------------------------------------------

import random
from typing import List, Tuple


# ----------------------------------------------------------------------
# Public API – DO NOT rename or remove any of these functions.
# ----------------------------------------------------------------------
def load_word_list() -> List[str]:
    """
    Return a list of possible words for the game.
    In the starter version we ship a tiny built‑in list,
    but the student can later replace it with a file read if they want.
    """
    # A tiny list that is guaranteed to be present for the tests.
    return ["python"]


def choose_word(word_list: List[str]) -> str:
    """
    Pick a random word from ``word_list`` and return it in lower case.
    The test harness may monkey‑patch ``random.choice`` to make the
    result deterministic.
    """
    # TODO: implement – see the “Explanation” comment above.
    # Hint: use ``random.choice``.
    raise NotImplementedError


def mask_word(secret: str, guessed: List[str]) -> str:
    """
    Return the word with un‑guessed letters replaced by underscores.
    Example: secret='python', guessed=['p','o'] → 'p _ _ _ o _'
    """
    # TODO: implement – see the “Explanation” comment above.
    raise NotImplementedError


def is_guess_valid(guess: str, guessed: List[str]) -> Tuple[bool, str]:
    """
    Validate the player’s guess.
    * ``guess`` must be a single alphabetic character that has not been guessed yet.
    Returns a tuple ``(is_valid, message)`` where ``message`` explains why a guess is
    invalid (empty string if it is valid).
    """
    # TODO: implement – see the “Explanation” comment above.
    raise NotImplementedError


def update_state(
    secret: str, guessed: List[str], guess: str, remaining: int
) -> Tuple[List[str], int, bool]:
    """
    Apply the player’s guess to the game state.
    * ``guessed`` – list of letters already guessed (will be mutated).
    * ``guess`` – the new letter supplied by the player.
    * ``remaining`` – lives left before this guess.
    Returns a tuple ``(new_guessed, new_remaining, was_correct)``.
    """
    # TODO: implement – see the “Explanation” comment above.
    raise NotImplementedError


def is_game_won(secret: str, guessed: List[str]) -> bool:
    """
    Return ``True`` if every unique character in ``secret`` appears in ``guessed``.
    """
    # TODO: implement – see the “Explanation” comment above.
    raise NotImplementedError


def is_game_lost(remaining: int) -> bool:
    """
    Return ``True`` if the player has run out of lives.
    """
    # TODO: implement – see the “Explanation” comment above.
    raise NotImplementedError


def play_hangman(max_lives: int = 6) -> None:
    """
    Full interactive game loop.
    * This function should use the helpers above.
    * All input() / print() calls stay here – **do not** move them into the
      helper functions because the test script will call the helpers directly.
    * You may add extra private helper functions below if you like.
    """
    # ------------------------------------------------------
    # STUDENT: Fill in the whole body. Use the functions above
    # to keep the logic clean and testable.
    # ------------------------------------------------------
    raise NotImplementedError


# ----------------------------------------------------------------------
# OPTIONAL: Private helper – you may add more if you find them useful.
# ----------------------------------------------------------------------
def _display(message: str) -> None:
    """Simple wrapper around print – makes it easy to mute output in tests."""
    print(message)
