from pathlib import Path
import numpy as np
import re
from collections import defaultdict
import heapq
def parse_line(line):
    return [int(i) for i in re.findall(r'-?\d+', line)]


def in_range(mat,n):
    bounds = mat.shape
    for pos, bound in zip(n,bounds):
        if pos < 0 or pos >= bound:
            return False
    return True

#pos is (x,y) return is (x,y)
def get_neighbor(mat, pos):
    x,y  = pos
    neighbors = [(y-1,x), (y+1,x), (y,x-1), (y,x+1)]
    for n in neighbors:
        if in_range(mat,n):
            yield n[1], n[0]
def print_path(data,visited):
    m = data.copy()
    for x,y in visited:
        m[y,x] = 'X'
    print(m)

def djikstra(data,start,stop):
    q =[]
    score_dict = defaultdict(lambda: 1e12)
    # q = (steps, pos,dir)
    visited = set()
    q.append((0,start))
    heapq.heapify(q)
    while q:
        score,pos = heapq.heappop(q)
        if score > score_dict[(pos)] or pos in visited:
            continue
        score_dict[(pos)] = score

        if pos == stop:
            return score
        visited.add(pos)

        for nx,ny in get_neighbor(data,pos):
            if data[ny][nx] != '#':
                    s = (score+1 ,(nx,ny))
                    heapq.heappush(q,s)

with open(Path("2024") / "day18" / "day18_input.txt") as f:
# with open(Path("2024") / "day18" / "day18_test.txt") as f:
    corrupt = [parse_line(line) for line in f.read().split('\n')]

def part1(corrupt):
    size = 71
    data = np.zeros((size,size),dtype=str)
    data[:] = '.'
    for x,y in corrupt[:1024]:
        data[y][x]='#'
    print(data)
    res = djikstra(data,(0,0),(70,70))
    return res

#Should do binary search and only add one point each time but I'm lazy
def part2(corrupt):
    i = 1024
    while True:
        size = 71
        data = np.zeros((size,size),dtype=str)
        data[:] = '.'
        for x,y in corrupt[:i]:
            data[y][x]='#'
        res = djikstra(data,(0,0),(70,70))
        if res is None:
            return corrupt[:i][-1]
        i+=1
print(f'Answer {part1(corrupt)=}')
print(f'Answer {part2(corrupt)=}')