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
    next_arr = np.copy(X)
    while True:
        for i in range(1,orig_shape[0]+1):
            for j in range(1,orig_shape[1]+1):
                next_arr[i,j] = seat_state[X[i,j]](X[i-1:i+2,j-1:j+2])
        # print(X)
        if (X==next_arr).all():
            return next_arr
        else:
            X = next_arr.copy()

# Horibleness starts here
def get_part2_seat(X,i,j):
    if X[i,j] == '.':
        return '.'
    i_max, j_max = X.shape
    seated = 0
    for di in (-1,0,1):
        for dj in (-1,0,1):
            if (di == 0 and dj == 0): # Danger danger, dont be an idiot next time
                continue
            ii = di+i
            jj = dj+j
            while 0 <= ii < i_max and 0 <= jj < j_max:
                if(X[ii,jj] == '#'):
                    seated +=1
                    break
                elif(X[ii,jj] == 'L'):
                    break

                ii += di
                jj += dj

    if X[i,j] == 'L':
        if seated == 0:
            return '#'
        else:
            return 'L'
    if X[i,j] == '#':
        if seated >= 5:
            return 'L'
        else:
            return '#'
    raise RuntimeError('Missed logic')


def part2(X):
    next_arr = np.copy(X)
    while True:
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                next_arr[i,j] = get_part2_seat(X,i,j)
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
    print(x)
    assert 37 == (part1(x) == '#').sum()
    assert 26 == (part2(x) == '#').sum()

run_test()

with open(Path("2020") / "day11" / "day11_input.txt") as f:
   inp = np.array([[char for char in line ]for line in f.read().splitlines()])
   print(f"Part 1: {(part1(inp) == '#').sum()}")
   print(f"Part 2: {(part2(inp) == '#').sum()}")