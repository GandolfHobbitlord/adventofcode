from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict
from collections import deque
def parse_line(line):
    # [int(i) for i in re.findall(r'-?\d+', line)]
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password

with open(Path("2024") / "day9" / "day9_input.txt") as f:
# with open(Path("2024") / "day9" / "day9_test.txt") as f:
    data = [int(c) for c in f.read()]
def printd(dd):
    print("".join([str(d) for d in dd]))
def calc_checksum(s):
    return sum(i*v for i,v in  enumerate(s))
vals = list(enumerate(data[::2]))
spaces = data[1::2]
q = vals.copy()
id = 0
disk = []
for i, val in enumerate(data):
    if i % 2 == 0:
        for _ in range(val):
            disk.append(id)
        id += 1
    else:
        for _ in range(val):
            disk.append('.')
printd(disk)
ids = [i for i in disk if i != '.'] # this should be a dequeu
frag = []
for i in range(len(disk)):
    if not ids:
        break
    if disk[i] != '.':
        frag.append(ids.pop(0))
    else:
        frag.append(ids.pop())


printd(frag)
print(calc_checksum(frag))
print(len(disk))
print(len(data))