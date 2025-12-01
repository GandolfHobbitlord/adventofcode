from pathlib import Path

def parse_line(line):
    mul = 1 if line[0] is "R" else -1
    return mul*int(line[1:])

with open(Path("2025") / "day1" / "day1_input.txt") as f:
# with open(Path("2025") / "day1" / "day1_test.txt") as f:
    data = [parse_line(line) for line in f.read().split('\n')]

def part1(data):
    pos = 50
    count = 0
    for d in data:
        pos+=d
        pos = pos % 100 # Yay for python neg modulus
        if pos == 0:
            count +=1
    return count

def part2(data):
    count = 0
    pos = 50
    for d in data:
        # If it's stupid and works it aint stupid
        for _ in range(abs(d)):
            if d > 0:
                pos+=1
            else:
                pos-=1
            pos = pos % 100
            if pos == 0:
                count +=1
    return count

print(f"Answer {part1(data)=}")
print(f"Answer {part2(data)=}")
