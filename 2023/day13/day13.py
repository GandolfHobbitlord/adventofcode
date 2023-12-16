from pathlib import Path
import numpy as np

with open(Path("2023") / "day14" / "day14_input.txt") as f:
# with open(Path("2023") / "day14" / "day14_test.txt") as f:
    data = [map for map in f.read().split('\n\n')]

def find_row_reflection(a, part1=True):
    for i in range(1,len(a)):
        ref = np.flipud(a[:i,:])
        y = min(len(ref), len(a[i:]))
        if part1:
            if np.all(a[i:(i+y),:] == ref[:y,:]):
                return i
        else:
            if np.sum(a[i:(i+y),:] != ref[:y,:]) == 1:
                return i
    return 0

row_tot = 0
col_tot = 0
for m in data:
    a = np.array([list(line)for line in m.splitlines()])
    row_tot += find_row_reflection(a)
    col_tot += find_row_reflection(a.T)

print(f'Part 1: {col_tot + row_tot*100}')

row_tot = 0
col_tot = 0
for m in data:
    a = np.array([list(line)for line in m.splitlines()])
    row_tot += find_row_reflection(a, part1 = False)
    col_tot += find_row_reflection(a.T, part1 = False)

print(f'Part 2: {col_tot + row_tot*100}')