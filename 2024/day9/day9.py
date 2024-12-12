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

# with open(Path("2024") / "day9" / "day9_input.txt") as f:
with open(Path("2024") / "day9" / "day9_test.txt") as f:
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

def part1(disk):
    ids = [i for i in disk if i != '.'] # this should be a dequeu
    frag = []
    for i in range(len(disk)):
        if not ids:
            break
        if disk[i] != '.':
            frag.append(ids.pop(0))
        else:
            frag.append(ids.pop())

    return calc_checksum(frag)


def get_empty_spaces(x):
    i = 0
    while x[i] == '.':
        i += 1
    return i
ids = [i for i in disk if i != '.'] # this should be a dequeu
print(ids)
# count = sorted(Counter(ids).items(),reverse=True) # There must be a better
# frag = []
q = ids
print(count)
lfrag = data.copy()
rfrag = data.copy()

for i in range(len(disk)):
    if disk[i] != '.':
        frag.append(ids.pop(0))
    else:
        spaces = get_empty_spaces(disk[i:])

        test_id = q[-1]
        if q.count(test_id) < 0:
            frag.append()
        elif q.count(test_id) <= spaces:
            for j in range(q.count(test_id)):
                q.remove(test_id)
                frag.append(test_id)
            break

    i = len(frag)
# print(part1(disk))

