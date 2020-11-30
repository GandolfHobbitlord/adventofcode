from collections import defaultdict

f = open(r"day6\input.txt")

coords = []
for line in f:
    x,y = [int(s.strip()) for s in line.split(",")]
    print(x,y)
    coords.append((x,y))
print(coords)
min_x=min([x for x,y in coords])
min_y=min([y for x,y in coords])
max_x=max([x for x,y in coords])
max_y=max([y for x,y in coords])
print(min_x, min_y)
print(max_x, max_y)

def distance(x1,y1,x2,y2):
    return abs(x2-x1)+abs(y2-y1)

def get_closest_point(a,b):
    #print("Getting distance from point", a," ", b)
    ds = [(distance(a,b,p[0],p[1]), p) for p in coords]
    #print(ds)    
    ds.sort()
    if ds[0][0] < ds[1][0]:
        return ds[0][1]
    else:
        return (-1,-1)

def score_around(W):
    point_voter = defaultdict(int)
    for x in range(min_x-W,max_x+W):
    #for x in range(10):
        for y in range(min_y-W, max_y+W):
        #for y in range(10):
            id = get_closest_point(x,y)
            if id != (-1,-1):
                point_voter[id] += 1
    return point_voter

def within_region(a,b, region_lim):
    ds = sum([distance(a,b,p[0],p[1]) for p in coords])
    return ds < region_lim

def part2(W, region_lim):
    num_of_regions = 0
    for x in range(min_x-W,max_x+W):
        for y in range(min_y-W, max_y+W):
            if within_region(x,y,region_lim):
                num_of_regions += 1
    return num_of_regions

#S1 = score_around(1)
#S2 = score_around(2)

#S = [S1[k] for k in S1.keys() if S1[k] == S2[k]]   
#print("Valid Answers", max(S))
print(part2(10, 10000))