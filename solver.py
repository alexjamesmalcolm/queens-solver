from pulp import LpProblem, LpVariable, LpBinary

from queens import QueensGame


def solve_game(game: QueensGame):
    p = LpProblem("Solve Queens Game")

    board = LpVariable.dicts("board", game.grid, cat=LpBinary)

    # Each row must have exactly 1 queen
    for row in range(game.size):
        pass

    # Each column must have exactly 1 queen
    for col in range(game.size):
        pass

    # Each color must have exactly 1 queen

    # Queens cannot be adjacent (including diagonal) of each other
