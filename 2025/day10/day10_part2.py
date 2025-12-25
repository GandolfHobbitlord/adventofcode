from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict
import z3

def parse_line(line):
    # [int(i) for i in re.findall(r'-?\d+', line)]
    parts = line.split(" ")
    buttons = []
    for button in parts[1:-1]:
        buttons.append([int(i) for i in re.findall(r'-?\d+',button)])
    # print(buttons)
    target = [int(i) for i in re.findall(r'-?\d+',parts[-1])]
    # print(target)
    return buttons, target

with open(Path("2025") / "day10" / "day10_input.txt") as f:
# with open(Path("2025") / "day10" / "day10_test.txt") as f:
    # data = [line for line in f.read().split('\n')]
    data = [parse_line(line) for line in f.read().split('\n')]
res = 0
for buttons, target in data:
    pushes = [z3.Int(f"press{i}") for i in range(len(buttons))]
    s = z3.Optimize()
    s.add(z3.And([push >= 0 for push in pushes]))
    for pos in range(len(target)):
        s.add(z3.And(sum([pushes[i] for i, button in enumerate(buttons) if pos in button]) == target[pos]))
    s.minimize(sum(pushes))
    assert s.check() == z3.sat
    m = s.model()
    res += sum([m[push].as_long() for push in pushes])
print(res)