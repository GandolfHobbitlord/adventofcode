from pathlib import Path
import numpy as np
import re

def parse_board(board,shift):
    board = board.splitlines()
    top = [int(i) for i in re.findall(r'-?\d+', board[0])]
    bottom = [int(i) for i in re.findall(r'-?\d+', board[1])]
    b = np.array([int(i) + shift for i in re.findall(r'-?\d+', board[2])])
    A = np.array((top,bottom)).T
    return A,b

with open(Path("2024") / "day13" / "day13_input.txt") as f:
# with open(Path("2024") / "day13" / "day13_test.txt") as f:
    data = [board for board in f.read().split('\n\n')]

def solve(data,shift = 0):
    boards = [parse_board(b,shift) for b in data]
    solves = [np.linalg.solve(A,b) for A, b in boards]
    pruned = [solve for solve in solves if np.all(np.isclose(solve,np.round(solve),atol=0.01,rtol=0))]
    return round(sum([np.dot((3,1),s) for s in pruned]))

print(f'Answer part1: {solve(data)}')
print(f'Answer part2: {solve(data,shift=10000000000000)}')