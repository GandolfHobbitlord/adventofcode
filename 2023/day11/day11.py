from pathlib import Path
import numpy as np
from itertools import combinations

with open(Path("2023") / "day11" / "day11_input.txt") as f:
# with open(Path("2023") / "day11" / "day11_test.txt") as f:
    data = np.array([list(line) for line in f.read().split('\n')])

def expand_galaxy(data,expansion = 1):
    positions = np.array(np.where(data == '#'))
    yy,xx = np.where(data == '#')
    xx = np.array(xx)
    yy = np.array(yy)

    empty_rows = [row_nr for row_nr, row in enumerate(data) if np.all(row == '.')]
    adders = np.zeros_like(yy)
    for y in empty_rows:
        adders[y<yy] += expansion
    yy += adders

    empty_cols = [row_nr for row_nr, row in enumerate(data.T) if np.all(row == '.')]
    adders = np.zeros_like(xx)
    for x in empty_cols:
        adders[x<xx] += expansion
    xx += adders
    positions = [(x,y) for x,y in zip(xx,yy)]
    return positions

def total_distance(positions):
    tot = 0
    for (x0,y0), (x1,y1) in combinations(positions,2):
        distance = abs(x0-x1) + abs(y0-y1)
        tot += distance
    return tot

p1 = total_distance(expand_galaxy(data,1))
p2 = total_distance(expand_galaxy(data,1000000-1))
print(f"Answer part 1: {p1}")
print(f"Answer part 1: {p2}")
