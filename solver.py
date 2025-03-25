from pulp import LpProblem, LpVariable, lpSum

from queens import QueensGame


def solve_game(game: QueensGame):
    p = LpProblem("Solve Queens Game")
    # Each row must have exactly 1 queen
    # Each column must have exactly 1 queen
    # Each color must have exactly 1 queen
    # Queens cannot be adjacent (including diagonal) of each other
