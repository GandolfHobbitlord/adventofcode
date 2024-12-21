numeric = { '7' : (0,0), '8' : (1,0), '9' : (2,0),
            '4' : (0,1), '5' : (1,1), '6' : (2,1),
            '1' : (0,2), '2' : (1,2), '3' : (2,2),
                         '0' : (1,3), 'A' : (2,3)}

arrow = {             '^' : (1,0), 'A' : (2,0),
         '<' : (0,1), 'v' : (1,1), '>' : (2,1)}

def get_numeric(start,goal):
    sx,sy = numeric[start]
    gx,gy = numeric[goal]
    dx,dy = gx-sx, gy-sy
    out = ''
    if dx < 0:
        out += '<' * abs(dx)
    else:
        out += '>' * dx
    if dy < 0:
        out += '^' * abs(dy)
    else:
        out += 'v' * dy
    return out

def get_numeric(start,goal):
    sx,sy = numeric[start]
    gx,gy = numeric[goal]
    dx,dy = gx-sx, gy-sy
    out = ''
    if dx < 0:
        out += '<' * abs(dx)
    else:
        out += '>' * dx
    if dy < 0:
        out += '^' * abs(dy)
    else:
        out += 'v' * dy
    return out

def get_numeric(start,goal):
    sx,sy = numeric[start]
    gx,gy = numeric[goal]
    dx,dy = gx-sx, gy-sy
    out = ''
    if dx < 0:
        out += '<' * abs(dx)
    else:
        out += '>' * dx
    if dy < 0:
        out += '^' * abs(dy)
    else:
        out += 'v' * dy
    return out
def get_arrow(start,goal):
    sx,sy = arrow[start]
    gx,gy = arrow[goal]
    dx,dy = gx-sx, gy-sy
    out = ''
    if dx < 0:
        out += '<' * abs(dx)
    else:
        out += '>' * dx
    if dy < 0:
        out += '^' * abs(dy)
    else:
        out += 'v' * dy
    return out

def run_tests():
    assert '>>'  == get_numeric('1','3')
    assert '<<'  == get_numeric('6','4')
    assert '^^^' == get_numeric('A','9')
    assert '>>v' == get_numeric('1','A')
    assert '>' == get_arrow('^','A')
    assert '^' == get_arrow('>','A')
    assert '>>^' == get_arrow('<','A')

def run(phrase):
    return run_arrow(run_arrow(run_numeric(phrase)))

def run_example():
    phrase = '029A'
    a = run_numeric(phrase)
    assert a in ['<A^A>^^AvvvA', '<A^A^>^AvvvA', '<A^A^^>AvvvA']
    a = run_arrow(a)
    assert len(a) == len('v<<A>>^A<A>AvA<^AA>A<vAAA>^A')
    a = run_arrow(a)
    assert len(a) ==len('<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A')
    assert len(run('029A')) == len('<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A')
    assert len(run('980A')) == len('<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A')
    # assert len(run('179A')) == len('<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A')
    assert len(run('456A')) == len('<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A')




def run_numeric(phrase):
    prev = 'A'
    out = ''
    for p in phrase:
        out += get_numeric(prev,p)
        out += 'A'
        prev = p
    print(out)
    return out

def run_arrow(phrase):
    prev = 'A'
    out = ''
    for p in phrase:
        out += get_arrow(prev,p)
        out += 'A'
        prev = p
    print(out)
    return out
run_example()

def part1():
    code = ['340A','149A','582A','780A','463A']
    return sum ([int(c[:-1]) * len(run(c)) for c in code])

# print(part1())