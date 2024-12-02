from pathlib import Path
import re
from collections import defaultdict, Counter
import heapq
import random
import networkx  as nx
def create_graph(data):
    edges = defaultdict(set)
    vertices = set()
    for line in data:
        vert, conn = line.split(':')
        conns = re.findall(r'\w+',conn)
        for c in conns:
            edges[vert].add(c)
            edges[c].add(vert)
            vertices.add(c)
        vertices.add(vert)
    return edges, vertices
with open(Path("2023") / "day25" / "day25_input.txt") as f:
# with open(Path("2023") / "day25" / "day25_test.txt") as f:
    data = [line for line in f.read().split('\n')]
edges, vertices = create_graph(data)

def djikstra(edges,vertices,start,stop):
    q =[]
    min_steps = defaultdict(lambda : 100000000)
    # q = (steps, pos, visited,edges used)
    q.append((0,start,set(),[]))
    heapq.heapify(q)
    while q:
        steps, pos, visited, visited_edges = heapq.heappop(q)
        if pos == stop:
            return visited_edges
        visited.add(pos)
        for neighbor in edges[pos]:
            if neighbor not in visited:
                if min_steps[neighbor] > steps + 1:
                    min_steps[neighbor] = steps + 1
                    s = tuple(sorted((pos,neighbor)))
                    visited_edges.append(s)
                    heapq.heappush(q,(steps + 1,neighbor,visited.copy(),visited_edges))

def get_subgraphs(edges,vertices):
    start = list(vertices)[0]
    visited = set()
    q = []
    q.append(start)
    while q:
        pos = q.pop()
        visited.add(pos)
        for neighbor in edges[pos]:
            if neighbor not in visited:
                q.append(neighbor)
    print(len(visited))
    print(len(vertices-visited))
    return len(vertices-visited) * len(visited)

#This worked surprisingly well :O
# Just find shortest paths betwen random vertices. The minimal cut we should pass most times (hopefully)
# After doing it a few times, remove that edge most commonly used and do the same thing again
samples = 100
for cut_nr in range(3):
    print(cut_nr)
    count = Counter()
    sample = 0
    # for start, goal in combinations(vertices,2):
    for sample in range(samples):
        start, goal = random.sample(list(vertices),2)

        visited = djikstra(edges,vertices, start, goal)
        count.update(visited)
        sample += 1
        if sample >= samples:
            break

    for (v0,v1) , _ in count.most_common(1):
        print(v0,v1)
        edges[v0].remove(v1)
        edges[v1].remove(v0)

# Traverses through graph and print len of vertices visited and not visited
print(get_subgraphs(edges,vertices))