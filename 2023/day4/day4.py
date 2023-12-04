from pathlib import Path
import re
from collections import defaultdict
import numpy as np

def parse_line(line):
    game, d = line.split(':')
    winners, my_numbers = d.split('|')
    winners = [int(w) for w in re.findall('\d+',winners)]
    numbers = [int(w) for w in re.findall('\d+',my_numbers)]
    return winners, numbers

def part1(data):
    points = 0
    for winners, numbers in data:
        matches = defaultdict(int)
        w = set(winners)
        for n in numbers:
            if n in w:
                matches[n] = matches[n] + 1
        m = sum(matches.values())
        if m > 0:
            points += 2**(m-1)
    print(points)

def part2(data):
    cards = np.ones(len(data))
    for i, (winners, numbers) in enumerate(data):
        matches = defaultdict(int)
        w = set(winners)
        for n in numbers:
            if n in w:
                matches[n] = matches[n] + 1
        m = sum(matches.values())
        if m > 0:
            cards[i+1:i+m+1] += cards[i]
    print(sum(cards))

with open(Path("2023") / "day4" / "day4_input.txt") as f:
    data = [parse_line(line) for line in f.read().splitlines()]
    part1(data)
    part2(data)

