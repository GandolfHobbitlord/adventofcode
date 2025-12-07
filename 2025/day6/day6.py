from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict

def parse_line(line):
    return [int(i) for i in re.findall(r'-?\d+', line)]
def parse_last_line(line):
    return [i for i in re.findall(r'[\+\*]', line)]

with open(Path("2025") / "day6" / "day6_input.txt") as f:
# with open(Path("2025") / "day6" / "day6_test.txt") as f:
    data = [line for line in f.read().split('\n')]
numbers = np.array([parse_line(l) for l in data[:-1]])
ops = parse_last_line(data[-1])
print(numbers)
print(ops)
ans = 0
for op, col in zip(ops,numbers.T):
    print(op,col)
    if op == '+':
        ans += col.sum()
    elif op == '*':
        ans += np.prod(col,dtype=np.longlong)
    else:
        raise RuntimeError(op)
    print(ans)

print(ans)