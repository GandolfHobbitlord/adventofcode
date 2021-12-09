import numpy as np
from pathlib import Path
from skimage.segmentation import flood_fill

def parse_line(line):
    return [int(char) for char in line]

def data_to_np_array(data):
    mat = np.array([parse_line(line)for line in data.splitlines()])
    return np.pad(mat, 1, mode='constant', constant_values=9)

def score1(lowests):
    return sum(num +1 for num in lowests)

def score2(flood_areas):
    return np.prod(sorted(flood_areas)[-3:])

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
    lowests = []
    points = []
    colmuns, rows = X.shape
    for col in range(1,colmuns):
        for row in range(1,rows):
            if is_lowest(X,col,row):
                lowests.append(X[col,row])
                points.append((col,row)) #remove padding
    return lowests, points

def get_flooded_area(X, flood_point):
    basin_map = (X == 9).astype(int)
    flooded = flood_fill(basin_map, flood_point, 2, connectivity=1)
    return np.sum(flooded == 2)

def part1(X):
    return score1(get_lowpoints(X)[0])
def part2(X):
    _, points = get_lowpoints(X)
    flood_areas = [get_flooded_area(X, point) for point in points]
    return score2(flood_areas)

def run_tests():
    inp = """2199943210
3987894921
9856789892
8767896789
9899965678"""
    X = data_to_np_array(inp)
    lowests, points = get_lowpoints(X)
    assert score1(lowests) == 15
    assert part2(X) == 1134
run_tests()

with open(Path("2021") / "day9" / "day9_input.txt") as f:
   X = data_to_np_array(f.read())

run_tests()

print(f"Answer part 1 {part1(X)}")
print(f"Answer part 2 {part2(X)}")
