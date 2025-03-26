from solver import solve_game
from queens import QueensGame, QueensColor

game = QueensGame(
    size=7,
    colors=[
        QueensColor(
            color_code="#FFC993",
            tiles=[
                (0, 0),
                (1, 0),
                (0, 1),
                (1, 1),
                (1, 2),
                (1, 3),
            ],
        ),
        QueensColor(color_code="#A3CB92", tiles=[(0, 2)]),
        QueensColor(
            color_code="#AA94CD",
            tiles=[
                (0, 3),
                (0, 4),
                (1, 4),
                (0, 5),
                (1, 5),
                (2, 5),
                (0, 6),
                (1, 6),
                (2, 6),
            ],
        ),
        QueensColor(
            color_code="#FF7B60",
            tiles=[
                (2, 0),
                (3, 0),
                (4, 0),
                (5, 0),
                (6, 0),
                (4, 1),
                (5, 1),
                (6, 1),
                (4, 2),
                (5, 2),
                (6, 2),
            ],
        ),
        QueensColor(
            color_code="#A3D2D8",
            tiles=[
                (2, 1),
                (3, 1),
                (2, 2),
                (3, 2),
                (2, 3),
                (3, 3),
                (4, 3),
                (5, 3),
                (6, 3),
                (2, 4),
                (3, 4),
                (4, 4),
                (5, 4),
                (3, 5),
                (4, 5),
                (3, 6),
                (4, 6),
            ],
        ),
        QueensColor(color_code="#7899CD", tiles=[(5, 5), (6, 5), (5, 6), (6, 6)]),
        QueensColor(color_code="#DFA0BF", tiles=[(6, 4)]),
    ],
)

print(f"All colors fit on the board: {game.colors_all_fit_on_board}")
print(f"Every tile has a color: {game.every_tile_has_color}")
print(f"No colors overlap with each other: {game.has_no_overlap}")

solve_game(game)
