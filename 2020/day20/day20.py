import re
from pathlib import Path
import numpy as np

def get_perms(tile):
    perms = []
    for _ in range(2):
        tile = np.fliplr(tile)
        for _ in range(4):
            tile = np.rot90(tile)
            perms.append(tile)
    return perms

def get_tile(inp):
    tile_nr = re.search(r'\d+', inp.splitlines()[0])[0]
    print(inp.splitlines()[1:])
    t = np.array([[c for c in line] for line in inp.splitlines()[1:]])
    return int(tile_nr), get_perms(t)

def parse_input(inp):
    tiles = inp.split('\n\n')
    return [get_tile(tile) for tile in tiles]

def check(tile, other):
    return (tile[0,:] == other[0,:]).all()

def get_num_of_neighbors(tile_tuple, other_tiles):
    tile_nr, tile_perms = tile_tuple
    neighbor = 0
    # print(tile)
    for other_nr,other_perms in other_tiles:
        if tile_nr == other_nr:
            continue
        for other_perm in other_perms:
            for tile in tile_perms:
                # print(other_perm)
                if check(tile, other_perm):
                    neighbor += 1
    return neighbor // 2 # will find each neighbor twice




def part1(tiles):
    corners = [nr for nr, perms in tiles if get_num_of_neighbors((nr,perms),tiles) == 2]
    print(corners)
    return  np.prod(corners,dtype=np.uint64)
        # print(nr, get_num_of_neighbors((nr,perms),tiles))


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