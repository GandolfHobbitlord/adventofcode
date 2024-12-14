from pathlib import Path
import numpy as np

#Quite happy with my idea for a solution but not with the crappy code
def in_range(mat,n):
    bounds = mat.shape
    for pos, bound in zip(n,bounds):
        if pos < 0 or pos >= bound:
            return False
    return True
def get_neighbor(mat, pos,diag=False):
    x,y  = pos
    neighbors = [(y-1,x), (y+1,x), (y,x-1), (y,x+1)]
    if diag:
        neighbors += [(y-1,x-1),(y-1,x+1),(y+1,x+1), (y+1,x-1)]
    for n in neighbors:
        if in_range(mat,n):
            yield n[1], n[0]

def get_same_neighbor(mat,pos,diag=False):
    for x,y in get_neighbor(mat,pos,diag):
        if mat[pos[1],pos[0]] == mat[y,x]:
            yield x,y

def get_different_neighbor(mat,pos,blob,diag=False):
    for x,y in get_neighbor(mat,pos,diag):
        if (x,y) not in blob:
            yield x,y

def get_fences(mat,blob):
    num = 0
    for pos in blob:
        num += 4 - len(list(get_same_neighbor(mat,pos)))
    return num

with open(Path("2024") / "day12" / "day12_input.txt") as f:
# with open(Path("2024") / "day12" / "day12_test.txt") as f:
    data = np.array([list(line) for line in f.read().split('\n')])
# data = [parse_line(line) for line in f.read().split('\n')]
print(data)
h,w = data.shape
visited = set()
blobs =[]
for x in range(w):
    for y in range(h):
        if (x,y) in visited:
            continue
        val = data[y,x]
        q = [(x,y)]
        blob = set()
        while q:
            pos = q.pop()
            blob.add(pos)
            q += [(nx,ny) for nx,ny in get_same_neighbor(data,pos) if (nx,ny) not in blob]
        visited |= blob
        blobs.append(blob)
print(blobs)

ans = [get_fences(data,b) * len(b) for b in blobs]
print(sum(ans))

m = np.pad(data,[1,1],mode='constant')


N = (0,-1)
W = (-1,0)
E = (1,0)
S = (0,1)

opposite = {}
opposite[N] = S
opposite[S] = N
opposite[W] = E
opposite[E] = W

#There should be a clever way to do this
dir_order = {}
dir_order[N] = [W,N,E,S]
dir_order[W] = [S,W,N,E]
dir_order[S] = [E,S,W,N]
dir_order[E] = [N,E,S,W]

def get_next_dir(pos, curr_dir, bound,dbg):
    for d_x,d_y in dir_order[curr_dir]:
        if (pos[0] + d_x, pos[1] +  d_y) in bound:
            return (d_x,d_y)
    return None
def get_good_start(blob,bound,dbg):
    for cord in bound:
        if (cord[0] + 1, cord[1]) in blob:
            return cord

def get_corners_from_bound(bound,blob,dbg):
    bound = set(bound)
    pos = get_good_start(blob,bound,dbg)
    pos_dir = get_next_dir(pos,S,bound,dbg)
    if pos_dir is None: #nowhere to go
        if len(bound) == 1:
            return 4 #Just single point
        bound.remove(pos)
        return 4+get_corners_from_bound(bound,blob,dbg)
    corners = 0
    start = (pos,pos_dir)
    dbg[pos[1],pos[0]] = 'X'
    visited = set()
    visited.add(pos)
    while True:
        # print(dbg)
        next_pos = pos[0] + pos_dir[0], pos[1] + pos_dir[1]
        dbg[next_pos[1],next_pos[0]] = 'X'
        pos = next_pos
        visited.add(pos)
        new_dir = get_next_dir(pos,pos_dir,bound,dbg)
        if  new_dir == opposite[pos_dir]:
            corners +=2
        elif new_dir == pos_dir:
            corners += 0
        else:
            corners += 1
        pos_dir = new_dir
        if (next_pos, pos_dir) == start: # Made a loop
            if bound != visited:
                not_visited = bound-visited
                corners += get_corners_from_bound(not_visited,blob,dbg)
            break
    print(corners)
    return corners
def parse_blob(data, orig_blob):

    m = np.pad(data,[1,1],mode='constant')
    blob = [(b_x +1, b_y + 1) for b_x,b_y in orig_blob] # fix padding coord
    bounds = []

    dbg = m.copy()
    for pos in blob:
        bounds += set(get_different_neighbor(m,pos,blob=blob,diag=True))
    print(dbg)
    for x,y in bounds:
        dbg[y,x] = '.'
    print(dbg)
    print(len(blob))
    return get_corners_from_bound(bounds,blob,dbg)
print(m)
# print(blobs[1])
print([len(b) for b in blobs])
score = [(len(blob),parse_blob(data,blob)) for blob in blobs]
print(score)
print( [a * b for a,b in score])
print(sum([a * b for a,b in score]))
# print(sum(score))
