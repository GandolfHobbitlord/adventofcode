from pathlib import Path
import numpy as np

def parse_data(inp):
    numbers = [int(num) for num in inp[0].split(',')]
    boards = []
    for board in inp[1:]:
        boards.append(np.fromstring(board,sep=' ', dtype='int8').reshape(-1, 5))
    return boards, numbers

MARK = -1 # No negative numbers so use that to signal marked number
def mark(boards, num):
    for board in boards:
        board[board == num] = MARK

def is_winner(board):
    np.all(row == MARK) for row in board:
        if np.all(row == MARK):
            return True
    for column in board.T:
        if np.all(column == MARK):
            return True
    return False

def score(board, num):
    return np.sum(board[board != MARK])* num

def part1(data):
    boards, numbers = parse_data(data)
    for num in numbers:
        mark(boards, num)
        for board in boards:
            if is_winner(board):
                return score(board, num)

def part2(data):
    boards, numbers = parse_data(data)
    for num in numbers:
        mark(boards, num)
        keep = [board for board in boards if not is_winner(board)]
        if len(keep) == 0:
            return score(boards[0],num)
        boards = keep

with open(Path("2021") / "day4" / "day4_input.txt") as f:
    # Split so we get a list of boards (first item is the lotto numbers)
    inp = [line for line in f.read().split('\n\n')]
print(f'Answer part 1 {part1(inp)}')
print(f'Answer part 2 {part2(inp)}')