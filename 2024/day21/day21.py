numeric = { '7' : (0,0), '8' : (1,0), '9' : (2,0),
            '4' : (0,1), '5' : (1,1), '6' : (2,1),
            '1' : (0,2), '2' : (1,2), '3' : (2,2),
                         '0' : (1,3), 'A' : (2,3)}

arrow = {             '^' : (1,0), 'A' : (2,0),
         '<' : (0,1), 'v' : (1,1), '>' : (2,1)}

dirs = {(-1,0) : '<', (1,0) : '>', (0,1) : 'v', (0,-1) : '^'}
import functools
def get_neighbor(d, pos):
    x,y = pos
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
        n = x + dx, y + dy
        if n in d.values():
            yield n

def get_numeric(start,goal):
    q = [(numeric[start],'')]
    goal_pos = numeric[goal]
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
        for n in get_neighbor(numeric,pos):
            d = n[0] - pos[0], n[1] - pos[1]
            n_path = path +dirs[d]
            q.append((n,n_path))
            q.sort(key=lambda x: len(x[1]),reverse=True)
    return ans

def get_arrow(start,goal):
    q = [(arrow[start],'')]
    goal_pos = arrow[goal]
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
        for n in get_neighbor(arrow,pos):
            d = n[0] - pos[0], n[1] - pos[1]
            n_path = path +dirs[d]
            q.append((n,n_path))
            q.sort(key=lambda x: len(x[1]),reverse=True)
    return ans

def run_tests():
    assert ['<<']  == get_numeric('6','4')
    assert ['^^^'] == get_numeric('A','9')
    assert '>>v' in get_numeric('1','A')
    assert ['>'] == get_arrow('^','A')
    assert ['^'] == get_arrow('>','A')
    assert '>>^' in get_arrow('<','A')

def run(phrase):
    return run_arrow(run_arrow(run_numeric(phrase)))

def run_example():
    phrase = '029A'
    a = run_numeric(phrase)
    ans = parse(phrase,level=0,MAX_LEVEL=1)
    # assert set(a) == set(['<A^A>^^AvvvA', '<A^A^>^AvvvA', '<A^A^^>AvvvA'])
    assert ans == len('<A^A^>^AvvvA')
    ans = parse(phrase,level=0,MAX_LEVEL=2)
    assert ans == len('v<<A>>^A<A>AvA<^AA>A<vAAA>^A')

    ans = parse(phrase,level=0,MAX_LEVEL=3)
    assert ans == len('<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A')
    assert parse('029A',level =0,MAX_LEVEL=3) == len('<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A')
    assert parse('980A',level =0,MAX_LEVEL=3) == len('<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A')
    assert parse('179A',level =0,MAX_LEVEL=3) == len('<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A')
    assert parse('456A',level =0,MAX_LEVEL=3) == len('<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A')

@functools.cache
def parse(code, level,MAX_LEVEL):
    if level == MAX_LEVEL:
        # print(code)
        return len(code)
    moves = 0
    fn = get_numeric if level == 0 else get_arrow
    for start, goal in zip('A'+code, code):
        paths = [parse(path + 'A', level+1,MAX_LEVEL) for path in fn(start,goal)]
        moves += min(paths)
    return moves

def run_numeric(phrase):
    solves = []
    prev = 'A'
    for p in phrase:
        solves = [a +'A' for a in get_numeric(prev,p)]

    print(solves)
    return solves

# run_tests()
run_example()


def part1():
    code = ['340A','149A','582A','780A','463A']
    return sum ([int(c[:-1]) * parse(c,level=0,MAX_LEVEL=3) for c in code])

def part2():
    code = ['340A','149A','582A','780A','463A']
    return sum ([int(c[:-1]) * parse(c,level=0,MAX_LEVEL=26) for c in code])
print(part1())
print(part2())

