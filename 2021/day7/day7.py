from pathlib import Path


with open(Path("2021") / "day7" / "day7_input.txt") as f:
   data = [int(line) for line in f.read().split(',')]

def find_cost(crabs):
    cost = []
    for i in range(min(crabs), max(crabs)):
        cost.append(sum([abs(crab-i) for crab in crabs]))
    return cost

def calc_sum(num):
    return num *(num+1) // 2

def find_cost2(crabs):
    cost = []
    for i in range(min(crabs), max(crabs)):
        cost.append(sum([calc_sum(abs(crab-i)) for crab in crabs]))
    return cost

def run_tests():
    inp = [16,1,2,0,4,2,7,1,2,14]
    c = find_cost(inp)
    assert min(c) == 37
    c = find_cost2(inp)
    assert min(c) == 168


run_tests()
print(f"Crab movment cost part 1 {min(find_cost(data))}")
print(f"Crab movment cost part 2 {min(find_cost2(data))}")