import numpy as np
import re
from pathlib import Path

def to_matrix(mat_raw, folds):
    points = [(int(x), int(y)) for x,y in re.findall('(\d+),(\d+)', mat_raw)]
    max_x = max([line for axis , line in folds if axis == 'x'])
    max_y = max([line for axis , line in folds if axis == 'y'])
    output = np.zeros((max_y * 2 + 1,max_x * 2 + 1), dtype=int)
    for x, y in points:
        output[y,x] = 1
    return output

def parse_data(input):
    raw_points, raw_fold = input.split('\n\n')
    folds = [(axis, int(line)) for axis, line in re.findall('fold along (\w)=(\d+)', raw_fold)]
    paper = to_matrix(raw_points, folds)
    return paper, folds

def fold_paper(paper, fold):
    axis, line = fold
    if axis == 'y':
        folded = paper[:line, :] | np.flipud(paper[line+1:, :])
        return folded
    if axis == 'x':
        folded = paper[:, :line] | np.fliplr(paper[:, line+1:])
        return folded

def print_paper(paper):
    return '\n'.join([' '.join(['#' if val == 1 else " " for val in row]) for row in paper])

def count_dots(paper):
    return np.sum(paper)

def run_tests():
    with open(Path("2021") / "day13" / "day13_test.txt") as f:
        paper, folds = parse_data(f.read())
        assert count_dots(fold_paper(paper,folds[0])) == 17
        for fold in folds:
            paper = fold_paper(paper,fold)
        ans = np.array([[1, 1, 1, 1, 1],[1, 0, 0, 0, 1],[1, 0, 0, 0, 1],[1, 0, 0, 0, 1],[1, 1, 1, 1, 1],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]])
        assert np.all(paper == ans)

run_tests()
with open(Path("2021") / "day13" / "day13_input.txt") as f:
    paper, folds = parse_data(f.read())

print(f"answer part 1 {count_dots(fold_paper(paper,folds[0]))}")

for fold in folds:
    paper = fold_paper(paper,fold)
    P= paper ==1

print(f"Answer part 2: \n{print_paper(paper)}")
