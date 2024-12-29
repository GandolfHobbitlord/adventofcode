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

print(data)
conn = defaultdict(set)
for a,b in data:
    conn[a].add(b)
    conn[b].add(a)
conn = dicts(conn)

# def BronKerbosch(R,P,X):
#     if not P and not X:
#         # print("HELLO")
#         print(R)
#         yield R
#     while P:
#         v = P.pop()
#         res_P = P & conn[v]
#         new = P | set([v])
#         res_X = X & conn[v]
#         yield from BronKerbosch(new,res_P,res_X)
#         X.add(v)

def BronKerbosch(P, R=None, X=None):
    P = set(P)
    R = set() if R is None else R
    X = set() if X is None else X
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from BronKerbosch(
            P=P.intersection(conn[v]), R=R.union([v]), X=X.intersection(conn[v]))
        X.add(v)

P = set(conn.keys())

ans = [v for v in BronKerbosch(P,R=None,X=None)]
ans.sort(key=lambda x: len(x),reverse=True)
print(','.join(sorted(ans[0])))