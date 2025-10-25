# ------------------------------------------------------------
# test_hangman.py
# ------------------------------------------------------------
# Automated test suite for the Hang‑Man starter file.
# ------------------------------------------------------------

import unittest
import importlib.util
import sys
import builtins
from unittest.mock import patch


# ------------------------------------------------------------
# Helper – import the student’s module (hangman_template.py)
# ------------------------------------------------------------
def load_student_module():
    """
    Dynamically load ``hangman_template.py`` from the current directory.
    The loaded module is returned and also inserted into ``sys.modules``
    under the name ``hangman_student``.
    """
    spec = importlib.util.spec_from_file_location(
        "hangman_student", "hangman_template.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["hangman_student"] = module
    spec.loader.exec_module(module)  # type: ignore
    return module


# ------------------------------------------------------------
# Test Cases
# ------------------------------------------------------------
class HangmanAPITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load the student implementation once for the whole suite.
        cls.student = load_student_module()

        # Make random.choice deterministic – always return the first element.
        cls.rand_patch = patch("random.choice", side_effect=lambda seq: seq[0])
        cls.rand_patch.start()

    @classmethod
    def tearDownClass(cls):
        cls.rand_patch.stop()

    # ----------------------------------------------------------------
    # 1️⃣ load_word_list
    # ----------------------------------------------------------------
    def test_load_word_list(self):
        words = self.student.load_word_list()
        self.assertIsInstance(words, list)
        self.assertGreater(len(words), 0)
        for w in words:
            self.assertIsInstance(w, str)

    # ----------------------------------------------------------------
    # 2️⃣ choose_word (deterministic via patched random.choice)
    # ----------------------------------------------------------------
    def test_choose_word(self):
        lst = ["alpha", "beta", "gamma"]
        chosen = self.student.choose_word(lst)
        self.assertEqual(chosen, "alpha")  # first element because of our patch

    # ----------------------------------------------------------------
    # 3️⃣ mask_word
    # ----------------------------------------------------------------
    def test_mask_word(self):
        secret = "python"
        guessed = ["p", "o"]
        self.assertEqual(self.student.mask_word(secret, guessed), "p _ _ _ o _")

        self.assertEqual(self.student.mask_word(secret, []), "_ _ _ _ _ _")

        self.assertEqual(
            self.student.mask_word(secret, list(secret)),
            "p y t h o n".replace(" ", " "),
        )

    # ----------------------------------------------------------------
    # 4️⃣ is_guess_valid
    # ----------------------------------------------------------------
    def test_is_guess_valid(self):
        guessed = ["a", "b"]
        ok, msg = self.student.is_guess_valid("ab", guessed)
        self.assertFalse(ok)
        self.assertIn("single", msg.lower())

        ok, msg = self.student.is_guess_valid("5", guessed)
        self.assertFalse(ok)
        self.assertIn("letters", msg.lower())

        ok, msg = self.student.is_guess_valid("a", guessed)
        self.assertFalse(ok)
        self.assertIn("already", msg.lower())

        ok, msg = self.student.is_guess_valid("C", guessed)
        self.assertTrue(ok)
        self.assertEqual(msg, "")

    # ----------------------------------------------------------------
    # 5️⃣ update_state
    # ----------------------------------------------------------------
    def test_update_state(self):
        secret = "hangman"
        guessed = []
        lives = 6

        # correct guess
        guessed, lives, correct = self.student.update_state(secret, guessed, "a", lives)
        self.assertTrue(correct)
        self.assertIn("a", guessed)
        self.assertEqual(lives, 6)

        # incorrect guess
        guessed, lives, correct = self.student.update_state(secret, guessed, "z", lives)
        self.assertFalse(correct)
        self.assertIn("z", guessed)
        self.assertEqual(lives, 5)

    # ----------------------------------------------------------------
    # 6️⃣ win / loss detection
    # ----------------------------------------------------------------
    def test_is_game_won(self):
        secret = "code"
        self.assertFalse(self.student.is_game_won(secret, []))
        self.assertTrue(self.student.is_game_won(secret, list(set(secret))))

    def test_is_game_lost(self):
        self.assertFalse(self.student.is_game_lost(3))
        self.assertTrue(self.student.is_game_lost(0))
        self.assertTrue(self.student.is_game_lost(-1))

    # ----------------------------------------------------------------
    # 7️⃣ Full game simulation – LOSS
    # ----------------------------------------------------------------
    @patch.object(
        builtins,
        "input",
        side_effect=[
            "x",
            "q",
            "z",
            "b",
            "c",
            "d",  # six wrong guesses – all NOT in "python"
        ],
    )
    def test_play_hangman_lose(self, mock_input):
        """
        Simulate a player that never guesses a correct letter.
        After six wrong guesses the game should end with a loss.
        """
        # Silence output – we patch the *actual* module’s private display func
        with patch.object(self.student, "_display"):
            # Force the secret word to be “python”
            with patch.object(self.student, "choose_word", return_value="python"):
                self.student.play_hangman(max_lives=6)

        # If we reach this point without a StopIteration the loop finished
        # correctly (i.e., it asked exactly six inputs).

    # ----------------------------------------------------------------
    # 8️⃣ Full game simulation – WIN
    # ----------------------------------------------------------------
    @patch.object(builtins, "input", side_effect=["p", "y", "t", "h", "o", "n"])
    def test_play_hangman_win(self, mock_input):
        """
        Simulate a perfect player that guesses the word character‑by‑character.
        The final display should contain a congratulatory message.
        """
        captured = []

        # Replace the private _display with a lambda that records the messages.
        def fake_display(msg: str) -> None:
            captured.append(msg)

        with patch.object(self.student, "_display", side_effect=fake_display):
            with patch.object(self.student, "choose_word", return_value="python"):
                self.student.play_hangman(max_lives=6)

        # Verify that at least one of the captured messages contains “Congratulations”
        self.assertTrue(
            any("Congratulations" in msg for msg in captured),
            msg="Winning message not found in captured output.",
        )


# ------------------------------------------------------------
# Run the tests when executed directly.
# ------------------------------------------------------------
if __name__ == "__main__":
    unittest.main(verbosity=2)
