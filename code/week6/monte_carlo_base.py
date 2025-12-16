# --------------------------------------------------------------
# tic_tac_toe_cli_mc_base.py
# --------------------------------------------------------------
# STUDENT STARTER FILE – MONTE‑CARLO AI LOGIC IS MISSING.
# --------------------------------------------------------------

import random
from typing import List, Optional, Tuple

# ----------------------------------------------------------------
# TYPE ALIASES
# ----------------------------------------------------------------
Board = List[List[Optional[str]]]  # 3×3 grid – "X", "O", or None
Move = Tuple[int, int]  # (row, col) – 0‑based indices


# ----------------------------------------------------------------
# 1. initialise_board()
# ----------------------------------------------------------------
def initialize_board() -> Board:
    """Create a brand‑new empty board."""
    return [[None for _ in range(3)] for _ in range(3)]


# ----------------------------------------------------------------
# 2. make_move()
# ----------------------------------------------------------------
def make_move(board: Board, row: int, col: int, player: str) -> bool:
    """
    Place ``player`` ("X" or "O") at ``(row, col)`` if the cell is free.
    Returns ``True`` when the move was applied, otherwise ``False``.
    """
    if board[row][col] is None:
        board[row][col] = player
        return True
    return False


# ----------------------------------------------------------------
# 3. check_winner()
# ----------------------------------------------------------------
def check_winner(board: Board) -> Optional[str]:
    """Return the winner symbol ('X' or 'O') or None if there is no winner yet."""
    lines = []

    for i in range(3):
        lines.append(board[i])  # rows
        lines.append([board[0][i], board[1][i], board[2][i]])  # columns

    # diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])  # \
    lines.append([board[0][2], board[1][1], board[2][0]])  # /

    for line in lines:
        if line[0] is not None and line[0] == line[1] == line[2]:
            return line[0]
    return None


# ----------------------------------------------------------------
# 4. is_draw()
# ----------------------------------------------------------------
def is_draw(board: Board) -> bool:
    """True when the board is full and there is no winner."""
    board_full = all(cell is not None for row in board for cell in row)
    return board_full and check_winner(board) is None


# ----------------------------------------------------------------
# 5. get_available_moves()
# ----------------------------------------------------------------
def get_available_moves(board: Board) -> List[Move]:
    """Return a list of every empty square as (row, col) tuples."""
    moves: List[Move] = []
    for r in range(3):
        for c in range(3):
            if board[r][c] is None:
                moves.append((r, c))
    return moves


# ----------------------------------------------------------------
# 6. pretty_print()
# ----------------------------------------------------------------
def pretty_print(board: Board) -> None:
    """Print a nice, human‑readable representation of the board."""

    def sym(cell: Optional[str]) -> str:
        return cell if cell is not None else " "

    rows = [" | ".join(sym(board[r][c]) for c in range(3)) for r in range(3)]
    separator = "\n-----------\n"
    print("\n" + separator.join(rows) + "\n")


# ----------------------------------------------------------------
# MONTE‑CARLO HELPER – YOU WILL IMPLEMENT THIS FUNCTION
# ----------------------------------------------------------------
def _run_random_playout(
    board: Board,
    current_player: str,
    ai_player: str,
    human_player: str,
) -> Optional[str]:
    """
    Simulate a *complete* game from the supplied board state.
    Both players choose moves uniformly at random.

    Parameters
    ----------
    board : Board
        A **copy** of the current board (do NOT modify the original board!).
    current_player : str
        Whose turn it is to play in this simulated game.
    ai_player / human_player : str
        Symbols used by the AI and the human (e.g. "O" and "X").

    Returns
    -------
    Optional[str]
        "X" or "O" if one of the players wins, or ``None`` for a draw.

    -------------------------------------------------------------------------
    What you need to do:
    1. Loop until the game ends.
    2. At the start of each loop iteration, check whether the board already
       contains a winner (``check_winner``) or is a draw (``is_draw``).  If so,
       return the appropriate result.
    3. Otherwise pick a random legal move from ``get_available_moves(board)``.
    4. Apply that move with ``make_move``.
    5. Switch ``current_player`` to the opponent and repeat.
    -------------------------------------------------------------------------
    """
    # ---------------------  INSERT YOUR CODE  ---------------------
    # Replace the `raise NotImplementedError` below with the logic described
    # above.  The implementation will be identical to the one shown in the
    # completed solution file.
    raise NotImplementedError
    # -------------------------------------------------------------


# ----------------------------------------------------------------
# AI LOGIC – YOU WILL IMPLEMENT THIS FUNCTION
# ----------------------------------------------------------------
def ai_move(board: Board, ai_player: str, human_player: str) -> Move:
    """
    Choose a move for the AI using Monte‑Carlo simulations.

    Overview of the algorithm you must code:
    --------------------------------------------------------------
    1. Get the list of all legal moves with ``get_available_moves``.
    2. For each candidate move:
         a. Make a *copy* of the board and apply the candidate move.
         b. Run a number of random playouts (the helper above) that
            start with the opponent to move.
         c. Count how many playouts the AI wins.
         d. Compute a win‑rate = wins / simulations.
    3. Return the move with the highest win‑rate.
    --------------------------------------------------------------

    Hints for you:
    * Use a constant like ``SIMULATIONS_PER_MOVE = 500`` – you can
      adjust it later for speed vs strength.
    * Copy a board with ``[row[:] for row in board]`` (shallow copy of rows).
    * The helper ``_run_random_playout`` already does a full random game;
      you only need to call it.
    * If two moves have the same win‑rate you may pick any of them
      (e.g. the first one you encounter).

    The function **must not** modify the original ``board`` argument.
    It should finally ``return (row, col)`` of the selected move.
    """
    # ----------  INSERT YOUR CODE BELOW  ----------
    # Replace the line below with the Monte‑Carlo implementation.
    # For now we keep a temporary random move so the program can still run
    # while you are working on the algorithm.
    return random.choice(get_available_moves(board))
    # ----------  END OF YOUR CODE  -----------------


# ----------------------------------------------------------------
# MAIN GAME LOOP (already complete – do NOT change)
# ----------------------------------------------------------------
def play_game() -> None:
    """Run the interactive console game: Human (X) vs AI (O)."""
    board = initialize_board()
    human_player = "X"
    ai_player = "O"
    current_player = human_player  # Human starts

    while True:
        pretty_print(board)

        if current_player == human_player:
            # -------- Human turn ----------
            while True:
                try:
                    move = input("Enter your move (1‑9): ").strip()
                    pos = int(move)
                    if not 1 <= pos <= 9:
                        raise ValueError
                    row, col = divmod(pos - 1, 3)
                    if make_move(board, row, col, human_player):
                        break
                    else:
                        print("That square is already taken. Try again.")
                except ValueError:
                    print(
                        "Please enter a number from 1 to 9 corresponding to an empty square."
                    )
        else:
            # -------- AI turn ----------
            row, col = ai_move(board, ai_player, human_player)
            make_move(board, row, col, ai_player)
            print(f"AI chooses square {row * 3 + col + 1}")

        # -------- Check end of game ----------
        winner = check_winner(board)
        if winner:
            pretty_print(board)
            if winner == human_player:
                print("Congratulations – you win!")
            else:
                print("AI wins – better luck next time!")
            break

        if is_draw(board):
            pretty_print(board)
            print("It's a draw!")
            break

        # -------- Switch player ----------
        current_player = ai_player if current_player == human_player else human_player


if __name__ == "__main__":
    play_game()
