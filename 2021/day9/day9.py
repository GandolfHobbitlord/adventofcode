import numpy as np
from pathlib import Path
from skimage.segmentation import flood_fill
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
    points = []
    X = np.pad(X,1,mode='constant',constant_values=10)
    Y = np.zeros(size)
    for i in range(1,size[0]+1):
        for j in range(1,size[1]+1):
            if is_lowest(X,i,j):
                lowests.append(X[i,j])
                points.append((i-1,j-1)) #remove padding
    return lowests, points
#TODO cleanup
def part2(X):
    _, points = get_lowpoints(X)
    tot_flooded = []
    for point in points:
        basin_map = (X == 9).astype(int)
        flooded = flood_fill(basin_map,point,2,connectivity=1)
        tot_flooded.append(np.sum(flooded == 2))
    return (np.prod(sorted(tot_flooded)[-3:])) #Select 3 largest and product_sum

def score(lowests):
    return sum(num +1 for num in lowests)

def run_tests():
    inp = """2199943210
3987894921
9856789892
8767896789
9899965678"""
    X = data_to_np_array(inp)
    lowests, points = get_lowpoints(X)
    assert part2(X) == 1134
    assert 15 == score(lowests)
run_tests()

def part1(X):
    return score(get_lowpoints(X)[0])

with open(Path("2021") / "day9" / "day9_input.txt") as f:
   X = data_to_np_array(f.read())
run_tests()
print(part1(X))
print(part2(X))
