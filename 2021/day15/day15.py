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

def create_graph(mat):
    distances = np.full(mat.shape, np.inf)
    q = []
    q.append((0,0))
    distances[(0,0)] = 0
    visited = set()
    while q:
        vertice = q.pop()
        if vertice in visited:
            continue
        curr_dist = distances[vertice]
        for neigh_pos in get_neighbor(mat,vertice):
            new_distance = curr_dist + mat[neigh_pos]
            if new_distance < distances[neigh_pos]:
                distances[neigh_pos] = new_distance
        for neighbor in get_neighbor(mat,vertice):
            if (neighbor not in visited):
                q.append(neighbor)
        visited.add(vertice)
        q = sorted(q, key=lambda x: distances[x], reverse=True)
    # print(distances)
    return distances[-1,-1]

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
    assert create_graph(mat) == 40
    assert create_graph(tile(mat.copy())) == 315
    a = np.ones((1,1)) *8
    print(a)
    print(tile(a))
run_tests()

with open(Path("2021") / "day15" / "day15_input.txt") as f:
    dangers = to_matrix(f.read())
    print(create_graph(dangers))
    print(create_graph(tile(dangers.copy())))
