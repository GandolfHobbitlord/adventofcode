from pathlib import Path

with open(Path("2025") / "day2" / "day2_input.txt") as f:
# with open(Path("2025") / "day2" / "day2_test.txt") as f:
    data = [line for line in f.read().split(',')]
    # data = [parse_line(line) for line in f.read().split('\n')]

count = []
for d in data:
    lo,hi = [int(d) for d in d.split('-')]
    for d in range(lo,hi+1):
        i = str(d)
        left = i[:len(i)//2]
        right = i[len(i)//2:]
        if left == right:
            count.append(d)
            # print(left, right)
            print(d)


print(sum(count))