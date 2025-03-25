from unittest import TestCase

from queens import QueensGame, QueensColor


class TestQueens(TestCase):
    def test_every_tile_has_color_should_be_true(self):
        game = QueensGame(
            size=3,
            colors=[
                QueensColor(
                    color_code="", tiles=[(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)]
                ),
                QueensColor(color_code="", tiles=[(1, 1), (1, 2), (2, 1), (2, 2)]),
            ],
        )

        self.assertTrue(game.every_tile_has_color)

    def test_every_tile_has_color_should_be_false(self):
        game = QueensGame(
            size=3,
            colors=[
                QueensColor(
                    color_code="", tiles=[(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)]
                ),
                QueensColor(color_code="", tiles=[(1, 1), (1, 2), (2, 2)]),
            ],
        )

        self.assertFalse(game.every_tile_has_color)
