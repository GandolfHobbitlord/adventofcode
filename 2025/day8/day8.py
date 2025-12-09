from pathlib import Path
import numpy as np
import re
import itertools

def parse_line(line):
    return np.array(list(int(i) for i in re.findall(r'-?\d+', line)))

with open(Path("2025") / "day8" / "day8_input.txt") as f:
# with open(Path("2025") / "day8" / "day8_test.txt") as f:
    data = [parse_line(line) for line in f.read().split('\n')]



def part1(data):
    pairs = [(np.linalg.norm(a-b,ord=2), (tuple(a.flatten()),tuple(b.flatten()))) for a,b in itertools.combinations(data,2)]
    pairs = sorted(pairs, key=lambda x: x[0])
    junctions = []
    for pair in pairs[:1000]:
        _, (a,b) = pair
        new_set = set([a,b])
        removes = []
        for junc in junctions:
            if a in junc or b in junc:
                new_set |= junc
                removes.append(junc)
        for r in removes:
            junctions.remove(r)
        junctions.append(new_set)
    return np.prod(sorted([len(j) for j in junctions],reverse=True)[:3])


def part2(data):
    pairs = [(np.linalg.norm(a-b,ord=2), (tuple(a),tuple(b))) for a,b in itertools.combinations(data,2)]
    pairs.sort()
    junctions = []
    used = set()
    for pair in pairs:
        _, (a,b) = pair
        new_set = set([a,b])
        used |= new_set
        removes = []
        for junc in junctions:
            if a in junc or b in junc:
                new_set |= junc
                removes.append(junc)
        for r in removes:
            junctions.remove(r)
        junctions.append(new_set)
        if len(used) == len(data) and len(junctions) == 1:
            return np.prod([a[0],b[0]],dtype=np.longlong)

print(f"Answer part1: {part1(data)}")
print(f"Answer part2: {part2(data)}")
