from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict

def parse_line(line):
    # [int(i) for i in re.findall(r'-?\d+', line)]
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password

def parse_presents(presents):
    ps = []
    for present in presents:
        ps.append(np.array([list(line) for line in present.splitlines()[1:]]))
    return ps

def parse_trees(trees):
    res = []
    for tree in trees.splitlines():
        l, r = tree.split(":")
        area = [int(i) for i in re.findall(r'-?\d+', l)]
        packages = [int(i) for i in re.findall(r'-?\d+', r)]
        res.append((area,packages))
    return res
with open(Path("2025") / "day12" / "day12_input.txt") as f:
# with open(Path("2025") / "day12" / "day12_test.txt") as f:
    data = [line for line in f.read().split('\n\n')]


presents = parse_presents(data[:-1])
num_squares = [np.sum(p=='#') for p in presents]
package_area = [np.prod(p.shape) for p in presents]
trees = parse_trees(data[-1])
res = 0
for area, packages in trees: #No tesselation required :O
    space = area[0]*area[1]
    tot_squares = sum([pack * squares for pack, squares in zip(packages,num_squares)])
    worst_case = sum([pack * squares for pack, squares in zip(packages,package_area)])
    if tot_squares >= space:
        continue
    elif worst_case <= space:
        res += 1
        continue
    else:
        raise RuntimeError("OH NO")
print(f"Answer part 1: {res}")