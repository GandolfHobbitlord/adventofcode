
import functools
from pathlib import Path

numeric_map = { '7' : (0,0), '8' : (1,0), '9' : (2,0),
            '4' : (0,1), '5' : (1,1), '6' : (2,1),
            '1' : (0,2), '2' : (1,2), '3' : (2,2),
                         '0' : (1,3), 'A' : (2,3)}

arrow_map = {         '^' : (1,0), 'A' : (2,0),
         '<' : (0,1), 'v' : (1,1), '>' : (2,1)}

dirs = {(-1,0) : '<', (1,0) : '>', (0,1) : 'v', (0,-1) : '^'}

def get_neighbor(d, pos):
    x,y = pos
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
        n = x + dx, y + dy
        if n in d.values():
            yield n

# Should cache this but i have a dict as argument which is not hashable
# should change to hashable but meh, it works.
def get_shortest_paths(start,goal,map):
    q = [(map[start],'')]
    goal_pos = map[goal]
    shortest = 100
    ans = []
    while q:
        pos, path = q.pop()
        if len(path) > shortest:
            continue
        if pos == goal_pos:
            shortest = len(path)
            ans.append(path)
            continue
        for n in get_neighbor(map,pos):
            d = n[0] - pos[0], n[1] - pos[1]
            n_path = path +dirs[d]
            q.append((n,n_path))
            q.sort(key=lambda x: len(x[1]),reverse=True)
    return ans

def run_tests():
    assert ['<<']  == get_shortest_paths('6','4',numeric_map)
    assert ['^^^'] == get_shortest_paths('A','9',numeric_map)
    assert '>>v' in get_shortest_paths('1','A',numeric_map)
    assert ['>'] == get_shortest_paths('^','A',arrow_map)
    assert ['^'] == get_shortest_paths('>','A',arrow_map)
    assert '>>^' in get_shortest_paths('<','A',arrow_map)

def run_example():
    phrase = '029A'
    ans = get_minimum_moves(phrase,level=0,MAX_LEVEL=1)
    assert ans == len('<A^A^>^AvvvA')
    ans = get_minimum_moves(phrase,level=0,MAX_LEVEL=2)
    assert ans == len('v<<A>>^A<A>AvA<^AA>A<vAAA>^A')

    assert get_minimum_moves(phrase,level=0,MAX_LEVEL=3) == len('<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A')
    assert get_minimum_moves('029A',level =0,MAX_LEVEL=3) == len('<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A')
    assert get_minimum_moves('980A',level =0,MAX_LEVEL=3) == len('<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A')
    assert get_minimum_moves('179A',level =0,MAX_LEVEL=3) == len('<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A')
    assert get_minimum_moves('456A',level =0,MAX_LEVEL=3) == len('<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A')

@functools.cache
def get_minimum_moves(code, level,MAX_LEVEL):
    if level == MAX_LEVEL:
        return len(code)
    moves = 0
    map = numeric_map if level == 0 else arrow_map
    for start, goal in zip('A'+code, code):
        paths = [get_minimum_moves(path + 'A', level+1,MAX_LEVEL) for path in get_shortest_paths(start,goal,map)]
        moves += min(paths)
    return moves

run_tests()
run_example()

def solve(codes, MAX_LEVEL):
    return sum ([int(c[:-1]) * get_minimum_moves(c,level=0,MAX_LEVEL=MAX_LEVEL) for c in codes])

with open(Path("2024") / "day21" / "day21_input.txt") as f:
    codes = [line for line in f.read().split('\n')]

print(f'Answer Part 1: {solve(codes,MAX_LEVEL=3)}')
print(f'Answer Part 2: {solve(codes,MAX_LEVEL=26)}')