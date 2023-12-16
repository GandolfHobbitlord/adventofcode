from pathlib import Path
import numpy as np
import re

def parse_line(line):
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password

# with open(Path("2023") / "day14" / "day14_input.txt") as f:
with open(Path("2023") / "day14" / "day14_test.txt") as f:
    data = [list(line) for line in f.read().split('\n')]
    # data = [parse_line(line) for line in f.read().split('\n')]

# print(data)
def move_north(data):
    data = np.array(data)
    moved = np.zeros_like(data,dtype='str')
    moved[:] = '.'
    latest_filled = [0] * len(data[0,:])
    for i,line in enumerate(data):
        for j, _ in enumerate(line):
            if data[i,j] =='O':
                potential_pos = latest_filled[j]
                while moved[potential_pos,j] != '.':
                    potential_pos += 1
                moved[potential_pos,j] = 'O'
            if data[i,j] == '#':
                moved[i,j] = '#'
                latest_filled[j] = i
    return moved

def calc_load(data):
    load = 0
    m = len(data)
    for row_nr, row in enumerate(data):
        stones = np.sum(row == 'O')
        # print(stones)
        load += (m-row_nr) * stones
    return load
moved_data = move_north(data)
print(calc_load(moved_data))
def cycle(data):
    m = data.copy()
    for _ in range(4):
        m = np.rot90(move_north(m),3)
    print(m)
    return m
# for i in range(2):

# print(moved_data)
# print('------')
# print(moved)