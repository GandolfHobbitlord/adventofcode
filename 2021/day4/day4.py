from pathlib import Path
import numpy as np

MARK = -1 # No negative numbers so use that as marked
def mark(num, boards):
    for board in boards:
        board[board == num] = MARK

def run_tests():
    with open(Path("2021") / "day4" / "day4_input.txt") as f:
        inp = [line for line in f.read().split('\n\n')]
    # print(numbers)
    numbers = [int(num) for num in inp[0].split(',')]
    boards = []
    for board in inp[1:]:
        boards.append(np.fromstring(board,sep=' ', dtype='int8').reshape(-1, 5))
        print(boards[-1])
        print('\n')

    for num in numbers:
        print(num)
        mark(num, boards)
        for board in boards:
            if winner(board):
                print("Winner")
                print(board)
                score(board, num)
                exit()

def score(board, num):
    print(np.sum(board[board != MARK])* num)

def winner(board):
    for row in board:
        if np.all(row ==  MARK):
            return True

    for column in board.T:
        if np.all(column ==  MARK):
            return True
run_tests()