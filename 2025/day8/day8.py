from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict
import itertools

def parse_line(line):
    print(line)
    return np.array(list(int(i) for i in re.findall(r'-?\d+', line)))

with open(Path("2025") / "day8" / "day8_input.txt") as f:
# with open(Path("2025") / "day8" / "day8_test.txt") as f:
    data = [parse_line(line) for line in f.read().split('\n')]

print(data)
pairs = [(np.linalg.norm(a-b,ord=2), (tuple(a.flatten()),tuple(b.flatten()))) for a,b in itertools.combinations(data,2)]
pairs = sorted(pairs, key=lambda x: x[0])
# pairs = [p.flatten() for p in pairs]
junctions = []
for pair in pairs[:1000]:
    _, (a,b) = pair
    new_set = set([a,b])
    print(new_set)
    removes = []
    for i, junc in enumerate(junctions):
        if a in junc or b in junc:
            new_set |= junc
            removes.append(junc)
    for r in removes:
        junctions.remove(r)
    junctions.append(new_set)
    print(junctions)

print(np.prod(sorted([len(j) for j in junctions],reverse=True)[:3]))