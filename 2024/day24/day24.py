from pathlib import Path
import re
from collections import defaultdict
import graphviz

def parse_wires(wirs):
    wires = {}
    for w in wirs.splitlines():
        print(w)
        name, val = w.split(':')
        wires[name] = int(val)
    return wires

def parse_gate(line):
    m = re.match(r'([a-zA-Z0-9]+) (\w+) ([a-zA-Z0-9]+) -> ([a-zA-Z0-9]+)', line)
    return m.groups()

with open(Path("2024") / "day24" / "day24_input.txt") as f:
# with open(Path("2024") / "day24" / "day24_test.txt") as f:
    wires, gates =  f.read().split('\n\n')
    wires = parse_wires(wires)
    gates = [parse_gate(g) for g in gates.splitlines()]

def run_simulation(wires,g_in):
    gates = g_in.copy()
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
    ans = 0
    for w, val in wires.items():
        if w.startswith('z'):
            ans +=  val << int(w[1:])
    return ans

#Just visually looked for errors...
def show_as_pretty_dot(gates):
    ops = defaultdict(list)
    edges = []
    for g0, op, g1, out in gates:
        ops[op].append(out)
        edges.append((g0,out))
        edges.append((g1,out))

    dot = graphviz.Digraph()
    for n in ops["AND"]:
        dot.node(n,style='filled',color='lightblue')
    for n in ops["OR"]:
        dot.node(n,style='filled',color='green')
    for n in ops["XOR"]:
        dot.node(n,style='filled',color='red')
    dot.edges(edges)
    dot.render('graph', view=True)

print(f'Part 1: {run_simulation(wires,gates)}')
show_as_pretty_dot(gates)

