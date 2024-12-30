from pathlib import Path
import re
from collections import defaultdict

def parse_line(line):
    m = re.match(r'(\w+)-(\w+)', line)
    a,b = m.groups()
    return a,b

with open(Path("2024") / "day23" / "day23_input.txt") as f:
# with open(Path("2024") / "day23" / "day23_test.txt") as f:
    # data = [line for line in f.read().split('\n')]
    data = [parse_line(line) for line in f.read().split('\n')]

def BronKerbosch(R,P,X):
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from BronKerbosch(R=R | set([v]), P=P & conn[v], X=X & conn[v])
        X.add(v)

conn = defaultdict(set)
for a,b in data:
    conn[a].add(b)
    conn[b].add(a)
conn = dict(conn)

P = set(conn.keys())
ans = [v for v in BronKerbosch(R=set(),P=P,X=set())]

ans.sort(key=lambda x: len(x))
print(','.join(sorted(ans[-1])))