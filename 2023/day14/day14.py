from pathlib import Path
import numpy as np
import re

def parse_line(line):
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password

with open(Path("2023") / "day14" / "day14_input.txt") as f:
# with open(Path("2023") / "day14" / "day14_test.txt") as f:
    data = [map for map in f.read().split('\n\n')]
    # data = [parse_line(line) for line in f.read().split('\n')]

def find_row_reflection(a):
    for i in range(1,len(a)):
        # print(i)
        ref = np.flipud(a[:i,:])
        y = min(len(ref), len(a[i:]))
        if np.all(a[i:(i+y),:] == ref[:y,:]):
            print(f'found reflection at line {i}')
            return i
    return 0
row_tot = 0
col_tot = 0
for m in data:
    a = np.array([list(line)for line in m.splitlines()])
    print(a)
    print("Rows")
    row_tot += find_row_reflection(a)
    print("Cols")
    col_tot += find_row_reflection(a.T)
print(row_tot,col_tot)
print(f'{col_tot + row_tot*100}')
# print(data)