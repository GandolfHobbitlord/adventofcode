import re
from pathlib import Path
import numpy as np

class Tile():
    def __init__(self,tile,nr):
        self.tile = tile.copy()
        self.nr = nr
    @property
    def up(self):
        return self.tile[0,:]
    @property
    def left(self):
        return self.tile[:,0]
    @property
    def down(self):
        return self.tile[-1,:]
    @property
    def right(self):
        return self.tile[:,-1]
    def edges(self):
        return [self.right, self.left, self.up, self.down]

def rotate(tile):
    return Tile(np.rot90(tile),tile.nr)

def fliplr(tile):
    return Tile(np.fliplr(tile),tile.nr)

def get_tile(inp):
    tile_nr = re.search(r'\d+', inp.splitlines()[0])[0]
    print(inp.splitlines()[1:])
    t = np.array([[c for c in line] for line in inp.splitlines()[1:]])
    return Tile(t, int(tile_nr))

def parse_input(inp):
    tiles = inp.split('\n\n')
    return [get_tile(tile) for tile in tiles]

def are_neighbors(tile,other):
    if tile.nr == other.nr:
        raise RuntimeError("Neighbors are same tile")

    for edge in tile.edges():
        for other_edge in other.edges():
            if (edge == other_edge).all() or (np.flipud(edge) == other_edge).all() :
                return True
    return False

def get_neighbors(tile, other_tiles):
    neighbors = []
    for other in other_tiles:
        if tile.nr == other.nr:
            continue
        if are_neighbors(tile, other):
            neighbors.append(other)
    # print(neighbors)
    return neighbors




def part1(tiles):
    corners = [tile.nr for tile in tiles if len(get_neighbors(tile,tiles)) == 2]
    print(corners)
    return  np.prod(corners,dtype=np.uint64)


def run_test():
    with open(Path("2020") / "day20" / "day20_test.txt") as f:
        inp = f.read()
    tiles = parse_input(inp)
    assert part1(tiles) == 20899048083289

run_test()

with open(Path("2020") / "day20" / "day20_input.txt") as f:
    inp = f.read()

tiles = parse_input(inp)
print(part1(tiles))
print(part2(tiles))