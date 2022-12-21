import re
from pathlib import Path
from symbol import factor
import numpy as np
from collections import Counter
from collections import defaultdict

mats = {"ore" : 0, "clay" : 1, "obsidian" :2, "geod" : 3}

class Factory():
    def __init__(self, ore_robot, clay_robot, obsidian_robot_ore, obsidion_robot_clay,
                        geod_robot_ore, geod_robot_obsidian):
        self.ore_robot = [ore_robot, 0, 0,0]
        self.clay_robot = [clay_robot,0,0,0]
        self.obsidian_robot = [obsidian_robot_ore, obsidion_robot_clay,0,0]
        self.geod_robot = [geod_robot_ore, 0, geod_robot_obsidian,0]

def able_to_build(stock, schem):
    for type, val in stock.items():
        if val >= schem[mats[type]]:
            continue
        else:
            return False
    return True

def pay(stock, schematic):
    new_stock = {}
    new_stock['ore'] = stock['ore'] - schematic[0]
    new_stock['clay'] = stock['clay'] - schematic[1]
    new_stock['obsidian'] = stock['obsidian'] - schematic[2]
    new_stock['geod'] = stock['geod'] - schematic[3]
    return new_stock

def collect(bots,stock):
    new_stock = {}
    for type, num in bots.items():
        new_stock[type] = stock[type] + num
    return new_stock

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
        # print(f'Minute: {minutes}')
        if able_to_build(stock, factory.ore_robot):
            new_stock = pay(stock, factory.ore_robot)
            new_stock = collect(bots, new_stock)
            new_bots = bots.copy()
            new_bots['ore'] += 1
            simulate(new_stock,new_bots,factory,minutes+1,end_time)
        elif able_to_build(stock, factory.clay_robot):
            new_stock = pay(stock, factory.clay_robot)
            new_stock = collect(bots, new_stock)
            new_bots = bots.copy()
            new_bots['clay'] += 1
            # print('clay bot build')
            simulate(new_stock,new_bots,factory,minutes+1,end_time)
        elif able_to_build(stock, factory.obsidian_robot):
            new_stock = pay(stock, factory.obsidian_robot)
            new_stock = collect(bots, new_stock)
            new_bots = bots.copy()
            new_bots['obsidian'] += 1
            # print('obsidian bot build')
            simulate(new_stock,new_bots,factory,minutes+1,end_time)
        elif able_to_build(stock, factory.geod_robot):
            new_stock = pay(stock, factory.geod_robot)
            new_stock = collect(bots, new_stock)
            new_bots = bots.copy()
            new_bots['geod'] += 1
            simulate(new_stock,new_bots,factory,minutes+1,end_time)
            # print('clay bot build')
        else:
            for type, num in bots.items():
                stock[type] += num
                if num != 0:
                    # print(f"{num} {type}-collecting robot collects {num} {type}; you now have {stock[type]} {type}.")
    bestest.append(stock['geod'])

stock  = {"ore" : 0, "clay" : 0, "obsidian" :0, "geod" : 0}
bots  = {"ore" : 1, "clay" : 0, "obsidian" : 0, "geod" : 0}
simulate(stock, bots, factory, current_time=0, end_time=24)
print(max(bestest))