from pathlib import Path
import numpy as np
import re
from itertools import combinations
def parse_line(line):
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password

with open(Path("2023") / "day11" / "day11_input.txt") as f:
# with open(Path("2023") / "day11" / "day11_test.txt") as f:
    data = np.array([list(line) for line in f.read().split('\n')])

def expand_rows(data):
    tmp = []
    for row in data:
        tmp.append(row.copy())
        if np.all(row == '.'):
            tmp.append(row.copy())
    return np.vstack(tmp)

data = expand_rows(data)
data = expand_rows(data.T).T

rows, cols = np.where(data == '#')
positions = [(x,y) for y,x in zip(rows,cols)]

ans = 0
for (x0,y0), (x1,y1) in combinations(positions,2):
    distance = abs(x0-x1) + abs(y0-y1)
    ans += distance
print(ans)