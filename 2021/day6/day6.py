from pathlib import Path

def to_bins(inp):
    return [inp.count(i) for i in range(9)]

def pass_days(inp, days):
    fishes = to_bins(inp)
    for _ in range(days):
        fishes = fishes[1:] + [fishes[0]]
        fishes[6] += fishes[-1]
    return sum(fishes)


def run_tests():
    data = [3,4,3,1,2]
    assert 5 == pass_days(data,1)
    assert 6 == pass_days(data,2)
    assert 7 == pass_days(data,3)
    assert 26 == pass_days(data,18)
    assert 5934 == pass_days(data,80)

with open(Path("2021") / "day6" / "day6_input.txt") as f:
   data = [int(line) for line in f.read().split(',')]
run_tests()

print(f"Answer after 80  days: {pass_days(data, 80)}")
print(f"Answer after 256 days: {pass_days(data, 256)}")
