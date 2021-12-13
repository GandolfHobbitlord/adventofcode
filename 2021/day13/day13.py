import numpy as np
import re
from pathlib import Path
def to_matrix(mat_raw):
    points = re.findall('(\d+),(\d+)', mat_raw)
    points = [(int(x), int(y)) for x,y in points]
    max_x = max([x for x,_ in points])
    max_y = max([y for _,y in points])
    # FIX ME Should look at size of folds to determine matrix. max_x + 1 worked for test but not for input
    mat = np.zeros((895,max_x+1), dtype=int)
    for x, y in points:
        mat[y,x] = 1
    return mat

def parse_data(input):
    raw_points, raw_fold = input.split('\n\n')
    folds = re.findall('fold along (\w)=(\d+)', raw_fold)
    mat = to_matrix(raw_points)
    return mat, folds

def fold_paper(paper, fold):
    print(paper.shape)
    axis, line = fold
    line = int(line)
    if axis == 'y':
        flippy = np.flipud(paper[line+1:,:])
        folded = paper[: line, :] | flippy
        return folded
    if axis == 'x':
        flippy = np.fliplr(paper[:,line+1:])
        folded = paper[:,:line] | flippy
        return folded

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

# run_tests()
with open(Path("2021") / "day13" / "day13_input.txt") as f:
    paper, folds = parse_data(f.read())
# print(f"answer part 1 {count_dots(fold_paper(paper,folds[0]))}")
for fold in folds:
    paper = fold_paper(paper,fold)
    P= paper ==1

print('\n'.join([' '.join(['#' if val == 1 else "." for val in row]) for row in
    paper]))
