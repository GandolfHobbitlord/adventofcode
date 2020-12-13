import numpy as np
from pathlib import Path

def occupied_seat(window):
    if (window == '#').sum() > 4:
        return 'L'
    else:
        return '#'

def empty_seat(window):
    if ((window == '#').sum() == 0):
        return '#'
    else:
        return 'L'

def floor(window):
    return '.'

seat_state = {
    '.' : floor,
    '#' : occupied_seat,
    'L' : empty_seat
}


def part1(x):
    orig_shape = x.shape
    X = np.pad(x,((1,1),(1,1)),'constant', constant_values=('.'))
    next_arr = np.zeros(X.shape,dtype=str)
    while True:
        next_arr = np.copy(X)
        for i in range(1,orig_shape[0]+1):
            for j in range(1,orig_shape[1]+1):
                next_arr[i,j] = seat_state[X[i,j]](X[i-1:i+2,j-1:j+2])
        # print(X)
        if (X==next_arr).all():
            return next_arr
        else:
            X = next_arr.copy()

def empty_seat2(X,i,j):
    f
seat_state2 = {
    '.': floor,
    '#': empty_seat2,
    'L': occupied_seat2
}

def get_part2_seat(X,i,j):
    ii, jj = X.shape




def part2(x):
    orig_shape = x.shape
    X = np.pad(x,((1,1),(1,1)),'constant', constant_values=('.'))
    next_arr = np.zeros(X.shape,dtype=str)
    while True:
        next_arr = np.copy(X)
        for i in range(1,orig_shape[0]+1):
            for j in range(1,orig_shape[1]+1):
                next_arr[i,j] = get_part2_seat(X,i,j)
        # print(X)
        if (X==next_arr).all():
            return next_arr
        else:
            X = next_arr.copy()

def run_test():
    inp = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""
    x = np.array([[char for char in l ]for l in inp.splitlines()])
    # print(x)
    assert 37 == (part1(x) == '#').sum()

run_test()

with open(Path("2020") / "day11" / "day11_input.txt") as f:
    inp = np.array([[char for char in line ]for line in f.read().splitlines()])
    print(f"Part 1: {(part1(inp) == '#').sum()}")