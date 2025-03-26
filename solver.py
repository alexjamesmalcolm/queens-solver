from pulp import LpProblem, LpVariable, LpBinary, lpSum

from queens import QueensGame


def solve_game(game: QueensGame, QUEENS_PER_ROW=1, QUEENS_PER_COL=1):
    p = LpProblem("Solve Queens Game")

    board = LpVariable.dicts("board", game.grid, cat=LpBinary)

    # Each row must have exactly 1 queen
    for row in range(game.size):
        p += lpSum(board[col, row] for col in range(game.size)) == 1, f""

    # Each column must have exactly 1 queen
    for col in range(game.size):
        p += lpSum(board[col, row] for row in range(game.size)) == 1, f""

    # Each color must have exactly 1 queen

    # Queens cannot be adjacent (including diagonal) of each other
