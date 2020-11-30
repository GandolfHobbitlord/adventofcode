import re
import numpy as np

def update(points):
    result =[]
    for x,y,vx,vy in points:
        x=x+vx
        y=y+vy
        result.append([x,y,vx,vy])
    return result

def get_bounds(p):
    minx = min([x for x, _, _, _ in p])
    miny = min([y for _, y, vx, vy in p])
    maxx = max([x for x, _, _, _ in p])
    maxy = max([y for _, y, _, _ in p])
    #print(minx, miny, maxx, maxy)
    return minx, miny, maxx, maxy

def print_points(p):
    x0,y0,x1,y1 = get_bounds(p)
    points = [(x,y) for x,y, _, _ in p]
    for y in range(y0, y1+1):
        row = ""
        for x in range(x0, x1+1):
            if (x,y) in points:
                row +="#"
            else:
                row += "."
        print(row)        

f = open(r"day10\input.txt")
lines = [line.rstrip("\n") for line in f]
p = [[int(i) for i in re.findall(r'-?\d+', l)] for l in lines]
result = []
for i in range(20000):
    #print_points(p)
    p = update(p)
    x0,y0,x1,y1= get_bounds(p)
    box = (y1-y0) * (x1-x0)
    result.append((p,box))

box =[ b for p, b in result]
index_min = np.argmin(box)
print(index_min+1)
print_points(result[index_min][0])