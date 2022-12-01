from pathlib import Path

with open(Path("2022") / "day1" / "day1_input.txt") as f:
    elfs = [x for x in f.read().split('\n\n')]
cals = list()
for elf in elfs:
    e = [int(x) for x in elf.splitlines()]
    cals.append(sum(e))

cals.sort()

print(f'Answer part 1: {cals[-1]}')
print(f'Answer part 2:{sum(cals[-3:])}')
