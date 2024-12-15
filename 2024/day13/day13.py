from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict

def parse_board(board):
    board = board.splitlines()
    top = [int(i) for i in re.findall(r'-?\d+', board[0])]
    bottom = [int(i) for i in re.findall(r'-?\d+', board[1])]
    b = np.array([int(i) for i in re.findall(r'-?\d+', board[2])])

    A = np.array((top,bottom)).T
    return A,b

with open(Path("2024") / "day13" / "day13_input.txt") as f:
# with open(Path("2024") / "day13" / "day13_test.txt") as f:
    data = [board for board in f.read().split('\n\n')]

def part1(data):
    boards = [parse_board(b) for b in data]
    solves = [np.linalg.solve(A,b) for A, b in boards]
    pruned = [solve.astype(np.int16) for solve in solves if np.all(np.isclose(solve,np.round(solve)))]
    print(sum([np.dot((3,1),s) for s in pruned]))

# part1(data)
part1(data)