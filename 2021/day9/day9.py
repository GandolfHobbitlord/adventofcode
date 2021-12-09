import numpy as np
from pathlib import Path
from skimage.segmentation import flood, flood_fill
def parse_line(line):
    return [int(char) for char in line]

def data_to_np_array(data):
    return np.array([parse_line(line)for line in data.splitlines()])

def is_lowest(X,i,j):
    val = X[i,j]
    for ii in [i-1,i+1]:
        if X[ii,j] <= val:
            return False
    for jj in [j-1,j+1]:
        if X[i,jj] <= val:
            return False
    return True
def get_lowpoints(X):
    size = X.shape
    lowests = []
    X = np.pad(X,1,mode='constant',constant_values=10)
    Y = np.zeros(size)
    print(X)
    for i in range(1,size[0]+1):
        for j in range(1,size[1]+1):
            if is_lowest(X,i,j):
                print(X[i,j], (i,j))
                lowests.append(X[i,j])
    return lowests

    print(Y)
def score(lowests):
    return sum(num +1 for num in lowests)
def run_tests():
    inp = """2199943210
3987894921
9856789892
8767896789
9899965678"""
    X = data_to_np_array(inp)
    lowests = get_lowpoints(X)
    assert 15 == score(lowests)
run_tests()

def part1(X):
    return score(get_lowpoints(X))

with open(Path("2021") / "day9" / "day9_input.txt") as f:
   X = data_to_np_array(f.read())
print(part1(X))
# run_tests()
