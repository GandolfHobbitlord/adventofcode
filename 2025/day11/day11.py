from pathlib import Path

def parse_line(line):
    print(line)
    key, val = line.split(': ')
    vals = [v for v in val.split(' ')]
    return key,vals

with open(Path("2025") / "day11" / "day11_input.txt") as f:
# with open(Path("2025") / "day11" / "day11_test.txt") as f:
    data = dict([parse_line(line) for line in f.read().split('\n')])

def find_num_paths(src,goal):
    if src == goal:
        return 1
    else:
        return sum(find_num_paths(next_node,goal) for next_node in data[src])

cache = {}
def find_num_paths_2(src,goal,visited):
    key = (src,goal, "fft" in visited, "dac" in visited)
    if key in cache:
        return cache[key]
    if src == goal:
        if 'fft' in visited and 'dac' in visited:
            return 1
        else:
            return 0
    else:
        s = sum(find_num_paths_2(next_node, goal, visited | {next_node}) for next_node in data[src])
        cache[key] = s
        return s

print(f"Part 1 {find_num_paths("you", "out")}")
print(f"Part 2 {find_num_paths_2("svr", "out",set())}")

