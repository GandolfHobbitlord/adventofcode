from pathlib import Path
from collections import Counter
from collections import defaultdict
import re
import numpy as np

def parse_line(line):
    m = re.findall(r'(\d)', line)
    return [int(x) for x in m]
def see_trees(arr):

    count = 0
    curr_largest = -1
    visible = np.zeros(arr.shape)
    for i, val in enumerate(arr):
        if val > curr_largest:
            visible[i] = 1
            curr_largest = val
        else:
            continue
    curr_largest = -1
    for i, val in enumerate(np.flip(arr),):
        if val > curr_largest:
            visible[len(visible)-1-i] = 1
            curr_largest = val
        else:
            continue
    return visible
with open(Path("2022") / "day8" / "day8_input.txt") as f:
    data = np.array([parse_line(x) for x in f.read().splitlines()])
tot_trees = 0
row_list = []
col_list = []

for row in data:
    row_list.append(see_trees(row))
for col in data.T:
    col_list.append(see_trees(col))
a1 = np.array(row_list)
a2 = np.array(col_list).T
print(a1)
a3 = np.logical_or(a1 ==1 , a2 == 1)
print(np.sum(a3))
print(a3)