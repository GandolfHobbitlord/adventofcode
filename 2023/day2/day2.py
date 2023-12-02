from pathlib import Path
import re
from collections import defaultdict
def to_dict(line):
    _, games = line.split(':')
    game_dict = defaultdict(int)
    games = games.split(';')
    for game in games:
        for val, col in re.findall(r'(\d+) (\w+)', game):
            if game_dict[col] < int(val):
                game_dict[col] = int(val)
    return game_dict




with open(Path("2023") / "day2" / "day2_input.txt") as f:
    data = [to_dict(x) for x in f.read().splitlines()]
    ok = []
    for i, game in enumerate(data,1):
        if game['red'] <= 12 and game['green'] <= 13 and game['blue'] <= 14:
            ok.append(i)

    print(sum(ok))
