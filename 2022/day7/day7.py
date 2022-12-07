from pathlib import Path
from collections import defaultdict

with open(Path("2022") / "day7" / "day7_input.txt") as f:
    data = [x.split() for x in f.read().splitlines()]

current_loc = ['/']
fs = defaultdict(list)

for cmd in data:
    if cmd[1] == 'cd':
        #Cd
        dest = cmd[2]
        if dest == '/':
            current_loc = ['/']
        elif dest == '..':
            current_loc = current_loc[:-1]
        else:
            current_loc.append(dest + '/')
    elif cmd[1] != 'ls':
        fs["".join(current_loc)].append((cmd[1],cmd[0]))

sizes = {}
def calc_dir_size(curr_dir):
    tot = 0
    for name, t in fs[curr_dir]:
        if t == 'dir':
            tot += calc_dir_size(curr_dir + name + '/')
        else:
            tot += int(t)
    sizes[curr_dir] = tot
    return tot

tot_space = calc_dir_size("/")


unused_space = 70000000 - tot_space
ans_p1 = sum([v for v in sizes.values() if v <= 100000])
ans_p2 = min([v for v in sizes.values() if unused_space + v  >= 30000000])

print(f"Answer part 1 {ans_p1}")
print(f"Answer part 2 {ans_p2}")