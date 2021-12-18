import numpy as np
from pathlib import Path

def to_matrix(inp):
    lines = [line for line in inp.splitlines()]
    mat=[]
    for line in lines:
        mat.append([int(char) for char in line])
    return np.array(mat)

def in_range(mat,n):
    bounds = mat.shape
    for pos, bound in zip(n,bounds):
        if pos < 0 or pos >= bound:
            return False
    return True

def get_neighbor(mat, pos):
    x,y  = pos
    neighbors = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
    for n in neighbors:
        if in_range(mat,n):
            yield n

def find_shortest_path(risk_levels):
    tot_risk = np.full(risk_levels.shape, np.inf)
    q = []
    q.append((0,0))
    tot_risk[(0,0)] = 0
    visited = set()
    finish_pos = (risk_levels.shape[0]-1 ,risk_levels.shape[1] -1)
    while finish_pos not in visited:
        vertice = q.pop()
        if vertice in visited:
            continue
        curr_risk = tot_risk[vertice]
        for neighbor in get_neighbor(risk_levels, vertice):
            new_risk = curr_risk + risk_levels[neighbor]
            if new_risk < tot_risk[neighbor]:
                tot_risk[neighbor] = new_risk
            if (neighbor not in visited):
                q.append(neighbor)
        visited.add(vertice)
        # TODO Use a heap, list is sorted each time but developer time < runtime
        q = sorted(q, key=lambda x: tot_risk[x], reverse=True)
    return tot_risk[finish_pos]

def tile(mat):
    mat = np.concatenate([mat + i for i in range(5)],axis=0)
    mat = np.concatenate([mat + i for i in range(5)],axis=1)
    mat[mat > 9] -= 9
    return mat

def run_tests():
    input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
    mat = to_matrix(input)
    assert find_shortest_path(mat) == 40
    assert find_shortest_path(tile(mat.copy())) == 315
run_tests()

def part1(dangers):
    return find_shortest_path(dangers)
def part2(dangers):
    return find_shortest_path(tile(dangers.copy()))

with open(Path("2021") / "day15" / "day15_input.txt") as f:
    dangers = to_matrix(f.read())
print(f'Total danger part 1: {part1(dangers)}')
print(f'Total danger part 2: {part2(dangers)}')