# ------------------------------------------------------------
# hangman_final.py
# ------------------------------------------------------------
# This file shows the fully‑implemented Hangman game.
# It follows the exact same public API as hangman_start.py,
# so the test script works unchanged.
# ------------------------------------------------------------

import random
from typing import List, Tuple


# ----------------------------------------------------------------------
# Public API – DO NOT rename – used by the test harness.
# ----------------------------------------------------------------------
def load_word_list() -> List[str]:
    """Return a static list of possible secret words."""
    return ["python", "hangman", "challenge", "intermediate", "program"]


def choose_word(word_list: List[str]) -> str:
    """Pick a random word from *word_list* and return it lower‑cased."""
    # ``random.choice`` is deterministic when the random seed is fixed,
    # which the tests do.
    return random.choice(word_list).lower()


def mask_word(secret: str, guessed: List[str]) -> str:
    """
    Return a spaced mask of the secret word.
    Guessed letters appear, unknown letters become '_' .
    Example: secret='python', guessed=['p','o'] → 'p _ _ _ o _'
    """
    masked = [ch if ch in guessed else "_" for ch in secret]
    return " ".join(masked)


def is_guess_valid(guess: str, guessed: List[str]) -> Tuple[bool, str]:
    """
    Validate the player’s guess.
    Returns (True, "") if the guess is acceptable,
    otherwise (False, <explanation>).
    """
    if len(guess) != 1:
        return False, "Please guess a single character."
    if not guess.isalpha():
        return False, "Only letters are allowed."
    guess = guess.lower()
    if guess in guessed:
        return False, f"You already guessed '{guess}'."
    return True, ""


def update_state(
    secret: str, guessed: List[str], guess: str, remaining: int
) -> Tuple[List[str], int, bool]:
    """
    Apply *guess* to the current game state.
    Returns (new_guessed, new_remaining, was_correct).
    """
    guess = guess.lower()
    guessed.append(guess)  # record the guess

    if guess in secret:
        was_correct = True
    else:
        was_correct = False
        remaining -= 1  # lose a life on a miss

    return guessed, remaining, was_correct


def is_game_won(secret: str, guessed: List[str]) -> bool:
    """True if every distinct letter of *secret* has been guessed."""
    return set(secret).issubset(set(guessed))


def is_game_lost(remaining: int) -> bool:
    """True when the player has no lives left."""
    return remaining <= 0


def play_hangman(max_lives: int = 6) -> None:
    """
    Interactive Hangman session.
    The flow mirrors the classic textbook version:
      1. Choose a secret word.
      2. Show the masked word.
      3. Prompt for a guess.
      4. Validate → update → re‑display.
      5. Repeat until win or loss.
    """
    word_list = load_word_list()
    secret = choose_word(word_list)
    guessed: List[str] = []
    remaining = max_lives

    _display("Welcome to Hangman!")
    _display(f"You have {remaining} lives. Good luck!\n")

    while True:
        # 1️⃣ Show current progress
        masked = mask_word(secret, guessed)

        _display(f"Word: {masked}")
        _display(f"Lives left: {remaining}")
        _display(
            f"Guessed letters: {', '.join(sorted(guessed)) if guessed else 'none'}"
        )

        # 2️⃣ Get player input
        guess = input("\nEnter a letter: ").strip().lower()

        # 3️⃣ Validate
        valid, msg = is_guess_valid(guess, guessed)
        if not valid:
            _display(f"❌ {msg}\n")
            continue

        # 4️⃣ Update state
        guessed, remaining, correct = update_state(secret, guessed, guess, remaining)

        # 5️⃣ Feedback
        if correct:
            _display(f"✅ Good! '{guess}' is in the word.\n")
        else:
            _display(f"❎ Sorry, '{guess}' is not in the word.\n")

        # 6️⃣ Check termination conditions
        if is_game_won(secret, guessed):
            _display(f"🎉 Congratulations! You guessed the word: {secret}")
            break
        if is_game_lost(remaining):
            _display(f"💀 Game over. The word was: {secret}")
            break


# ----------------------------------------------------------------------
# Private helper – isolates print so the test suite can silence output.
# ----------------------------------------------------------------------
def _display(message: str) -> None:
    print(message)


# ------------------------------------------------------------
# If the file is executed directly, start the game.
# ------------------------------------------------------------
if __name__ == "__main__":
    play_hangman()
