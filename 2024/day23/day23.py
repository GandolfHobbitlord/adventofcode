from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict

def parse_line(line):
    m = re.match(r'(\w+)-(\w+)', line)
    a,b = m.groups()
    return a,b

with open(Path("2024") / "day23" / "day23_input.txt") as f:
# with open(Path("2024") / "day23" / "day23_test.txt") as f:
    # data = [line for line in f.read().split('\n')]
    data = [parse_line(line) for line in f.read().split('\n')]

conn = defaultdict(set)
for a,b in data:
    conn[a].add(b)
    conn[b].add(a)

conn = dict(conn)
clique_3 = set()
for v0, edge0 in conn.items():
    for v1, edge1 in conn.items():
        if v1 in edge0:
            common = edge0 & edge1
            for c in common:
                clique_3.add(frozenset((v0,v1,c)))
# print(len(clique_3))
ts = []
for c in clique_3:
    if any([node.startswith('t') for node in c]):
        ts.append(c)
print(len(ts))
