import re
from pathlib import Path
import numpy as np
from collections import Counter
from collections import defaultdict
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

    def tick(self):
        out = []
        while len(self.items):
            self.inspect += 1
            old = self.items.pop(0)
            new = self.op(old)
            # print(new)
            new = new // 3
            if self.test(new):
                out.append((new, self.true_throw))
            else:
                out.append((new, self.false_throw))
        return out
# with open(Path("2022") / "day11" / "day11_input.txt") as f:
#     data = [parse_line(x) for x in f.read().splitlines()]
# print(data)

# monkeys =[Monkey([79,98],lambda old : old * 19, lambda x : 0 ==(x % 23), true_throw=2,false_throw=3),
#     Monkey([54, 65, 75, 74],lambda old : old + 6, lambda x : 0 ==(x % 19), true_throw=2,false_throw=0),
#     Monkey([79, 60, 97],lambda old : old * old, lambda x : 0 ==(x % 13), true_throw=1,false_throw=3),
#     Monkey([74],lambda old : old + 3, lambda x : 0 ==(x % 17), true_throw=0,false_throw=1)]

monkeys =[Monkey([53, 89, 62, 57, 74, 51, 83, 97],lambda old : old * 3, lambda x : 0 ==(x % 13), true_throw=1,false_throw=5),
        Monkey([85, 94, 97, 92, 56],lambda old : old + 2, lambda x : 0 ==(x % 19), true_throw=5,false_throw=2),
        Monkey([86, 82, 82],lambda old : old + 1, lambda x : 0 ==(x % 11), true_throw=3,false_throw=4),
        Monkey([94, 68],lambda old : old + 5, lambda x : 0 ==(x % 17), true_throw=7,false_throw=6),
        Monkey([83, 62, 74, 58, 96, 68, 85],lambda old : old + 4, lambda x : 0 ==(x % 3), true_throw=3,false_throw=6),
        Monkey([50, 68, 95, 82],lambda old : old + 8, lambda x : 0 ==(x % 7), true_throw=2,false_throw=4),
        Monkey([75],lambda old : old * 7, lambda x : 0 ==(x % 5), true_throw=7,false_throw=0),
        Monkey([92, 52, 85, 89, 68, 82],lambda old : old * old, lambda x : 0 ==(x % 2), true_throw=0,false_throw=1)]






for round in range(20):
    print(round)
    for m in monkeys:
        throws = m.tick()
        for item, target in throws:
            monkeys[target].catch(item)
print('----')
a = sorted([m.inspect for m in monkeys])
print(a[-1] * a[-2])
