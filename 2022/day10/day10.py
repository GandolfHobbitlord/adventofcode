from pathlib import Path
import numpy as np

with open(Path("2022") / "day10" / "day10_input.txt") as f:
    data = [x for x in f.read().splitlines()]

def print_screen(arr):
    for row in arr:
        print(''.join(row))

def get_signals(data):
    X = [1]
    for line in data:
        cmd = line.split()
        X.append(X[-1])
        if cmd[0] == 'addx':
            X.append(X[-1] + int(cmd[1]))
    return X

def part1(data):
    X = get_signals(data)
    sig = [20, 60, 100, 140, 180, 220]
    print(f'Answer part 1 {sum([X[x-1]*x for x in sig])}')

def part2(data):
    X = get_signals(data)
    screen = np.full((6, 40), ' ')
    for cycle, sprite_pos in enumerate(X):
        x = cycle % 40
        y = cycle // 40
        if sprite_pos -1  <= x and x <= sprite_pos + 1:
            screen[y, x] = '#'
    print_screen(screen)

part1(data)
part2(data)