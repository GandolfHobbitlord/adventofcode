from pathlib import Path

with open(Path("2022") / "day1" / "day1_input.txt") as f:
    elfs = [x for x in f.read().split('\n\n')]

calories = list()
for elf in elfs:
    calories.append(sum([int(x) for x in elf.splitlines()]))

calories.sort()

print(f'Answer part 1: {calories[-1]}')
print(f'Answer part 2: {sum(calories[-3:])}')
