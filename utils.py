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

def xy_to_grid(a, size):
    res = np.zeros((size))
    np.add.at(res, tuple(zip(*a)), 1)
    np.rot90(res)
    return res

def get_neighbors(r, c, grid):
    ### Get valid neighbors for a cell in the grid. ###
    neighbors = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            neighbors.append((nr, nc))
    return neighbors


def print_grid(grid):
    for y in range(grid_size_y):
        line = ""
        for x in range(grid_size_x):
            line += grid[x,y]
        print(line)

def djikstra(data,start,stop):
    q =[]
    score_dict = defaultdict(lambda: 1e12)
    # q = (steps, pos,dir)
    visited = set()
    q.append((0,start,E))
    heapq.heapify(q)
    while q:
        score,pos,curr_dir = heapq.heappop(q)
        if score > score_dict[(pos,curr_dir)]:
            continue
        score_dict[(pos,curr_dir)] = score

        if pos == stop:
            return score
        visited.add(pos)
        for nx,ny in get_neighbor(data,pos):
            if data[ny][nx] != '#' and (nx,ny) not in visited:
                    new_dir = (nx-pos[0], ny-pos[1])
                    if new_dir != curr_dir:
                        n_score = score + 1001
                    else:
                        n_score = score + 1
                    s = (n_score,(nx,ny),new_dir)
                    heapq.heappush(q,s)