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
run_test()

with open(Path("2020") / "day24" / "day24_input.txt") as f:
    inp = f.read()
black_tiles = get_starting_black_tiles(parse_input(inp))
print(f"Answer part 1 {len(black_tiles)}")

# part2(black_tiles)