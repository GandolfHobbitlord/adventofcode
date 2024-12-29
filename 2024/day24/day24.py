from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict


def parse_wires(wirs):
    wires = {}
    for w in wirs.splitlines():
        print(w)
        name, val = w.split(':')
        wires[name] = int(val)
    return wires

def parse_gate(line):
    # [int(i) for i in re.findall(r'-?\d+', line)]
    m = re.match(r'([a-zA-Z0-9]+) (\w+) ([a-zA-Z0-9]+) -> ([a-zA-Z0-9]+)', line)
    return m.groups()
    g0, op, g1, out = m.groups()

with open(Path("2024") / "day24" / "day24_input.txt") as f:
# with open(Path("2024") / "day24" / "day24_test.txt") as f:
    wires, gates =  f.read().split('\n\n')
    wires = parse_wires(wires)
    gates = [parse_gate(g) for g in gates.splitlines()]
    # data = [parse_line(line) for line in f.read().split('\n')]


while gates:
    g0, op, g1, out = gates.pop(0)
    if g0 not in wires or g1 not in wires:
        gates.append((g0, op, g1, out))
        continue
    val0 = wires[g0]
    val1 = wires[g1]
    if op == "AND":
        res = val0 & val1
    elif op == 'OR':
        res = val0 | val1
    elif op == 'XOR':
        res = val0 ^ val1
    else:
        raise RuntimeError("UH OH")
    wires[out] = res
print(wires)
ans = 0
for w, val in wires.items():
    if w.startswith('z'):
        # print(z)
        ans +=  val << int(w[1:])

print(ans)