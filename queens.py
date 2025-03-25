from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class QueensColor:
    color_code: str
    tiles: List[Tuple[int, int]]


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
        pass

    @property
    def colors_all_fit_on_board(self) -> bool:
        pass


def do_tiles_overlap(
    tiles_a: List[Tuple[int, int]], tiles_b: List[Tuple[int, int]]
) -> bool:
    for tile_a in tiles_a:
        for tile_b in tiles_b:
            if tile_a[0] == tile_b[0] and tile_a[1] == tile_b[1]:
                return True
    return False
