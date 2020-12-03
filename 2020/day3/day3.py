from pathlib import Path


def num_of_trees(inp, direction):
    pos = [0,0]
    trees = 0
    width = len(inp[0])
    while pos[0] < len(inp):
        if inp[pos[0]][pos[1] % width] == '#':
            trees +=1
        pos[0] += direction[0]
        pos[1] += direction[1]
    return trees

def run_tests():
    with open(Path("2020") / "day3" / "day3_test.txt") as f:
        inp = [line for line in f.read().splitlines()]
    assert num_of_trees(inp, [1,1]) == 2
    assert num_of_trees(inp, [1,3]) == 7
    assert num_of_trees(inp, [1,5]) == 3
    assert num_of_trees(inp, [1,7]) == 4
    assert num_of_trees(inp, [2,1]) == 2

run_tests()
with open(Path("2020") / "day3" / "day3_input.txt") as f:
    inp = [line for line in f.read().splitlines()]

print(f"Part 1 hits {num_of_trees(inp,[1,3])} trees")
directions = [[1,1],[1,3],[1,5],[1,7],[2,1]]
ans2 = 1
for d in directions:
    ans2 *= num_of_trees(inp,d)
print(f"Answer part 2: {ans2}")