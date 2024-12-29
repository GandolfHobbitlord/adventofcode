from pathlib import Path
import numpy as np
import re
from itertools import combinations
import z3

def parse_line(line):
    pos, vel = line.split('@')
    p = np.array(re.findall(r'-?\d+', pos),dtype=float)
    v = np.array(re.findall(r'-?\d+', vel),dtype=float)
    print(p)
    return np.hstack([p,v])

def to_vect_part1(data,lo,hi):
    A = np.vstack(data)
    pos = A[:,:3]
    vel = A[:,3:-1]
    k = vel[:,1]/vel[:,0]
    m = pos[:,1].T - k.T*pos[:,0]

    crossing = 0
    for i in  range(len(k)):
        for j in range(len(k)):
            if i >= j:
                continue
            # print('---------')
            # print(data[i])
            # print(data[j])

            k0 = k[i]

            m0 = m[i]
            k1 = k[j]
            m1 = m[j]
            if k0 == k1:
                continue
            x = (m1-m0)/(k0-k1)
            if not(x >= lo and x <= hi):
                # print('outside')
                continue
            if (pos[i,0]-x) / vel[i,0] >= 0:
                # print('i in past')
                continue
            if (pos[j,0]-x) / vel[j,0] >= 0:
                # print('j in past')
                continue
            # print('Crossing')
            crossing += 1
    return crossing

def p1(hailstones, lower, upper):
    ret = 0
    for (x1, y1, _, vx1, vy1, _), (x2, y2, _, vx2, vy2, _) in combinations(hailstones, 2):
        m1, m2 = vy1 / vx1, vy2 / vx2
        if m1 == m2:
            continue
        A = np.array([[m1, -1], [m2, -1]])
        b = np.array([m1 * x1 - y1, m2 * x2 - y2])
        x, y = np.linalg.solve(A, b)
        if not (lower <= x <= upper and lower <= y <= upper):
            continue
        t1 = (x - x1) / vx1
        t2 = (x - x2) / vx2
        if t1 > 0 and t2 > 0:
            ret += 1
    return ret

with open(Path("2023") / "day24" / "day24_input.txt") as f:
# with open(Path("2023") / "day24" / "day24_test.txt") as f:
    # data = [line for line in f.read().split('\n')]
    data = [parse_line(line) for line in f.read().split('\n')]

# print(p1(data,7,27))
print(p1(data,200000000000000,400000000000000))
print(to_vect_part1(data,200000000000000,400000000000000))
exit()
# Using a solver kind of feels like cheating...
# TODO: Find a "smart way"
x = z3.Real('x')
y = z3.Real('y')
z = z3.Real('z')
vx = z3.Real('vx')
vy = z3.Real('vy')
vz = z3.Real('vz')
solver = z3.Solver()
i = 0
for xx,yy,zz, vxx,vyy, vzz in data:
    t = z3.Real(f't{i}')
    i+=1
    solver.add(t > 0)
    solver.add(xx + vxx*t == x + vx*t)
    solver.add(yy + vyy*t == y + vy*t)
    solver.add(zz + vzz*t == z + vz*t)

print(solver.check())
model = solver.model()
x_ans = model.eval(x).as_long()
y_ans = model.eval(y).as_long()
z_ans = model.eval(z).as_long()
# print(model)
print(sum([x_ans,y_ans,z_ans]))

# print(data)
