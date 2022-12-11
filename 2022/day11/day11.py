import re
from pathlib import Path
import numpy as np
from collections import Counter
from collections import defaultdict

# Longest time spent realising you need to change this when running test input
# also these are primes which makes this worko otherwise need to find lowest common.
common = np.product([13,
19,
11,
17,
3,
7,
5,
2])
class Monkey():
    def __init__(self,starting_items,op, test, true_throw, false_throw,):
        self.items = starting_items.copy()
        self.false_throw = false_throw
        self.true_throw = true_throw
        self.test = test
        self.op = op
        self.active = 0
        self.inspect = 0
    def catch(self, item):
        self.items.append(item)

    def tick(self, part1= True):
        out = []
        while len(self.items):
            self.inspect += 1
            old = self.items.pop(0)
            old = np.dtype('int64').type(old)
            new = self.op(old)
            if part1:
                new = new // 3
            new %= common
            if self.test(new):
                out.append((new, self.true_throw))
            else:
                out.append((new, self.false_throw))
        return out

def get_monkeys():
    monkeys =[Monkey([53, 89, 62, 57, 74, 51, 83, 97],lambda old : old * 3, lambda x : 0 ==(x % 13), true_throw=1,false_throw=5),
            Monkey([85, 94, 97, 92, 56],lambda old : old + 2, lambda x : 0 ==(x % 19), true_throw=5,false_throw=2),
            Monkey([86, 82, 82],lambda old : old + 1, lambda x : 0 ==(x % 11), true_throw=3,false_throw=4),
            Monkey([94, 68],lambda old : old + 5, lambda x : 0 ==(x % 17), true_throw=7,false_throw=6),
            Monkey([83, 62, 74, 58, 96, 68, 85],lambda old : old + 4, lambda x : 0 ==(x % 3), true_throw=3,false_throw=6),
            Monkey([50, 68, 95, 82],lambda old : old + 8, lambda x : 0 ==(x % 7), true_throw=2,false_throw=4),
            Monkey([75],lambda old : old * 7, lambda x : 0 ==(x % 5), true_throw=7,false_throw=0),
            Monkey([92, 52, 85, 89, 68, 82],lambda old : old * old, lambda x : 0 ==(x % 2), true_throw=0,false_throw=1)]
    return monkeys


def part1():
    monkeys = get_monkeys()
    for round in range(20):
        for m in monkeys:
            throws = m.tick(part1=True)
            for item, target in throws:
                monkeys[target].catch(item)
    a = sorted([m.inspect for m in monkeys])
    return a[-1] * a[-2]

def part2():
    monkeys = get_monkeys()
    for round in range(10000):
        for m in monkeys:
            throws = m.tick(part1=False)
            for item, target in throws:
                monkeys[target].catch(item)
    a = sorted([m.inspect for m in monkeys])
    return a[-1] * a[-2]

print(f"Answer Part 1: {part1()}")
print(f"Answer Part 2: {part2()}")