from pathlib import Path
from collections import defaultdict

with open(Path("2022") / "day7" / "day7_input.txt") as f:
    data = [x.split() for x in f.read().splitlines()]

current_loc = ['/']
fs = defaultdict(list)
i = 0

while i < len(data):
    cmd = data[i]
    if len(cmd) == 3:
        #Cd
        dest = cmd[2]
        if dest == '/':
            current_loc = ['/']
        elif dest == '..':
            current_loc = current_loc[:-1]
        else:
            current_loc.append(dest + '/')
        i+=1
    if cmd[1] == 'ls':
        if len(fs["".join(current_loc)]) != 0:
            #Already seen
            i+=1
            continue
        while True:
            i+=1
            if i >= len(data) or data[i][0] == "$":
                break
            cmd = data[i]
            fs["".join(current_loc)].append((cmd[1],cmd[0]))

sizes = {}
def calc_dir_size(curr_dir,tot = 0):
    for name, t in fs[curr_dir]:
        if t == 'dir':
            tot += calc_dir_size(curr_dir + name + '/',0)
        else:
            tot += int(t)
    sizes[curr_dir] = tot
    return tot

tot_space = calc_dir_size("/")

ans_p1 = sum([v for v in sizes.values() if v <= 100000])

print(f"Answer part 1 {ans_p1}")
unused_space = 70000000 - tot_space
s2 = sorted([v for v in sizes.values() if unused_space + v  >= 30000000])

print(f"Answer part 2 {s2[0]}")