from typing import List, Tuple, NamedTuple
from dataclasses import dataclass


class QueensTile(NamedTuple):
    col: int
    row: int


@dataclass
class QueensColor:
    color_code: str
    tiles: List[QueensTile]

    def does_color_have_tile(self, tile: QueensTile) -> bool:
        for tile_of_color in self.tiles:
            if tile == tile_of_color:
                return True
        return False


@dataclass
class QueensGame:
    size: int
    colors: List[QueensColor]

    @property
    def has_no_overlap(self) -> bool:
        for color_a in self.colors:
            for color_b in self.colors:
                if color_a != color_b and do_tiles_overlap(
                    color_a.tiles, color_b.tiles
                ):
                    return False
        return True

    @property
    def every_tile_has_color(self) -> bool:
        for tile in self.grid:
            if not any(color.does_color_have_tile(tile) for color in self.colors):
                return False
        return True

    @property
    def colors_all_fit_on_board(self) -> bool:
        for color in self.colors:
            for tile_of_color in color.tiles:
                if (
                    tile_of_color[0] >= self.size
                    or tile_of_color[0] < 0
                    or tile_of_color[1] >= self.size
                    or tile_of_color[1] < 0
                ):
                    return False
        return True

    @property
    def grid(self) -> List[QueensTile]:
        return get_grid(self.size)


def get_grid(size: int) -> List[QueensTile]:
    grid = []
    for x in range(size):
        for y in range(size):
            grid.append(QueensTile(x, y))
    return grid


def do_tiles_overlap(tiles_a: List[QueensTile], tiles_b: List[QueensTile]) -> bool:
    for tile_a in tiles_a:
        for tile_b in tiles_b:
            if tile_a == tile_b:
                return True
    return False


def get_horizontal_adjacency_pairs(n: int) -> List[Tuple[QueensTile]]:
    grid = get_grid(n)
    pairs: List[Tuple[QueensTile]] = []
    for tile in grid:
        right_tile = QueensTile(tile.col + 1, tile.row)
        if right_tile in grid:
            pairs.append((tile, right_tile))
    return pairs


def get_vertical_adjacency_pairs(n: int) -> List[Tuple[QueensTile]]:
    return []


def get_diagonal_adjacency_pairs(n: int) -> List[Tuple[QueensTile]]:
    return []
