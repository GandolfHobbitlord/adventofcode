from pathlib import Path
import re
import numpy as np
from collections import defaultdict

def to_dict(line):
    _, games = line.split(':')
    game_dict = defaultdict(int)
    for val, col in re.findall(r'(\d+) (\w+)', games):
        if game_dict[col] < int(val):
            game_dict[col] = int(val)
    return game_dict

def part2(data):
    ans = 0
    for game in data:
        ans += np.prod(list(game.values()))
    return ans

def part1(data):
    ans = 0
    for i, game in enumerate(data,1):
        if game['red'] <= 12 and game['green'] <= 13 and game['blue'] <= 14:
            ans += i
    return ans

with open(Path("2023") / "day2" / "day2_input.txt") as f:
    data = [to_dict(x) for x in f.read().splitlines()]

print(f'Answer part 1: {part1(data)}')
print(f'Answer part 2: {part2(data)}')
