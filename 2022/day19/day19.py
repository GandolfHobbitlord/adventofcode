import re
from pathlib import Path
import numpy as np
from collections import Counter
from collections import defaultdict

mats = {"ore" : 0, "clay" : 1, "obsidian" :2}

class Factory():
    def __init__(self, ore_robot, clay_robot, obsidion_robot_ore, obsidion_robot_clay,
                        geod_robot_ore, geod_robot_obsidian):
        self.ore_robot = [ore_robot, 0, 0]
        self.clay_robot = [clay_robot,0,0]
        self.obisian_robot = [obsidion_robot_ore, obsidion_robot_clay,0]
        self.geod_robot_ore = [geod_robot_ore, 0, geod_robot_obsidian]

def able_to_build(stock, schem):
    for type, val in stock.items():
        if val >= schem[mats[type]]:
            continue
        else:
            return False
    return True


def parse_line(line):
    search = r'Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.'
    m = re.search(search, line)
    inp =[int(val)for val in m.groups()]
    return Factory(*inp)

with open(Path("2022") / "day19" / "day19_input.txt") as f:
    factory = [parse_line(x) for x in f.read().splitlines()][0]


bestest = []
def simulate(stock, bots, factory, current_time, end_time):
    for minutes in range(current_time, end_time):
        print(f'Minute: {minutes}')
        if able_to_build(stock, factory.ore_robot):
            print('ore bot build')
        if able_to_build(stock, factory.clay_robot):
            print('clay bot build')
        for type, num in bots.items():
            stock[type] += num
            if num != 0:
                print(f"{num} {type}-collecting robot collects {num} {type}; you now have {stock[type]} {type}.")

stock  = {"ore" : 0, "clay" : 0, "obsidian" :0}
bots  = {"ore" : 1, "clay" : 0, "obsidian" : 0}
maximum_time = 3
simulate(stock, bots, factory, current_time=0, end_time=5)

print(stock)
print(bots)