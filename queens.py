from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class QueensColor:
    color_code: str
    tiles: List[Tuple[int, int]]

    def does_color_have_tile(self, tile: Tuple[int, int]) -> bool:
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
                if do_tiles_overlap(color_a.tiles, color_b.tiles):
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
    def grid(self) -> List[Tuple[int, int]]:
        return get_grid(self.size)


def get_grid(size: int) -> List[Tuple[int, int]]:
    grid = []
    for x in range(size):
        for y in range(size):
            grid.append((x, y))
    return grid


def do_tiles_overlap(
    tiles_a: List[Tuple[int, int]], tiles_b: List[Tuple[int, int]]
) -> bool:
    for tile_a in tiles_a:
        for tile_b in tiles_b:
            if tile_a == tile_b:
                return True
    return False
