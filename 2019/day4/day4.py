def valid(num_list):
    double = False
    for i, _ in enumerate(num_list[:-1],start=1):
        if num_list[i] < num_list[i-1]:
            return False
        if num_list[i] == num_list[i-1]:
            double = True
    return double



lo, hi = 347312,805915 

part1, part2 = 0, 0
for i in range(lo,hi+1):
   if valid(str(i)):
        part1 += 1
        #Know its sorted already
        if  2 in [str(i).count(d) for d in str(i)]:
            part2 += 1

print("Answer 1: {}, Answer 2: {}".format(part1,part2))