import numpy as np
from collections import defaultdict
from pathlib import Path

DIRECTIONS = {'e' : np.array([1,0]) , 'se':np.array([0,1]), 'sw':np.array([-1,1]),
 'w':np.array([-1,0]), 'nw':np.array([0,-1]), 'ne':np.array([1,-1])}

def get_starting_black_tiles(tot_commands):
    tiles = defaultdict(int)
    for command in tot_commands:
        current_pos = np.array([0,0])
        for direction in command:
            current_pos += DIRECTIONS[direction]
        tiles[tuple(current_pos)] += 1
    return [key for key,val in tiles.items() if val % 2]

def neighbors(tile):
    for direction in DIRECTIONS.values():
        yield tuple(tile + direction)

def get_num_of_neighbors(tile, tiles):
    return len([neighbor for neighbor in neighbors(tile) if tuple(neighbor) in tiles])

def part2(tiles):
    new_tiles = set()
    # print(tiles)
    for tile in tiles:
        num_neighbors = get_num_of_neighbors(tile,tiles)
        if 0 < num_neighbors <= 2:
            new_tiles.add(tile)
        for neighbor in neighbors(tile):
            # print(neighbor)
            if tuple(neighbor) not in tiles and get_num_of_neighbors(neighbor,tiles) == 2:
                new_tiles.add(neighbor)
    # print(new_tiles)
    return list(new_tiles)

def parse_input(inp):
    total_commands = []
    for line in inp.splitlines():
        commands = []
        tmp = ''
        for char in line:
            tmp += char
            if tmp in DIRECTIONS:
                commands.append(tmp)
                tmp = ''
        total_commands.append(commands)
    return total_commands

def run_test():
    inp = 'nwwswee'
    tot_commands = parse_input(inp)
    get_starting_black_tiles(tot_commands) == [(0,0)]
    with open(Path("2020") / "day24" / "day24_test.txt") as f:
        inp = f.read()
    tot_commands = parse_input(inp)
    tiles = get_starting_black_tiles(tot_commands)
    assert len(tiles) == 10
    for _ in range(3):
        tiles = part2(tiles)
        print(len(tiles))
run_test()

with open(Path("2020") / "day24" / "day24_input.txt") as f:
    inp = f.read()
black_tiles = get_starting_black_tiles(parse_input(inp))
print(f"Answer part 1 {len(black_tiles)}")

for _ in range(100):
    black_tiles = part2(black_tiles)
    print(len(black_tiles))

