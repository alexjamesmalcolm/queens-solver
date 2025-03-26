from pulp import LpProblem, LpVariable, LpBinary, lpSum

from queens import QueensGame


def solve_game(game: QueensGame, queens_per_row=1, queens_per_col=1):
    p = LpProblem("Solve Queens Game")

    board = LpVariable.dicts("board", game.grid, cat=LpBinary)

    # Each row must have exactly 1 queen
    for row in range(game.size):
        p += (
            lpSum(board[col, row] for col in range(game.size)) == 1,
            f"row_{row}_must_have_{queens_per_row}_queen",
        )

    # Each column must have exactly 1 queen
    for col in range(game.size):
        p += (
            lpSum(board[col, row] for row in range(game.size)) == 1,
            f"col_{col}_must_have_{queens_per_col}_queen",
        )

    # Each color must have exactly 1 queen

    # Queens cannot be adjacent (including diagonal) of each other
    print(p)
