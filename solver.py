from typing import List
from pulp import LpProblem, LpVariable, LpBinary, lpSum

from queens import (
    QueensGame,
    QueensTile,
    get_horizontal_adjacency_pairs,
    get_vertical_adjacency_pairs,
    get_diagonal_adjacency_pairs,
)


def solve_game(
    game: QueensGame, queens_per_row=1, queens_per_col=1, queens_per_color=1
) -> List[QueensTile]:
    p = LpProblem("Solve Queens Game")

    board = LpVariable.dicts("board", game.grid, cat=LpBinary)

    # Each row must have exactly 1 queen
    for row in range(game.size):
        p += (
            lpSum(board[col, row] for col in range(game.size)) == queens_per_row,
            f"row_{row}_must_have_{queens_per_row}_queen",
        )

    # Each column must have exactly 1 queen
    for col in range(game.size):
        p += (
            lpSum(board[col, row] for row in range(game.size)) == queens_per_col,
            f"col_{col}_must_have_{queens_per_col}_queen",
        )

    # Each color must have exactly 1 queen
    for color in game.colors:
        p += (
            lpSum(board[tile] for tile in color.tiles) == queens_per_color,
            f"color_{color.color_code}_must_have_{queens_per_color}_queen",
        )

    # Queens cannot be adjacent (including diagonal) of each other
    # Horizontal adjacency
    for left, right in get_horizontal_adjacency_pairs(game.size):
        p += board[left] + board[right] <= 1

    # Vertical adjacency
    for top, bottom in get_vertical_adjacency_pairs(game.size):
        p += board[top] + board[bottom] <= 1

    # Diagonal adjacency
    for a, b in get_diagonal_adjacency_pairs(game.size):
        p += board[a] + board[b] <= 1

    # Solve
    p.solve()

    found_queens = []
    for tile, variable in board.items():
        if variable.varValue == 1:
            found_queens.append(tile)
    return found_queens


# adjacency
