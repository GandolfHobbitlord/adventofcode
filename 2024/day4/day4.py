from pathlib import Path
import numpy as np
import re
from collections import Counter
from collections import defaultdict

def parse_line(line):
    # [int(i) for i in re.findall(r'-?\d+', line)]
    m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, password = m.groups()
    return int(lo), int(hi), char, password

def find_xmas(mat):
    ans = 0
    for row in mat:
        a = ''.join(x for x in row)

        ans += len([m.start() for m in re.finditer('XMAS',a)])
        ans += len([m.start() for m in re.finditer('SAMX',a)])
    return ans
with open(Path("2024") / "day4" / "day4_input.txt") as f:
# with open(Path("2024") / "day4" / "day4_test.txt") as f:
    data = [line for line in f.read().split('\n')]

data=np.array([list(i) for i in data])
# data = np.array(data)

def get_diagonals(grid, bltr = True):
  dim = len(grid)
  assert dim == len(grid[0])
  return_grid = [[] for total in range(2 * len(grid) - 1)]
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if bltr: return_grid[row + col].append(grid[col][row])
      else:    return_grid[col - row + (dim - 1)].append(grid[row][col])
  return return_grid

def part1(data):
    ans = find_xmas(data)
    ans += find_xmas(np.rot90(data,1))

    ans += find_xmas(get_diagonals(data))
    ans += find_xmas(get_diagonals(data,False))
    print(f"Answer {part1(data)}")

def part2(mat):
    h,w = mat.shape
    ans = 0
    for y in range(1,h-1):
        for x in range(1,w-1):
            if mat[y,x] != 'A':
                continue
            n = Counter([mat[y-1,x-1],mat[y-1,x+1], mat[y+1,x+1], mat[y+1,x-1]])
            if n == Counter('MMSS'):
                if mat[y-1,x-1] != mat[y+1,x+1]: #Took me way too long to figure out that this is needed
                    ans += 1
    return ans

print(part2(data))
# print(f"Answer {part1(data)}")